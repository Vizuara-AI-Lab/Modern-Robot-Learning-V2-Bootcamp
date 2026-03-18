#!/usr/bin/env python3
"""
Ghost Video Pipeline — Narrated Slidev Presentation
====================================================
Generates a full narrated video from a Slidev presentation + narration script.

Steps:
  1. Export Slidev slides to PDF → convert to PNG images
  2. Generate TTS audio for each slide via ElevenLabs API
  3. Assemble slide images + audio into a final MP4 video with ffmpeg

Usage:
  python3 pipeline.py                    # Run full pipeline
  python3 pipeline.py --step audio       # Only generate audio
  python3 pipeline.py --step video       # Only assemble video (needs audio + images)
  python3 pipeline.py --step export      # Only export slides
"""

import json
import os
import struct
import subprocess
import sys
import time
import wave
from pathlib import Path

import requests

# ─── Configuration ───────────────────────────────────────────────────────────

BASE_DIR = Path(__file__).parent
PROJECT_DIR = BASE_DIR.parent
SCRIPT_FILE = BASE_DIR / "script.json"
AUDIO_DIR = BASE_DIR / "audio"
SLIDES_DIR = BASE_DIR / "slides"  # PNG images of slides
OUTPUT_DIR = BASE_DIR / "output"

# ElevenLabs
ELEVENLABS_API_KEY = "sk_f111dd4737e3eb957937808da97438a38f06b683b2f7afa9"
ELEVENLABS_VOICE_ID = "lZORFNDokoBmfd0S06vf"
ELEVENLABS_MODEL = "eleven_multilingual_v2"

# Video settings
VIDEO_WIDTH = 1920
VIDEO_HEIGHT = 1080
VIDEO_FPS = 30
FFMPEG = "/opt/homebrew/bin/ffmpeg"

# ─── Helpers ─────────────────────────────────────────────────────────────────

def log(msg):
    print(f"  → {msg}")

def get_mp3_duration(filepath):
    """Get duration of an MP3 file using ffprobe."""
    try:
        result = subprocess.run(
            [FFMPEG.replace("ffmpeg", "ffprobe"), "-v", "quiet", "-show_entries",
             "format=duration", "-of", "csv=p=0", str(filepath)],
            capture_output=True, text=True
        )
        return float(result.stdout.strip())
    except Exception:
        return 0.0


# ─── Step 1: Export Slides ───────────────────────────────────────────────────

def export_slides():
    """Export Slidev presentation to PDF, then convert to PNG images."""
    print("\n╔══════════════════════════════════════╗")
    print("║  Step 1: Exporting Slides to Images  ║")
    print("╚══════════════════════════════════════╝\n")

    SLIDES_DIR.mkdir(parents=True, exist_ok=True)
    pdf_path = BASE_DIR / "slides.pdf"

    # Export to PDF using slidev
    log("Exporting Slidev presentation to PDF...")
    slidev_bin = PROJECT_DIR / "node_modules" / ".bin" / "slidev"

    result = subprocess.run(
        [str(slidev_bin), "export", "--output", str(pdf_path),
         "--timeout", "120000"],
        cwd=str(PROJECT_DIR),
        capture_output=True, text=True, timeout=300
    )

    if result.returncode != 0:
        print(f"  ⚠ Slidev export stderr: {result.stderr[:500]}")
        # Try alternative: use --format png if available
        result2 = subprocess.run(
            [str(slidev_bin), "export", "--format", "png",
             "--output", str(SLIDES_DIR), "--timeout", "120000"],
            cwd=str(PROJECT_DIR),
            capture_output=True, text=True, timeout=300
        )
        if result2.returncode != 0:
            print(f"  ✗ Slidev export failed. Please export manually:")
            print(f"    cd {PROJECT_DIR}")
            print(f"    npx slidev export --format png --output {SLIDES_DIR}")
            print(f"    OR: npx slidev export --output {pdf_path}")
            return False

    if pdf_path.exists():
        log(f"PDF exported: {pdf_path}")
        # Convert PDF to PNGs using sips (macOS) or ffmpeg
        log("Converting PDF pages to PNG images...")
        convert_pdf_to_pngs(pdf_path)
    else:
        # Check if PNGs were exported directly
        pngs = sorted(SLIDES_DIR.glob("*.png"))
        if pngs:
            log(f"Found {len(pngs)} PNG slides exported directly.")
        else:
            print("  ✗ No slides found. Export manually.")
            return False

    pngs = sorted(SLIDES_DIR.glob("*.png"))
    log(f"Total slide images: {len(pngs)}")
    return True


