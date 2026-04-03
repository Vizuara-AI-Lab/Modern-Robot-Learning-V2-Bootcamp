"""Generate PaperBanana figures for Lecture 3: From VLAs to Real Robots.

Usage:
    python generate_figures.py              # generate only missing figures
    python generate_figures.py --all        # regenerate everything
    python generate_figures.py --only 1 2   # generate only Parts 1 & 2 figures
"""
import os
import sys
import asyncio
import shutil

os.environ["GOOGLE_API_KEY"] = "AIzaSyBo74cqFdD84RxEpnsqhwKNkpF_FsvsbOI"

from paperbanana import PaperBananaPipeline, GenerationInput, DiagramType
from paperbanana.core.config import Settings

settings = Settings(
    vlm_model="gemini-2.0-flash",
    image_model="gemini-3-pro-image-preview",
    refinement_iterations=2,
    google_api_key=os.environ["GOOGLE_API_KEY"],
)

FIGURES_DIR = os.path.join(os.path.dirname(__file__), "public", "figures")
os.makedirs(FIGURES_DIR, exist_ok=True)

FIGURES = [
    # ── Recap ──
    {
        "name": "vla-recap-diagram",
        "description": """A clean horizontal pipeline showing the three components of a Vision-Language-Action model.

        LEFT: Camera image icon → blue box labeled 'Vision Encoder (ViT / SigLIP)' → blue arrow labeled 'Visual Tokens'
        MIDDLE: Text input 'pick up the red cup' → orange box labeled 'Language Model (Transformer)' → orange arrow labeled 'Fused Understanding'
        The blue visual tokens also feed into the Language Model box.
        RIGHT: The fused understanding → teal box labeled 'Action Head (Diffusion / Tokenization)' → teal arrow → 'Robot Joint Angles'

        Below, show three color-coded labels: V = Vision (blue), L = Language (orange), A = Action (teal).
        A large bracket under everything labeled 'VLA = Vision-Language-Action Model'.

        White background, clean academic style. Vision in blue (#5B8CB8), Language in orange (#D97757),
        Action in teal (#7DA488). Simple, not cluttered.""",
        "intent": "Provide a clear recap diagram of what a VLA is — three modalities flowing through a unified pipeline",
        "type": DiagramType.METHODOLOGY,
        "part": 0,
    },
    # ── Part 1: Open-Source VLAs ──
    {
        "name": "siglip-vs-dinov2",
        "description": """A side-by-side comparison showing what SigLIP and DinoV2 'see' when looking at the same image.

        TOP: A photograph/illustration of a workspace with a red cup on a table.

        BOTTOM-LEFT labeled 'SigLIP (Semantic Features)':
        Show a heatmap/attention overlay on the image where the ENTIRE cup region is highlighted uniformly,
        with a text bubble: 'I see a RED CUP (confident: 0.95)'. The highlight is broad, covering the whole object.
        Below: 'Trained on image-text pairs. Knows WHAT things are. Spatially coarse.'

        BOTTOM-RIGHT labeled 'DinoV2 (Spatial Features)':
        Show a different heatmap where precise EDGES are highlighted — the rim of the cup, the handle outline,
        the table edge, with small dots at key geometric points.
        Below: 'Self-supervised on images only. Knows WHERE edges are. No language understanding.'

        BOTTOM CENTER: An arrow merging both into a combined feature: 'Together: WHAT + WHERE = pick up the red cup at position (312, 247)'

        White background. SigLIP features in blue (#5B8CB8), DinoV2 features in teal (#7DA488),
        combined in orange (#D97757).""",
        "intent": "Visually demonstrate the complementary nature of SigLIP (semantic) and DinoV2 (spatial) — why OpenVLA needs both vision encoders",
        "type": DiagramType.METHODOLOGY,
        "part": 1,
    },
    {
        "name": "oxe-dataset-samples",
        "description": """A grid showing sample images from the Open X-Embodiment dataset used to train OpenVLA.

        Show a 3×3 grid of diverse robot manipulation scenes:
        - Different robot embodiments: a Franka Panda arm, a WidowX arm, a Google Robot
        - Different tasks: picking up objects, opening a drawer, pouring, pushing
        - Different environments: kitchen, tabletop, lab bench

        Each cell has a small label: robot name and task.
        Below the grid: 'Open X-Embodiment: 970K trajectories, 22 robot types, 21+ labs worldwide'

        White background, clean academic grid layout. Each cell has a thin border.
        Labels in warm brown (#8b6f4e).""",
        "intent": "Show the diversity and scale of the Open X-Embodiment dataset that OpenVLA was trained on — many robots, many tasks, many environments",
        "type": DiagramType.METHODOLOGY,
        "part": 1,
    },
    {
        "name": "pixelshuffle-compression",
        "description": """A diagram showing how PixelShuffle reduces visual tokens from 256 to 64.

        LEFT: A 16×16 grid of small squares labeled '256 patch tokens' (each square is a patch).
        A group of 4 adjacent patches (2×2 block) is highlighted in blue.

        ARROW in the middle labeled 'PixelShuffle 4×: merge 2×2 → 1 token (4× channels)'

        RIGHT: An 8×8 grid of slightly larger squares labeled '64 tokens (4× deeper)'.
        The merged token is highlighted in blue, shown as thicker/deeper to represent more channels.

        Below: 'Spatial info preserved — just packed into fewer, richer tokens.
        256 tokens × d → 64 tokens × 4d. Attention cost: 16× cheaper.'

        White background, clean academic style. Original patches in light blue (#5B8CB8),
        merged tokens in darker blue. Arrow in orange (#D97757).""",
        "intent": "Visualize how PixelShuffle compresses visual tokens — merging spatial neighbors into channel dimensions",
        "type": DiagramType.METHODOLOGY,
        "part": 1,
    },
    {
        "name": "layer-skipping",
        "description": """A diagram showing SmolVLA's layer skipping strategy.

        Show a vertical stack of transformer layers (12 total, numbered 1-12 from bottom to top).

        BOTTOM HALF (layers 1-6): Highlighted in blue with a checkmark. Labeled 'Bottom N/2 layers: Visual features, spatial layout, object detection'. An arrow exits from the top of layer 6 labeled 'VLM features → Action Expert'.

        TOP HALF (layers 7-12): Grayed out with an X mark. Labeled 'Top N/2 layers: Complex reasoning, abstract concepts'. A large 'SKIP' stamp or strikethrough across these layers.

        On the right side, show two boxes:
        - 'Kept: WHERE is the cup? WHAT does it look like?' (in blue, checkmark)
        - 'Discarded: Write a poem about the cup' (in gray, X mark)

        Below: 'Result: 50% less VLM compute with minimal manipulation performance loss'

        White background. Active layers in blue (#5B8CB8), skipped layers in light gray.
        Labels in warm brown.""",
        "intent": "Show that lower transformer layers capture the spatial/visual features needed for motor control while upper reasoning layers can be safely discarded",
        "type": DiagramType.METHODOLOGY,
        "part": 1,
    },
    {
        "name": "attention-pattern-comparison",
        "description": """A three-panel comparison showing attention patterns for OpenVLA, pi0, and SmolVLA.

        Each panel shows an attention matrix (colored grid) with labeled axes.

        PANEL 1 'OpenVLA: Causal LLM Attention':
        Axes: rows and columns both labeled 'image | text | action₁ | action₂ | ... | action₇'
        Show a lower-triangular matrix (standard causal attention). All tokens attend to all previous tokens.
        Color: orange (#D97757). Note: 'All tokens in one sequence. Action tokens decoded one at a time.'

        PANEL 2 'pi0: Block-Wise Attention':
        Axes: rows and columns labeled 'VLM block | State block | Action block'
        Show three diagonal blocks (bidirectional within each) plus off-diagonal causal blocks
        (action can see VLM, but VLM cannot see action).
        Color: purple (#9B7EC8). Note: 'Three blocks concatenated. Bidirectional within, causal between.'

        PANEL 3 'SmolVLA: Interleaved CA+SA':
        Show TWO smaller matrices side by side within the panel:
        - CA matrix: rows = action tokens, columns = VLM tokens. Full attention (every action sees every VLM token).
        - SA matrix: rows = columns = action tokens only. Lower-triangular (causal self-attention).
        Color: teal (#7DA488). Note: 'Action tokens alternate between seeing the world (CA) and coordinating (SA).'

        White background, clean academic style. Each panel in a bordered box.""",
        "intent": "Directly compare the three attention strategies — showing how each architecture connects vision/language understanding to action generation",
        "type": DiagramType.METHODOLOGY,
        "part": 1,
    },
    {
        "name": "openvla-architecture",
        "description": """A clean academic architecture diagram of OpenVLA showing three components flowing left to right.

        LEFT: A camera image flows into TWO parallel vision encoders stacked vertically:
        - Top encoder: blue box labeled 'SigLIP (400M)' with subtitle 'Semantic features'
        - Bottom encoder: teal box labeled 'DinoV2 (300M)' with subtitle 'Spatial features'
        Both outputs merge with a '+' symbol into a combined feature vector.

        MIDDLE: The combined features flow through a small box labeled 'Projector MLP (2 layers)'
        then into a large orange box labeled 'Llama 2 7B' with subtitle 'Autoregressive Decoder'.
        A text input 'pick up the red cup' also enters the Llama box from below.

        RIGHT: The Llama box outputs 7 sequential tokens: '147', '52', '230', '89', '12', '201', '155'
        each in a small numbered box, with an arrow labeled 'Decode to continuous' pointing to
        final output 'Robot Actions (7 DoF)'.

        White background, clean academic style. SigLIP in blue (#5B8CB8), DinoV2 in teal (#7DA488),
        Llama in orange (#D97757), action tokens in purple (#9B7EC8). Monospace font for numbers.""",
        "intent": "Show the complete OpenVLA architecture — dual vision encoder, projector, Llama 2 backbone, and action tokenization output",
        "type": DiagramType.METHODOLOGY,
        "part": 1,
    },
    {
        "name": "smolvla-architecture",
        "description": """A clean academic architecture diagram of SmolVLA showing two main modules.

        LEFT MODULE (VLM Backbone - labeled 'SmolVLM2 (~350M)'):
        - Camera image → blue box 'SigLIP Vision Encoder' → '64 visual tokens' (emphasized as small count)
        - Text 'pick up the red cube' → orange box 'SmolLM2 Decoder'
        - Visual tokens and text tokens merge inside SmolVLM2
        - A dashed line cuts the VLM in half horizontally, labeled 'Only bottom N/2 layers used'
        - Arrow exits from the bottom half labeled 'VLM features'

        RIGHT MODULE (Action Expert - labeled '~100M'):
        - A transformer block with alternating layers labeled 'CA' (cross-attention, blue) and 'SA' (self-attention, teal)
        - Stacked vertically: CA → SA → CA → SA → CA → SA
        - VLM features arrow enters each CA layer from the left
        - Bottom input: 'Noisy Actions + τ' entering the stack
        - Top output: 'Predicted Velocity (50 × 7)' → 'Flow Matching (10 steps)' → 'Clean Action Chunk'

        White background, clean academic diagram. VLM module in warm orange border,
        Action Expert in purple border. Use blue (#5B8CB8) for vision, orange (#D97757) for language,
        purple (#9B7EC8) for action expert, teal (#7DA488) for self-attention layers.""",
        "intent": "Show SmolVLA's two-module architecture with emphasis on the three efficiency tricks: 64 visual tokens, layer skipping, and interleaved CA+SA",
        "type": DiagramType.METHODOLOGY,
        "part": 1,
    },
    {
        "name": "smolvla-action-expert",
        "description": """A detailed close-up diagram of SmolVLA's Action Expert transformer showing the interleaved attention pattern.

        Show a vertical stack of 6 transformer layers, alternating between two types:
        - BLUE layers labeled 'Cross-Attention (CA)': Action tokens (purple dots on left) attend to VLM features (orange dots on right). Show attention arrows from purple to orange.
        - TEAL layers labeled 'Self-Attention (SA)': Action tokens attend to each other with causal masking. Show arrows between purple dots, with a triangular causal mask overlay.

        Bottom input: A sequence of purple dots labeled 'Noisy Actions [a₁, a₂, ..., a₅₀] + timestep τ'
        Top output: Purple dots labeled 'Predicted Velocity [v₁, v₂, ..., v₅₀]'

        On the right side, show VLM features as a column of orange dots labeled 'VLM Features (64 visual + text tokens)' with arrows going into each CA layer.

        Add a note: 'Causal masking in SA → each action only sees past actions → temporally smooth motions'

        White background, clean academic style. CA layers in blue (#5B8CB8), SA layers in teal (#7DA488),
        action tokens in purple (#9B7EC8), VLM features in orange (#D97757).""",
        "intent": "Provide a detailed view of the interleaved cross-attention and self-attention pattern in SmolVLA's action expert",
        "type": DiagramType.METHODOLOGY,
        "part": 1,
    },
    # ── Part 2: Flow Matching ──
    {
        "name": "ddpm-vs-flow-paths",
        "description": """A side-by-side comparison of DDPM and Flow Matching trajectories in 2D space.

        LEFT PANEL labeled 'DDPM: Curved, Stochastic Paths':
        - Show 5 trajectories from noise points (red dots, scattered) to data points (blue dots, clustered).
        - The paths are CURVED and WIGGLY — like drunk walks that eventually reach the destination.
        - Small arrows along the paths show the stochastic direction changes.
        - Label: '50-1000 steps needed'

        RIGHT PANEL labeled 'Flow Matching: Straight, Deterministic Paths':
        - Show 5 trajectories from the SAME noise points to the SAME data points.
        - The paths are STRAIGHT LINES — direct connections from noise to data.
        - Clean arrows along the straight paths.
        - Label: '5-10 steps sufficient'

        Background: light grid. Noise region labeled 'Noise N(0,I)' in light red.
        Data region labeled 'Robot Actions' in light blue.
        DDPM paths in red/orange with wiggly style. Flow paths in blue/teal with clean straight style.
        White background, academic style.""",
        "intent": "Visually contrast the curved stochastic paths of DDPM with the straight deterministic paths of flow matching — making clear why fewer steps suffice",
        "type": DiagramType.METHODOLOGY,
        "part": 2,
    },
    {
        "name": "flow-matching-interpolation",
        "description": """A diagram showing linear interpolation from noise to data along a timeline.

        HORIZONTAL TIMELINE from left (τ=0) to right (τ=1), with 5 marked points: τ=0, 0.25, 0.5, 0.75, 1.0.

        At τ=0: A fuzzy/noisy blob labeled 'x₀ ~ N(0,I)' (pure noise) in red.
        At τ=0.25: A slightly less noisy blob (75% noise, 25% signal).
        At τ=0.5: A half-and-half mix — you can start to see the shape of the data.
        At τ=0.75: Mostly clean with slight noise.
        At τ=1.0: A clean robot action trajectory labeled 'x₁ (data)' in blue.

        Below the timeline, show the formula: x_τ = (1 - τ) · x₀ + τ · x₁

        A large arrow along the timeline labeled 'Velocity: v = x₁ - x₀ (constant!)'.

        The transition from red (noisy) to blue (clean) should be a smooth gradient.
        White background, clean academic style. Noise in red (#D4543A), data in blue (#5B8CB8),
        timeline in warm brown (#8b6f4e).""",
        "intent": "Visualize the linear interpolation path from noise to data, showing how the mixture evolves over time and highlighting the constant velocity",
        "type": DiagramType.METHODOLOGY,
        "part": 2,
    },
    {
        "name": "flow-matching-training",
        "description": """A step-by-step training diagram for flow matching, showing the 4-step process.

        Four panels arranged horizontally with arrows between them:

        PANEL 1 'Sample': Show a noise vector x₀ (red jagged line) and a data sample x₁ (blue smooth trajectory).
        Also show τ sampled from uniform [0,1], displayed as a dice roll showing '0.3'.

        PANEL 2 'Mix': Show the linear interpolation x_τ = 0.7·x₀ + 0.3·x₁, resulting in a partially
        noisy trajectory (orange, between red and blue in appearance).

        PANEL 3 'Predict': The mixed sample x_τ and τ=0.3 enter a neural network (purple rounded rectangle
        labeled 'v_θ(τ, x_τ)'). The network outputs a predicted velocity vector (purple arrow).

        PANEL 4 'Loss': The predicted velocity (purple arrow) is compared with the target velocity
        x₁ - x₀ (green arrow). An MSE loss formula: L = ||v̂ - (x₁ - x₀)||²

        White background, clean academic diagram. Noise in red (#D4543A), data in blue (#5B8CB8),
        mixed in orange (#D97757), network in purple (#9B7EC8), target in teal (#7DA488).""",
        "intent": "Show the complete flow matching training loop in four clear steps — sample, mix, predict velocity, compute MSE loss",
        "type": DiagramType.METHODOLOGY,
        "part": 2,
    },
    {
        "name": "flow-matching-inference",
        "description": """A diagram showing the flow matching inference process: ODE integration from noise to clean actions.

        Show a horizontal sequence of 11 states (τ=0.0 to τ=1.0 in steps of 0.1):
        - τ=0.0: Noisy blob (pure noise, red)
        - τ=0.1 to τ=0.9: Progressively cleaner states, transitioning from red to blue
        - τ=1.0: Clean action trajectory (blue smooth curve)

        Between each pair of states, show an arrow labeled 'v_θ' (the network predicts velocity).
        Below each arrow, show the Euler update: x_{τ+Δτ} = x_τ + Δτ · v_θ(τ, x_τ)

        At the bottom, a bar showing 'Step 1', 'Step 2', ..., 'Step 10' with '10 forward passes total'.

        Emphasize: the path is nearly straight (the intermediate states fall roughly on a line).

        White background, academic style. Noisy states in red (#D4543A) transitioning to
        clean states in blue (#5B8CB8). Velocity arrows in purple (#9B7EC8). Step labels in warm brown.""",
        "intent": "Visualize the Euler integration process during inference — 10 network evaluations transform noise into clean robot actions along a nearly straight path",
        "type": DiagramType.METHODOLOGY,
        "part": 2,
    },
    # ── Part 3: SO-101 Hardware ──
    {
        "name": "so101-overview",
        "description": """A clean diagram showing the SO-101 robot arm system with labels.

        CENTER: A side-view illustration of a 6-DOF robot arm (similar to SO-101 design) with labeled joints:
        - Joint 1: 'Base Rotation' (at the bottom, rotating left/right)
        - Joint 2: 'Shoulder' (tilting the upper arm up/down)
        - Joint 3: 'Elbow' (bending the forearm)
        - Joint 4: 'Wrist Pitch' (tilting the hand up/down)
        - Joint 5: 'Wrist Roll' (rotating the hand)
        - Joint 6: 'Gripper' (opening/closing)

        LEFT: A second, lighter-colored arm labeled 'Leader Arm (you control this)' with a hand icon.
        An arrow from leader to follower labeled 'Teleoperation: leader moves → follower copies'.

        RIGHT: A USB cable icon connecting to a laptop icon, labeled 'USB Serial (Feetech STS3215 bus)'.

        BOTTOM: Camera icon labeled 'USB Webcam (640×480, 30 FPS)' pointing at the workspace.
        A small price tag: '~$100 total'.

        White background, clean technical illustration style. Arm in blue (#5B8CB8),
        leader in lighter blue, labels in warm brown (#8b6f4e), price in teal (#7DA488).""",
        "intent": "Provide a clear overview of the SO-101 system — follower arm, leader arm, USB connection, camera, and labeled joints",
        "type": DiagramType.METHODOLOGY,
        "part": 3,
    },
    {
        "name": "so101-parts",
        "description": """An exploded/parts diagram showing all components of the SO-101 robot arm.

        Arrange components in a clean grid layout with labels:

        TOP ROW:
        - 6 × Feetech STS3215 servo motors (show as small blue boxes labeled '6× STS3215 Servo')
        - USB-to-TTL adapter (small green box)
        - 12V power supply (small gray box with plug icon)

        MIDDLE ROW:
        - 3D printed frame pieces (several orange pieces showing arm segments, base plate, gripper)
        - Assembly hardware: screws, nuts, bearings

        BOTTOM ROW:
        - Complete assembled arm (showing how all pieces fit together)
        - Text: 'Assembly time: 2-4 hours'

        Arrows from individual parts to their location on the assembled arm.
        White background, clean parts-list style. Servos in blue (#5B8CB8),
        3D prints in orange (#D97757), electronics in teal (#7DA488).""",
        "intent": "Show all physical components of the SO-101 in an organized parts diagram — making it clear what you need to buy and build",
        "type": DiagramType.METHODOLOGY,
        "part": 3,
    },
    # ── Part 4: Deployment Pipeline ──
    {
        "name": "dataset-structure",
        "description": """A diagram showing the structure of a LeRobot dataset from recording.

        TOP: A filmstrip showing 5 sequential camera frames from a pick-and-place task
        (simplified: colored rectangles representing robot arm + cube at different positions).
        Label: 'observation.images.front (480×640 RGB, 30 FPS)'

        MIDDLE: A graph/chart showing 6 joint angle curves over time (6 colored lines),
        with subtle annotations at key moments: 'reach', 'grasp', 'lift', 'place'.
        Two rows: 'observation.state (6 joint angles)' and 'action (6 target angles)'.

        BOTTOM: A data table showing:
        | Episode | Frames | Task | Duration |
        | 001 | 200 | "Pick up the red cube..." | 6.7s |
        | 002 | 185 | "Pick up the red cube..." | 6.2s |
        | ... | ... | ... | ... |
        | 050 | 210 | "Pick up the red cube..." | 7.0s |
        Text: '50 episodes × ~200 frames = 10,000 samples'

        White background, academic style. Images in blue (#5B8CB8), states in orange (#D97757),
        actions in teal (#7DA488), table in warm brown.""",
        "intent": "Visualize the complete structure of a recorded robot dataset — camera frames, joint angles over time, and the tabular episode structure",
        "type": DiagramType.METHODOLOGY,
        "part": 4,
    },
    {
        "name": "control-loop",
        "description": """A circular diagram showing the real-time control loop for deploying SmolVLA.

        Draw a circular flow with 4 nodes connected by arrows:

        NODE 1 (top, blue): 'Observe' — Camera icon capturing an image. Label: '640×480 RGB frame'
        Arrow down-right to Node 2.

        NODE 2 (right, orange): 'Encode + Plan' — Brain/network icon. Sub-steps listed:
        '1. SigLIP → 64 tokens'
        '2. SmolVLM2 → VLM features'
        '3. Flow Matching (10 steps) → 50 actions'
        Label: '~300ms total'

        NODE 3 (bottom, teal): 'Execute' — Robot arm icon. Label: 'Send first 15 actions to servos (0.5s)'
        Arrow up-left to Node 4.

        NODE 4 (left, purple): 'Repeat' — Clock/loop icon.
        Label: 'Re-observe every 0.5s'
        Arrow up to Node 1.

        In the center of the circle: 'SmolVLA Control Loop @ 10-30 Hz'

        White background, clean circular flow diagram. Use the standard color palette.""",
        "intent": "Show the observe-encode-execute-repeat control loop that runs continuously during SmolVLA deployment on a real robot",
        "type": DiagramType.METHODOLOGY,
        "part": 4,
    },
    # ── NEW: Cross-attention introduction and SmolVLA deep-dive ──
    {
        "name": "self-attention-to-cross-attention",
        "description": """A three-panel progression showing the evolution from self-attention to cross-attention.

        PANEL 1 'Self-Attention (what you know)':
        Show a row of 5 colored tokens (purple circles labeled Q1-Q5).
        Arrows from each token to all others (bidirectional or causal).
        All tokens come from the SAME sequence.
        Matrix visualization: a 5x5 attention grid, all same color (purple).
        Label: 'Queries, Keys, Values all come from the SAME input sequence.'

        PANEL 2 'The Conditioning Problem':
        Show the same 5 purple action tokens on the left.
        On the right, show 4 orange observation tokens (camera image, language instruction, robot state).
        A thought bubble from the purple tokens: 'How do I see the observations?'
        Two bad options crossed out:
        - 'Concatenate everything?' → wasteful, O((A+O)²)
        - 'Ignore observations?' → blind robot
        Label: 'Action tokens need to be CONDITIONED on what the robot sees.'

        PANEL 3 'Cross-Attention (the solution)':
        Show 5 purple tokens on the left (labeled 'Queries from actions').
        Show 4 orange tokens on the right (labeled 'Keys & Values from observations').
        Arrows go FROM purple TO orange (queries attend to keys/values).
        Matrix visualization: a 5×4 rectangular grid (not square!). Purple rows, orange columns.
        Label: 'Queries from one sequence, Keys/Values from another. Action tokens "look at" the world.'

        White background, clean academic style. Action tokens in purple (#9B7EC8),
        observation tokens in orange (#D97757). Arrows in blue (#5B8CB8).""",
        "intent": "Gradually introduce cross-attention by building from self-attention — showing that CA is simply SA where K,V come from a different sequence, which naturally gives conditioning",
        "type": DiagramType.METHODOLOGY,
        "part": 1,
    },
    {
        "name": "cross-attention-conditioning",
        "description": """A diagram explaining WHY cross-attention equals conditioning on observations.

        TOP: Show a mathematical formulation side by side:
        LEFT: 'Self-Attention: Attn(Q, K, V) where Q=K=V= f(same input)'
        RIGHT: 'Cross-Attention: Attn(Q, K, V) where Q=f(actions), K=V=g(observations)'

        MIDDLE: A concrete robot example:
        - Show a robot arm image on the right with 4 orange feature tokens extracted from it
        - Show 5 purple action tokens on the left (noisy actions being refined)
        - Arrow from each purple token to the orange tokens: 'Each action asks: what does the world look like?'
        - Attention weights shown as varying-thickness arrows: action token 1 (reaching phase) strongly attends to cup position, action token 40 (placing phase) strongly attends to bowl position

        BOTTOM: The key insight in a highlighted box:
        'Cross-attention = Each action token computes a WEIGHTED AVERAGE of observation features.
        The weights are learned based on what's relevant for THAT specific action step.
        This IS conditioning — the action output depends on (is conditioned by) the observation input.'

        White background. Actions purple (#9B7EC8), observations orange (#D97757),
        insight box in teal (#7DA488).""",
        "intent": "Explain the mathematical equivalence between cross-attention and conditioning — each action token reads from observations via learned attention weights",
        "type": DiagramType.METHODOLOGY,
        "part": 1,
    },
    {
        "name": "smolvla-attention-mask",
        "description": """A detailed attention mask diagram for SmolVLA's action expert, showing exactly which tokens can see which.

        Show a large matrix/heatmap representing the attention pattern inside the action expert.

        The matrix has two sections along each axis:
        - VLM features (64 visual + text tokens) — labeled in orange on the axis
        - Action tokens (50 action steps) — labeled in purple on the axis

        For CROSS-ATTENTION layers:
        - Rows = Action tokens (50), Columns = VLM features (64+text)
        - The entire rectangular block is FILLED (colored teal) — every action token can attend to every VLM token
        - Label: 'Full attention: every action sees the complete scene'

        For SELF-ATTENTION layers:
        - Rows = Columns = Action tokens only (50×50)
        - LOWER TRIANGULAR pattern (causal) — action t can only see actions 1..t-1
        - The upper triangle is empty/white
        - The diagonal is filled
        - Label: 'Causal: action t only sees past actions → temporally smooth'

        Show both matrices side by side with labels 'CA Layer' and 'SA Layer'.

        Below: 'These two patterns ALTERNATE: CA → SA → CA → SA → ... (6+ layers total)
        CA grounds actions in perception. SA ensures temporal coherence.'

        White background. CA blocks in teal (#7DA488), SA blocks in blue (#5B8CB8),
        VLM tokens in orange (#D97757), action tokens in purple (#9B7EC8).""",
        "intent": "Show the exact attention mask pattern in SmolVLA — full cross-attention to VLM features, causal self-attention among action tokens, alternating layer by layer",
        "type": DiagramType.METHODOLOGY,
        "part": 1,
    },
    {
        "name": "smolvla-async-inference",
        "description": """A timeline diagram comparing synchronous vs asynchronous inference in SmolVLA.

        Show TWO horizontal timelines, one above the other:

        TIMELINE 1 'Synchronous (naive)':
        Show alternating blocks on a single timeline:
        - Blue block 'Observe + VLM encode' (300ms)
        - Purple block 'Flow matching (10 steps)' (100ms)
        - Green block 'Execute 15 actions' (500ms)
        - Then IDLE gap while waiting
        - Blue block 'Observe + VLM encode' (300ms)
        - Purple block 'Flow matching' (100ms)
        - Green block 'Execute 15 actions' (500ms)
        Total cycle: ~900ms. The robot sits idle during encoding.
        Mark idle periods with red hatching. Label: 'Robot idle while brain thinks — 13.7s per task'

        TIMELINE 2 'Asynchronous (SmolVLA)':
        Show TWO parallel tracks:
        Track A (VLM + Flow): Blue block 'Observe + VLM' overlapping with green execution below
        Track B (Robot): Green block 'Execute chunk' running simultaneously
        The key: while the robot executes chunk N, the VLM is already processing observation N+1.
        No idle gaps! The blocks overlap perfectly.
        Label: 'Brain thinks while hands move — 9.7s per task (30% faster)'

        Below both: 'Key insight: Decouple perception from execution. The 50-step action chunk gives
        a 500ms buffer — plenty of time for the VLM to process the next observation.'

        White background. VLM encoding in blue (#5B8CB8), flow matching in purple (#9B7EC8),
        execution in teal (#7DA488), idle in red hatching (#D4543A).""",
        "intent": "Show the concrete timing advantage of asynchronous inference — the robot never waits because perception happens during action execution",
        "type": DiagramType.METHODOLOGY,
        "part": 1,
    },
    {
        "name": "openvla-sequential-bottleneck",
        "description": """A diagram showing the sequential token generation bottleneck in OpenVLA, especially with action chunking.

        TOP SECTION 'Single-Step OpenVLA (7 tokens)':
        Show a horizontal sequence of 7 boxes being generated left to right, each with a clock icon:
        Token 1 (joint 1) → Token 2 (joint 2) → ... → Token 7 (gripper)
        Each arrow labeled '~50ms (one 7B forward pass)'
        Total: 7 × 50ms = 350ms. Labeled 'Manageable: ~3 Hz'

        MIDDLE SECTION 'What if OpenVLA tried action chunking? (hypothetical)':
        Show a much longer sequence: 16 timesteps × 7 joints = 112 tokens
        Group them visually: [t1: j1 j2 j3 j4 j5 j6 j7] [t2: j1 j2 j3 j4 j5 j6 j7] ... [t16: ...]
        Each group is a different shade, showing the 16 timesteps
        Total: 112 × 50ms = 5.6 seconds. Labeled in RED: '5.6 seconds — UNUSABLE for real-time control'
        A large red X over this section.

        BOTTOM SECTION 'SmolVLA comparison':
        Show a single block labeled 'Flow Matching: 10 Euler steps through 100M network'
        Inside: ALL 50×7=350 values generated SIMULTANEOUSLY in each step
        Total: 10 × 30ms = 300ms. Labeled in GREEN: '300ms for 50 steps — 166 Hz effective throughput'

        White background. OpenVLA tokens in orange (#D97757), timing in red (#D4543A),
        SmolVLA block in teal (#7DA488). Clock icons in warm brown.""",
        "intent": "Make the sequential token bottleneck viscerally clear — showing why autoregressive action generation fundamentally cannot scale to action chunks",
        "type": DiagramType.METHODOLOGY,
        "part": 1,
    },
    {
        "name": "smolvla-deployment-pipeline",
        "description": """A wide horizontal pipeline diagram showing the complete SmolVLA deployment process from recording to running.

        Four major stages connected by thick arrows:

        STAGE 1 'Record' (accent/orange):
        - Icon: Person moving leader arm, follower arm copies
        - Below: '50 episodes, 30 FPS, ~10K frames'
        - Camera + joint data flowing into a dataset icon

        STAGE 2 'Upload & Train' (blue):
        - Icon: HuggingFace logo → GPU icon
        - Below: 'Fine-tune SmolVLA (450M) for 20K steps'
        - Small flow matching diagram (noise → velocity → clean)
        - '2-4 hours on H100'

        STAGE 3 'Deploy' (teal):
        - Icon: Laptop (MacBook) → robot arm
        - Below: 'Load checkpoint, MPS backend'
        - 'Camera → SigLIP → SmolVLM2 → Action Expert → Servos'

        STAGE 4 'Run' (purple):
        - Icon: Robot arm picking up a cube
        - Below: '10-30 Hz, action chunking (50 steps, execute 15)'
        - Small success checkmark

        White background, clean pipeline style. Each stage a rounded rectangle with its color.
        Thick connecting arrows between stages.""",
        "intent": "Show the complete end-to-end pipeline from recording demonstrations to a working robot — the full journey in one diagram",
        "type": DiagramType.METHODOLOGY,
        "part": 4,
    },
]


