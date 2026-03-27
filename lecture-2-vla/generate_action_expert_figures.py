"""Generate PaperBanana figures for the expanded Action Expert slides.

Usage:
    python generate_action_expert_figures.py
"""
import os
import sys
import asyncio
import shutil

os.environ["GOOGLE_API_KEY"] = "AIzaSyC4Bl7-5DaheriWuV3maoeYuEkLdNucvQI"

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
    {
        "name": "action-expert-transition",
        "description": """A conceptual diagram showing the transition from understanding to action.

        LEFT SIDE: A large purple/blue rounded box labeled 'Fused Embeddings from VLM'.
        Inside it, show a grid of small colored rectangles representing tokens:
        - Blue rectangles labeled '196 Visual Tokens' — each carrying grounded image features
        - Teal rectangles labeled 'N Text Tokens' — language grounded in vision
        Below the box: 'Rich understanding: "There is a red cup at position (x,y), and the instruction says pick it up"'

        CENTER: A large arrow with a big question mark '?' on it, with dashed border.
        Text above the arrow: 'How do we get from understanding to movement?'

        RIGHT SIDE: A robot arm (6-DOF) drawn in clean schematic style with labeled joint angles:
        θ₁ = 1.42, θ₂ = -0.38, θ₃ = 2.15, θ₄ = 0.67, θ₅ = -1.23, θ₆ = 0.91
        Below the arm, a vector: Action = [1.42, -0.38, 2.15, 0.67, -1.23, 0.91]
        Label: '7 precise continuous numbers'

        White background, clean academic diagram style.
        VLM embeddings in blue/purple (#5B8CB8/#9B7EC8), action/robot in orange (#D97757),
        question mark in gray dashed.""",
        "intent": "Show the gap between VLM understanding (rich embeddings) and robot action (precise joint angles) — setting up the need for an Action Expert",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "action-expert-ddpm-pipeline",
        "description": """A clean pipeline diagram showing DDPM applied to robot action generation.

        TOP ROW (inputs flowing into the denoiser):
        - LEFT: A box labeled 'Random Noise' containing 7 random numbers [0.5, 0.8, -0.3, 1.1, -0.7, 0.2, 0.9]
          shown as a red/orange noisy waveform icon. Arrow down labeled 'Noisy Actions'.
        - RIGHT: A large purple/blue box labeled 'Fused Embeddings (from VLM)' containing small token rectangles.
          Arrow labeled 'Conditioning' pointing toward the denoiser.
        - SMALL: A circle labeled 't' (timestep) with arrow into denoiser.

        CENTER: A large rounded orange box labeled 'Denoiser Neural Network (Action Expert)'.
        Three arrows entering: noisy actions from top, timestep from side, conditioning from right.
        One arrow exiting bottom: 'Predicted Noise ε̂'

        BOTTOM: A horizontal denoising chain showing the iterative process:
        Step T (pure noise) → Step T-1 → Step T-2 → ... → Step 1 → Step 0 (clean actions)
        At each step, show the action vector getting progressively cleaner:
        - Step T: [0.5, 0.8, -0.3, ...] in red (random)
        - Step T/2: [1.1, -0.2, 1.5, ...] in orange (partially denoised)
        - Step 0: [1.42, -0.38, 2.15, ...] in green (clean)

        Below: 'Same DDPM from Lecture 1 — now conditioned on scene understanding!'

        White background. Noise in red, denoiser in orange (#D97757), conditioning in purple (#9B7EC8),
        clean actions in teal/green (#7DA488). Clean academic flow diagram.""",
        "intent": "Show the complete DDPM pipeline for action generation — noisy actions are iteratively denoised by a neural network conditioned on VLM embeddings, producing clean robot actions",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "action-expert-black-box",
        "description": """A diagram showing the Action Expert denoiser as a black box with clearly labeled inputs and outputs.

        CENTER: A large dark gray/black rounded rectangle labeled 'Neural Network' with a large '?' inside.
        The box has a subtle question mark pattern or texture to emphasize it's unknown.

        THREE INPUTS entering from the left (with arrows):
        1. TOP INPUT: Orange box 'Noisy Actions' containing a small vector [x_t] with noise squiggles.
           Arrow labeled 'What to denoise'
        2. MIDDLE INPUT: Small blue circle labeled 't = timestep' with a clock icon.
           Arrow labeled 'How noisy?'
        3. BOTTOM INPUT: Large purple/blue box 'Fused Embeddings' with small token grid inside.
           Arrow labeled 'Scene context (conditioning)'

        ONE OUTPUT exiting from the right:
        Orange arrow labeled 'Predicted Noise ε̂' leading to a vector with noise pattern.
        Below: 'Subtract from input → cleaner actions'

        BELOW the black box, in a callout:
        'What architecture should this be?'
        '• MLP? Too shallow for complex conditioning'
        '• CNN? Designed for spatial data, not sequences'
        '• Transformer? Has attention — can deeply read embeddings ✓'

        White background. Black box in dark gray (#333), inputs color-coded:
        noisy actions in orange (#D97757), timestep in blue (#5B8CB8),
        embeddings in purple (#9B7EC8), output in orange.""",
        "intent": "Present the Action Expert denoiser as a black box with clear inputs and output, then pose the question of what architecture to use — guiding toward Transformers",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "action-expert-deep-conditioning",
        "description": """A side-by-side comparison of shallow vs deep conditioning for the denoiser.

        LEFT SIDE — 'Shallow Conditioning (✗)':
        A purple box 'Fused Embeddings (196+N tokens)' at top.
        Arrow labeled 'Average Pool' into a single small vector labeled 'context (2048-d)'.
        This single vector is concatenated (shown as stacking) with an orange 'Noisy Actions' vector.
        Both feed into a simple box labeled 'MLP (2 layers)'.
        Output: 'Predicted Noise'.
        RED annotation: 'ALL scene information compressed into ONE vector!'
        RED annotation: 'Cannot ask: which patch has the cup?'
        Red X marks beside the annotations.

        RIGHT SIDE — 'Deep Conditioning (✓)':
        Same purple box 'Fused Embeddings' at top, but now showing individual tokens clearly.
        Orange 'Action Tokens' below them.
        Both sets of tokens feed into a box labeled 'Transformer with Attention'.
        Inside the Transformer, show ATTENTION ARROWS from action tokens to specific VLM tokens:
        - An arrow from action token to a visual token labeled 'cup patch' (thick, green)
        - An arrow from action token to text token 'pick up' (thick, green)
        - Thin/faint arrows to other tokens
        Output: 'Predicted Noise'.
        GREEN annotation: 'Attends to INDIVIDUAL tokens!'
        GREEN annotation: 'Can ask: where exactly is the cup?'
        Green checkmarks beside annotations.

        Center divider with 'vs' in circle.

        White background. Shallow side has red warning styling, deep side has green success styling.
        Embeddings in purple (#9B7EC8), actions in orange (#D97757), attention arrows in teal (#7DA488).""",
        "intent": "Contrast shallow conditioning (averaging embeddings into one vector) with deep conditioning (attention over individual tokens) — showing why the denoiser needs a Transformer with attention to properly use the fused embeddings",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "action-expert-two-transformers",
        "description": """A diagram showing two Transformers side by side — the VLM and the Action Expert.

        LEFT TRANSFORMER (blue/purple):
        A tall stack of transformer layers (26 layers shown as stacked rounded rectangles).
        Label at top: 'VLM Transformer (PaliGemma)'.
        Input from top: blue 'Visual Tokens' + teal 'Text Tokens' entering the stack.
        Output at bottom: purple 'Fused Embeddings'.
        Snowflake ❄ icon. Label: 'Frozen — 2.4B params'.
        Each layer shows: 'Self-Attention → FFN'.

        RIGHT TRANSFORMER (orange):
        A similar but smaller stack of transformer layers.
        Label at top: 'Action Expert Transformer'.
        Input from top: orange 'Noisy Action Tokens'.
        Output at bottom: orange 'Denoised Actions'.
        Flame 🔥 icon. Label: 'Trainable — ???M params'.
        Each layer shows: 'Self-Attention → FFN'.

        BETWEEN THEM: A large gap with a dashed box containing '?' and text:
        'Both are Transformers operating on 2048-d token sequences.
        They speak the same "language."
        But how do we CONNECT them?'

        Both operate on 2048-d vectors — show matching dimension annotations.

        White background. VLM in blue/purple (#5B8CB8/#9B7EC8), Action Expert in orange (#D97757).
        Clean academic architecture diagram.""",
        "intent": "Show the VLM and Action Expert as two separate Transformers that speak the same token language, but need a connection mechanism — setting up the shared attention solution",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "action-expert-connection-question",
        "description": """A diagram showing two Transformer stacks with a prominent question about how to connect them.

        LEFT: VLM Transformer stack (blue/purple, 26 layers, frozen ❄).
        At its output, fused embeddings shown as a sequence of colored rectangles:
        [blue blue blue ... teal teal teal] representing [visual tokens | text tokens].
        Label: 'Rich scene understanding — but trapped inside the VLM!'

        RIGHT: Action Expert Transformer stack (orange, trainable 🔥).
        At its input, noisy action tokens shown as orange rectangles.
        Label: 'Needs scene understanding — but can't see it!'

        BETWEEN THEM: Three possible connection options shown as different arrow styles:
        Option A (top, grayed out): 'Pass final output only' — single thick arrow from VLM output to Action input.
        Red annotation: 'Only sees last-layer features. Loses intermediate representations.'

        Option B (middle, grayed out): 'Cross-attention at every layer' — many crossing arrows between layers.
        Yellow annotation: 'Complex. Requires modifying both architectures.'

        Option C (bottom, highlighted in green): 'Merge into ONE transformer' — the two stacks shown merging/overlapping.
        Green annotation: 'Simple. Elegant. Let everyone share attention!'

        A large green arrow pointing to Option C with text: 'pi0's solution →'

        White background. VLM in blue (#5B8CB8), Action Expert in orange (#D97757),
        winning option highlighted in teal/green (#7DA488).""",
        "intent": "Present three possible ways to connect the VLM and Action Expert Transformers, and highlight pi0's elegant solution: merge them into one shared-attention Transformer",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "action-expert-shared-attention",
        "description": """A visualization of the shared self-attention mechanism with all token types in one room.

        TOP: A conference room metaphor. A large oval table seen from above with seats around it.
        Around the table, three groups of seats:
        - LEFT seats (blue): labeled 'Visual Tokens' — 6-8 blue circles representing image patches
        - TOP seats (teal): labeled 'Text Tokens' — 4-5 teal circles labeled 'pick', 'up', 'the', 'red', 'cup'
        - RIGHT seats (orange): labeled 'Action Tokens' — 3-4 orange circles

        CONNECTIONS: Lines between seats showing attention:
        - THICK orange→blue lines: Action tokens attending to visual tokens (labeled 'Where is the cup?')
        - THICK orange→teal lines: Action tokens attending to text tokens (labeled 'What should I do?')
        - MEDIUM blue↔teal lines: Visual-text cross-attention (maintained from VLM)
        - THIN same-color lines: Within-group attention

        BELOW the table metaphor, a mathematical representation:
        A large attention matrix divided into a 3×3 block grid:
        Rows: [Visual | Text | Action]
        Columns: [Visual | Text | Action]
        All 9 blocks are filled (not blocked/masked), showing every token type attends to every other.
        The Action→Visual and Action→Text blocks are highlighted in bright orange.
        Label: 'Full attention — no masking. Everyone sees everyone.'

        White background. Visual in blue (#5B8CB8), text in teal (#7DA488), action in orange (#D97757).
        Conference room in warm gray. Clean academic style with clear metaphor.""",
        "intent": "Visualize shared self-attention as 'everyone in the same room' — showing how action tokens can naturally read from visual and text tokens when all participate in the same attention mechanism",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "action-expert-input-sequence",
        "description": """A diagram showing the assembly of the full input token sequence for the combined Transformer.

        TOP ROW — Three separate token streams with their sources:
        LEFT: Camera image icon → blue box 'SigLIP + Projection' → row of 196 small blue rectangles.
        Label: '196 Visual Tokens (2048-d each)'. Snowflake ❄.
        CENTER: Text 'pick up the red cup' → teal box 'Tokenizer + Embed' → row of 5 teal rectangles.
        Label: 'N Text Tokens (2048-d each)'. Snowflake ❄.
        RIGHT: Noise icon → orange box 'Action Embed' → row of 7 small orange rectangles.
        Label: '7 Action Tokens (2048-d each)'. Flame 🔥.

        CENTER: Three downward arrows converge at a bar labeled 'Concatenate'.

        BOTTOM: One long horizontal sequence of rectangles:
        [blue blue blue ... blue | teal teal teal teal teal | orange orange orange orange orange orange orange]
        Labels below each section:
        '← 196 visual tokens →  ← N text tokens →  ← 7 action tokens →'

        Below the sequence:
        'Total sequence length: 196 + N + 7 tokens'
        'All tokens are 2048-d vectors — they all "fit" in the same Transformer.'

        Annotations:
        - Over blue section: 'Carry grounded visual features'
        - Over teal section: 'Carry language understanding'
        - Over orange section: 'Start as noise — will be refined'

        White background. Visual in blue (#5B8CB8), text in teal (#7DA488), action in orange (#D97757).
        Clean academic diagram with clear flow from separate streams to unified sequence.""",
        "intent": "Show how the three types of tokens (visual, text, action) are assembled into one unified sequence — all at 2048-d — ready to be processed by shared self-attention in the combined Transformer",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "action-expert-attention-matrix",
        "description": """A SQUARE attention matrix (heatmap) showing cross-modal attention in the combined Transformer.

        CRITICAL: The matrix MUST be perfectly SQUARE. Both rows AND columns must have ALL THREE token types: Visual Tokens, Text Tokens, AND Action Tokens. The columns must mirror the rows exactly.

        ROWS (queries, left side labels):
        - Top rows: 'Visual Tokens' in blue — show 'patch₁', 'patch₂', '...', 'patchₙ'
        - Middle rows: 'Text Tokens' in teal — show 'pick', 'up', 'the', 'red', 'cup'
        - Bottom rows: 'Action Tokens' in orange — show 'act₁', 'act₂', ..., 'act₇'

        COLUMNS (keys, top labels) — MUST MIRROR THE ROWS EXACTLY:
        - Left columns: 'Visual Tokens' in blue — show 'patch₁', 'patch₂', '...', 'patchₙ'
        - Middle columns: 'Text Tokens' in teal — show 'pick', 'up', 'the', 'red', 'cup'
        - Right columns: 'Action Tokens' in orange — show 'act₁', 'act₂', ..., 'act₇'

        The result is a 3×3 BLOCK structure within the square matrix:
        [Visual×Visual | Visual×Text  | Visual×Action ]
        [Text×Visual   | Text×Text    | Text×Action   ]
        [Action×Visual | Action×Text  | Action×Action ]

        HEATMAP block intensities:
        - Visual×Visual (top-left): medium orange — spatial self-attention
        - Visual×Text and Text×Visual: medium-high orange — cross-modal grounding
        - Text×Text: medium orange — language self-attention
        - Action×Visual (bottom-left): BRIGHT/DARK orange — action reads image (label '0.85' in act₁×cup-patch cell)
        - Action×Text (bottom-middle): BRIGHT/DARK orange — action reads instruction (label '0.72' in act₁×pick cell)
        - Visual×Action and Text×Action (right column blocks): very LIGHT/PALE — VLM doesn't need to read noise
        - Action×Action (bottom-right): medium — action self-attention

        Color-coded bracket labels on each side grouping the three sections.

        Callout box: 'THE KEY INTERACTIONS: Action tokens learn WHICH visual patches and WHICH words matter for generating the correct motor commands.'

        Below: 'This attention is computed JOINTLY — action tokens naturally participate in the existing VLM attention.'

        White background. Visual in blue (#5B8CB8), text in teal (#7DA488), action in orange (#D97757).
        Heatmap uses warm orange colors (light = low attention, dark = high). Clean academic matrix.""",
        "intent": "Show the full SQUARE attention matrix of the combined Transformer with ALL THREE token types on BOTH axes — highlighting how action tokens attend strongly to relevant visual patches and instruction words",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "action-expert-ffn-dilemma",
        "description": """A diagram illustrating the FFN problem when VLM and Action Expert share one Transformer.

        TOP: A combined token sequence flowing downward: [blue visual | teal text | orange action tokens].
        Arrow into a box labeled 'Shared Self-Attention ✓' (green checkmark) — this is fine, no problem.

        MIDDLE — THE PROBLEM:
        All tokens exit attention and flow into ONE large box labeled 'Single Shared FFN'.
        Inside the FFN, show the two linear layers: 'Linear (2048→8192) → GELU → Linear (8192→2048)'.

        RED WARNING ARROWS:
        - Arrow from 'Training Loss' at bottom flowing backward (backpropagation) through the FFN.
        - Red highlight on the FFN weights being updated.
        - Blue/teal VLM tokens passing through the SAME updated FFN.
        - Red explosion/warning icon where VLM tokens touch the updated weights.

        RED CALLOUT BOX:
        'PROBLEM: Training updates these FFN weights.
        But frozen VLM tokens also pass through them!
        → VLM pre-training is CORRUPTED.
        → 2.4B params of internet knowledge DESTROYED.'

        BOTTOM: Two outcomes side by side:
        LEFT (red X): 'Shared FFN → VLM weights modified → Catastrophic forgetting'
        RIGHT (green ?): 'Solution: ??? → VLM weights safe → Pre-training preserved'

        White background. FFN box in orange (#D97757), warning elements in red (#D4543A),
        VLM tokens in blue (#5B8CB8), backprop arrows in red dashed. Clean academic diagram.""",
        "intent": "Clearly illustrate why a single shared FFN breaks the frozen VLM — backpropagation during training would update weights that VLM tokens depend on, corrupting pre-trained knowledge",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "action-expert-moe-ffn",
        "description": """A detailed diagram of the Mixture of Experts FFN solution inside one Transformer layer.

        TOP: Combined token sequence after shared attention:
        [blue visual tokens | teal text tokens | orange action tokens]

        SPLIT POINT: A horizontal router bar labeled 'Token Router: split by type'.
        Two arrows diverge from here:

        LEFT PATH (blue/teal, snowflake ❄):
        Blue visual tokens + teal text tokens flow into a large blue box:
        'VLM Expert FFN (Frozen ❄)'
        Inside: 'Linear → GELU → Linear'
        Label below: '2.4B params — from PaliGemma pre-training'
        Label: 'Weights NEVER updated during training'
        Blue lock/snowflake icon.

        RIGHT PATH (orange, flame 🔥):
        Orange action tokens flow into an orange box:
        'Action Expert FFN (Trainable 🔥)'
        Inside: 'Linear → GELU → Linear'
        Label below: '300M params — trained on robot data'
        Label: 'Weights updated by backpropagation'
        Orange flame icon.

        MERGE POINT: Both paths rejoin at a bar labeled 'Recombine into one sequence'.
        Output: [blue visual | teal text | orange action] — same format as input.

        BOTTOM annotation box in green (#7DA488):
        'The genius: Attention is SHARED (action tokens read VLM features).
        FFNs are SEPARATE (training only touches action expert weights).
        VLM stays perfectly intact!'

        White background. VLM path in blue (#5B8CB8), frozen styling.
        Action path in orange (#D97757), trainable styling.
        Router in gray. Clean academic diagram with clear split-and-merge flow.""",
        "intent": "Show the Mixture of Experts solution: after shared attention, tokens are routed to separate FFN experts — frozen for VLM tokens, trainable for action tokens — then recombined, protecting the VLM while enabling learning",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "action-expert-complete-layer",
        "description": """A comprehensive diagram of one complete Action Expert Transformer layer showing all four steps.

        The diagram is a vertical flow through one layer, with step numbers on the left.

        STEP 1 (top):
        Horizontal bar showing combined input: [blue visual | teal text | orange action] tokens.
        Label: 'Step 1: Combined Input Sequence'

        ARROW DOWN into →

        STEP 2:
        Large rounded rectangle labeled 'Shared Self-Attention'.
        Inside, show a small attention pattern: crossing lines between all token types.
        Blue/teal/orange dots representing tokens with arrows between them.
        Label: 'Step 2: All tokens attend to all tokens'
        On the side: 'Action tokens READ visual & text features'

        ARROW DOWN into →

        STEP 3:
        The sequence SPLITS at a junction into two parallel paths:
        LEFT: blue/teal tokens → blue box 'VLM Expert FFN ❄' (frozen, with padlock)
        RIGHT: orange tokens → orange box 'Action Expert FFN 🔥' (trainable, with flame)
        Then both paths MERGE back together.
        Label: 'Step 3: Separate FFNs — protected VLM'

        RESIDUAL CONNECTIONS: Curved arrows from Step 1 bypassing to after Step 2 (with + circles),
        and from before Step 3 to after Step 3 (with + circles). Label: 'Residual connections'

        STEP 4:
        Output sequence: [blue visual | teal text | orange action] tokens (enriched).
        Label: 'Step 4: Output → Next Layer'

        DASHED BOX around the entire layer with label: 'Repeat × 26 layers'

        RIGHT SIDE summary:
        '26 layers of refinement
        Each layer: action tokens get closer to the correct actions
        VLM tokens unchanged — frozen weights'

        White background. Visual in blue (#5B8CB8), text in teal (#7DA488), action in orange (#D97757).
        Frozen elements with blue/gray styling, trainable with orange/warm. Clean academic layer diagram.""",
        "intent": "Show the complete structure of one Action Expert Transformer layer: shared attention → split FFN (MoE) → residual connections, repeated 26 times, with clear annotations of what's frozen vs trainable",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "action-expert-summary",
        "description": """A full summary diagram of the pi0 Action Expert showing the complete pipeline from inputs to outputs.

        TOP INPUTS (left to right):
        1. Camera image → blue 'SigLIP (Frozen ❄, 400M)' → '196 visual tokens'
        2. Text instruction → teal 'Tokenizer + Gemma Embed' → 'N text tokens'
        3. Random noise → orange 'Action Embedding' → '7 action tokens (noisy)'

        MIDDLE: All tokens concatenate into one sequence entering a large rounded box:
        'Combined Transformer (26 layers)'

        Inside the transformer box, show ONE representative layer:
        - 'Shared Self-Attention' spanning full width (all tokens interact)
        - Below attention: a split showing two FFN boxes:
          LEFT: 'VLM Expert FFN ❄ (Frozen)' processing blue/teal tokens
          RIGHT: 'Action Expert FFN 🔥 (Trainable)' processing orange tokens

        DENOISING LOOP: Below the transformer, show the DDPM iterative process:
        An arrow loops from the output back to the input with labels:
        'Step T: noise → Step T-1 → ... → Step 0: clean actions'
        Show 3-4 stages of the noisy actions getting progressively cleaner.

        BOTTOM OUTPUT: Clean action vector [1.42, -0.38, 2.15, 0.67, -1.23, 0.91, 0.30]
        Arrow to a robot arm schematic executing the action.
        Label: 'Precise, continuous joint angles — no discretization!'

        KEY STATS in corner boxes:
        - 'Frozen: 2.4B params (VLM)' with ❄ icon
        - 'Trainable: 300M params (Action Expert)' with 🔥 icon
        - 'Output: Continuous actions via DDPM'

        White background. Vision in blue (#5B8CB8), text in teal (#7DA488),
        action expert in orange (#D97757), clean output in green/teal.
        Clean academic architecture summary diagram.""",
        "intent": "Provide a complete summary of the pi0 Action Expert architecture: frozen VLM + trainable Action Expert with shared attention and separate FFNs, iterative DDPM denoising to produce precise continuous robot actions",
        "type": DiagramType.METHODOLOGY,
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

    figs_to_gen = FIGURES
    # Skip figures that already exist unless --all
    if "--all" not in sys.argv:
        figs_to_gen = [f for f in FIGURES
                       if not os.path.exists(os.path.join(FIGURES_DIR, f"{f['name']}.png"))]

    if not figs_to_gen:
        print("All Action Expert figures already exist. Use --all to regenerate.")
        return

    print(f"Generating {len(figs_to_gen)} Action Expert figures...\n")

    success = 0
    for fig in figs_to_gen:
        ok = await generate_figure(pipeline, fig)
        if ok:
            success += 1
        await asyncio.sleep(2)

    print(f"\nDone: {success}/{len(figs_to_gen)} figures generated in {FIGURES_DIR}")


if __name__ == "__main__":
    asyncio.run(main())