def convert_pdf_to_pngs(pdf_path):
    """Convert a PDF to individual PNG images using sips/Quartz on macOS."""
    SLIDES_DIR.mkdir(parents=True, exist_ok=True)

    # Try using Python + subprocess with sips (macOS native)
    # First, split PDF into pages using Python
    try:
        # Use macOS Quartz via Python to split PDF
        result = subprocess.run(
            ["python3", "-c", f"""
import subprocess, os
from pathlib import Path

pdf = "{pdf_path}"
out_dir = "{SLIDES_DIR}"

# Use sips to convert (only works on single-page, so we need to split first)
# Alternative: use Quartz PDFKit
import Quartz
from CoreFoundation import CFURL, kCFAllocatorDefault

pdf_url = CFURL.fileURLWithPath_(pdf)
pdf_doc = Quartz.CGPDFDocumentCreateWithURL(pdf_url)

if pdf_doc is None:
    print("Failed to open PDF")
    exit(1)

num_pages = Quartz.CGPDFDocumentGetNumberOfPages(pdf_doc)
print(f"PDF has {{num_pages}} pages")

for i in range(1, num_pages + 1):
    page = Quartz.CGPDFDocumentGetPage(pdf_doc, i)
    if page is None:
        continue

    rect = Quartz.CGPDFPageGetBoxRect(page, Quartz.kCGPDFMediaBox)
    w, h = int(rect.size.width), int(rect.size.height)

    # Scale to 1920x1080
    scale_x = {VIDEO_WIDTH} / w
    scale_y = {VIDEO_HEIGHT} / h
    scale = min(scale_x, scale_y)
    new_w = int(w * scale)
    new_h = int(h * scale)

    color_space = Quartz.CGColorSpaceCreateDeviceRGB()
    ctx = Quartz.CGBitmapContextCreate(
        None, {VIDEO_WIDTH}, {VIDEO_HEIGHT}, 8, {VIDEO_WIDTH} * 4,
        color_space,
        Quartz.kCGImageAlphaPremultipliedFirst
    )

    # White background
    Quartz.CGContextSetRGBFillColor(ctx, 1, 1, 1, 1)
    Quartz.CGContextFillRect(ctx, Quartz.CGRectMake(0, 0, {VIDEO_WIDTH}, {VIDEO_HEIGHT}))

    # Center the slide
    x_offset = ({VIDEO_WIDTH} - new_w) / 2
    y_offset = ({VIDEO_HEIGHT} - new_h) / 2
    Quartz.CGContextTranslateCTM(ctx, x_offset, y_offset)
    Quartz.CGContextScaleCTM(ctx, scale, scale)
    Quartz.CGContextDrawPDFPage(ctx, page)

    image = Quartz.CGBitmapContextCreateImage(ctx)
    out_path = os.path.join(out_dir, f"slide_{{i:03d}}.png")
    url = CFURL.fileURLWithPath_(out_path)
    dest = Quartz.CGImageDestinationCreateWithURL(url, "public.png", 1, None)
    Quartz.CGImageDestinationAddImage(dest, image, None)
    Quartz.CGImageDestinationFinalize(dest)
    print(f"  Exported slide {{i}}")
"""],
            capture_output=True, text=True, timeout=120
        )
        if result.returncode == 0:
            log("PDF conversion successful via Quartz.")
            print(result.stdout)
            return True
        else:
            print(f"  Quartz conversion error: {result.stderr[:300]}")
    except Exception as e:
        print(f"  Quartz method failed: {e}")

    # Fallback: use ffmpeg to convert PDF to images
    log("Trying ffmpeg PDF conversion...")
    result = subprocess.run(
        [FFMPEG, "-i", str(pdf_path), "-vf",
         f"scale={VIDEO_WIDTH}:{VIDEO_HEIGHT}:force_original_aspect_ratio=decrease,"
         f"pad={VIDEO_WIDTH}:{VIDEO_HEIGHT}:(ow-iw)/2:(oh-ih)/2:white",
         str(SLIDES_DIR / "slide_%03d.png")],
        capture_output=True, text=True, timeout=120
    )
    if result.returncode == 0:
        log("PDF conversion successful via ffmpeg.")
        return True

    print("  ✗ Could not convert PDF to PNGs automatically.")
    print("  Please install poppler: brew install poppler")
    print(f"  Then run: pdftoppm -png -r 300 {pdf_path} {SLIDES_DIR}/slide")
    return False