async def generate_figure(pipeline, fig_spec):
    """Generate a single figure."""
    print(f"  Generating: {fig_spec['name']}...")
    try:
        result = await pipeline.generate(
            GenerationInput(
                source_context=fig_spec["description"],
                communicative_intent=fig_spec["intent"],
                diagram_type=fig_spec["type"],
            )
        )
        dest = os.path.join(FIGURES_DIR, f"{fig_spec['name']}.png")
        shutil.copy2(result.image_path, dest)
        print(f"  ✓ {fig_spec['name']} → {dest}")
        return True
    except Exception as e:
        print(f"  ✗ {fig_spec['name']} failed: {e}")
        return False


async def main():
    pipeline = PaperBananaPipeline(settings=settings)

    # Parse CLI args
    args = sys.argv[1:]
    regenerate_all = "--all" in args
    only_parts = None
    if "--only" in args:
        idx = args.index("--only")
        only_parts = [int(p) for p in args[idx + 1:] if p.isdigit()]

    # Filter figures
    figs_to_gen = FIGURES
    if only_parts:
        figs_to_gen = [f for f in FIGURES if f.get("part") in only_parts]
    elif not regenerate_all:
        # Skip figures that already exist
        figs_to_gen = [f for f in FIGURES
                       if not os.path.exists(os.path.join(FIGURES_DIR, f"{f['name']}.png"))]

    if not figs_to_gen:
        print("All figures already exist. Use --all to regenerate or --only 1 2 for specific parts.")
        return

    parts_str = f" (Parts {only_parts})" if only_parts else ""
    print(f"Generating {len(figs_to_gen)} figures for Lecture 3{parts_str}...\n")

    # Generate sequentially to avoid rate limits
    success = 0
    for fig in figs_to_gen:
        ok = await generate_figure(pipeline, fig)
        if ok:
            success += 1
        await asyncio.sleep(2)  # brief pause between calls

    print(f"\nDone: {success}/{len(figs_to_gen)} figures generated in {FIGURES_DIR}")


if __name__ == "__main__":
    asyncio.run(main())
