"""Generate all PaperBanana figures for the World Models lecture."""
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

# All figures with descriptions and communicative intent
FIGURES = [
    {
        "name": "three-paradigms",
        "description": """A clear academic diagram showing three world model paradigms side by side:
        LEFT: 'Action-Conditioned' — shows an observation box (camera icon) and action arrow feeding into a world model box, outputting predicted next state. Equation: x' = f(x, a). Examples listed: V-JEPA 2, DreamerV3, DINO-WM.
        CENTER: 'Video World Model + Inverse Dynamics' — shows observation feeding into world model generating video frames, then an inverse dynamics module extracting actions. Equation: x' = f(x), a = g(x, x'). Examples: DreamGen, 1x World Model.
        RIGHT: 'Joint World-Action Model (WAM)' — shows observation feeding into a single model that outputs BOTH predicted state AND action simultaneously. Equation: (x', a) = f(x). Examples: DreamZero, Fast WAM.
        Use a warm academic color palette: rust (#c2785c), teal (#6a9a5b), blue (#5a7fa5). Light cream background (#faf8f5). Clean arrows, rounded boxes, sans-serif labels.""",
        "intent": "Compare three fundamentally different approaches to world modeling — action-conditioned, video-only, and joint — so students can see the structural differences at a glance",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "wm-vs-vla",
        "description": """A split comparison diagram showing two parallel paths from observation to action:
        TOP PATH (labeled 'VLA — Direct Mapping'): Camera image + language instruction → single large neural network box (labeled 'Vision-Language-Action Model') → robot action output. Arrow is direct, one-step.
        BOTTOM PATH (labeled 'World Model — Imagine then Act'): Camera image + language instruction → World Model box (labeled 'Imagine Future') → multiple predicted future frames shown as small thumbnails → Planning/Optimization box → robot action output. Arrow goes through multiple stages.
        Between them, a comparison callout: VLA = 'Fast but reactive (no lookahead)', World Model = 'Slower but deliberate (plans ahead)'.
        Use warm academic style with rust (#c2785c) for VLA path, teal (#6a9a5b) for World Model path. Cream background.""",
        "intent": "Show students the fundamental architectural difference between VLAs (direct reactive mapping) and World Models (imagine-then-plan), making it clear these are two complementary approaches to robot intelligence",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "architectural-zoo",
        "description": """A taxonomy tree diagram of world model architectures, organized as a tree from top to bottom:
        ROOT: 'World Models' at top.
        LEVEL 1 branches into 4 categories:
        1. 'Pre-trained Features' (teal) → leaf: DINO-WM, LeWorld
        2. 'Discrete Tokens + GPT' (blue) → leaf: IRIS, DIAMOND
        3. 'Latent Dynamics' (purple) → leaf: DreamerV3, TD-MPC2
        4. 'Joint World-Action' (rust) → leaf: DreamZero, Fast WAM
        Each leaf node has a small icon: frozen snowflake for pre-trained, grid for discrete, wave for latent, handshake for joint.
        Clean tree layout with connecting lines. Warm cream background. The branches we cover in this lecture should be highlighted with a subtle glow or thicker border.""",
        "intent": "Give students a mental map of the entire world model landscape so they can place each architecture we study in context",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "dino-wm-architecture",
        "description": """A horizontal pipeline diagram of the DINO World Model architecture:
        Stage 1 (left): A robot camera image (colored photo placeholder) → passes through a large box labeled 'Frozen DINOv2 Encoder' (with a snowflake icon to indicate frozen/no training) → outputs a grid of colored patches labeled 'DINO Feature Patches (14x14)'.
        Stage 2 (center): The feature patches + a small 'Action' input → feed into a box labeled 'Transformer Predictor' (the only trainable component, highlighted with a colored border) → outputs 'Predicted Next Features'.
        Stage 3 (right, shown with dashed lines to indicate optional): Predicted features → small box labeled 'VQ-VAE Decoder' → reconstructed image (for visualization only).
        Below the pipeline, a key insight box: 'Only the Transformer Predictor is trained — everything else is frozen or optional.'
        Use warm colors: teal for frozen components, rust (#c2785c) for trainable components, gray dashed for optional. Cream background.""",
        "intent": "Show the complete DINO-WM pipeline, emphasizing that the key insight is predicting in frozen feature space — only one small component needs training",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "pixel-vs-feature-prediction",
        "description": """A side-by-side comparison of two prediction approaches:
        LEFT side (labeled 'Pixel Prediction — Hard'): Shows a robot scene image at top, then an arrow pointing down to a predicted image that looks blurry/noisy with artifacts. A caption: 'Must predict every pixel: shadows, textures, lighting... 256×256×3 = 196,608 values'. A red X mark.
        RIGHT side (labeled 'Feature Prediction — Smart'): Shows the same robot scene at top, arrow through a 'DINO Encoder' box, then a compact colored grid of abstract features (14×14 = 196 values). Arrow to 'Predict next features'. A green checkmark. Caption: 'Only predict what matters: object identity, pose, spatial layout. 196 feature vectors'.
        The contrast should be stark — left side messy/complex, right side clean/compact.
        Warm academic colors, cream background.""",
        "intent": "Viscerally show why predicting in feature space is dramatically more efficient and meaningful than predicting raw pixels",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "cem-planning",
        "description": """A step-by-step diagram of Cross-Entropy Method (CEM) planning with a world model:
        Step 1: 'Sample' — A cloud of diverse random action trajectories (shown as colorful curved arrows spreading in different directions from a starting point).
        Step 2: 'Imagine' — Each trajectory feeds through a 'World Model' box, producing predicted future states (small image thumbnails at each trajectory endpoint).
        Step 3: 'Evaluate' — Each predicted endpoint is compared to a 'Goal' image using a distance metric. Green check for close matches, red X for far ones.
        Step 4: 'Refine' — Keep top-K trajectories (highlighted in green), discard rest. Sample new trajectories around the best ones (narrower distribution).
        Step 5: 'Repeat' — Arrow looping back to Step 1 with refined distribution. After 3-5 iterations, select the best action.
        Layout as a circular/iterative flow. Warm colors, cream background.""",
        "intent": "Walk students through the CEM planning loop step by step, showing how a world model enables planning by imagining and evaluating possible futures",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "rl-agent-environment",
        "description": """A classic reinforcement learning agent-environment interaction loop diagram:
        Two main boxes: 'Agent' (top, colored in rust #c2785c) and 'Environment' (bottom, colored in teal #6a9a5b).
        Arrows forming a loop:
        - Agent → Environment: thick arrow labeled 'Action a_t' (going down-right)
        - Environment → Agent: two arrows going up-left:
          1. 'State s_{t+1}' (observation of new state)
          2. 'Reward r_{t+1}' (scalar feedback signal)
        Inside the Agent box: 'Policy π(a|s)' — decides what to do.
        Inside the Environment box: 'Dynamics p(s'|s,a)' — physics of the world.
        A time step indicator: 't → t+1 → t+2 → ...'
        Clean, bold arrows. Standard RL diagram layout. Warm academic cream background.""",
        "intent": "Establish the fundamental RL interaction loop that students need to understand before learning how IRIS trains agents entirely in imagined environments",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "actor-critic-architecture",
        "description": """A diagram of the actor-critic architecture used in model-based RL:
        CENTER: A shared 'State Representation' box receiving observation input.
        LEFT branch: Arrow to 'Actor (Policy Network)' box in rust (#c2785c). Output arrow labeled 'Action a ~ π(a|s)'. Description below: 'Decides WHAT to do'.
        RIGHT branch: Arrow to 'Critic (Value Network)' box in blue (#5a7fa5). Output arrow labeled 'Value V(s)'. Description below: 'Evaluates HOW GOOD the state is'.
        Between them: A feedback arrow from Critic to Actor labeled 'Advantage Signal: A(s,a) = Q(s,a) - V(s)' — tells the actor which actions are better than average.
        Below both: 'Training signal: Actor improves actions based on Critic feedback. Critic improves estimates based on actual returns.'
        Warm academic style, cream background.""",
        "intent": "Show the actor-critic architecture that IRIS uses to train policies inside its world model dreams — the actor decides, the critic evaluates, and they improve together",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "dream-learning",
        "description": """A conceptual diagram comparing real environment learning vs dream learning:
        LEFT (labeled 'Traditional RL — Real World'): A physical robot arm interacting with a real table and objects. Slow clock icon. Labels: '1 episode = 5 minutes real time', 'Expensive, risky, slow'.
        RIGHT (labeled 'Dream Learning — Imagination'): A thought bubble containing a simplified/abstract version of the same scene (stylized, slightly translucent). Fast clock icon. Labels: '1000 episodes = 10 seconds GPU time', 'Free, safe, fast'.
        CENTER arrow: 'World Model' connecting real to dream. Arrow from real world labeled 'Learn dynamics from real data' → World Model. Arrow from World Model to dream bubble labeled 'Imagine unlimited experiences'.
        Bottom comparison: 'Real: 100K steps needed' vs 'Dreams: Only 1000 real steps + 100K imagined steps'.
        Warm academic style, cream background.""",
        "intent": "Make the power of dream-based learning visceral — show the massive speedup and safety advantage of training in imagination vs reality",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "iris-vqvae-tokenization",
        "description": """A detailed diagram of IRIS VQ-VAE image tokenization:
        LEFT: An Atari game frame (simple colored blocks representing a game screen, e.g. Breakout with paddle, ball, bricks).
        ARROW → through 'VQ-VAE Encoder' (convolutional neural network, shown as a series of shrinking feature map rectangles).
        CENTER: A 4×4 grid of continuous latent vectors. Each cell has a small colored vector.
        ARROW → 'Vector Quantization' step. Each continuous vector snaps to its nearest codebook entry. Show a small codebook (catalog of 512 entries) with arrows from each vector to its nearest match.
        RIGHT: A 4×4 grid of discrete token IDs (integers like 42, 187, 3, 511, etc.). These 16 tokens ARE the image.
        BOTTOM: 'VQ-VAE Decoder' takes the 16 token IDs → reconstructs the game frame. Show original vs reconstruction side by side.
        Warm academic colors, cream background.""",
        "intent": "Show exactly how IRIS converts a game frame into 16 discrete tokens via VQ-VAE — this is the foundation that makes treating world modeling as language modeling possible",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "iris-sequence-construction",
        "description": """A diagram showing how IRIS constructs a single training sequence from multiple timesteps:
        Show 3 consecutive timesteps (t, t+1, t+2) laid out as a horizontal sequence:
        Timestep t: [reward_t (gold)] [done_t (gray)] [action_t (rust)] [obs_token_1 ... obs_token_16 (teal, 16 blocks)]
        Timestep t+1: [reward_{t+1}] [done_{t+1}] [action_{t+1}] [obs_token_1 ... obs_token_16]
        Timestep t+2: [reward_{t+2}] [done_{t+2}] [action_{t+2}] [obs_token_1 ... obs_token_16]
        All concatenated into ONE long sequence (like a sentence of ~57 tokens for 3 steps).
        Color-coded legend: Gold = reward tokens, Gray = done tokens, Rust = action tokens, Teal = observation tokens.
        Caption: 'Just like a document of text — but the words are game states. The Transformer predicts the next token.'
        Below: Show the causal attention mask — each token can only attend to previous tokens (lower-triangular matrix).
        Warm academic style, cream background.""",
        "intent": "Show the key IRIS insight: by encoding game states as discrete tokens and concatenating timesteps, the world modeling problem becomes identical to language modeling",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "iris-training-pipeline",
        "description": """A 4-phase pipeline diagram for IRIS training:
        Phase 1 (top-left, blue border): 'Collect Real Data' — Show a game controller icon → game screen → stored in a replay buffer (cylinder/database icon). Label: 'Random/behavioral policy plays real game'.
        Phase 2 (top-right, teal border): 'Train VQ-VAE' — Show game frames → encoder → codebook → decoder → reconstructed frames. Label: 'Learn to tokenize images into 16 discrete tokens'.
        Phase 3 (bottom-left, rust border): 'Train World Model Transformer' — Show tokenized sequences → GPT-style Transformer → next-token prediction. Label: 'Learn game dynamics as language modeling (cross-entropy loss)'.
        Phase 4 (bottom-right, purple border): 'Train Actor-Critic in Dreams' — Show the world model generating imagined trajectories (thought bubbles) → actor and critic networks training on imagined data. Label: 'Policy trained entirely in imagination — no real environment needed!'.
        Arrows connect phases: 1→2→3→4, with a feedback loop from 4 back to 1 (use improved policy to collect better data).
        Warm academic style, cream background.""",
        "intent": "Give students a clear overview of the complete IRIS training pipeline — four phases that transform raw game data into a policy trained entirely in dreams",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "leworld-architecture",
        "description": """A detailed architecture diagram of the LeWorld model:
        TOP-LEFT: Robot camera image (robot arm manipulating objects) → passes through 'Frozen DINOv2-G Encoder' (large box, snowflake icon, labeled '1536-dim features').
        TOP-RIGHT: Robot proprioception inputs: joint angles, gripper state, end-effector position → small 'State Encoder' MLP.
        CENTER: Both feature streams merge into a 'Latent Dynamics Model' (Transformer-based, highlighted with rust border as trainable). This takes: DINO features + robot state + commanded action → predicts next latent state.
        BOTTOM-LEFT: Multi-step prediction shown as a chain: z_t → z_{t+1} → z_{t+2} → ... → z_{t+H} (H-step lookahead).
        BOTTOM-RIGHT: 'MPC Planning' box: evaluates multiple action sequences through the dynamics model, selects the best trajectory toward the goal.
        Key difference callout vs DINO-WM: 'Learns compressed latent dynamics (not direct feature prediction) + multi-step rollout + real robot data'.
        Warm academic style, cream background.""",
        "intent": "Show how LeWorld extends DINO-WM to real robots by adding learned latent dynamics, multi-step prediction, and MPC planning — the mature version of feature-space world modeling",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "dreamzero-architecture",
        "description": """A diagram of the DreamZero joint world-action model:
        LEFT: 'Observation History' — a stack of 3-4 previous frames (robot camera images stacked with slight offset).
        CENTER: A single large model box labeled 'Joint World-Action Model' with two internal components visible:
          - Top half: 'World Prediction Head' — outputs predicted next state/frame (teal colored)
          - Bottom half: 'Action Prediction Head' — outputs optimal action (rust colored)
          - Shared backbone in the middle (purple) labeled 'Shared Representation'
        RIGHT: Two outputs:
          - Top: 'Predicted Future State' (image/latent)
          - Bottom: 'Predicted Optimal Action' (robot joint commands)
        KEY INNOVATION callout: 'ONE model, TWO outputs — predicts what WILL happen AND what SHOULD happen simultaneously. No separate planning step needed!'
        Below: Training data sources: 'Internet video (no actions needed)' feeds world head, 'Robot data (with actions)' feeds both heads.
        Warm academic style, cream background.""",
        "intent": "Show how DreamZero eliminates the separation between world modeling and policy learning by jointly predicting futures and actions in a single forward pass",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "wfm-full-pipeline",
        "description": """A 3-phase horizontal pipeline diagram for building a World Foundation Model from scratch:
        PHASE 1 (left, blue): 'Data Curation'
        - Icon: film reel + filter
        - Steps stacked: Download (2.3 TB) → Split (1.67M clips) → Filter (motion + aesthetics + text) → Caption (Qwen2.5-VL) → 1.44M curated clips
        - Cost: ~$50 compute

        PHASE 2 (center, teal): 'Video Tokenizer'
        - Icon: compression symbol
        - Show: Raw video frames (25 frames, 256×256) → NVIDIA Cosmos Tokenizer → compressed latent [1, 16, 4, 32, 32]
        - Stats: 38× compression, 34-41 dB PSNR
        - 241K pre-tokenized latents
        - Cost: ~$20 compute

        PHASE 3 (right, rust): 'Diffusion World Model'
        - Icon: neural network / transformer
        - Show: Latents + text caption → 1.56B DiT (3D patches, RoPE, AdaLN) → generated video
        - Stats: Loss 3.06 → 0.65 in 500 steps
        - Cost: TBD (scales with compute)

        Arrows connecting phases left to right. Each phase box has a small 'DONE' checkmark or progress indicator.
        Warm academic style, cream background.""",
        "intent": "Give students a bird's-eye view of the complete pipeline for building a world model from scratch — data, tokenization, and generation — with real numbers from your actual project",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "dit-architecture",
        "description": """A detailed diagram of the Diffusion Transformer (DiT) architecture for video generation:
        INPUT (left): A noisy latent tensor [1, 16, 4, 32, 32] (shown as a 3D volume with T=4, H=32, W=32 axes labeled).
        STEP 1: '3D Patchify' — the volume is divided into non-overlapping 3D patches of size (1, 2, 2). Each patch becomes a token. Result: sequence of 2048 patch tokens.
        STEP 2: 'Token Embedding + 3D RoPE' — each patch token gets a position encoding that encodes its (time, height, width) position.
        STEP 3: 'Transformer Layers (×16)' — a stack of DiT blocks. Each block contains:
          - Self-Attention with QK-normalization
          - Cross-Attention to text embeddings (from frozen T5 encoder, shown as side input)
          - AdaLN-LoRA conditioning on noise level σ (shown as side input)
          - MLP with SwiGLU activation
        STEP 4: 'Unpatchify' — tokens reassembled back into denoised latent tensor.
        OUTPUT (right): Denoised latent → Cosmos Decoder → generated video frames.
        Show the overall flow left to right. Key numbers: 1.56B params, 16 layers, 2048 dim, 16 heads.
        Warm academic style, cream background.""",
        "intent": "Break down the DiT architecture layer by layer so students understand exactly how a diffusion transformer processes video latents — from 3D patchification through transformer layers to video output",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "video-tokenizer-compression",
        "description": """A visual showing the compression power of the Cosmos video tokenizer:
        LEFT: '25 Raw Video Frames at 256×256' — shown as a filmstrip of 25 small frames (robot arm doing a task). Total size labeled: '~5 MB (25 × 256 × 256 × 3 bytes)'.
        CENTER: 'Cosmos CV8×8×8 Tokenizer' — shown as a funnel/compression box. Labels on the funnel: '8× temporal compression', '8× height compression', '8× width compression'.
        RIGHT: 'Latent Tensor [1, 16, 4, 32, 32]' — shown as a small compact 3D cube/grid. Total size labeled: '~132 KB'. The 16 channels shown as depth.
        BOTTOM: Bar chart comparing sizes: Raw (5 MB) vs Latent (132 KB) = 38× compression.
        Also show: 'Reconstruction quality: 34-41 dB PSNR (near lossless to human eye)'.
        Warm academic style, cream background.""",
        "intent": "Visually demonstrate the massive compression achieved by the Cosmos tokenizer — 38× smaller while maintaining near-lossless quality — making it feasible to train transformers on video",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "world-models-summary-comparison",
        "description": """A comprehensive comparison table/infographic of all 5 world models covered in the lecture:
        5 columns, one per model: DINO-WM | IRIS | LeWorld | DreamZero | Diffusion WFM
        Rows:
        - 'Core Idea' (icon + 1-line summary for each)
        - 'Representation': Features | Discrete tokens | Latent | Joint latent | Continuous latent
        - 'Prediction': Direct | Autoregressive | Dynamics model | Joint | Diffusion
        - 'Planning': CEM (slow) | None (fast) | MPC (slow) | None (fast) | N/A
        - 'Training Data': Small robot | Game episodes | Robot demos | Video + robot | Massive video
        - 'Strength': Data efficient | Sample efficient | Real robots | Best generalization | Scalable
        - 'Limitation': Error compounds | Blocky images | Slow planning | New/untested | Compute heavy

        Each column has a distinct color from the Vizuara palette. The table should be visually appealing with rounded cells and colored headers.
        Warm academic style, cream background.""",
        "intent": "Provide a single reference diagram that students can use to compare all five world model approaches covered in the lecture — their trade-offs, strengths, and ideal use cases",
        "type": DiagramType.METHODOLOGY,
    },
]


async def generate_figure(pipeline, fig_spec):
    """Generate a single figure."""
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
        # Copy the generated image to our figures dir
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
    print(f"Generating {len(FIGURES)} figures for World Models lecture...")
    pipeline = PaperBananaPipeline(settings=settings)

    # Generate figures with concurrency limit (avoid rate limits)
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