# ─── Step 2: Generate Audio ─────────────────────────────────────────────────

def generate_audio():
    """Generate TTS audio for each slide using ElevenLabs API."""
    print("\n╔══════════════════════════════════════╗")
    print("║  Step 2: Generating Narration Audio  ║")
    print("╚══════════════════════════════════════╝\n")

    AUDIO_DIR.mkdir(parents=True, exist_ok=True)

    with open(SCRIPT_FILE) as f:
        script = json.load(f)

    total = len(script)
    total_duration = 0.0

    for i, entry in enumerate(script):
        slide_num = entry["slide"]
        title = entry["title"]
        text = entry["narration"]
        out_file = AUDIO_DIR / f"slide_{slide_num:03d}.mp3"

        # Skip if already generated
        if out_file.exists() and out_file.stat().st_size > 1000:
            dur = get_mp3_duration(out_file)
            total_duration += dur
            log(f"[{i+1}/{total}] Slide {slide_num} — cached ({dur:.1f}s)")
            continue

        log(f"[{i+1}/{total}] Slide {slide_num}: {title}")

        # Call ElevenLabs TTS API
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVENLABS_VOICE_ID}"
        headers = {
            "xi-api-key": ELEVENLABS_API_KEY,
            "Content-Type": "application/json",
            "Accept": "audio/mpeg"
        }
        payload = {
            "text": text,
            "model_id": ELEVENLABS_MODEL,
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.75,
                "style": 0.2,
                "use_speaker_boost": True
            }
        }

        try:
            resp = requests.post(url, json=payload, headers=headers, timeout=60)
            if resp.status_code == 200:
                with open(out_file, "wb") as f:
                    f.write(resp.content)
                dur = get_mp3_duration(out_file)
                total_duration += dur
                log(f"  ✓ Generated ({dur:.1f}s, {len(resp.content)/1024:.0f} KB)")
            else:
                print(f"  ✗ ElevenLabs error {resp.status_code}: {resp.text[:200]}")
                # Rate limit handling
                if resp.status_code == 429:
                    log("  Rate limited. Waiting 30s...")
                    time.sleep(30)
                    # Retry once
                    resp = requests.post(url, json=payload, headers=headers, timeout=60)
                    if resp.status_code == 200:
                        with open(out_file, "wb") as f:
                            f.write(resp.content)
                        dur = get_mp3_duration(out_file)
                        total_duration += dur
                        log(f"  ✓ Retry succeeded ({dur:.1f}s)")
        except Exception as e:
            print(f"  ✗ Error: {e}")

        # Small delay to avoid rate limiting
        time.sleep(0.5)

    log(f"\nTotal narration duration: {total_duration:.1f}s ({total_duration/60:.1f} min)")
    return True


# ─── Step 3: Assemble Video ─────────────────────────────────────────────────

