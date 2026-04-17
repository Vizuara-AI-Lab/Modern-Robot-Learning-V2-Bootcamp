"""Generate PaperBanana figures for V-JEPA / V-JEPA 2 slides."""
import asyncio
import os
import sys
from pathlib import Path

# Use provided API key directly
os.environ["GOOGLE_API_KEY"] = "AIzaSyDGrcsxxmyNe50l37Ufdit56DUiF7INZQ8"

# Add PaperBanana to path
sys.path.insert(0, "/Users/raj/Desktop/Course_Creator")
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
        "name": "jepa-core-concept",
        "description": """A conceptual diagram explaining the JEPA (Joint Embedding Predictive Architecture) philosophy.
        THREE COLUMNS showing different prediction approaches:

        LEFT column (labeled 'Generative — Pixel Prediction', crossed out with red):
        Shows an input image → Encoder → Decoder → output pixels (blurry reconstructed image).
        Below: 'Wastes capacity on textures, lighting, exact pixel values'
        Has a red X or cross-out.

        CENTER column (labeled 'Contrastive — Binary Match', shown in gray):
        Shows two images → two encoders → arrows pointing to a 'Same or Different?' comparison node.
        Below: 'Only learns to match, not predict'

        RIGHT column (labeled 'JEPA — Predict in Latent Space', highlighted with a golden border):
        Shows an input image → 'Context Encoder' box → abstract latent representation (colored blob/vector).
        A 'Predictor' box takes the latent + 'What to predict' input → predicted latent.
        A separate path: target image → 'Target Encoder (EMA)' → target latent, with a stop-gradient symbol.
        L1 loss between predicted and target latents.
        Below: 'Predicts abstract meaning, not pixels — learns what matters'

        A quote from Yann LeCun at the bottom: 'Humans don't predict exact pixels of the future — they predict abstract concepts.'

        Warm academic palette: rust (#c2785c) for JEPA highlight, teal (#6a9a5b) for encoders, blue (#5a7fa5) for predictor. Cream background (#faf8f5). Clean sans-serif labels.""",
        "intent": "Explain the fundamental philosophical difference between generative, contrastive, and JEPA approaches to self-supervised learning — showing why predicting in latent space is the key insight",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "jepa-architecture-detailed",
        "description": """A detailed architectural diagram of the JEPA pretraining framework for video:

        TOP: A video clip shown as a filmstrip of 5-6 frames (small thumbnails).

        The video is divided into two regions with different colored overlays:
        - VISIBLE REGION (shown in teal/green, ~25% of patches): scattered patches that the model can see
        - MASKED REGION (shown in gray with hatching, ~75% of patches): large contiguous spatiotemporal blocks that are hidden

        LEFT PATH (Context Encoder):
        Visible patches → large box labeled 'Context Encoder (ViT)' with 'trainable' tag → output: 'Visible Token Representations' (small colored circles)

        CENTER (Predictor):
        Visible representations + learnable gray mask tokens (with position info) → smaller box labeled 'Predictor (small ViT)' with 'trainable' tag → 'Predicted Representations' for masked positions

        RIGHT PATH (Target Encoder):
        ALL patches (both visible and masked) → large box labeled 'Target Encoder (EMA copy)' with a snowflake + 'stop-gradient' symbol → 'Target Representations' for masked positions

        BOTTOM: An L1 loss arrow connecting predicted representations to target representations.
        A note: 'Target encoder = exponential moving average of context encoder. No gradients flow back.'

        Color coding: teal boxes for encoders, rust (#c2785c) for predictor, gray dashed for EMA/stop-grad. Cream background.""",
        "intent": "Show the complete JEPA pretraining loop with all three components — context encoder, predictor, and EMA target encoder — making the stop-gradient and masking strategy crystal clear",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "vjepa-multiblock-masking",
        "description": """A visual explanation of the multiblock masking strategy used in V-JEPA:

        TOP: A video shown as a 3D grid (time × height × width), like a rectangular prism made of small cubes.
        Each small cube represents a spatiotemporal patch/tubelet.

        STEP 1 (left): The full 3D grid is shown intact, labeled 'Original Video (T × H × W patches)'

        STEP 2 (center): Several LARGE contiguous blocks within the 3D grid are colored RED/GRAY, showing they are masked out. These blocks are large rectangular regions spanning multiple frames and spatial positions. The remaining visible patches are colored TEAL. Labels: 'Masked: ~75%' and 'Visible: ~25%'. An arrow pointing to the large masked blocks says 'Large contiguous blocks — NOT random individual patches'

        STEP 3 (right): Two separate views:
        - TOP: 'Context Encoder sees ONLY visible patches' — shows sparse teal patches
        - BOTTOM: 'Predictor must reconstruct latents of ENTIRE masked regions' — shows the model predicting large areas

        BOTTOM callout box: 'Why large blocks? Random masking is trivially easy (just interpolate neighbors). Large blocks force the model to understand object dynamics, motion, and causal structure.'

        Warm colors: teal for visible, rust for masked, cream background. 3D perspective with clean lines.""",
        "intent": "Visually demonstrate why the masking strategy is critical — large contiguous blocks force deep understanding of video dynamics, not just spatial interpolation",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "vjepa2-scaling-axes",
        "description": """A bar chart / progression diagram showing V-JEPA 2's four scaling improvements over V-JEPA 1:

        A STACKED BAR or WATERFALL CHART showing cumulative accuracy improvement:

        Starting baseline: 'V-JEPA 1 (ViT-L)' at the left

        Four additive bars stacked to the right, each a different color:
        1. DATA SCALING (+1.0 pts) — teal bar — '2M → 22M videos (11× more)'
        2. MODEL SCALING (+1.5 pts) — rust bar — '300M → 1B params (3.3× larger)'
        3. TRAINING DURATION (+0.8 pts) — blue bar — '90K → 252K iterations (2.8× longer)'
        4. RESOLUTION SCALING (+0.7 pts) — purple bar — '16f@256 → 64f@384 (progressive)'

        Final total: '+4.0 points average accuracy' shown prominently at the right end

        Below the chart, a side-by-side comparison table:
        | Aspect | V-JEPA 1 | V-JEPA 2 |
        | Encoder | ViT-L (300M) | ViT-g (1B) |
        | Dataset | 2M videos | 22M videos + images |
        | Training | 90K iters | 252K iters |
        | Position enc. | Sinusoidal | 3D RoPE |
        | Frames | 16 | Up to 64 |

        Warm academic palette, cream background, clean typography.""",
        "intent": "Quantitatively show the four scaling axes that transformed V-JEPA 1 into V-JEPA 2, making it clear that each improvement contributes measurably",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "vjepa2-architecture",
        "description": """A detailed architecture diagram of V-JEPA 2's ViT-g encoder:

        LEFT: Input video clip shown as frames → divided into TUBELETS (2 × 16 × 16) — show a small 3D cube labeled '2 frames × 16px × 16px = 1 tubelet token'

        CENTER: The ViT-g Encoder architecture:
        - Input: tubelet tokens (e.g., for 16 frames at 256×256 → 16×16 = 256 spatial patches per frame, 8 temporal groups = 2048 tokens)
        - 3D RoPE block: 'Rotary Position Embedding' with three separate rotation axes labeled T (temporal), H (height), W (width). Show the feature dimension split into 3 equal parts, each getting its own rotation.
        - Transformer layers: Stack of blocks labeled 'Self-Attention + FFN × 40 layers'
        - Output: '16 × 16 × 1408' feature maps per frame

        RIGHT: Key specs in a card:
        - Parameters: 1 Billion
        - Patch size: 2 × 16 × 16
        - Hidden dim: 1408
        - Heads: 16
        - Layers: 40
        - Position: 3D RoPE

        BOTTOM: A callout showing the advantage of 3D RoPE over absolute sinusoidal:
        '3D RoPE → generalizes to different resolutions and video lengths without retraining'

        Warm palette: teal for encoder blocks, rust for RoPE highlight, blue for attention. Cream background.""",
        "intent": "Show the complete ViT-g encoder architecture with emphasis on the tubelet tokenization and 3D RoPE — the key architectural innovations of V-JEPA 2",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "vjepa2-progressive-training",
        "description": """A timeline diagram showing V-JEPA 2's progressive resolution training strategy:

        A HORIZONTAL TIMELINE from left to right:

        PHASE 1 — WARMUP (12K iters):
        - Small box, light color
        - '16 frames @ 256×256'
        - 'Linear LR warmup'

        PHASE 2 — CONSTANT (228K iters):
        - Large box (proportional to duration), main teal color
        - '16 frames @ 256×256'
        - 'Peak learning rate'
        - Arrow showing this is the bulk of training

        PHASE 3 — COOLDOWN (12K iters):
        - Medium box, highlighted in rust/gold
        - '64 frames @ 384×384' (much bigger resolution text)
        - 'Linear LR decay'
        - A callout: 'Resolution increased ONLY here!'

        Below the timeline:
        A comparison:
        - 'Naive approach: Train at 64f@384 for ALL 252K iters → ~60 GPU-years'
        - 'Progressive approach: Low-res then high-res cooldown → ~7.1 GPU-years'
        - '8.4× compute savings!' shown in a highlighted box

        Total: '252K iterations total'

        Warm colors, cream background, clean timeline visualization.""",
        "intent": "Explain the clever progressive resolution training trick that achieves 8.4x compute savings — training at low resolution for most of the run and only increasing in the final cooldown phase",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "vjepa2-videomix22m",
        "description": """A dataset composition diagram for VideoMix22M:

        A TREEMAP or PIE CHART showing the five data sources with proportional sizing:

        1. YT-Temporal-1B (largest, 19M samples, 1.6M hours) — rust color — 'Exo-video, web-scale'
        2. HowTo100M (1.1M samples, 134K hours) — teal — 'Instructional videos'
        3. Kinetics (733K samples, 614 hours) — blue — 'Human activities'
        4. ImageNet (1M samples, images) — purple — 'Static images (diversity)'
        5. Something-Something v2 (168K samples, 168 hours) — warm gold — 'Ego-centric manipulation'

        Total in center or header: '22M samples, >1M hours of video'

        Side panel showing sampling weights:
        - YT-Temporal: 18.8%
        - HowTo100M: 31.8%
        - Kinetics: 18.8%
        - ImageNet: 25.0%
        - SSv2: 5.6%

        A note: 'YT-Temporal is curated via cluster-based retrieval filtering → +1.4 pt improvement'

        Warm academic palette, cream background, clean labels.""",
        "intent": "Show the massive scale and diversity of the VideoMix22M training dataset, highlighting how different sources contribute different types of visual understanding",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "vjepa2-understanding-results",
        "description": """A benchmark results comparison figure showing V-JEPA 2's video understanding performance:

        A GROUPED BAR CHART comparing V-JEPA 2 against previous methods:

        Benchmarks on X-axis:
        - SSv2 (77.3%)
        - Diving-48 (87.5%)
        - Kinetics-400 (85.7%)
        - Epic-Kitchens Anticipation (39.7 — 44% relative improvement!)
        - ImageNet (84.7%)

        Bars for each:
        - V-JEPA 1 (light color)
        - V-JEPA 2 (bold rust color, taller)
        - Previous SOTA where applicable (gray)

        HIGHLIGHT: Epic-Kitchens anticipation shows the biggest jump, with a callout: '44% relative improvement over previous SOTA'

        BOTTOM section: Video QA with LLM results
        A card showing: 'V-JEPA 2 + Qwen2-7B = SOTA at 8B scale'
        - PerceptionTest: 84.0
        - TempCompass: 76.9
        - Key insight: 'No language supervision during pretraining — yet SOTA when aligned with LLM'

        Warm colors, cream background.""",
        "intent": "Demonstrate that V-JEPA 2's self-supervised pretraining achieves state-of-the-art video understanding WITHOUT language supervision — a key finding that challenges the assumption that CLIP-style training is necessary",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "vjepa2-ac-architecture",
        "description": """Architecture diagram of V-JEPA 2-AC (Action-Conditioned World Model):

        TOP: A video sequence of robot frames (Franka arm manipulating objects).

        PIPELINE:
        1. FROZEN ENCODER (left): Video frames → large 'V-JEPA 2 Encoder (1B, FROZEN)' box with snowflake icon → visual tokens z_1, z_2, ... z_T

        2. ACTION-CONDITIONED PREDICTOR (center, highlighted):
        A large box labeled '300M Action-Conditioned Predictor'
        Inputs flowing in:
        - Visual tokens z_t (from frozen encoder)
        - Action tokens a_t (7D: end-effector changes)
        - Pose tokens s_t (7D: current end-effector state)
        Internal: 'Block-Causal Attention (24 layers, 16 heads)'
        - 3D RoPE applied: 'Spatial RoPE for visual patches, Temporal-only RoPE for action/pose tokens'
        Output: Predicted next visual tokens z_hat_{t+1}

        3. LOSS (right):
        Two loss terms shown:
        - 'Teacher Forcing Loss' — predict z_{t+1} from ground-truth z_t
        - 'Rollout Loss (T=2)' — predict z_{t+2} autoregressively, differentiating through 1 step

        BOTTOM: Training details card:
        - 'Only 62 hours of robot data (Droid dataset)'
        - 'Encoder stays FROZEN — only predictor trains'
        - 'Input: 256×256, 4 fps, 16 frames (4-second clips)'

        Colors: teal for frozen encoder (with snowflake), rust for trainable predictor, blue for actions. Cream background.""",
        "intent": "Show how V-JEPA 2-AC builds on the frozen V-JEPA 2 encoder by adding an action-conditioned predictor — emphasizing that only 62 hours of robot data and a relatively small predictor are needed",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "vjepa2-planning-cem",
        "description": """A diagram showing V-JEPA 2's planning algorithm for robot control:

        TOP: 'Goal-Conditioned Planning via Energy Minimization'

        STEP 1 (left):
        'Current State' — robot arm in starting position → frozen encoder → z_current
        'Goal State' — robot arm at goal position → frozen encoder → z_goal

        STEP 2 (center):
        'Cross-Entropy Method (CEM) Optimization'
        Show iterative refinement:
        - Round 1: Sample N action sequences from Gaussian → evaluate each through world model → rank by distance to z_goal → keep top-K
        - Round 2: Refit Gaussian to top-K → sample again → evaluate → keep top-K
        - Round 3: Final refinement → select best action sequence

        Energy equation: E(a_1:T) = ||P(a_1:T; s, z_current) - z_goal||_1

        STEP 3 (right):
        'Receding Horizon Control'
        Execute ONLY the first action → observe new state → RE-PLAN
        Show a timeline: plan → execute 1 step → re-plan → execute 1 step → ...

        BOTTOM: Performance card:
        - '16 seconds per action on RTX 4090'
        - '15× faster than Cosmos baseline'
        - 'Zero-shot: deployed on robots NOT in training data'

        Warm colors, cream background, clean flow arrows.""",
        "intent": "Explain the complete planning loop — from goal specification through CEM optimization in latent space to receding horizon execution — showing how V-JEPA 2 enables zero-shot robot control",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "vjepa2-robot-results",
        "description": """A results figure showing V-JEPA 2-AC's zero-shot robot manipulation performance:

        TOP: Photo-style illustration of a Franka Emika Panda robot arm with a gripper, viewed from a monocular camera.

        CENTER: A bar chart showing success rates for different tasks:

        Tasks (Y-axis):
        - Reach → 100% (both V-JEPA 2-AC and Octo)
        - Grasp Cup → 65% vs 15% (Octo)
        - Grasp Box → 25% (V-JEPA 2-AC only)
        - Reach w/ Object Cup → 75%
        - Reach w/ Object Box → 75%
        - Pick & Place Cup → 80% vs 10% (Octo)
        - Pick & Place Box → 65% vs 10% (Octo)

        Two bar colors: rust for V-JEPA 2-AC, gray for Octo baseline.

        CALLOUT boxes:
        - 'Pick & Place: 80% vs 10%' — 8× improvement highlighted
        - 'Zero-shot: tested in labs NOT in training data'
        - 'Uncalibrated low-res monocular RGB camera'

        BOTTOM: Key insight: 'Trained on 62 hours of generic robot data → zero-shot manipulation on unseen robots'

        Warm academic palette, cream background.""",
        "intent": "Show the impressive zero-shot robot manipulation results — V-JEPA 2 dramatically outperforms Octo on complex tasks despite using no task-specific training data",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "vjepa2-energy-landscape",
        "description": """A visualization of V-JEPA 2's energy landscape for planning:

        A 3D SURFACE PLOT or CONTOUR MAP showing the energy function E(actions):

        LEFT (V-JEPA 2-AC): A smooth, locally convex energy surface with a clear minimum near the ground-truth action. The landscape is clean with a single dominant basin of attraction. Color gradient from blue (low energy, good) to red (high energy, bad). A star marks the minimum, labeled 'Optimal action sequence'. Ground truth action marked nearby.

        RIGHT (Weak baseline): A noisy, flat energy landscape with many local minima and no clear structure. The ground-truth action is not at a minimum. Label: 'Noisy/flat — CEM cannot find good actions'

        BOTTOM: Explanation:
        'Good world model → smooth energy landscape → CEM easily finds optimal actions'
        'Bad world model → noisy/flat landscape → CEM gets stuck in local minima'

        Warm colors: teal for V-JEPA 2, gray for baseline. Cream background.""",
        "intent": "Visually explain why V-JEPA 2's learned representations create a smooth, plannable energy landscape — making CEM optimization effective for robot control",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "vjepa1-vs-vjepa2-summary",
        "description": """A comprehensive side-by-side comparison of V-JEPA 1 vs V-JEPA 2:

        TWO COLUMNS with a VS symbol in the middle:

        LEFT (V-JEPA 1, lighter colors):
        - Icon: ViT-L
        - Encoder: 300M parameters
        - Data: 2M videos
        - Training: 90K iterations
        - Position: Absolute sinusoidal
        - Frames: 16
        - Resolution: Fixed
        - Robot capabilities: None
        - LR Schedule: Half-cosine

        RIGHT (V-JEPA 2, bold highlighted):
        - Icon: ViT-g
        - Encoder: 1B parameters (3.3×)
        - Data: 22M videos + images (11×)
        - Training: 252K iterations (2.8×)
        - Position: 3D RoPE
        - Frames: Up to 64
        - Resolution: Progressive (256→384)
        - Robot capabilities: Zero-shot manipulation!
        - LR Schedule: Warmup-constant-decay

        Each comparison row has an arrow or multiplier showing the improvement factor.

        BOTTOM: 'Result: +4.0 points average accuracy + zero-shot robot control'

        Warm palette, cream background, clean comparison layout.""",
        "intent": "Provide a complete at-a-glance comparison of V-JEPA 1 vs V-JEPA 2, showing every key improvement and its magnitude",
        "type": DiagramType.METHODOLOGY,
    },
]


async def generate_all():
    import shutil
    pipeline = PaperBananaPipeline(settings)

    for fig in FIGURES:
        outpath = FIGURES_DIR / f"{fig['name']}.png"
        if outpath.exists():
            print(f"[SKIP] {fig['name']} already exists")
            continue
        print(f"\n[GEN] {fig['name']}...")
        try:
            inp = GenerationInput(
                source_context=fig["description"],
                communicative_intent=fig["intent"],
                diagram_type=fig["type"],
            )
            result = await pipeline.generate(inp)
            if result and result.image_path:
                shutil.copy2(result.image_path, str(outpath))
                print(f"  ✓ Saved → {outpath.name}")
            else:
                print(f"  ✗ No image returned")
        except Exception as e:
            print(f"  ✗ FAILED: {e}")


if __name__ == "__main__":
    asyncio.run(generate_all())
