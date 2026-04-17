#!/usr/bin/env python3
"""Generate PaperBanana figures for LeCun's philosophy / motivation slides."""

import asyncio
import os
import shutil
import sys

os.environ["GOOGLE_API_KEY"] = "AIzaSyDGrcsxxmyNe50l37Ufdit56DUiF7INZQ8"
sys.path.insert(0, "/Users/raj/Desktop/Course_Creator/paperbanana_pkg")
sys.path.insert(0, "/Users/raj/Desktop/Course_Creator")

from paperbanana import PaperBananaPipeline, GenerationInput, DiagramType
from paperbanana.core.pipeline import Settings

FIGURES = [
    {
        "id": "lecun-learning-efficiency",
        "description": (
            "A comparison chart showing learning efficiency across biological and artificial systems. "
            "Left side: Human baby icon with '~6 months' to learn walking, teenager icon with '~20 hours' "
            "driving practice to get a license. Right side: LLM icon requiring ~10 trillion tokens of text, "
            "autonomous driving car icon requiring millions of hours of driving data + billions in compute. "
            "Title: 'The Learning Efficiency Gap'. The gap is orders of magnitude — humans learn from "
            "far less data because they build internal world models. Use warm academic colors: "
            "accent=#c2785c, warm=#8b6f4e, teal=#6a9a5b, blue=#5a7fa5."
        ),
        "intent": "Show students the dramatic gap between human and AI learning efficiency, motivating why we need world models",
        "type": "METHODOLOGY",
    },
    {
        "id": "lecun-three-challenges",
        "description": (
            "A diagram showing LeCun's three fundamental challenges for AI. Three columns: "
            "(1) 'Learning World Representations' — icon of a brain with a globe inside, text: "
            "'How to learn representations of the world that capture enough info for prediction and planning'. "
            "(2) 'Handling Uncertainty' — icon of branching paths with question marks, text: "
            "'How to deal with the inherent uncertainty of predictions about the world'. "
            "(3) 'Learning to Reason' — icon of a chess board or planning tree, text: "
            "'How to learn to reason at multiple levels of abstraction and time horizons'. "
            "Title: 'Three Fundamental AI Challenges (LeCun 2022)'. "
            "Use warm academic colors: accent=#c2785c, warm=#8b6f4e, teal=#6a9a5b."
        ),
        "intent": "Present LeCun's three core challenges that motivate the entire JEPA framework",
        "type": "METHODOLOGY",
    },
    {
        "id": "lecun-cognitive-architecture",
        "description": (
            "A detailed architectural diagram of LeCun's proposed cognitive architecture with 6 modules "
            "connected by arrows. Center: 'World Model' (largest box, highlighted in accent=#c2785c) — "
            "it connects to everything. Top-left: 'Configurator' (purple=#8a6baa) — adjusts all other modules. "
            "Left: 'Perception' (blue=#5a7fa5) — takes 'Observation x(t)' as input, outputs 's(t) = Enc(x)'. "
            "Bottom-left: 'Short-Term Memory' — stores state history. "
            "Right: 'Cost Module' (two parts — Intrinsic Cost C_i for drives/instincts, "
            "Trainable Critic C_c for learned costs). "
            "Bottom-right: 'Actor' (teal=#6a9a5b) — outputs 'Action a(t)'. "
            "The World Model predicts future states: s(t+1) = Pred(s(t), a(t)). "
            "Environment arrow loops from Actor output back to Perception input. "
            "Title: 'Cognitive Architecture for Autonomous Intelligence'. "
            "Clean, professional diagram with clear data flow arrows."
        ),
        "intent": "Show LeCun's complete 6-module cognitive architecture — the central role of the world model",
        "type": "METHODOLOGY",
    },
    {
        "id": "lecun-system1-vs-system2",
        "description": (
            "A side-by-side comparison diagram of System 1 (Reactive) vs System 2 (Deliberative) reasoning, "
            "inspired by Daniel Kahneman's framework applied to AI. "
            "Left panel (System 1 — Reactive, blue=#5a7fa5): A simple direct path from Perception → Actor. "
            "Single forward pass, no world model involvement. Examples: 'Catching a ball', 'Reflexive braking'. "
            "Label: 'Fast, unconscious, habitual'. "
            "Right panel (System 2 — Deliberative, accent=#c2785c): A complex loop involving "
            "Perception → World Model → (simulate multiple actions → evaluate costs → pick best) → Actor. "
            "Multiple forward passes through the world model. Examples: 'Planning a route', 'Playing chess'. "
            "Label: 'Slow, conscious, deliberate'. "
            "Title: 'System 1 vs System 2: Two Modes of Intelligence'. "
            "The key insight is that System 2 uses the world model to simulate before acting."
        ),
        "intent": "Explain the two modes of reasoning and show why world models are essential for System 2 deliberative reasoning",
        "type": "METHODOLOGY",
    },
    {
        "id": "lecun-generative-vs-jepa",
        "description": (
            "A two-panel comparison diagram. Top panel: 'Generative Architecture' — shows "
            "an encoder processing input x, then a decoder/generator trying to reconstruct "
            "a full output ŷ in pixel space. Arrow from ŷ to y (ground truth) with "
            "'Reconstruction Loss D(y, ŷ)' label. Problem highlighted: 'Must predict EVERY detail — "
            "every pixel, every blade of grass'. Red X marks showing this is problematic. "
            "Bottom panel: 'Joint Embedding Predictive Architecture (JEPA)' — shows "
            "x-encoder producing representation sx, y-encoder producing representation sy, "
            "and a predictor going from sx to ŝy in REPRESENTATION SPACE (not pixel space). "
            "Loss is D(sy, ŝy) in latent space. Advantage highlighted: 'Predicts only the "
            "ABSTRACT representation — ignores irrelevant details'. Green checkmark. "
            "Title: 'Why NOT Generate Pixels?'. "
            "Use warm academic colors: accent=#c2785c, teal=#6a9a5b."
        ),
        "intent": "Contrast generative approaches with JEPA to show why prediction in latent space is fundamentally better",
        "type": "METHODOLOGY",
    },
    {
        "id": "lecun-energy-landscape-collapse",
        "description": (
            "A figure showing energy-based model landscapes and the collapse problem. "
            "Three subplots arranged horizontally: "
            "(1) 'Good Energy Function' — A 2D energy surface (heatmap style) with low energy "
            "(dark/cool colors) around data points and high energy (warm/hot colors) everywhere else. "
            "Data manifold is a curve with low energy along it. "
            "(2) 'Collapsed Energy' — The entire surface is flat and low energy everywhere — "
            "the model has 'collapsed' and assigns low energy to everything. Label: 'Trivial solution: "
            "f(x) = constant'. Red warning marker. "
            "(3) 'Contrastive Fix' — Shows data points with low energy and explicit 'negative samples' "
            "pushed to high energy. Label: 'Needs carefully chosen negatives'. "
            "Title: 'The Collapse Problem in Energy-Based Models'. "
            "Use warm academic colors for the heatmap."
        ),
        "intent": "Explain the fundamental collapse problem in representation learning and why it matters for JEPA",
        "type": "METHODOLOGY",
    },
    {
        "id": "lecun-four-approaches-collapse",
        "description": (
            "A four-quadrant comparison showing the four methods to prevent collapse in "
            "self-supervised learning. Title: 'Four Methods to Prevent Representation Collapse'. "
            "(1) Top-left: 'Contrastive' (SimCLR, MoCo) — icon of push/pull, positive pairs attracted, "
            "negative pairs repelled. Pro: 'Works well'. Con: 'Needs many negatives, cost grows with data'. "
            "(2) Top-right: 'Regularization' (VICReg, Barlow Twins) — icon of a covariance matrix with "
            "off-diagonals minimized. Pro: 'No negatives needed'. Con: 'Requires careful tuning'. "
            "(3) Bottom-left: 'Distillation / EMA' (BYOL, DINO) — icon showing a student network and "
            "a teacher network (exponential moving average). Pro: 'Simple, effective'. Con: 'EMA is a heuristic'. "
            "(4) Bottom-right: 'Architectural' (Masking / I-JEPA) — icon showing masked input with "
            "only partial information visible. Pro: 'Natural information bottleneck'. Con: 'Design-dependent'. "
            "LeCun advocates the combination of Regularization + Masking used in JEPA. "
            "Use warm academic colors: accent=#c2785c, warm=#8b6f4e, teal=#6a9a5b, blue=#5a7fa5, purple=#8a6baa."
        ),
        "intent": "Survey the landscape of collapse prevention methods and position JEPA's approach",
        "type": "METHODOLOGY",
    },
    {
        "id": "lecun-hierarchical-jepa",
        "description": (
            "A multi-level hierarchical diagram showing LeCun's vision of Hierarchical JEPA (H-JEPA). "
            "Three levels stacked vertically: "
            "Bottom level (Level 1): 'Low-level, short-term predictions' — fast time scale (milliseconds). "
            "Shows a sequence of detailed video frames being predicted one by one. "
            "Middle level (Level 2): 'Mid-level, medium-term predictions' — medium time scale (seconds). "
            "Shows more abstract representations being predicted — object positions, scene layouts. "
            "Top level (Level 3): 'High-level, long-term predictions' — slow time scale (minutes/hours). "
            "Shows very abstract goal states being planned — task completion, sub-goals. "
            "Arrows show that higher levels set goals/targets for lower levels (top-down planning). "
            "Title: 'Hierarchical JEPA: Multi-Scale World Models'. "
            "Annotation: 'Higher levels predict more abstract, longer-horizon outcomes'. "
            "Use warm academic colors: accent=#c2785c, teal=#6a9a5b, blue=#5a7fa5."
        ),
        "intent": "Present LeCun's grand vision of hierarchical world models that predict at multiple time scales and abstraction levels",
        "type": "METHODOLOGY",
    },
    {
        "id": "lecun-self-supervised-paradigm",
        "description": (
            "A timeline or evolution diagram showing the progression of self-supervised learning paradigms. "
            "Three stages shown left to right with arrows: "
            "(1) 'Contrastive Era (2018-2020)' — SimCLR, MoCo, CPC. Icon: push-pull between positive/negative pairs. "
            "Limitation: 'Exponentially many negatives needed in high dimensions'. "
            "(2) 'Non-Contrastive Era (2020-2022)' — BYOL, VICReg, Barlow Twins. Icon: twin networks. "
            "Limitation: 'Still operates on augmented views, not predictions'. "
            "(3) 'JEPA Era (2022-present)' — I-JEPA, V-JEPA, V-JEPA 2. Icon: masked prediction in latent space. "
            "Advantage: 'Predictive, non-generative, handles uncertainty'. "
            "Arrow at the end pointing to 'H-JEPA (future)' in dotted outline. "
            "Title: 'Evolution of Self-Supervised Learning'. "
            "Use warm academic colors."
        ),
        "intent": "Show how JEPA fits in the broader evolution of self-supervised learning, building on lessons from contrastive and non-contrastive methods",
        "type": "METHODOLOGY",
    },
    {
        "id": "lecun-world-model-role",
        "description": (
            "A central diagram showing the role of the world model in LeCun's architecture. "
            "The World Model box is large and central, colored in accent=#c2785c. "
            "Four key functions radiate outward: "
            "(1) Arrow up: 'Estimate missing information' — filling in unobserved parts of the world. "
            "(2) Arrow right: 'Predict future states' — given current state and action, predict what happens next. "
            "(3) Arrow down: 'Simulate action consequences' — mental simulation before acting. "
            "(4) Arrow left: 'Plan action sequences' — search for optimal actions by rolling out the model. "
            "Below, a dashed box showing: 'World Model = Deterministic + Latent Variable. "
            "s(t+1) = Pred(s(t), z(t), a(t)) where z captures uncertainty'. "
            "Title: 'The World Model: Core of Autonomous Intelligence'. "
            "Use warm academic colors."
        ),
        "intent": "Highlight the four key roles of the world model and why it's the most critical module",
        "type": "METHODOLOGY",
    },
    {
        "id": "lecun-prediction-uncertainty",
        "description": (
            "A diagram explaining how JEPA handles prediction uncertainty vs generative models. "
            "Two rows: "
            "Top row (Generative): Input video frame → Decoder → predicted PIXEL output. "
            "The predicted output shows multiple blurry/averaged possible futures (like a blurry face "
            "because the model averages over possibilities). Label: 'Averaging over modes → blur'. "
            "Bottom row (JEPA): Input video frame → Encoder → Predictor → predicted REPRESENTATION. "
            "The representation is shown as a compact vector/embedding. A latent variable z feeds into "
            "the predictor, and different z values give different predicted representations. "
            "These representations map to distinct, sharp possibilities (not blurry). "
            "Label: 'Latent variable captures multimodality → sharp predictions'. "
            "Title: 'Handling Prediction Uncertainty'. "
            "Use warm academic colors."
        ),
        "intent": "Explain why predicting in representation space handles uncertainty better than pixel-space generation",
        "type": "METHODOLOGY",
    },
    {
        "id": "lecun-crepes-multiscale",
        "description": (
            "An illustration of LeCun's 'making crepes' analogy for multi-scale prediction. "
            "A cooking scene with three prediction levels shown simultaneously: "
            "Level 1 (bottom, detailed): Frame-by-frame prediction of hand movements while pouring batter — "
            "'Predict exact wrist angle in 100ms'. Fine motor control. "
            "Level 2 (middle, abstract): Step-level prediction — 'After pouring, spread the batter, "
            "then flip after 30s'. Task decomposition. "
            "Level 3 (top, goal): Goal-level prediction — 'Stack of finished crepes on plate in 10 minutes'. "
            "Each level has a different temporal resolution shown on a time axis. "
            "Title: 'Multi-Scale Prediction: The Crepe-Making Example'. "
            "Key insight: 'You can predict the outcome (crepe on plate) without predicting every pixel "
            "of the batter spreading'. Use warm academic colors."
        ),
        "intent": "Use LeCun's cooking analogy to make multi-scale prediction intuitive — you don't need pixel-perfect prediction for planning",
        "type": "METHODOLOGY",
    },
    {
        "id": "lecun-abandoning-generation",
        "description": (
            "A comparison showing why LeCun argues against generative models for world models. "
            "Left side ('Generative World Model'): A tree diagram where each node branches into many "
            "possible pixel-level predictions. The tree explodes exponentially — combinatorial explosion. "
            "Label: 'Intractable: must model every pixel detail'. "
            "The branches are colored red to show the problem. "
            "Right side ('JEPA World Model'): The same tree but in representation space — far fewer "
            "meaningful branches because irrelevant details are abstracted away. "
            "Label: 'Tractable: only model what matters'. "
            "The branches are colored green to show the solution. "
            "Center quote: '\"Generative models are doomed to waste resources on predicting irrelevant "
            "details\" — Yann LeCun'. "
            "Title: 'The Case Against Generative World Models'. "
            "Use warm academic colors."
        ),
        "intent": "Drive home LeCun's core argument against generative models and for JEPA-style prediction",
        "type": "METHODOLOGY",
    },
]


async def main():
    settings = Settings(
        vlm_model="gemini-2.0-flash",
        image_model="gemini-3-pro-image-preview",
        refinement_iterations=2,
    )
    pipeline = PaperBananaPipeline(settings=settings)
    outdir = "/Users/raj/Desktop/Robotics Research/Modern-Robot-Learning-V2-Bootcamp/lecture-world-models-jepa/public/figures"

    for fig in FIGURES:
        outpath = os.path.join(outdir, f"{fig['id']}.png")
        if os.path.exists(outpath):
            print(f"[SKIP] {fig['id']} already exists")
            continue

        print(f"\n[GEN] {fig['id']} ...")
        dtype = DiagramType.METHODOLOGY
        inp = GenerationInput(
            source_context=fig["description"],
            communicative_intent=fig["intent"],
            diagram_type=dtype,
        )
        try:
            result = await pipeline.generate(inp)
            shutil.copy2(result.image_path, outpath)
            print(f"  ✓ saved → {outpath}")
        except Exception as e:
            print(f"  ✗ FAILED: {e}")

    print("\nDone — all LeCun motivation figures generated.")


if __name__ == "__main__":
    asyncio.run(main())