def assemble_video():
    """Combine slide images + audio into a final MP4 video."""
    print("\n╔══════════════════════════════════════╗")
    print("║  Step 3: Assembling Final Video      ║")
    print("╚══════════════════════════════════════╝\n")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    with open(SCRIPT_FILE) as f:
        script = json.load(f)

    slide_images = sorted(SLIDES_DIR.glob("slide_*.png"))
    if not slide_images:
        print("  ✗ No slide images found. Run --step export first.")
        return False

    log(f"Found {len(slide_images)} slide images")

    # Build list of (image_path, audio_path, duration) for each segment
    segments = []
    concat_list = OUTPUT_DIR / "concat.txt"

    for i, entry in enumerate(script):
        slide_num = entry["slide"]
        audio_file = AUDIO_DIR / f"slide_{slide_num:03d}.mp3"
        # Map slide number to image file (1-indexed)
        image_file = SLIDES_DIR / f"slide_{slide_num:03d}.png"

        if not image_file.exists():
            # Try to find closest match
            if slide_num <= len(slide_images):
                image_file = slide_images[slide_num - 1]
            else:
                image_file = slide_images[-1]

        if not audio_file.exists():
            log(f"  ⚠ Missing audio for slide {slide_num}, skipping")
            continue

        duration = get_mp3_duration(audio_file)
        if duration < 0.5:
            log(f"  ⚠ Audio too short for slide {slide_num}: {duration:.1f}s")
            continue

        # Add 1.0s padding after each slide for breathing room
        segments.append({
            "slide": slide_num,
            "image": str(image_file),
            "audio": str(audio_file),
            "duration": duration + 1.0  # 1s pause between slides
        })

    log(f"Processing {len(segments)} segments")

    # Generate individual video segments
    segment_files = []
    for i, seg in enumerate(segments):
        seg_file = OUTPUT_DIR / f"seg_{seg['slide']:03d}.mp4"
        segment_files.append(str(seg_file))

        if seg_file.exists() and seg_file.stat().st_size > 1000:
            log(f"  [{i+1}/{len(segments)}] Slide {seg['slide']} — cached")
            continue

        log(f"  [{i+1}/{len(segments)}] Slide {seg['slide']} ({seg['duration']:.1f}s)")

        # Create video segment: static image + audio
        # -loop 1: loop input image
        # -t: duration (audio duration + padding)
        # -shortest: stop when audio ends
        cmd = [
            FFMPEG, "-y",
            "-loop", "1",
            "-i", seg["image"],
            "-i", seg["audio"],
            "-c:v", "libx264",
            "-tune", "stillimage",
            "-c:a", "aac",
            "-b:a", "192k",
            "-vf", f"scale={VIDEO_WIDTH}:{VIDEO_HEIGHT}:force_original_aspect_ratio=decrease,"
                   f"pad={VIDEO_WIDTH}:{VIDEO_HEIGHT}:(ow-iw)/2:(oh-ih)/2:color=white,"
                   f"format=yuv420p",
            "-t", str(seg["duration"]),
            "-pix_fmt", "yuv420p",
            "-r", str(VIDEO_FPS),
            str(seg_file)
        ]

        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        if result.returncode != 0:
            print(f"    ✗ ffmpeg error: {result.stderr[:300]}")
            continue

    # Create concat file
    with open(concat_list, "w") as f:
        for sf in segment_files:
            if Path(sf).exists():
                f.write(f"file '{sf}'\n")

    # Concatenate all segments
    output_file = OUTPUT_DIR / "Diffusion_Policy_Lecture_Full.mp4"
    log(f"\nConcatenating {len(segment_files)} segments into final video...")

    cmd = [
        FFMPEG, "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", str(concat_list),
        "-c:v", "libx264",
        "-crf", "20",
        "-preset", "medium",
        "-c:a", "aac",
        "-b:a", "192k",
        "-movflags", "+faststart",
        str(output_file)
    ]

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    if result.returncode != 0:
        print(f"  ✗ Concat error: {result.stderr[:500]}")
        return False

    # Get final video info
    duration = get_mp3_duration(output_file)
    size_mb = output_file.stat().st_size / (1024 * 1024)

    print(f"\n  ╔══════════════════════════════════════╗")
    print(f"  ║  ✓ Video Generated Successfully!      ║")
    print(f"  ╠══════════════════════════════════════╣")
    print(f"  ║  File: {output_file.name:<30}║")
    print(f"  ║  Duration: {duration/60:.1f} minutes{' ' * 20}║")
    print(f"  ║  Size: {size_mb:.0f} MB{' ' * 25}║")
    print(f"  ╚══════════════════════════════════════╝\n")

    # Cleanup segment files
    log("Cleaning up segment files...")
    for sf in segment_files:
        p = Path(sf)
        if p.exists():
            p.unlink()
    concat_list.unlink(missing_ok=True)

    log(f"Final video: {output_file}")
    return True


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Ghost Video Pipeline")
    parser.add_argument("--step", choices=["export", "audio", "video", "all"],
                        default="all", help="Which step to run")
    args = parser.parse_args()

    print("╔══════════════════════════════════════════════╗")
    print("║  Ghost Video Pipeline — Diffusion Policy     ║")
    print("║  Vizuara Modern Robot Learning Bootcamp       ║")
    print("╚══════════════════════════════════════════════╝")

    if args.step in ("export", "all"):
        if not export_slides():
            if args.step == "all":
                print("\n⚠ Slide export failed. Continuing with audio generation...")
                print("  You can export slides manually and re-run with --step video")

    if args.step in ("audio", "all"):
        generate_audio()

    if args.step in ("video", "all"):
        assemble_video()


if __name__ == "__main__":
    main()
