#!/usr/bin/env python3
"""Batch-generate PaperBanana figures for the World Models Paradigms lecture.
Only generates figures that don't already exist on disk.
"""
import asyncio
import shutil
import sys
import os
from pathlib import Path

sys.path.insert(0, "/Users/raj/Desktop/Course_Creator/.pip_packages")
os.chdir("/Users/raj/Desktop/Course_Creator")

from dotenv import load_dotenv
load_dotenv("/Users/raj/Desktop/Course_Creator/.env.local")

OUTPUT_DIR = Path("/Users/raj/Desktop/Robotics Research/world-models-paradigms-lecture/public/figures")

PALETTE_NOTE = (
    "Warm dark background (#1A1915), accent terracotta (#D97757), "
    "warm orange (#C4956A), teal (#7DA488), blue (#5B8CB8), purple (#9B7EC8), "
    "soft cream text (#E8DED0). Minimal, clean, educational, academic. "
    "NO emoji. Sans-serif labels. Subtle drop shadows. "
)

FIGURES = [
    # === Paradigm A figures ===
    ("three-categories-taxonomy.png",
     f"A horizontal comparison diagram of THREE categories of world-model-based robot learning, arranged left-to-right. CATEGORY 1 (left, orange #D97757): 'Paradigm A: Video → Inverse Dynamics' — two boxes stacked vertically: a big 'Video Diffusion Model' box producing a filmstrip of 4 small frames, then an arrow DOWN to a small 'Inverse Dynamics MLP' box outputting an action symbol. Label 'Two separate models'. CATEGORY 2 (center, blue #5B8CB8): 'Model-Based RL' — two boxes side by side: 'World Model (RSSM/Latent)' connected by double arrows to 'Policy MLP'. Label 'Two networks, coupled by RL training. Examples: Dreamer, DINO-WM, IRIS, DIAMOND'. CATEGORY 3 (right, teal #7DA488): 'Paradigm B: Joint World-Action Model' — one single big box labeled 'One Model — Joint Denoiser' showing video latents AND action latents being denoised together in the same forward pass. Label 'One network emits both'. {PALETTE_NOTE}",
     "Visualize the three categories of world-model-based robot learning side by side, showing how Paradigm A, MBRL, and Paradigm B differ architecturally."),

    ("paradigm-a-pipeline.png",
     f"An educational flowchart showing the generic Paradigm A two-stage pipeline. LEFT: inputs as two small boxes stacked vertically — 'Text: pour the tea' and 'First frame (small image of a teapot on a table)'. Middle-left: big terracotta box labeled 'Video Diffusion Model'. Arrow into middle: filmstrip of 8 generated frames showing a teapot pouring into a cup (sequential frames of the motion). Middle-right: blue box labeled 'Inverse Dynamics Model (tiny MLP)'. Arrow into right: an action trajectory as a sequence of 7 action vectors (small boxes). Caption below the big video-diffusion box: 'Foundation model (internet-scale prior)'. Caption below the inverse dynamics box: 'Small model (robot data only)'. {PALETTE_NOTE}",
     "Show the generic Paradigm A pipeline: text+image -> video diffusion -> filmstrip -> inverse dynamics -> action sequence."),

    ("unipi-overview.png",
     f"A detailed architecture diagram of UniPi showing its two-stage pipeline. TOP row labeled 'Stage 1: Text-Conditioned Video Diffusion'. Left: two input boxes - 'Language: put the red block on the green block' (blue box) and 'First Frame o_0' (small image of blocks on a table). Arrows into a large terracotta 3D U-Net box labeled 'Video Diffusion (3D U-Net)'. Right output: a filmstrip of 16 frames showing the block manipulation unfolding, labeled 'τ̂ = [o_0, o_1, ..., o_15]'. BOTTOM row labeled 'Stage 2: Inverse Dynamics'. Shows two adjacent frames (o_t, o_{{t+1}}) feeding into a small blue 'Inverse Dynamics MLP' box, outputting 'a_t' (action vector). Arrows indicating that this runs for each adjacent frame pair across the video. Clean educational diagram. {PALETTE_NOTE}",
     "Show the full UniPi architecture: text + first frame -> 3D U-Net video diffusion -> 16-frame video -> adjacent frame pairs -> inverse dynamics MLP -> actions."),

    ("unipi-architecture.png",
     f"A clean block diagram of the UniPi 3D U-Net video diffusion model, focusing on internal structure. CENTER: a U-shaped architecture with encoder arm (descending) and decoder arm (ascending). Each block shows spatial dimensions shrinking while time axis is preserved: 24×40×16 → 12×20×16 → 6×10×16 → 3×5×16 (bottleneck) → 6×10×16 → 12×20×16 → 24×40×16. Skip connections drawn as horizontal arrows. CROSS-ATTENTION arrows from a text embedding box on the top-left feed into every level. Channel-wise concat from 'first frame o_0' shown at the leftmost input. Labels: 'Space conv + Time conv at each block'. {PALETTE_NOTE}",
     "Show the UniPi 3D U-Net architecture with space+time convolutions, cross-attention from text, and channel-wise first-frame conditioning."),

    ("unipi-hierarchical.png",
     f"An educational diagram showing UniPi's hierarchical temporal super-resolution. THREE stacked rows, top to bottom, each a horizontal filmstrip. ROW 1 (top, labeled 'Coarse video — 16 frames, 2s apart'): 16 sparsely-sampled frames showing a robot arm at keyframes of a long task (initial, mid-grasp, mid-pour, final). Large time gaps between frames indicated visually by whitespace. ROW 2 (middle, labeled 'After 1st temporal super-resolution — 64 frames'): same frames but with 3 intermediate frames interpolated between each original pair. ROW 3 (bottom, labeled 'Final dense video — 256 frames'): smooth continuous filmstrip with many frames. Arrows between rows labeled 'Temporal Super-Resolution Diffusion'. On the right, a label says 'Coarse plan → refined trajectory. Emergent hierarchy in pixel space.' {PALETTE_NOTE}",
     "Visualize UniPi's coarse-to-fine hierarchical video generation: sparse coarse video gets temporally super-resolved twice into a dense video."),

    ("unipi-combinatorial.png",
     f"A bar chart comparison showing UniPi's combinatorial generalization result. X-axis: two groups of bars, 'Seen Combinations' (left) and 'Held-out Combinations' (right). Within each group, two bars side by side: 'Transformer BC' (muted red, #D4543A) and 'UniPi' (teal, #7DA488). For 'Seen': BC ≈ 85, UniPi ≈ 88. For 'Held-out': BC ≈ 20 (small bar), UniPi ≈ 80 (large bar). Y-axis: 'Success Rate (%)'. Above the chart, a small legend showing example task: 'place [color] [shape] on [color] [shape]' with a small composite image of colored shapes. Below the chart, a caption: 'UniPi generalizes to novel combinations. Pixel-space composition beats action-space baking.' Clean chart style. {PALETTE_NOTE}",
     "Bar chart showing UniPi vs Transformer BC on seen vs held-out combinatorial tasks: UniPi dramatically wins on held-out combinations."),

    ("susie-overview.png",
     f"An educational diagram contrasting SuSIE with UniPi. TOP (muted, labeled 'UniPi (16 frames)'): a long filmstrip of 16 frames dreaming a full manipulation task, with a small label '16× generation cost'. BOTTOM (highlighted, labeled 'SuSIE (1 subgoal image)'): just the CURRENT frame on the left, then an arrow to a SINGLE subgoal image ~2 seconds in the future (highlighted with teal border), then an arrow to a goal-conditioned diffusion policy box outputting action chunks. Between current and subgoal: label 'InstructPix2Pix (image-editing diffusion)'. Below subgoal: label 'Goal-Conditioned Diffusion Policy closes the 2s gap'. On the right: 'Loop: re-query subgoal every 2s (receding horizon)'. {PALETTE_NOTE}",
     "Compare UniPi's full video generation with SuSIE's single subgoal image approach, showing the InstructPix2Pix editor and goal-conditioned policy."),

    ("susie-instructpix2pix.png",
     f"A two-phase diagram showing how SuSIE transfers InstructPix2Pix knowledge. TOP PHASE labeled 'InstructPix2Pix pretraining (internet)': three example triplets shown in rows — (image of beach, 'make it winter', edited winter beach); (image of room, 'add a dog', edited with dog); (image of scene, 'move cup left', edited cup shifted). Arrow labeled 'Pretrained on MILLIONS of internet edit triplets'. BOTTOM PHASE labeled 'SuSIE fine-tuning (robot)': now the model is shown being fine-tuned — input (current robot frame), edit instruction (task: 'put block on plate'), output (frame 2s later showing block on plate). Arrow labeled 'Fine-tune on robot demos. Transfers scene + object priors.' {PALETTE_NOTE}",
     "Show how SuSIE leverages InstructPix2Pix's internet-scale image editing prior and transfers it via fine-tuning to produce robot subgoal images."),

    ("hip-three-levels.png",
     f"A vertical three-level hierarchical planning diagram. LEVEL 1 (top, purple #9B7EC8): a large box labeled 'LLM — Language Subgoal Planner'. Input: 'Task: make a salad' text. Output: a numbered list of subgoals: '1. wash lettuce, 2. chop tomato, 3. mix in bowl'. LEVEL 2 (middle, terracotta #D97757): a box labeled 'Video Diffusion Model — Visual Planner'. Input arrow from LEVEL 1 with one subgoal highlighted. Output: a short filmstrip of 8 frames depicting the chopping action visually. LEVEL 3 (bottom, teal #7DA488): box labeled 'Inverse Dynamics Model — Motor Executor'. Input arrows from LEVEL 2 filmstrip pairs. Output: a sequence of action vectors. Vertical arrows flow top-to-bottom between levels. On the right side of the diagram: a small bracket label saying 'Three specialists, each a pretrained foundation model'. {PALETTE_NOTE}",
     "Show HiP's three hierarchical levels: LLM for language planning, video diffusion for visual planning, inverse dynamics for actions."),

    ("hip-iterative-refinement.png",
     f"A circular/cyclic refinement diagram showing HiP's iterative consistency process. FOUR nodes arranged in a circle with arrows flowing clockwise. Node 1 (top, purple): 'LLM proposes language subgoal'. Node 2 (right, orange): 'Video Model dreams video of subgoal'. Node 3 (bottom, blue): 'VLM + Dynamics Model score consistency' with two sub-labels: 'Semantic score: does video match LLM subgoal?' and 'Physical score: is motion feasible?'. Node 4 (left, red if low, teal if high): 'If low score → RESAMPLE. If high → execute.' A feedback arrow goes back from Node 4 up to Node 1. Center of circle: label 'Iterative Consistency Loop'. Side panel with small text: 'Ablation: removing this drops success by 20-30%.' {PALETTE_NOTE}",
     "Visualize HiP's iterative consistency refinement as a cyclic loop: LLM -> Video -> Scoring -> Resample if inconsistent."),

    ("gr1-architecture.png",
     f"A clean architecture diagram of GR-1 showing a causal transformer processing an interleaved token sequence. BOTTOM row: horizontal token sequence with alternating token types (labeled): [lang_1 ... lang_5] [o_1 patches (blue)] [s_1 (orange)] [a_1 (green)] [o_2 patches] [s_2] [a_2] [o_3 patches] ... Each token is a small colored square. ABOVE: a large rectangular block labeled 'Causal Transformer (shared backbone)' spanning the full width, with attention arrows drawn among tokens (only looking backward). ABOVE THE TRANSFORMER: two prediction heads — 'Pixel Head → reconstructs next image' (on the left, blue) and 'Action Head → predicts next action' (on the right, orange). Both heads split off from the transformer output. Below: formula 'L = L_pixel + λ · L_action'. {PALETTE_NOTE}",
     "Show the GR-1 architecture: interleaved language/observation/state/action tokens flowing through one causal transformer with two output heads for pixels and actions."),

    ("gr1-two-stage.png",
     f"A horizontal two-stage training pipeline diagram. LEFT STAGE labeled 'Stage 1: Ego4D Pretraining': a box showing a collage of egocentric human video thumbnails (cooking, cleaning, using hands). Below: '~800K clips, action-free video'. Only the 'Pixel Loss' is highlighted, 'Action Loss' is greyed out. RIGHT STAGE labeled 'Stage 2: Robot Fine-tuning (CALVIN + RT-1)': a box showing robot arm workspace thumbnails. Below: 'action-labeled robot demos'. Both 'Pixel Loss' AND 'Action Loss' highlighted. Arrow between stages labeled 'Transfer the learned dynamics prior'. Below: a small label 'Ablation: 60-70% of final gain comes from Stage 1.' {PALETTE_NOTE}",
     "Illustrate GR-1's two-stage training: action-free Ego4D pretraining then joint robot fine-tuning, highlighting which losses are active at each stage."),

    ("gr1-calvin-results.png",
     f"A clean bar chart comparing policy performance on the CALVIN chain-of-5-subtasks benchmark. Y-axis: 'Chain Success Rate (%)'. Bars from left to right: 'HULC (prior SOTA)' ≈ 47 (muted blue), 'GR-1 (no pretrain)' ≈ 50 (warm orange, shaded like baseline), 'GR-1 (Ego4D pretrained)' ≈ 94 (bold teal, tall bar). Above the bars, visible callouts: 'Success = ALL 5 subtasks correct in sequence'. Below the chart: 'Pretraining IS the method.' Clean minimal bar chart style. {PALETTE_NOTE}",
     "Bar chart of CALVIN chain-success results showing HULC ~47%, GR-1 without pretrain ~50%, and GR-1 with Ego4D pretraining ~94%."),

    ("vpp-features.png",
     f"A side-by-side comparison diagram. LEFT panel labeled 'UniPi / SuSIE: full generation': shows a video diffusion model running through all denoising steps (multiple iterations of noise → clean frames), producing a final video. A bracket annotation: 'Expensive at inference'. RIGHT panel labeled 'VPP: stop early, use latent features': shows the same video diffusion model but the denoising process stops at an intermediate step (shown partially-denoised noisy-video), and an arrow extracts the internal U-Net activations as a 'feature vector'. That feature vector feeds into a small diffusion ACTION policy that outputs actions directly. Label: 'One forward pass. Use latent of imagination, not pixels.' {PALETTE_NOTE}",
     "Compare full video generation (UniPi/SuSIE) vs VPP's early-stopped feature extraction that feeds into a diffusion action policy."),

    # === Paradigm B figures (Cosmos only — DreamZero figures already copied from existing lecture) ===
    ("cosmos-overview.png",
     f"An overview diagram of NVIDIA Cosmos World Foundation Model platform. CENTER: a large terracotta rectangle labeled 'Cosmos — World Foundation Model Platform' with subtext '20M+ hours of video, physical-AI focused'. THREE components branch out from the center as colored boxes: BOX 1 (top-left, teal): 'Cosmos Predict — autoregressive next-frame video model' with a small filmstrip icon. BOX 2 (top-right, blue): 'Cosmos Diffusion — text/action-conditioned video diffusion' with a noise→image icon. BOX 3 (bottom, orange): 'Cosmos Tokenizer — CV8×8×8 VAE for video compression' with a compression arrow icon. AT THE BOTTOM, below the whole diagram: a horizontal list of derivative models: 'DreamZero · GR00T Dreams · WFM · Custom fine-tunes' with arrows pointing UP to the Cosmos platform, indicating they're all built on it. Clean educational. {PALETTE_NOTE}",
     "Overview of the NVIDIA Cosmos platform: Predict, Diffusion, and Tokenizer as three components with downstream robotics models built on top."),

    # === SO-101 build story figures ===
    ("so101-data-pipeline.png",
     f"A horizontal left-to-right data pipeline diagram showing the SO-101 data conversion process. STAGE 1 (far left, blue): 'HuggingFace LeRobot v3.0 dataset' — icon of a cloud with HF logo, subtext '400 episodes concatenated in 1 parquet + 3 videos (front/gripper/top)'. Arrow labeled 'Download (4.5 GB)'. STAGE 2 (center-left, orange): 'Parquet splitting' — shows a big parquet file breaking into 400 small per-episode parquets, subtext '<1 second'. STAGE 3 (center, teal): 'Video splitting' — shows 3 concatenated video files being decoded (162 GB RAM) and re-sliced into 400×3 = 1200 per-episode h264 MP4s, subtext '~2 hours'. STAGE 4 (center-right, purple): 'GEAR metadata generation' — shows JSON files being written: 'modality.json, embodiment.json, stats.json, tasks.jsonl, episodes.jsonl, info.json'. STAGE 5 (far right, accent): 'DreamZero-ready dataset' — showing a clean folder icon labeled 'so101_gear/' with tick marks. {PALETTE_NOTE}",
     "Visualize the SO-101 data conversion pipeline: HF LeRobot v3.0 -> parquet split -> video split -> GEAR metadata -> DreamZero-ready dataset.")
]


