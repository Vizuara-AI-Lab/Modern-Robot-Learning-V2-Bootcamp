"""Generate PaperBanana figures for Lecture 2: VLA Models (Parts 1–5).

Usage:
    python generate_figures.py              # generate only missing figures
    python generate_figures.py --all        # regenerate everything
    python generate_figures.py --only 3 4   # generate only Parts 3 & 4 figures
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
        "name": "recap-cnn-diffusion",
        "description": """A clean academic diagram showing what students already know from Lecture 1.
        Left side: a camera image of a robot arm flows into a blue box labeled 'CNN Vision Encoder (ResNet-18)'
        which outputs a vector labeled 'Visual Features (512-d)'.
        Right side: a noisy trajectory flows into an orange box labeled 'Diffusion Denoiser (1D U-Net)'
        which outputs a clean smooth trajectory labeled 'Robot Actions'.
        Between them, a large question mark '?' with dashed border and text 'Language?' above it.
        The two known components are connected by solid arrows. The missing language piece is shown with dashed arrows.
        White background, clean minimal academic style. Use blue (#5B8CB8) for vision, orange (#D97757) for diffusion,
        gray dashed for the unknown language piece. Monospace font for dimensions.""",
        "intent": "Show students the two components they already know (vision encoding + action generation) and highlight the missing third piece (language) as a gap to fill",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "bag-of-words-encoding",
        "description": """A clean diagram comparing Bag of Words encoding of two robot instructions.
        Top row: sentence 'pick up the red cup' is broken into words, each word maps to a position in a vocabulary vector.
        Show the sparse vector with 1s at positions for 'pick', 'up', 'the', 'red', 'cup' and 0s elsewhere.
        Bottom row: sentence 'grab the crimson mug' similarly maps to a different sparse vector with 1s at
        'grab', 'the', 'crimson', 'mug'.
        Between the two vectors, show a cosine similarity computation with result = 0.2 (only 'the' overlaps).
        A red X mark with text 'These mean the same thing but look completely different!'
        White background, clean academic style. Use warm orange (#D97757) for the first sentence,
        teal (#7DA488) for the second sentence. Vocabulary shown as a horizontal bar with word slots.""",
        "intent": "Demonstrate that Bag of Words cannot capture semantic similarity — synonymous sentences have almost no overlap",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "word2vec-embedding-space",
        "description": """A 2D scatter plot showing word embedding vectors in a learned space.
        Plot words as labeled dots: 'king', 'queen', 'man', 'woman', 'prince', 'princess' clustered in one region.
        Robot words: 'pick', 'grab', 'grasp', 'lift' clustered nearby. 'cup', 'mug', 'glass' clustered together.
        'red', 'crimson', 'scarlet' clustered together.
        Draw a blue arrow from 'king' to 'man' labeled '- man', then a parallel blue arrow from 'queen' to 'woman'
        labeled '- woman', showing the analogy king-man ≈ queen-woman.
        Draw a green dashed circle around 'pick', 'grab', 'grasp', 'lift' labeled 'synonyms cluster together'.
        White background, scatter plot with light grid lines.
        Dot colors: royalty in purple (#9B7EC8), actions in orange (#D97757), objects in blue (#5B8CB8),
        colors in teal (#7DA488).""",
        "intent": "Show that word embeddings place semantically similar words close together, capturing meaning through geometry",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "gru-sequential-processing",
        "description": """A diagram showing a GRU (Gated Recurrent Unit) processing a sentence word by word.
        The sentence is 'pick up the red cup'.
        Show 5 GRU cells in a horizontal chain, each receiving one word from bottom and passing hidden state to the right.
        Each GRU cell is a rounded rectangle with 'GRU' inside.
        Bottom inputs (word embeddings): 'pick' → 'up' → 'the' → 'red' → 'cup', each as a small colored vector.
        Arrows flow left-to-right between cells showing h₁ → h₂ → h₃ → h₄ → h₅.
        The final hidden state h₅ exits from the last cell into a large vector labeled 'Sentence Embedding (128-d)'.
        Show the hidden state growing/accumulating information — make h₁ small/light, h₅ large/dark.
        Below, add a warning box: 'Bottleneck: entire sentence compressed into ONE vector'.
        White background, clean academic style. GRU cells in blue (#5B8CB8), word inputs in orange (#D97757),
        final embedding in teal (#7DA488). Warning box in light red.""",
        "intent": "Explain how GRU processes text sequentially and compresses everything into a single hidden state vector — highlighting the bottleneck",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "mini-vla-architecture",
        "description": """A detailed architecture diagram of the mini-VLA pipeline with three parallel encoder streams merging into a fusion module and diffusion head.

        TOP STREAM (Vision): Camera image → blue box 'TinyCNN' (3 conv layers + GAP) → blue vector '128-d'
        MIDDLE STREAM (Language): Text 'pick up the red cup' → orange box 'Embedding + GRU' → orange vector '128-d'
        BOTTOM STREAM (State): Joint angles [θ₁, θ₂, ...] → green box 'State MLP' → green vector '128-d'

        All three 128-d vectors flow with arrows into a central box labeled 'Concatenate' producing '384-d',
        then into 'Fusion MLP' (2 layers) producing '128-d fused context',
        then into a large purple box labeled 'Diffusion Head' (from Lecture 1) producing 'Robot Actions'.

        The concatenation point should be visually prominent — show the three vectors being stacked/joined.
        Label each encoder with its parameter count: TinyCNN ~50K, GRU ~25K, MLP ~10K, Fusion ~50K.

        White background, clean academic diagram. Use blue (#5B8CB8) for vision, orange (#D97757) for language,
        teal (#7DA488) for state, purple (#9B7EC8) for diffusion. Monospace for dimensions.""",
        "intent": "Show the complete mini-VLA architecture — three independent encoders fused by simple concatenation + MLP, feeding into diffusion action head",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "mini-vla-generalization-failure",
        "description": """A 2x2 grid showing four test scenarios for the mini-VLA, with checkmark/X results.

        TOP-LEFT (green check): 'Training distribution' — Image of robot + text 'push the cube' → correct action arrow.
        Label: 'Same instruction, same view → Works!'

        TOP-RIGHT (red X): 'New phrasing' — Same image + text 'move the block to the goal' → wrong action arrow.
        Label: 'Synonym words → GRU has never seen these words'

        BOTTOM-LEFT (red X): 'Different camera' — Slightly different view of same scene + same text → wrong action.
        Label: 'New viewpoint → CNN trained on limited angles'

        BOTTOM-RIGHT (red X): 'New task via language' — Image of cups + text 'stack the cups' → random action.
        Label: 'Unseen task → No transfer learning possible'

        Each cell has a colored border: green for success, red for failure.
        White background, clean layout. Success in green (#7DA488), failures in red (#D4543A).""",
        "intent": "Dramatically demonstrate the four failure modes of the naive mini-VLA approach — it only works within the exact training distribution",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "three-levels-language-encoding",
        "description": """A vertical progression diagram showing three levels of language encoding, from simplest to most sophisticated.

        LEVEL 0 (bottom, light gray): Box labeled 'Bag of Words' with icon of scattered letters.
        Arrow up labeled 'Add meaning'.
        Properties: 'No word order, no synonyms, sparse vectors'

        LEVEL 1 (middle, light blue): Box labeled 'Word Embeddings (Word2Vec)' with icon of clustered dots.
        Arrow up labeled 'Add sequence'.
        Properties: 'Semantic similarity, but one vector per word, no context'

        LEVEL 2 (top, light orange): Box labeled 'GRU / Recurrent Network' with icon of chain of cells.
        Properties: 'Word order matters, context-aware, but bottleneck in final hidden state'

        Each level is a wide horizontal band/card with increasing visual emphasis (brighter colors, thicker borders).
        An upward arrow on the left labeled 'Increasing sophistication'.

        White background. Level 0 in gray, Level 1 in blue (#5B8CB8), Level 2 in orange (#D97757).
        Clean, minimal academic diagram.""",
        "intent": "Provide a clear visual summary of the three language encoding approaches covered in Part 1, showing progressive improvement",
        "type": DiagramType.METHODOLOGY,
    },
    {
        "name": "duct-tape-fusion-problem",
        "description": """A visual metaphor showing why concatenation-based fusion is inadequate.

        LEFT SIDE: Three separate pipes (blue for vision, orange for language, green for state) carrying
        information streams. They converge at a junction held together by cartoon duct tape, labeled 'Concatenate + MLP'.
        The output pipe is purple but leaking/cracked, with question marks escaping.

        RIGHT SIDE (contrast): A single unified transformer pipe where blue, orange, and green streams
        flow TOGETHER through multiple layers, interweaving and mixing. The output is a solid, clean purple stream.
        Label: 'Cross-Modal Attention (Coming in Part 4)'.

        The left side is labeled 'mini-VLA: Modalities never interact during encoding'.
        The right side is labeled 'Modern VLA: Modalities attend to each other at every layer'.

        A big arrow between them labeled 'What we need to learn first: Transformers'.

        White background, clean academic style with a touch of humor in the duct tape visual.""",
        "intent": "Create an intuitive visual metaphor for why simple concatenation fails and tease the transformer-based solution coming later",
        "type": DiagramType.METHODOLOGY,
        "part": 2,
    },
    # ── Part 3: Transformers from Scratch ──
    {
        "name": "attention-key-idea",
        "description": """A clean academic diagram showing the self-attention mechanism for the sentence 'pick up the red cup'.

        Show 5 word boxes in a horizontal row at the bottom: 'pick', 'up', 'the', 'red', 'cup'.
        From each word, draw three upward arrows into three lanes labeled Q (Query), K (Key), V (Value).
        Each lane shows linear projections (W_q, W_k, W_v matrices) producing small colored vectors.

        Above the Q/K/V lanes, show a 5×5 attention matrix as a heatmap grid.
        Rows are queries (pick, up, the, red, cup), columns are keys (same words).
        Highlight the cell (row='red', col='cup') as darkest, showing 'red' attends strongly to 'cup'.
        The cell (row='cup', col='red') is also highlighted.

        Above the matrix, show the output: 5 enriched vectors, each a weighted sum of all Values.
        An arrow from the matrix to the outputs labeled 'softmax(QK^T/√d_k) · V'.

        White background, clean academic style. Query vectors in orange (#D97757), Key vectors in blue (#5B8CB8),
        Value vectors in teal (#7DA488). Attention heatmap uses warm colors (white to deep orange).
        Matrix cells clearly labeled.""",
        "intent": "Show the complete self-attention mechanism: words become Q/K/V, compute pairwise scores, and produce context-enriched outputs — the core of Transformers",
        "type": DiagramType.METHODOLOGY,
        "part": 3,
    },
    {
        "name": "transformer-block",
        "description": """A detailed diagram of a single Transformer block with all sub-components.

        Show a vertical flow through one block:
        1. INPUT: 'Token Embeddings [N × d]' at bottom as a horizontal bar of colored rectangles
        2. Arrow up into 'LayerNorm' (thin gray bar)
        3. Arrow into 'Multi-Head Self-Attention' (large blue rounded box with 4 small attention head icons inside)
        4. A RESIDUAL CONNECTION: curved arrow bypassing from input to after attention, merging with a '+' circle
        5. Arrow into another 'LayerNorm' (thin gray bar)
        6. Arrow into 'Feed-Forward Network (FFN)' (large orange rounded box showing: Linear → GELU → Linear, with width expanding 4× then back)
        7. Another RESIDUAL CONNECTION bypassing FFN, merging with '+' circle
        8. OUTPUT: 'Enriched Tokens [N × d]' at top

        On the right side, annotations:
        - Next to attention: 'Who should I listen to? (inter-token)'
        - Next to FFN: 'What should I think? (per-token)'
        - Next to residual: 'Skip connections for gradient flow'

        Show a dashed box around the entire block labeled 'Repeat × L layers'.
        White background. Attention in blue (#5B8CB8), FFN in orange (#D97757), residual arrows in gray dashed,
        LayerNorm in light gray. Clean academic style with clear flow direction.""",
        "intent": "Show the complete Transformer block architecture: attention + FFN + residual connections + LayerNorm, with clear annotations explaining each component's role",
        "type": DiagramType.METHODOLOGY,
        "part": 3,
    },
    {
        "name": "gru-vs-transformer",
        "description": """A side-by-side comparison diagram contrasting GRU and Transformer architectures processing the same sentence 'pick up the red cup'.

        LEFT SIDE (GRU):
        - 5 GRU cells chained left-to-right with arrows between them
        - Each cell receives one word from below
        - Only the LAST cell outputs a single vector labeled 'h₅ (128-d) — Bottleneck!'
        - Arrows only flow left-to-right (sequential)
        - A red circle around the final output labeled 'ONE vector for entire sentence'
        - Gray faded early cells to show information loss

        RIGHT SIDE (Transformer):
        - 5 token positions shown as columns
        - Arrows between ALL pairs of positions (N×N connections shown as crossing lines or a grid)
        - EACH position outputs a rich vector — 5 output vectors at the top
        - All arrows are bidirectional (every token sees every other)
        - Green highlights showing 'N vectors — one per token'
        - All connections computed in parallel (label: 'All at once')

        Center divider with 'vs' in a circle.
        Labels below: 'Sequential, bottleneck, one-directional' vs 'Parallel, per-token, bidirectional'.

        White background. GRU side in muted blue (#5B8CB8) with red warning colors.
        Transformer side in vibrant teal (#7DA488) with green success colors.
        Clean academic comparison layout.""",
        "intent": "Visually contrast the GRU (sequential bottleneck) with the Transformer (parallel, per-token) to show why Transformers fix the three failures identified in Part 2",
        "type": DiagramType.METHODOLOGY,
        "part": 3,
    },
    # ── Part 4: From VLMs to Modern VLAs ──
    {
        "name": "vit-patch-sequence",
        "description": """A diagram showing how a Vision Transformer (ViT) converts an image into a sequence of patch tokens.

        LEFT: A 224×224 image of a robot workspace (table with objects) shown with a 14×14 grid overlay,
        dividing it into 196 patches. A few patches are highlighted/colored to show individual 16×16 pixel regions.

        CENTER: Arrows from the grid patches to a vertical stack showing:
        - 'Flatten' → each 16×16×3 patch becomes a 768-d vector
        - 'Linear Projection' → maps to d_model dimensions
        - 'Add Position Encoding' → unique sinusoidal signal per patch

        RIGHT: A horizontal sequence of 196 colored rectangles labeled 'Patch Token 1', 'Patch Token 2', ..., 'Patch Token 196'.
        These flow into a Transformer block labeled '27 Transformer Layers'.
        Output: 196 enriched tokens, each now context-aware.

        Bottom annotation: 'An image is worth 16×16 words — each patch is a visual token'.
        White background. Image border in blue (#5B8CB8), patch highlights in various Vizuara palette colors,
        Transformer block in orange (#D97757). Clean academic style.""",
        "intent": "Show the core ViT idea: an image is split into patches that become tokens in a Transformer sequence, just like words in a sentence",
        "type": DiagramType.METHODOLOGY,
        "part": 4,
    },
    {
        "name": "vlm-architecture",
        "description": """A clean architecture diagram showing how PaliGemma VLM combines vision and language.

        TOP-LEFT: Camera image → blue box 'SigLIP ViT-So400M (Frozen)' → outputs '196 visual tokens × 1152-d'
        → passes through a small orange box 'Linear Projection' → '196 visual tokens × 2048-d'

        TOP-RIGHT: Text instruction "pick up the red cup" → gray box 'Tokenizer' → small tokens → teal box
        'Embedding Layer' → 'N text tokens × 2048-d'

        CENTER: Both token streams flow into a horizontal bar labeled 'Concatenate' producing a combined sequence:
        [196 visual tokens | N text tokens] × 2048-d

        BOTTOM: The combined sequence enters a large purple box labeled 'Gemma 2B LLM Backbone (Frozen)' containing
        stacked Transformer layers. Inside, show cross-attention arrows between visual and text positions
        (a text token 'red' connecting to red-colored visual patches).

        Output at bottom: 'Fused Vision-Language Embeddings'.

        Parameter counts labeled: SigLIP 400M, Projection ~2M, Gemma 2B.
        White background, clean academic style. Vision path in blue (#5B8CB8), language path in teal (#7DA488),
        projection in orange (#D97757), LLM backbone in purple (#9B7EC8).""",
        "intent": "Show the PaliGemma VLM architecture: SigLIP vision encoder + linear projection + Gemma LLM backbone, with cross-modal attention between image patches and text tokens",
        "type": DiagramType.METHODOLOGY,
        "part": 4,
    },
    {
        "name": "pi0-full-architecture",
        "description": """A comprehensive diagram of the pi0 VLA architecture showing all four components.

        INPUTS (top row, left to right):
        1. Camera image → blue box 'SigLIP (Frozen, 400M)' → '196 visual tokens'
        2. Text 'pick up the red cup' → teal box 'Tokenizer + Gemma Embedding' → 'N text tokens'
        3. Robot state [θ₁...θ₆] → small orange box 'State MLP' → 'state tokens'
        4. Noisy actions x_τ → small red box 'Action Embedding' → 'action tokens'

        MIDDLE: All four token streams concatenate into one sequence.
        This enters a large box labeled 'Combined Transformer (26 layers)'.
        Inside the transformer, show TWO FFN paths:
        - Left FFN path (blue/teal): 'VLM Expert FFN (Frozen, 3B)' — processes visual + text + state tokens
        - Right FFN path (orange): 'Action Expert FFN (Trainable, 300M)' — processes action tokens
        - A SHARED attention block spans across both: 'Shared Multi-Head Attention (all tokens interact)'

        BOTTOM: Action tokens exit → orange box 'Flow Matching Head' → 'Predicted velocity v_θ' → clean actions.
        Label: 'Continuous actions — no discretization'.

        Frozen components have a snowflake ❄ icon. Trainable components have a flame 🔥 icon.
        White background, clean academic style.
        Vision in blue (#5B8CB8), language in teal (#7DA488), action expert in orange (#D97757),
        flow matching in warm (#C4956A). Total params: 2.4B frozen + 300M trainable.""",
        "intent": "Show the complete pi0 architecture: frozen VLM backbone + trainable Action Expert with shared attention and separate FFN experts, flow matching for continuous action generation",
        "type": DiagramType.METHODOLOGY,
        "part": 4,
    },
    {
        "name": "vla-evolution-timeline",
        "description": """A horizontal timeline diagram showing the evolution of VLA architectures from 2023 to 2025.

        LEFT (2023): 'Duct-Tape VLA' — three separate boxes (CNN, GRU, MLP) with duct tape icon joining them.
        Label: 'Separate encoders + concat + MLP. 135K params. No pre-training.'
        Status: crossed-out/deprecated.

        CENTER (2024): 'RT-2 / OpenVLA' — a large VLM box with action tokens appended to the vocabulary.
        Label: 'Pre-trained VLM + tokenized actions. 2-55B params. Internet pre-training.'
        Show action bins (discretized) coming out.
        Status: good but limited by discretization.

        RIGHT (2025): 'pi0' — a VLM backbone with an Action Expert branch and flow field icon.
        Label: 'Frozen VLM + trainable Action Expert + flow matching. 2.7B params. Continuous actions.'
        Status: state of the art, green checkmark.

        A horizontal arrow connects all three, labeled 'Same idea — better ingredients'.
        Below each: key metric improvement:
        - Duct-tape: 'New phrasings: 15%'
        - RT-2: 'New phrasings: 76%'
        - pi0: 'New phrasings: 90%+'

        White background, timeline with year markers, clean academic style.
        2023 in gray (deprecated), 2024 in blue (#5B8CB8), 2025 in orange (#D97757) with golden highlight.""",
        "intent": "Show the rapid evolution of VLA architectures — from naive duct-tape approaches to pre-trained VLM-based systems with flow matching — same core concept, dramatically better results",
        "type": DiagramType.METHODOLOGY,
        "part": 5,
    },
    # ── Part 4 (new): Vision & Vision-Language Models — additional figures ──
    {
        "name": "cnn-vs-vit-attention",
        "description": """A side-by-side comparison diagram: CNN local receptive field vs ViT global attention.

        LEFT SIDE ('CNN — Local Vision'):
        A 7×7 grid of image patches representing a robot workspace. One center patch is highlighted in orange.
        A 3×3 blue outline around it shows the CNN's local receptive field — only the 8 immediate neighbors.
        Arrows connect the center patch only to its 8 neighbors. Text: '3×3 kernel → sees 9 patches'.
        Far-away patches (e.g., a cup in the top-right corner) are grayed out with a red X:
        'Cannot see distant context'.

        RIGHT SIDE ('ViT — Global Attention'):
        The same 7×7 grid. The same center patch is highlighted in orange.
        Thin teal lines radiate from the center patch to EVERY other patch in the grid (all 48 connections).
        The attention lines vary in thickness/opacity to show learned attention weights:
        thick lines to semantically related patches (the cup, the gripper), thin lines to background.
        Text: 'Self-attention → sees ALL 49 patches'.

        Between the two sides, a vertical divider with 'vs' in a circle.
        Below left: '3 layers of 3×3 = 7×7 effective field (still limited)'.
        Below right: '1 layer = full image context (instant global reasoning)'.

        White background, clean academic style. CNN side in blue (#5B8CB8), ViT side in teal (#7DA488).
        Grid patches in light gray, highlighted patch in orange (#D97757).""",
        "intent": "Visually contrast CNN's limited local receptive field with ViT's global self-attention — showing why ViT can reason about spatial relationships across the entire image in a single layer",
        "type": DiagramType.METHODOLOGY,
        "part": 4,
    },
    {
        "name": "vit-attention-heads",
        "description": """Three copies of the same robot workspace image (a table with a red cup, a blue plate, and a robot gripper) shown side by side, each with a different attention pattern overlay.

        IMAGE 1 — 'Head 1: Spatial Neighbors':
        A 14×14 grid overlay on the image. One patch near the center is marked as the query (orange dot).
        Attention lines (orange, varying thickness) connect strongly to the 4-8 nearest spatial neighbors.
        Distant patches have very faint or no connections. Caption: 'Learns local spatial structure'.

        IMAGE 2 — 'Head 5: Part-Whole Relationships':
        Same grid. Query patch is on the cup's handle. Thick purple attention lines connect to ALL patches
        covering the cup body, rim, and base — even though they're not spatially adjacent.
        Other objects (plate, gripper) have faint connections.
        Caption: 'Learns object parts belong together'.

        IMAGE 3 — 'Head 9: Color Grouping':
        Same grid. Query patch is on the red cup. Thick teal lines connect to ALL other red-colored patches
        in the image (the red cup body, any red object). Blue plate patches have zero attention.
        Caption: 'Learns color-based grouping'.

        Below all three: 'Different heads in the same ViT layer learn DIFFERENT visual patterns — automatically, from data!'

        White background. Head 1 uses orange (#D97757), Head 5 uses purple (#9B7EC8), Head 9 uses teal (#7DA488).
        Grid overlay in thin light gray. Clean academic style.""",
        "intent": "Show that different attention heads in a ViT learn qualitatively different visual patterns — spatial proximity, part-whole relationships, and color grouping — providing rich multi-faceted visual understanding",
        "type": DiagramType.METHODOLOGY,
        "part": 4,
    },
    {
        "name": "contrastive-similarity-matrix",
        "description": """A 5×5 similarity matrix showing SigLIP's contrastive learning objective.

        5 images along the left (rows): red cup, blue plate, robot arm, cat, sunset.
        5 captions along the top (columns): 'a red cup on a table', 'a blue dinner plate', 'a robotic arm', 'a cat sitting', 'a sunset over water'.

        The matrix cells show cosine similarity scores:
        - DIAGONAL cells (matching pairs): bright teal (#7DA488) with high scores: 0.92, 0.89, 0.94, 0.91, 0.88.
          Each diagonal cell has a green checkmark.
        - OFF-DIAGONAL cells (mismatched pairs): dim gray with low scores: 0.12, 0.08, 0.15, 0.05, etc.
          A few semantically related off-diagonal cells are slightly brighter: e.g., 'red cup' × 'blue dinner plate' = 0.35 (both tableware).

        Below the matrix, two annotations:
        LEFT arrow pointing to diagonal: 'Contrastive objective: MAXIMIZE these (matching pairs)'
        RIGHT arrow pointing to off-diagonal: 'MINIMIZE these (non-matching pairs)'

        At the bottom: 'After 400M pairs, the vision encoder learns: "red cup" text ≈ red cup image in embedding space'

        White background. Diagonal cells in teal (#7DA488). Off-diagonal in light gray.
        Row labels (images) shown as small thumbnail icons. Column labels (text) in orange (#D97757).
        Clean academic matrix style with clear grid lines.""",
        "intent": "Explain SigLIP's contrastive learning objective visually — matching image-text pairs should have high similarity (diagonal), non-matching pairs should have low similarity — this is how vision learns language-grounded features",
        "type": DiagramType.METHODOLOGY,
        "part": 4,
    },
    {
        "name": "cross-modal-attention-viz",
        "description": """A visualization showing cross-modal attention between text tokens and image patches.

        TOP: A 14×14 grid overlaid on a robot workspace image showing a red cup on a brown table with a robot gripper.
        The grid divides the image into 196 patch positions.

        BOTTOM: A row of text tokens: 'pick', 'up', 'the', 'red', 'cup'.
        Each text token is in an orange (#D97757) box.

        ATTENTION ARROWS:
        - From 'red' token: thick teal (#7DA488) arrows fan upward to the ~6 image patches that contain red-colored pixels
          (the cup body). These arrows are the thickest, showing highest attention weight (labeled '0.85').
        - From 'cup' token: thick blue (#5B8CB8) arrows connect to the ~8 patches containing the cup shape
          (body, handle, rim). Labeled '0.78'.
        - From 'pick' token: medium purple (#9B7EC8) arrows connect to the ~4 patches containing the robot gripper.
          Labeled '0.62'.
        - From 'up' and 'the': very faint gray arrows spread diffusely — these function words have low attention.

        RIGHT SIDE: A small legend box:
        'Thick arrow = high attention weight
         The model learned: "red" → red patches, "cup" → cup patches, "pick" → gripper patches'

        Below: 'Cross-modal attention emerges automatically from training — the model discovers which image regions correspond to which words.'

        White background, clean academic style. Text tokens in orange, attention arrows in palette colors,
        image grid in light gray.""",
        "intent": "Visualize how cross-modal attention in a VLM connects text tokens to their corresponding image patches — showing that 'red' attends to red pixels, 'cup' to cup shape, 'pick' to the gripper — this grounding emerges from pre-training",
        "type": DiagramType.METHODOLOGY,
        "part": 4,
    },
    # ── Part 5: Moving Well — Turning Understanding into Action ──
    {
        "name": "vlm-to-vla-gap",
        "description": """A conceptual diagram showing the gap between VLM understanding and robot action.

        LEFT SIDE: A thought bubble / brain icon labeled 'VLM Understanding'. Inside the bubble:
        - A camera image of a red cup on a table
        - Text 'pick up the red cup'
        - Output text: 'I see a red cup on the table, to the left of the blue plate.'
        The bubble is in blue (#5B8CB8) with clean styling, labeled 'World of Language & Images'.

        CENTER: A large gap / chasm / bridge with a big question mark '?' in the center.
        Dashed lines cross the gap. Label above: 'THE GAP — How do we get from understanding to movement?'

        RIGHT SIDE: A robot arm (6-DOF, like SO-101) with numerical labels at each joint:
        - Joint 1: 1.42 rad
        - Joint 2: -0.38 rad
        - Joint 3: 2.15 rad
        - Joint 4: 0.67 rad
        - Joint 5: -1.23 rad
        - Joint 6: 0.91 rad
        The arm is in orange (#D97757), labeled 'World of Joint Angles & Motor Commands'.

        Below the gap: 'This is the problem Part 5 solves.'

        White background, clean academic style. Left side (understanding) in calm blue, right side (action) in active orange,
        gap in gray dashed.""",
        "intent": "Dramatically show that understanding images and text (VLM) is not enough — there's a fundamental gap between comprehension and physical action that must be bridged",
        "type": DiagramType.METHODOLOGY,
        "part": 5,
    },
    {
        "name": "robot-action-dimensions",
        "description": """A labeled diagram of a 6-DOF robot arm (similar to SO-101) showing each joint as an action dimension.

        The robot arm is drawn in a clean side-view with 6 labeled joints:
        - Joint 1 (Base): circular arrow showing rotation, labeled 'θ₁ = 1.42 rad' in orange (#D97757)
        - Joint 2 (Shoulder): arc arrow showing lift, labeled 'θ₂ = -0.38 rad' in blue (#5B8CB8)
        - Joint 3 (Elbow): arc arrow showing bend, labeled 'θ₃ = 2.15 rad' in teal (#7DA488)
        - Joint 4 (Wrist Pitch): arc arrow showing tilt, labeled 'θ₄ = 0.67 rad' in purple (#9B7EC8)
        - Joint 5 (Wrist Roll): circular arrow, labeled 'θ₅ = -1.23 rad' in warm (#C4956A)
        - Joint 6 (Gripper): open/close arrows, labeled 'θ₆ = 0.30' in orange (#D97757)

        On the right side, a stacked vector representation:
        Action = [1.42, -0.38, 2.15, 0.67, -1.23, 0.30]
        Each element colored to match its corresponding joint.
        Label below: '6 action dimensions — one number per joint'

        At the bottom: 'At each timestep, the robot needs EXACTLY these 6 numbers to know where to move.'

        White background, clean academic diagram with the robot arm as the focal point.
        Each joint clearly labeled with both its name and its angle value.""",
        "intent": "Visually explain what 'action dimensions' are — each joint on a robot arm is one dimension, and a complete action is a vector of all joint angles",
        "type": DiagramType.METHODOLOGY,
        "part": 5,
    },
    {
        "name": "continuous-vs-discrete-actions",
        "description": """A side-by-side comparison showing continuous vs discrete values, applied to robot actions.

        TOP SECTION — 'Discrete (like words)':
        A horizontal number line from 0 to 10 with ONLY integer markers (0, 1, 2, 3, ..., 10).
        Dots sit exactly on the integers. No values between them.
        Label: 'Finite options: you must pick 0, 1, 2, 3... Nothing in between.'
        Examples below: 'Light switch: ON/OFF. Dice: 1-6. Word token: #4521.'
        Colored in blue (#5B8CB8).

        BOTTOM SECTION — 'Continuous (like joint angles)':
        A smooth horizontal number line from -π to +π with a continuous gradient fill.
        Several dots are placed at arbitrary non-integer positions: 1.4237, -0.387, 2.1519.
        Zoomed inset showing that between any two points, there are infinitely more points.
        Label: 'Infinite precision: 1.42, 1.421, 1.4217, 1.42173... Any value is valid.'
        Examples below: 'Dimmer switch: 0%-100%. Steering wheel. Joint angle: -3.14 to +3.14 rad.'
        Colored in orange (#D97757).

        CENTER arrow from discrete to continuous labeled: 'Robot joints live HERE — in the continuous world.'

        White background, clean academic style. Clear visual contrast between the sparse integer dots
        and the dense continuous gradient.""",
        "intent": "Make the distinction between discrete and continuous values crystal clear — robots operate in continuous space, which creates a fundamental challenge when trying to use token-based models",
        "type": DiagramType.METHODOLOGY,
        "part": 5,
    },
    {
        "name": "actions-as-tokens",
        "description": """A parallel analogy diagram showing how text tokens and action tokens work side by side.

        LEFT COLUMN — 'Text Tokens (how VLMs work)':
        1. A vocabulary list showing: 'pick' = #4521, 'up' = #892, 'the' = #103, 'red' = #2847, 'cup' = #6134
        2. The sentence 'pick up the red cup' broken into tokens with their numbers
        3. Arrow to VLM box → output: next token prediction #6134 ('cup')
        Colored in blue (#5B8CB8).

        RIGHT COLUMN — 'Action Tokens (RT-2's idea)':
        1. An action vocabulary showing: bin_0 = #32001, bin_1 = #32002, ... bin_147 = #32148, ... bin_255 = #32256
        2. A joint angle 1.42 rad mapped to bin 147 = token #32148
        3. Arrow to same VLM box → output: next token prediction #32148 (bin 147)
        Colored in orange (#D97757).

        CENTER: The VLM model box is shared between both columns, with a big '=' sign.
        Label: 'SAME MODEL predicts both words and actions!'

        Below: 'The trick: add 256 new tokens to the vocabulary. Now actions are just another "language" the VLM speaks.'

        A small note: 'But wait — joint angles are continuous. To make them into tokens, we need to DISCRETIZE...'

        White background, clean parallel layout. Text path in blue, action path in orange,
        shared VLM in purple (#9B7EC8).""",
        "intent": "Show the elegant parallel between text tokens and action tokens — both are just numbers from a vocabulary, and the same VLM can predict both",
        "type": DiagramType.METHODOLOGY,
        "part": 5,
    },
    {
        "name": "discretization-explained",
        "description": """A clear, step-by-step diagram explaining discretization using a simple number line example.

        STEP 1 — 'Start: A continuous range':
        A smooth number line from 0 to 10, with a gradient fill. A marker at position 3.7 labeled 'actual value = 3.7'.

        STEP 2 — 'Divide into bins':
        The same number line, now divided into 10 equal bins (0-1, 1-2, 2-3, 3-4, ..., 9-10).
        Each bin is a colored segment. Bin boundaries are marked with vertical tick lines.
        Bins are labeled: Bin 0, Bin 1, Bin 2, Bin 3, ..., Bin 9.
        The value 3.7 falls inside Bin 3 (range 3-4), which is highlighted in orange (#D97757).

        STEP 3 — 'Map to bin number':
        An arrow from the 3.7 marker to a box showing: '3.7 → Bin 3 (center: 3.5)'.
        The output is just the number '3' — the bin index.

        STEP 4 — 'Precision loss':
        A zoomed view showing the bin 3 range (3.0 to 4.0). The actual value 3.7 is marked,
        and the bin center 3.5 is marked. A red double-arrow between them labeled 'Error = 0.2'.
        Text: 'We wanted 3.7 but the bin gives us 3.5. This is discretization error.'

        Below: 'More bins = smaller error. 10 bins → error up to 0.5. 256 bins → error up to ~0.012.'

        White background, clean step-by-step academic layout.
        Number line in teal (#7DA488), highlighted bin in orange (#D97757), error in red (#D4543A).""",
        "intent": "Explain discretization from first principles using a simple number line — divide into bins, map values to bin indices, and show the inevitable precision loss",
        "type": DiagramType.METHODOLOGY,
        "part": 5,
    },
    {
        "name": "rt2-action-tokenization",
        "description": """A detailed diagram showing how RT-2 tokenizes a robot action into discrete tokens.

        TOP: A robot arm with 7 joints, each showing its desired angle:
        θ₁=1.42, θ₂=-0.38, θ₃=2.15, θ₄=0.67, θ₅=-1.23, θ₆=0.91, gripper=0.30

        MIDDLE: For each joint, show a number line from -π to +π divided into 256 bins.
        Highlight the bin each angle falls into:
        - θ₁ = 1.42 → bin 147 (highlighted in orange)
        - θ₂ = -0.38 → bin 112 (highlighted in blue)
        - θ₃ = 2.15 → bin 171 (highlighted in teal)
        - ... (show at least 3 joints in detail, others abbreviated with '...')

        BOTTOM: The final output sequence of token IDs:
        [147, 112, 171, 140, 72, 160, 135]
        These are shown as colored token blocks appended after text tokens:
        [img tokens...] [pick, up, the, red, cup] → [147, 112, 171, 140, 72, 160, 135]
        Label: '7 action tokens added to the VLM output sequence'

        White background, clean flow from physical joints → number lines → discrete tokens.
        Joint angles in orange (#D97757), bins in blue (#5B8CB8), tokens in teal (#7DA488).""",
        "intent": "Show the complete RT-2 action tokenization pipeline: continuous joint angles → discretized into 256 bins → output as a sequence of action tokens appended to the VLM output",
        "type": DiagramType.METHODOLOGY,
        "part": 5,
    },
    {
        "name": "rt2-architecture-diagram",
        "description": """A clean architecture diagram of the RT-2 VLA pipeline.

        INPUT (top-left): Camera image of a robot workspace with a red cup.
        INPUT (top-right): Text instruction 'pick up the red cup'.

        ENCODER: Both inputs flow into a large blue box labeled 'PaLI-X VLM (55B parameters)'.
        Inside the box: 'ViT image encoder + text tokenizer → Transformer backbone'.
        Label: 'Pre-trained on internet-scale image-text data'.

        VOCABULARY MODIFICATION: A callout box showing the expanded vocabulary:
        'Original vocab: 32,000 text tokens'
        '+ 256 new action bin tokens (#32001–#32256)'
        '= 32,256 total tokens'

        OUTPUT: The VLM outputs a sequence of tokens. Show the autoregressive process:
        Step 1: predict token #147 (Joint 1)
        Step 2: predict token #52 (Joint 2)
        ...
        Step 7: predict token #155 (Gripper)

        DECODER: The 7 action tokens map back to continuous angles:
        [147, 52, 230, 89, 12, 201, 155] → [1.41, -0.38, 2.14, 0.67, -1.22, 0.90, 0.31]

        Below: 'Fine-tuned on robot demonstrations — the VLM learns to "speak" in action tokens.'

        White background, clean flow diagram. VLM box in blue (#5B8CB8), action tokens in orange (#D97757),
        decoded actions in teal (#7DA488). Snowflake icon on pre-trained parts.""",
        "intent": "Show the complete RT-2 architecture: a pre-trained VLM with expanded vocabulary that outputs action tokens autoregressively, which are decoded back to continuous joint angles",
        "type": DiagramType.METHODOLOGY,
        "part": 5,
    },
    {
        "name": "discretization-precision-loss",
        "description": """A zoomed-in diagram showing precision loss from discretization in robot joint control.

        TOP: A zoomed view of ONE bin from the 256-bin discretization.
        The bin spans from 1.400 rad to 1.425 rad (width = 0.0245 rad).
        The bin center is marked at 1.4125 rad with a blue (#5B8CB8) circle.
        The desired angle is marked at 1.4237 rad with an orange (#D97757) triangle.
        A red double-arrow between them labeled 'Error: 0.011 rad ≈ 0.6°'.

        MIDDLE: Two side-by-side robot arm comparisons:
        LEFT: 'Desired pose' — robot arm at the exact angle (1.4237 rad), reaching the red cup perfectly.
        Label: 'Where the robot WANTS to be.'
        RIGHT: 'Actual pose' — robot arm at the bin center angle (1.4125 rad), slightly off target.
        Label: 'Where the bin puts it.'
        A small gap between the gripper and the cup is visible.

        BOTTOM: A scale showing error accumulation:
        '1 joint: 0.6° error — OK for reaching'
        '7 joints: up to 4.2° cumulative error — problematic for precision tasks'
        Icons: checkmark next to 'pushing a block', X next to 'threading a needle', X next to 'inserting USB'

        White background. Desired values in orange (#D97757), bin centers in blue (#5B8CB8),
        error indicators in red (#D4543A). Clean academic style with clear annotations.""",
        "intent": "Show exactly how discretization causes precision loss — zooming into a single bin to show the gap between desired angle and bin center, and how this compounds across multiple joints for precision tasks",
        "type": DiagramType.METHODOLOGY,
        "part": 5,
    },
    {
        "name": "autoregressive-speed-problem",
        "description": """A timeline diagram showing the sequential nature of autoregressive action prediction.

        TOP: A horizontal timeline from 0ms to 120ms, with the 100ms deadline marked by a red vertical line
        labeled '100ms budget (10 Hz control)'.

        The timeline shows 7 sequential blocks, each representing one token prediction:
        - Block 1 (0-15ms): 'Joint 1 → bin 147' in orange (#D97757)
        - Block 2 (15-30ms): 'Joint 2 → bin 52' in blue (#5B8CB8)
        - Block 3 (30-45ms): 'Joint 3 → bin 230' in teal (#7DA488)
        - Block 4 (45-60ms): 'Joint 4 → bin 89' in purple (#9B7EC8)
        - Block 5 (60-75ms): 'Joint 5 → bin 12' in warm (#C4956A)
        - Block 6 (75-90ms): 'Joint 6 → bin 201' in blue (#5B8CB8)
        - Block 7 (90-105ms): 'Joint 7 → bin 155' in orange (#D97757) — this block CROSSES the 100ms red line!

        Below the timeline: 'Total: 7 tokens × 15ms = 105ms — OVER the 100ms deadline!'

        CONTRAST (below): A single wide block labeled 'Flow Matching: ALL 7 joints in ~20ms' in teal,
        fitting well within the 100ms budget.

        An arrow comparing the two labeled: 'Sequential vs Simultaneous'.

        White background, clean timeline with colored blocks. Deadline in red (#D4543A),
        overrun section in light red fill.""",
        "intent": "Visualize why autoregressive action prediction is too slow for real-time robot control — 7 sequential token predictions exceed the 100ms control budget, while flow matching predicts all dimensions at once",
        "type": DiagramType.METHODOLOGY,
        "part": 5,
    },
    {
        "name": "flow-matching-intuition",
        "description": """A visual explanation of flow matching using a 2D vector field analogy.

        The diagram is a 2D action space (x-axis: Joint 1 angle, y-axis: Joint 2 angle).

        BACKGROUND: A dense field of small arrows (velocity vectors) covering the entire 2D space.
        The arrows all generally point toward one region — the target action (marked with a green star
        labeled 'Target: [1.42, -0.38]'). Arrows closer to the target are shorter (lower velocity),
        arrows far away are longer and more aligned toward the target.

        TRAJECTORY: A curved path starting from a random point (marked with a red circle labeled
        'Start: Random noise [0.5, 0.8]'). The path follows the arrow field through 5-6 waypoints
        (small dots along the path), eventually reaching the green target star.
        Steps labeled: 'Step 0 (noise)', 'Step 1', 'Step 2', '...', 'Step T (clean action)'.

        RIGHT SIDE: Three small snapshots showing the denoising process:
        1. 'τ = 0: Pure noise' — random point, far from target
        2. 'τ = 0.5: Halfway' — closer, velocity arrows guiding
        3. 'τ = 1.0: Clean action' — at the target, arrows near zero

        BOTTOM: 'The neural network learns this velocity field from robot demonstrations.
        At inference time, start from noise and follow the arrows to the correct action.'

        White background. Vector field arrows in light gray/teal (#7DA488).
        Trajectory in orange (#D97757). Target in green. Start in red.
        Clean academic style with labeled axes.""",
        "intent": "Provide an intuitive visual explanation of flow matching — a learned velocity field guides random noise points to the correct robot action, like a river current carrying a leaf to its destination",
        "type": DiagramType.METHODOLOGY,
        "part": 5,
    },
    {
        "name": "flow-vs-tokenization",
        "description": """A side-by-side comparison of action tokenization (RT-2) vs flow matching (pi0).

        LEFT SIDE — 'Action Tokenization (RT-2)':
        1. Continuous joint angles at top: [1.42, -0.38, 2.15, ...]
        2. Arrow down labeled 'Discretize' to bins: [147, 112, 171, ...]
        3. Arrow down to VLM with '7 sequential predictions' — show 7 boxes chained with arrows
        4. Arrow down labeled 'Decode' back to approximate values: [1.41, -0.39, 2.14, ...]
        5. Red annotation: 'Precision loss ✗' and 'Sequential: 105ms ✗'
        Colored in blue (#5B8CB8) with red warning marks.

        RIGHT SIDE — 'Flow Matching (pi0)':
        1. Random noise at top: [0.5, 0.8, -0.3, ...]
        2. Arrow down labeled 'Velocity field' with arrow swirl icon
        3. A single wide block showing 'ALL dimensions simultaneously' — one pass
        4. Arrow down to precise values: [1.4237, -0.3812, 2.1519, ...]
        5. Green annotation: 'Full precision ✓' and 'Simultaneous: ~20ms ✓'
        Colored in teal (#7DA488) with green checkmarks.

        CENTER divider with 'vs' in a circle.

        BOTTOM comparison table:
        | | Tokenization | Flow Matching |
        | Actions | Discrete | Continuous |
        | Speed | 105ms | ~20ms |
        | Precision | ~0.025 rad | Unlimited |

        White background, clean academic comparison layout.""",
        "intent": "Directly compare the two approaches to generating robot actions — showing that flow matching solves both the precision and speed problems of action tokenization",
        "type": DiagramType.METHODOLOGY,
        "part": 5,
    },
    {
        "name": "pi0-visual-encoding-detail",
        "description": """A detailed diagram of pi0's Step 1: Visual Encoding with SigLIP.

        LEFT: A camera image of a robot workspace (table with red cup, robot arm).
        Arrow labeled 'Camera capture' flowing right.

        CENTER-LEFT: The image shown with a 14×14 grid overlay, dividing it into 196 patches.
        A few patches are highlighted/numbered. Arrow labeled 'Split into patches' flowing right.

        CENTER: A blue box labeled 'SigLIP ViT-So400M' with a snowflake ❄ icon (frozen).
        Inside: '27 Transformer Layers, trained on 400M image-text pairs'.
        Each patch enters as a 768-d vector, exits as a 1152-d token.

        RIGHT: A row of 196 colored rectangles labeled 'Visual Tokens'.
        Each rectangle represents one patch token (1152-d).
        A few tokens are annotated: the patch covering the red cup is labeled 'knows this is a cup',
        the patch covering the gripper is labeled 'knows this is a gripper'.

        BOTTOM: 'Output: 196 visual tokens × 1152-d. Each token carries language-aligned visual features — not just pixels, but concepts.'

        White background. Image in natural colors, grid overlay in light gray, SigLIP encoder in blue (#5B8CB8),
        visual tokens in teal (#7DA488). Frozen snowflake icon prominent.""",
        "intent": "Show exactly how pi0's SigLIP encoder processes a camera image: split into patches, encode through frozen ViT, output 196 language-aligned visual tokens",
        "type": DiagramType.METHODOLOGY,
        "part": 5,
    },
    {
        "name": "pi0-vlm-backbone-detail",
        "description": """A detailed diagram of pi0's Step 2: VLM Backbone (PaliGemma).

        TOP-LEFT: A row of 196 blue rectangles labeled '196 Visual Tokens (1152-d each)' from SigLIP.
        Arrow into a small orange box labeled 'Linear Projection (1152 → 2048)'.
        Output: '196 Visual Tokens (2048-d)'.

        TOP-RIGHT: Text 'pick up the red cup' → gray box 'Tokenizer' → teal box 'Embedding Layer'
        → 'N Text Tokens (2048-d each)'.

        CENTER: Both token streams merge at a 'Concatenate' bar:
        [visual₁, visual₂, ..., visual₁₉₆ | text₁, text₂, ..., textₙ] — total sequence length = 196 + N.

        MAIN: The combined sequence enters a large purple box labeled 'Gemma 2B Backbone' with snowflake ❄ (frozen).
        Inside, show stacked transformer layers with self-attention arrows.
        Highlight cross-modal attention: text token 'red' has thick arrows to image patches containing the red cup.
        Text token 'cup' has arrows to cup-shaped patches.
        Label: '26 Transformer Layers — self-attention across vision AND language'.

        OUTPUT: 'Fused Embeddings (196 + N tokens × 2048-d)' — each visual token now enriched with language context,
        each text token enriched with visual grounding.

        BOTTOM: 'The VLM creates a shared understanding where "red cup" in text is connected to the actual red cup patches in the image.'

        White background. Visual path in blue (#5B8CB8), text path in teal (#7DA488), projection in orange (#D97757),
        Gemma backbone in purple (#9B7EC8). Frozen icon prominent.""",
        "intent": "Show how PaliGemma fuses visual and text tokens through self-attention in a frozen transformer backbone — creating cross-modal embeddings where language is grounded in vision",
        "type": DiagramType.METHODOLOGY,
        "part": 5,
    },
    {
        "name": "pi0-action-expert-detail",
        "description": """A detailed diagram of pi0's Step 3: Action Expert with Flow Matching.

        TOP-LEFT: 'Random Noise' — 7 random numbers [0.5, 0.8, -0.3, 1.1, -0.7, 0.2, 0.9] in red circles.
        Arrow labeled 'Action Embedding' into small orange box.
        Output: 'Noisy Action Tokens (7 tokens × 2048-d)'.

        TOP-RIGHT: 'Fused VLM Embeddings' — the output from Step 2, shown as a row of purple/blue/teal rectangles.
        Label: '196 visual + N text tokens (frozen, from PaliGemma)'.

        CENTER: A transformer layer shown in detail:
        - TOP HALF: 'Shared Self-Attention' (large teal box). Action tokens and VLM tokens ALL attend to each other.
          Show attention arrows from noisy action tokens to visual tokens (thick) and text tokens (medium).
          Label: 'Action tokens READ the scene understanding'.
        - BOTTOM HALF: 'Action Expert FFN' (orange box, flame 🔥 icon = trainable).
          Only action tokens pass through this FFN.
          Label: 'Predicts velocity: which direction should each joint move?'.

        BOTTOM: The flow matching denoising process shown as a horizontal sequence:
        Step 0 (noise: [0.5, 0.8, ...]) → Step 1 → Step 2 → ... → Step T (clean action: [1.42, -0.38, ...])
        Each step slightly closer to the target. Arrows between steps show velocity vectors.

        OUTPUT: 'Clean Actions: [1.4237, -0.3812, 2.1519, 0.6700, -1.2305, 0.9103, 0.3000]'
        Label: 'Continuous, precise, all dimensions simultaneously.'

        White background. Noisy actions in red/orange, VLM embeddings in blue/purple,
        Action Expert in orange (#D97757), clean actions in green/teal (#7DA488).""",
        "intent": "Show how the Action Expert uses cross-attention to read the VLM's scene understanding, then uses flow matching to transform random noise into precise continuous robot actions",
        "type": DiagramType.METHODOLOGY,
        "part": 5,
    },
    {
        "name": "pi0-moe-detail",
        "description": """A detailed diagram of pi0's Mixture of Experts architecture within one transformer layer.

        LAYOUT: A single transformer layer shown as a vertical flow.

        INPUT (top): A combined token sequence with three color-coded segments:
        - Blue segment: 'Visual Tokens (196)' labeled 'from SigLIP'
        - Teal segment: 'Text Tokens (N)' labeled 'from tokenizer'
        - Orange segment: 'Action Tokens (7)' labeled 'noisy actions'

        SHARED ATTENTION (middle section, large box):
        All three token types interact in one large attention computation.
        Draw attention arrows between ALL types:
        - Action → Visual (thick): 'action tokens learn what to look at'
        - Action → Text (thick): 'action tokens learn what was requested'
        - Visual → Text (medium): 'visual tokens get language grounding'
        - Visual → Visual, Text → Text (thin): 'within-modality attention'
        Label: 'SHARED Self-Attention — everyone sees everyone'

        SPLIT PATH (below attention):
        The token sequence splits into two paths:

        LEFT PATH (blue/teal, snowflake ❄):
        Visual + Text tokens → large box labeled 'VLM Expert FFN (Frozen, 2.4B)'.
        Label: 'Processes understanding tokens — weights never change.'

        RIGHT PATH (orange, flame 🔥):
        Action tokens → box labeled 'Action Expert FFN (Trainable, 300M)'.
        Label: 'Processes motor command tokens — only part that learns.'

        MERGE (bottom):
        Both paths merge back into one combined sequence for the next layer.
        Arrow labeled 'Repeat × 26 layers'.

        BOTTOM annotation: 'The genius: action tokens can READ visual/text features via shared attention,
        but training ONLY updates the Action Expert FFN. The VLM stays perfectly intact.'

        White background. Visual in blue (#5B8CB8), text in teal (#7DA488), action in orange (#D97757),
        frozen parts have snowflake, trainable parts have flame. Clean academic diagram.""",
        "intent": "Explain the Mixture of Experts architecture in pi0 — shared attention allows cross-modal interaction while separate FFN experts protect the frozen VLM from being modified during training",
        "type": DiagramType.METHODOLOGY,
        "part": 5,
    },
]

# Add "part" key to existing figures that don't have it
for fig in FIGURES:
    if "part" not in fig:
        fig["part"] = 1 if fig["name"] in ("recap-cnn-diffusion", "bag-of-words-encoding",
            "word2vec-embedding-space", "gru-sequential-processing", "three-levels-language-encoding") else 2


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
        print("All figures already exist. Use --all to regenerate or --only 3 4 for specific parts.")
        return

    parts_str = f" (Parts {only_parts})" if only_parts else ""
    print(f"Generating {len(figs_to_gen)} figures for Lecture 2{parts_str}...\n")

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
