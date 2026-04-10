"""Generate PaperBanana figures for the DIAMOND section of the lecture."""
import asyncio
import os
import sys
from pathlib import Path

# Load env from PaperBanana project
from dotenv import load_dotenv
load_dotenv("/Users/raj/Desktop/Course_Creator/.env.local")

from paperbanana import PaperBananaPipeline, GenerationInput, DiagramType
from paperbanana.core.pipeline import Settings

FIGURES_DIR = Path(__file__).parent / "public" / "figures"
FIGURES_DIR.mkdir(parents=True, exist_ok=True)

settings = Settings(
    vlm_model="gemini-2.0-flash",
    image_model="gemini-3-pro-image-preview",
    refinement_iterations=2,
)

FIGURES = [
    {
        "name": "diamond-big-picture",
        "description": """A clean "big picture" diagram for DIAMOND (Diffusion as a Model of Environment Dreams).
        LEFT side (labeled 'IRIS — Discrete Tokens'): Small Atari Asterix frame → VQ-VAE tokenizer → grid of 64 discrete codebook indices → GPT transformer predicting next tokens → decoded next frame (slightly blocky/blurry, with tiny sprites missing). Small label: 'Lossy quantization. Small rewards get averaged out.'
        RIGHT side (labeled 'DIAMOND — Diffusion in Pixel Space'): Same Atari Asterix frame → stacked with 3 past frames along channel dimension → a U-Net denoiser box labeled 'EDM Diffusion' → predicted next frame that is crisp with all small sprites intact. Small label: 'Direct pixel-space prediction. Visual details preserved.'
        At the top, paper title banner: 'DIAMOND: Visual Details Matter in Atari (NeurIPS 2024 Spotlight)'.
        At the bottom, headline result: 'Mean Human-Normalized Score: 1.46 on Atari 100K — new SOTA for agents trained entirely in a world model.'
        Use warm academic palette: rust (#c2785c), teal (#6a9a5b), blue (#5a7fa5), cream background (#faf8f5). Clean rounded boxes, readable labels.""",
        "intent": "Give students an immediate visual understanding of DIAMOND's core contribution: replacing discrete-token world modeling (IRIS) with continuous pixel-space diffusion, and why that preserves the tiny visual details that matter for Atari rewards.",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "diamond-architecture",
        "description": """A detailed architecture diagram of DIAMOND's diffusion denoiser for next-frame prediction.
        LEFT INPUTS (stacked vertically):
        1. Past observations o_{t-3}, o_{t-2}, o_{t-1}, o_t — shown as 4 small 64x64 RGB frames stacked along a channel axis arrow labeled 'Channel concat: L=4 past frames = 12 channels'.
        2. Noisy target frame x_tau — one frame labeled 'noisy next obs (σ)' (shown with visible noise grain). Arrow labeled '+ 3 channels'.
        3. Past actions a_{t-3}, a_{t-2}, a_{t-1}, a_t — shown as 4 discrete action tokens. Arrow labeled 'Embedding table → 256-dim'.
        4. Noise level σ — shown as a scalar arrow labeled 'log σ / 4 → sinusoidal embedding'.

        CENTER: A U-Net 2D box labeled 'Conv U-Net Denoiser (~4.4 M params)'. Inside: 4-level encoder/decoder with 64 channels per level, 2 residual blocks each. Arrows showing actions + noise embedding flowing into 'Adaptive GroupNorm' in every residual block.

        RIGHT OUTPUT: Predicted clean next frame x_0, shown as a crisp 64x64 image.

        BELOW THE MAIN FIGURE: A small formula box showing the EDM output combining:
        D_θ(x;σ) = c_skip(σ) · x + c_out(σ) · F_θ(c_in(σ)·x, c_noise(σ))

        And a key insight callout: 'Simple pure-conv U-Net with channel concatenation for frames and AdaGN for actions — no attention needed at 64×64.'

        Warm academic palette, cream background. Use rust (#c2785c) for trainable components, teal (#6a9a5b) for conditioning inputs, blue (#5a7fa5) for outputs.""",
        "intent": "Show students the exact way DIAMOND conditions its U-Net denoiser on past frames (channel concat), past actions (AdaGN via learned embedding), and noise level — with the EDM preconditioning formula visible.",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "diamond-edm-vs-ddpm",
        "description": """A two-panel comparison showing why EDM enables low-step diffusion where DDPM fails.
        LEFT PANEL (labeled 'DDPM — Noise Prediction (Unstable at Low Steps)'):
        - A graph with x-axis = 'Noise level σ' and y-axis = 'Model output target'.
        - A curve showing that when σ ≫ σ_data, the noise target ε_θ degenerates toward the input itself (identity function) — the curve flattens to the input line.
        - Text callout: 'At high noise, predicting the noise ≈ predicting the input itself. The clean-image estimate is nearly useless.'
        - Three small reconstructed images shown below for 1/3/50 denoising steps: 1 step = garbage, 3 steps = blurry, 50 steps = sharp.

        RIGHT PANEL (labeled 'EDM — Preconditioned Output (Stable at Low Steps)'):
        - Same graph axes.
        - A curve showing that the EDM-parameterized output D_θ remains close to the clean image x_0 target across all noise levels. The curve stays meaningful.
        - Text callout with the formula: 'D_θ(x;σ) = c_skip·x + c_out·F_θ(c_in·x, c_noise)' and 'c_skip and c_out are σ-dependent so the network target is always the clean image.'
        - Three small reconstructed images shown below for 1/3/50 denoising steps: 1 step = slightly soft but recognizable, 3 steps = crisp, 50 steps = crisp (no improvement).

        Header banner: 'Why DIAMOND uses EDM (Karras 2022), not DDPM.'
        Footer banner: 'Result: DIAMOND needs only 3 denoising steps per frame vs 16+ for DDPM — 5× cheaper rollouts.'

        Warm palette with a clear visual contrast: rust (#c2785c) for DDPM's failure mode, teal (#6a9a5b) for EDM's success. Cream background.""",
        "intent": "Make students understand, visually and intuitively, why EDM's preconditioning makes low-step diffusion stable — a pedagogical core of the DIAMOND paper.",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "diamond-mode-collapse",
        "description": """A two-column illustration from the DIAMOND paper showing the 1-step vs 3-step trade-off on Atari Boxing.
        LEFT COLUMN (labeled '1 Denoising Step — Mode Averaging'):
        - Top: Past frame of Atari Boxing showing the two fighters (white agent, black opponent).
        - Middle: A predicted next frame where the WHITE player (controlled by the agent's action) is crisp and clear, but the BLACK opponent is a ghostly SMEAR — clearly three overlapping ghost copies of the opponent in different poses. Caption arrow: 'Opponent's motion is stochastic → MSE averages all modes → blur.'
        - Bottom: Small text box: 'Single-step denoising interpolates between all possible futures and produces the pixel-wise mean — a blurry smear.'

        RIGHT COLUMN (labeled '3 Denoising Steps — Mode Selection'):
        - Top: Same past Boxing frame.
        - Middle: A predicted next frame where BOTH fighters are crisp. The opponent is shown in one specific committed pose. Caption arrow: 'First step commits to a seed → later steps refine that one mode → crisp.'
        - Bottom: Small text box: 'Multi-step sampling drives generation toward a particular mode — each rollout samples a different possible future, preserving stochasticity at the trajectory level.'

        CENTER DIVIDER: A small equation bar: '∂L/∂x_0 over all modes → conditional mean → blur' on left side and 'Iterative refinement → sample one mode → crisp' on right side.

        HEADER: 'DIAMOND Figure 4: Why 3 Steps Is the Magic Number'

        Warm academic palette. Use a faded/ghost effect for the blurry opponent on the left to make the averaging visible.""",
        "intent": "Explain intuitively why DIAMOND uses 3 denoising steps specifically — the 1-step averaging failure mode vs the 3-step mode selection success — so students understand the trade-off between compute and sample diversity.",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "diamond-training-loop",
        "description": """A detailed training loop diagram for DIAMOND.
        A circular / cyclic flowchart with 5 numbered stages arranged around a center circle:

        1. 'Collect' (top, teal): Real Atari environment → random rollout with current policy → replay buffer (shown as a film roll of (obs, action, reward, done) tuples). Label: '100 steps per epoch.'

        2. 'Train Denoiser' (right, rust): Buffer → sample batch of 32 trajectories → sample noise level log σ ~ N(-0.4, 1.2²) → apply EDM preconditioning → MSE denoising loss. Label: '400 grad steps / epoch, AdamW lr=1e-4.'

        3. 'Train Reward & End' (bottom-right, blue): Buffer → CNN-LSTM reward/termination model → cross-entropy losses. Label: 'Separate from diffusion.'

        4. 'Dream Rollouts' (bottom-left, purple): Real start state → denoiser autoregressively generates 15 imagined frames, each with 3 Euler steps → actor outputs action at each step → reward + end model scores them. Label: 'Horizon = 15 imagined steps.'

        5. 'Train Actor-Critic' (left, teal): Imagined rollouts → REINFORCE with value baseline + λ-returns Bellman target → updates policy π_φ and value V_φ. Label: '5000 grad steps first epoch, 400 / epoch after. γ=0.985, λ=0.95.'

        CENTER CIRCLE: 'DIAMOND Training Loop' with a diamond icon. An arrow from stage 5 loops back to stage 1 labeled 'Better policy → better data'.

        HEADER: 'DIAMOND Atari 100K training loop (~2.9 days on a single RTX 4090 per game).'

        Warm academic palette, cream background. Clean arrows, rounded boxes, readable font.""",
        "intent": "Show students the complete training loop of DIAMOND, making it clear how the denoiser, reward model, and actor-critic interact, and that all three are trained jointly with imagined rollouts feeding the policy update.",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "diamond-vs-iris-results",
        "description": """A results comparison infographic between DIAMOND and IRIS on Atari 100K.
        LEFT SECTION: A horizontal bar chart comparing Mean Human-Normalized Score on Atari 100K:
        - Human: 1.00 (grey reference line)
        - IRIS (2023): 1.05
        - DIAMOND (2024): 1.46 ← highlighted in rust (#c2785c) as the winner.
        Labels: 'Mean HNS on 26 Atari games (100K env steps = 2 hours of gameplay).'

        RIGHT SECTION: A side-by-side per-game comparison (vertical bars, 3 games):
        - Asterix: IRIS 853 | DIAMOND 3698 (4.3× better)
        - Breakout: IRIS 83 | DIAMOND 132 (1.6× better)
        - Road Runner: IRIS 9614 | DIAMOND 20673 (2.1× better)
        Each game shows tiny screenshots beside the bars.

        BOTTOM SECTION: A compact specs comparison:
        - Parameters: IRIS (~large transformer) | DIAMOND (~4.4M pure conv U-Net)
        - Steps per frame: IRIS 16 NFE | DIAMOND 3 NFE
        - Space: IRIS discrete tokens | DIAMOND continuous pixels
        - SOTA: Both were SOTA at release

        HEADER BANNER: 'DIAMOND vs IRIS: Smaller, Faster, Better on Atari 100K.'
        FOOTER: 'Key insight: 1-2 pixel sprite differences carry reward — diffusion preserves them, discrete tokenizers blur them.'

        Warm academic palette, cream background. Rust for DIAMOND, blue for IRIS, grey for human.""",
        "intent": "Show the headline numerical results: DIAMOND beats IRIS with fewer parameters and fewer compute steps per frame — concrete evidence for the 'visual details matter' thesis.",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "diamond-csgo",
        "description": """A diagram illustrating DIAMOND's CS:GO experiment — a fully playable neural Counter-Strike.
        TOP SECTION: A banner labeled 'DIAMOND CS:GO — A Playable Diffusion World Model' with a Counter-Strike Global Offensive screenshot composited on it.

        MIDDLE SECTION — Two-stage pipeline diagram:
        Stage 1 (labeled 'Dynamics Model — 330M params'):
        - Input: Past 4 frames at 56×30 low resolution + past 4 discrete actions (WASD + mouse).
        - U-Net denoiser → 3 EDM steps → predicted 56×30 frame.
        Stage 2 (labeled 'Upsampler — 51M params'):
        - Input: 56×30 predicted frame → U-Net denoiser → 10 EDM steps → 280×150 high-res output.

        BOTTOM SECTION — Training + demo stats (as info cards):
        - 'Data: 87 hours of human CS:GO deathmatch gameplay (~5.5M frames).'
        - 'Hardware: 1× RTX 4090.'
        - 'Training time: 12 days.'
        - 'Playback: 10 FPS real-time on RTX 3090.'
        - 'Players can walk, aim, shoot, interact — all inside the neural world model.'

        KEY INSIGHT CALLOUT: 'Same 3-step EDM recipe as the 4M Atari model — just scaled up by ~80× in parameters. Proof that the diffusion world-model recipe transfers across scales.'

        Warm academic palette, cream background. Include a subtle 'neural dream' grainy texture on the upsampled frame to hint at its generative origin.""",
        "intent": "Show that DIAMOND's recipe scales: the same method used for 4M-param Atari models also produces a playable 381M-param Counter-Strike environment, training in 12 days on a single 4090.",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "diamond-rollout-timeline",
        "description": """A horizontal timeline diagram showing a 15-step imagined rollout in DIAMOND, used to train the policy.
        LEFT EDGE: A real observation from an Atari game (e.g., Breakout) labeled 'Real start state from buffer'.

        CENTER: A left-to-right sequence of 15 imagined frames. Each frame shows:
        - A small Breakout screenshot that evolves over time (ball bouncing, paddle moving, bricks breaking).
        - Below each frame: the action the policy chose (e.g., NOOP, LEFT, RIGHT, FIRE).
        - Below that: a small tag 'r̂' with an imagined reward scalar.
        - Above each frame: a small '3 EDM steps' tag showing that each frame cost 3 denoising passes.

        Arrow between frames labeled 'D_θ(o_t, a_t, σ) → o_{t+1}'.

        RIGHT EDGE: The final imagined state, with a big arrow into a box labeled 'Actor-Critic Update: REINFORCE + λ-returns on the dreamed rollout.' showing the policy π_φ and value V_φ being updated.

        TOP BANNER: 'Imagined Rollouts for Dream RL (horizon = 15)'
        BOTTOM CALLOUT: 'The policy never touches the real environment during an update — all 15 steps are dreamed by the diffusion denoiser using only 3 EDM steps per frame.'

        Warm academic palette. Use a subtle 'dream' haze or glow around the imagined frames to visually distinguish them from the real start state on the far left.""",
        "intent": "Visually convey that DIAMOND's policy is trained entirely inside imagined rollouts — each one a 15-step chain of diffusion predictions — so students grasp that the real environment is only used for data collection, not for policy gradient steps.",
        "type": DiagramType.METHODOLOGY,
    },
]