async def generate_one(idx, filename, description, intent):
    from paperbanana import PaperBananaPipeline, GenerationInput, DiagramType
    from paperbanana.core.config import Settings

    output_path = OUTPUT_DIR / filename
    if output_path.exists():
        print(f"[{idx+1}/{len(FIGURES)}] SKIP (exists): {filename}")
        return filename

    print(f"[{idx+1}/{len(FIGURES)}] Generating: {filename}...")

    settings = Settings(
        vlm_model="gemini-2.5-flash",
        image_model="gemini-3-pro-image-preview",
        refinement_iterations=2,
        output_dir=str(OUTPUT_DIR / "pb_outputs"),
        output_resolution="2k",
    )

    pipeline = PaperBananaPipeline(settings=settings)
    result = await pipeline.generate(
        GenerationInput(
            source_context=description,
            communicative_intent=intent,
            diagram_type=DiagramType.METHODOLOGY,
        )
    )

    src = Path(result.image_path)
    shutil.copy2(str(src), str(output_path))
    print(f"[{idx+1}/{len(FIGURES)}] DONE: {filename}")
    return filename


async def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    semaphore = asyncio.Semaphore(3)

    async def bounded(idx, fn, desc, intent):
        async with semaphore:
            try:
                return await generate_one(idx, fn, desc, intent)
            except Exception as e:
                print(f"[{idx+1}/{len(FIGURES)}] FAILED: {fn} — {e}")
                return None

    tasks = [bounded(i, fn, desc, intent) for i, (fn, desc, intent) in enumerate(FIGURES)]
    results = await asyncio.gather(*tasks)
    done = [r for r in results if r]
    failed = [FIGURES[i][0] for i, r in enumerate(results) if not r]

    print(f"\n{'='*60}")
    print(f"Generated: {len(done)}/{len(FIGURES)}")
    if failed:
        print(f"Failed: {failed}")
    print(f"Output: {OUTPUT_DIR}")


if __name__ == "__main__":
    asyncio.run(main())
