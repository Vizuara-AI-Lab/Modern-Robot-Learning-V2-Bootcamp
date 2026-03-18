#!/usr/bin/env python3
"""
Fallback slide exporter — uses playwright directly to screenshot each slide
from a running Slidev dev server.

Usage:
  1. Start slidev dev server: cd robotics-bootcamp-slides && npx slidev --port 3030
  2. Run this: python3 screenshot_slides.py
"""

import subprocess
import time
import sys
from pathlib import Path

SLIDES_DIR = Path(__file__).parent / "slides"
NUM_SLIDES = 91  # Total slides in presentation
PORT = 3030
WIDTH = 1920
HEIGHT = 1080


def main():
    SLIDES_DIR.mkdir(parents=True, exist_ok=True)

    # Use playwright via npx
    script = f"""
const {{ chromium }} = require('playwright-chromium');

(async () => {{
    const browser = await chromium.launch({{ headless: true }});
    const page = await browser.newPage();
    await page.setViewportSize({{ width: {WIDTH}, height: {HEIGHT} }});

    for (let i = 1; i <= {NUM_SLIDES}; i++) {{
        const url = `http://localhost:{PORT}/${{i}}`;
        try {{
            await page.goto(url, {{ waitUntil: 'networkidle', timeout: 15000 }});
            // Wait a bit for animations/rendering
            await page.waitForTimeout(1000);
        }} catch (e) {{
            console.log(`Slide ${{i}}: timeout (using domcontentloaded fallback)`);
            try {{
                await page.goto(url, {{ waitUntil: 'domcontentloaded', timeout: 10000 }});
                await page.waitForTimeout(2000);
            }} catch (e2) {{
                console.log(`Slide ${{i}}: skipped`);
                continue;
            }}
        }}

        const padded = String(i).padStart(3, '0');
        await page.screenshot({{
            path: `{SLIDES_DIR}/slide_${{padded}}.png`,
            type: 'png'
        }});
        console.log(`Slide ${{i}} exported`);
    }}

    await browser.close();
    console.log('Done!');
}})();
"""

    # Write temp script
    tmp_script = Path(__file__).parent / "_screenshot.js"
    tmp_script.write_text(script)

    print(f"Screenshotting {NUM_SLIDES} slides from localhost:{PORT}...")
    result = subprocess.run(
        ["node", str(tmp_script)],
        cwd=str(Path(__file__).parent.parent),
        capture_output=False,
        timeout=600
    )

    tmp_script.unlink(missing_ok=True)

    pngs = sorted(SLIDES_DIR.glob("slide_*.png"))
    print(f"\nExported {len(pngs)} slides to {SLIDES_DIR}")


if __name__ == "__main__":
    main()