async def generate_figure(pipeline, fig_spec):
    name = fig_spec["name"]
    output_path = FIGURES_DIR / f"{name}.png"

    if output_path.exists():
        print(f"  SKIP {name} (already exists)")
        return name, True

    print(f"  GENERATING {name}...")
    try:
        result = await pipeline.generate(
            GenerationInput(
                source_context=fig_spec["description"],
                communicative_intent=fig_spec["intent"],
                diagram_type=fig_spec["type"],
            )
        )
        if result and result.image_path:
            import shutil
            shutil.copy2(result.image_path, str(output_path))
            print(f"  DONE {name} -> {output_path}")
            return name, True
        else:
            print(f"  FAIL {name} — no image returned")
            return name, False
    except Exception as e:
        print(f"  FAIL {name} — {e}")
        return name, False


async def main():
    print(f"Generating {len(FIGURES)} DIAMOND figures...")
    pipeline = PaperBananaPipeline(settings=settings)

    semaphore = asyncio.Semaphore(3)

    async def limited_generate(fig):
        async with semaphore:
            return await generate_figure(pipeline, fig)

    tasks = [limited_generate(fig) for fig in FIGURES]
    results = await asyncio.gather(*tasks)

    succeeded = sum(1 for _, ok in results if ok)
    failed = sum(1 for _, ok in results if not ok)
    print(f"\nDone! {succeeded} succeeded, {failed} failed out of {len(FIGURES)} total.")

    if failed:
        print("Failed figures:")
        for name, ok in results:
            if not ok:
                print(f"  - {name}")


if __name__ == "__main__":
    asyncio.run(main())
