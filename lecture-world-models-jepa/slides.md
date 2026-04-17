---
theme: default
title: "World Models Part 2: JEPA, V-JEPA 2, LeWorld & DreamZero"
info: |
  Lecture — Modern Robot Learning from Scratch V2 Bootcamp
  Vizuara — JEPA, V-JEPA 2, LeWorld, DreamZero
class: text-center
drawings:
  persist: true
  presenterOnly: false
  syncAll: true
transition: slide-left
mdc: true
css: unocss
---

<style>
@import url('https://fonts.googleapis.com/css2?family=Caveat:wght@400;500;600;700&display=swap');
:root {
  --claude-bg: #faf8f5;
  --claude-surface: #f5f0e8;
  --claude-card: #ffffff;
  --claude-accent: #c2785c;
  --claude-warm: #8b6f4e;
  --claude-teal: #6a9a5b;
  --claude-blue: #5a7fa5;
  --claude-purple: #8a6baa;
  --claude-text: #3a3025;
  --claude-muted: #8c7e6f;
  --claude-border: #e5ddd3;
  --claude-red: #d4543a;
  --claude-amber: #e8a838;
}
.slidev-layout { background: var(--claude-bg) !important; color: var(--claude-text) !important; overflow-y: auto; max-height: 100vh; }
.slidev-layout::after { content:''; position:absolute; top:14px; right:18px; width:90px; height:28px; background:url('/vizuara-logo.png') no-repeat center/contain; opacity:0.3; pointer-events:none; z-index:10; }
.slidev-layout h1 { font-family:'Caveat',cursive !important; color:var(--claude-accent) !important; font-size:2.1em !important; font-weight:700 !important; line-height:1.2 !important; }
.slidev-layout h2 { font-family:'Caveat',cursive !important; color:var(--claude-warm) !important; font-size:1.5em !important; font-weight:600 !important; }
.slidev-layout h3 { font-family:'Caveat',cursive !important; color:var(--claude-teal) !important; font-size:1.25em !important; font-weight:600 !important; }
.slidev-layout a { color:var(--claude-blue) !important; }
.slidev-layout strong { color:var(--claude-warm); }
.slidev-layout code { background:var(--claude-surface) !important; color:var(--claude-text) !important; border:1px solid var(--claude-border); }
.slidev-layout pre { background:var(--claude-surface) !important; border:1px solid var(--claude-border); border-left:3px solid var(--claude-accent); border-radius:0 8px 8px 0 !important; }
.slidev-layout pre code { color:var(--claude-text) !important; background:transparent !important; border:none !important; }
.shiki, .shiki span { color:var(--claude-text) !important; }
.slidev-layout blockquote { border-left:3px solid var(--claude-accent); background:var(--claude-surface); padding:8px 12px; border-radius:0 8px 8px 0; color:var(--claude-text) !important; }
.slidev-layout blockquote p { color:var(--claude-text) !important; opacity:1 !important; }
.slidev-layout table { border-collapse:collapse; width:100%; }
.slidev-layout th { background:var(--claude-surface); color:var(--claude-accent); padding:6px 10px; border-bottom:2px solid var(--claude-accent); font-family:'Caveat',cursive; font-size:1.1em; }
.slidev-layout td { padding:4px 10px; border-bottom:1px solid var(--claude-border); }
.card { background:var(--claude-card); border-radius:12px; padding:16px; border:1px solid var(--claude-border); }
.accent-card { background:rgba(194,120,92,0.06); border-radius:12px; padding:16px; border:1px solid rgba(194,120,92,0.25); }
.teal-card { background:rgba(106,154,91,0.06); border-radius:12px; padding:16px; border:1px solid rgba(106,154,91,0.25); }
.blue-card { background:rgba(90,127,165,0.06); border-radius:12px; padding:16px; border:1px solid rgba(90,127,165,0.25); }
.purple-card { background:rgba(138,107,170,0.06); border-radius:12px; padding:16px; border:1px solid rgba(138,107,170,0.25); }
.quiz-card { background:rgba(138,107,170,0.06); border-radius:12px; padding:16px; border:2px solid var(--claude-purple); }
.brainstorm-card { background:var(--claude-surface); border-radius:12px; padding:32px; border:2px dashed var(--claude-warm); min-height:280px; display:flex; align-items:center; justify-content:center; }
.notebook-card { background:rgba(90,127,165,0.06); border-radius:12px; padding:16px; border:1px solid rgba(90,127,165,0.25); }
.highlight { color:var(--claude-accent); font-weight:600; }
.inline-video { border-radius:12px; overflow:hidden; }
</style>

# World Models Part 2

## JEPA, V-JEPA 2, LeWorld & DreamZero

<div class="pt-8">
  <span class="px-4 py-2 rounded-lg text-lg" style="background:#c2785c;color:#fff;font-weight:700;">
    Modern Robot Learning from Scratch — V2
  </span>
</div>

<div class="pt-4 opacity-60">
  Vizuara Bootcamp
</div>

<div class="abs-br m-6 flex gap-2">
  <a href="https://vizuara.ai" target="_blank" class="text-sm opacity-50 hover:opacity-100">
    vizuara.ai
  </a>
</div>

---

# Lecture Roadmap

<div class="grid grid-cols-5 gap-3 mt-4">
<div class="accent-card text-sm">

### Part 1
LeCun's Vision — why world models?

</div>
<div class="teal-card text-sm">

### Part 2
JEPA Framework — foundations

</div>
<div class="blue-card text-sm">

### Part 3
V-JEPA → V-JEPA 2

</div>
<div class="purple-card text-sm">

### Part 4
LeWorld — tiny end-to-end JEPA

</div>
<div class="card text-sm" style="border:2px solid var(--claude-accent);">

### Part 5
DreamZero — joint world-action model

</div>
</div>

<div class="mt-6 text-center">

**Previously:** DINO-WM, IRIS, DIAMOND, Building a WFM from Scratch

**Today:** LeCun's philosophy → JEPA → V-JEPA 2 → LeWorld → DreamZero

</div>

---

# Narrative Arc

<div class="mt-4">

```
LeCun's Philosophy    JEPA         V-JEPA 2       LeWorld         DreamZero
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━▶

"Why world         "Predict in     "Scale to       "Tiny end-to-   "Joint world +
 models?"          latent space"   1B params"      end from        action — use
                                                    pixels"         internet video"
```

</div>

<div class="accent-card mt-4">

**Key question for today:** Can we build a world model that learns useful representations of the world — without generating pixels?

</div>

---
layout: center
---

# Part 1

## Yann LeCun's Vision for Autonomous Machine Intelligence

<div class="mt-4 opacity-60">

Based on "A Path Towards Autonomous Machine Intelligence" (LeCun, 2022)

</div>

---

# The Learning Efficiency Gap

<div class="grid grid-cols-2 gap-6 mt-4">
<div class="teal-card">

### Humans

- A **baby** learns to perceive the world in **months**
- A **teenager** learns to drive in **~20 hours** of practice
- A **child** learns physics intuitively just by **observing**
- We learn from **very few examples** — often just one

</div>
<div class="accent-card">

### Current AI

- LLMs need **~10 trillion tokens** of text
- Self-driving cars need **millions of hours** of driving data
- RL agents need **millions of episodes** in simulation
- Even then, they **fail at basic common sense**

</div>
</div>

<div class="mt-4">
<img src="/figures/lecun-learning-efficiency.png" class="mx-auto rounded-lg shadow-lg" style="max-height:220px" />
</div>

---

# Why Are Humans So Efficient?

<div class="mt-4">

LeCun's central thesis: Humans learn so efficiently because they have **internal world models**.

</div>

<div class="grid grid-cols-2 gap-6 mt-4">
<div class="blue-card">

### What a World Model Does

- **Fills in** missing information from partial observations
- **Predicts** what will happen next given an action
- **Simulates** consequences before we act
- **Plans** by mentally "trying out" action sequences

</div>
<div class="purple-card">

### The Key Insight

> "A 10-year-old child can learn to clear the dinner table in a few trials. No current AI system can learn this task."

The difference? The child already has a **world model** — years of observing how objects move, fall, and interact.

</div>
</div>

---

# LeCun's Three Fundamental Challenges

<img src="/figures/lecun-three-challenges.png" class="mx-auto rounded-lg shadow-lg mt-2" style="max-height:260px" />

<div class="grid grid-cols-3 gap-4 mt-4">
<div class="accent-card text-sm">

**1. Learning Representations**

How to learn representations of the world that capture enough information for downstream prediction and planning?

</div>
<div class="teal-card text-sm">

**2. Handling Uncertainty**

The world is inherently unpredictable. How do we represent and manage this uncertainty without generating every possible outcome?

</div>
<div class="blue-card text-sm">

**3. Multi-Scale Reasoning**

How to reason at multiple levels of abstraction — from low-level motor commands to high-level task planning?

</div>
</div>

---

# The Cognitive Architecture

<div class="mt-2">

LeCun proposes a **modular cognitive architecture** with six components — inspired by both neuroscience and control theory.

</div>

<img src="/figures/lecun-cognitive-architecture.png" class="mx-auto rounded-lg shadow-lg mt-2" style="max-height:350px" />

---

# The Six Modules — Explained

<div class="grid grid-cols-2 gap-4 mt-2">
<div class="accent-card text-sm">

### 🧠 World Model (Central)
Predicts future world states: $\hat{s}_{t+1} = \text{Pred}(s_t, z_t, a_t)$

Where $z_t$ is a latent variable capturing **uncertainty**.

This is the **most important** module — everything else serves it.

</div>
<div class="blue-card text-sm">

### 👁️ Perception Module
Encodes raw observations into abstract representations:

$s_t = \text{Enc}(x_t)$

Estimates **missing information** from partial observations.

</div>
<div class="teal-card text-sm">

### 🎬 Actor Module
Computes optimal actions to minimize costs:

**Reactive mode (System 1):** Direct mapping $a = \pi(s)$

**Deliberative mode (System 2):** Uses the world model to plan

</div>
<div class="purple-card text-sm">

### 💰 Cost Module
Two sub-modules:
- **Intrinsic Cost** $C_i$: Hard-wired drives (avoid pain, seek novelty)
- **Trainable Critic** $C_c$: Learned value function

Together they define "what is desirable."

</div>
</div>

<div class="grid grid-cols-2 gap-4 mt-2">
<div class="card text-sm">

### ⚙️ Configurator
Modulates all other modules based on context. Like an "executive control" — sets goals, adjusts perception focus, tunes the world model.

</div>
<div class="card text-sm">

### 📝 Short-Term Memory
Maintains state over time. Stores the current world state estimate and recent history for the world model to use.

</div>
</div>

---

# The World Model is Central

<img src="/figures/lecun-world-model-role.png" class="mx-auto rounded-lg shadow-lg mt-2" style="max-height:280px" />

<div class="accent-card mt-4">

### Four Key Roles of the World Model

| Role | Description | Example |
|------|-------------|---------|
| **Estimate** | Fill in missing information | Infer what's behind an occluded object |
| **Predict** | Forecast future states | "If I push this cup, it will fall" |
| **Simulate** | Mental rehearsal | Try actions in imagination before doing them |
| **Plan** | Optimize action sequences | Search for the best path to a goal |

</div>

---

# System 1 vs System 2

<img src="/figures/lecun-system1-vs-system2.png" class="mx-auto rounded-lg shadow-lg mt-2" style="max-height:280px" />

<div class="grid grid-cols-2 gap-6 mt-4">
<div class="blue-card">

### System 1 — Reactive
- **One forward pass** from perception to action
- No world model needed
- Fast, habitual, unconscious
- *"Catching a ball thrown at you"*

</div>
<div class="accent-card">

### System 2 — Deliberative
- **Multiple forward passes** through the world model
- Simulates consequences of candidate actions
- Slow, conscious, effortful
- *"Planning a route through a city"*

</div>
</div>

---

# Why Not Just Use LLMs as World Models?

<div class="mt-4">

A common question: "GPT-4 / Claude seem to understand the world. Why not just use them?"

</div>

<div class="grid grid-cols-2 gap-6 mt-4">
<div class="accent-card">

### Text-Only Limitations

- LLMs learn from **text** — a tiny fraction of human experience
- **No grounding** in physical reality
- Can describe "a cup falling" but can't predict the physics
- ~$10^{13}$ tokens of text vs ~$10^{15}$ bytes/day of visual perception

</div>
<div class="teal-card">

### LeCun's Argument

> "Text is a very impoverished representation of the world. A child learns more about the world in the first few years of life through vision and interaction than all the text ever written."

We need world models that learn from **sensory experience**, not just language.

</div>
</div>

<div class="mt-4 text-center text-sm opacity-70">

This is why LeCun advocates for **self-supervised learning from video** — the dominant modality.

</div>

---

# The Problem with Generative Models

<div class="mt-2">

Many world models (like the ones we saw in Part 1 — IRIS, DIAMOND) **generate pixel-level predictions**. LeCun argues this is fundamentally wrong.

</div>

<img src="/figures/lecun-abandoning-generation.png" class="mx-auto rounded-lg shadow-lg mt-2" style="max-height:260px" />

<div class="accent-card mt-4">

### Why Generating Pixels Fails

1. **Combinatorial explosion**: Must predict every pixel — grass blowing in the wind, shadows shifting, textures changing
2. **Wasted capacity**: Most pixel-level details are **irrelevant** for decision-making
3. **Blurry predictions**: Averaging over multiple possible futures gives blurry, useless outputs
4. **Doesn't scale**: Computational cost grows with resolution, not with task complexity

</div>

---

# Generative vs JEPA — The Core Contrast

<img src="/figures/lecun-generative-vs-jepa.png" class="mx-auto rounded-lg shadow-lg mt-2" style="max-height:300px" />

<div class="grid grid-cols-2 gap-6 mt-4">
<div class="accent-card text-sm">

### Generative (Predict Pixels)
$$\hat{y} = \text{Dec}(\text{Enc}(x))$$
$$\mathcal{L} = D(y, \hat{y}) \text{ in pixel space}$$

Must reconstruct **everything** — even irrelevant details.

</div>
<div class="teal-card text-sm">

### JEPA (Predict Representations)
$$\hat{s}_y = \text{Pred}(s_x)$$
$$\mathcal{L} = D(s_y, \hat{s}_y) \text{ in latent space}$$

Only predicts **what matters** — abstract, informative features.

</div>
</div>

---

# Handling Uncertainty — Why Latent Space Matters

<img src="/figures/lecun-prediction-uncertainty.png" class="mx-auto rounded-lg shadow-lg mt-2" style="max-height:280px" />

<div class="mt-4">

Consider predicting what happens next in a video:

</div>

<div class="grid grid-cols-2 gap-6 mt-2">
<div class="accent-card text-sm">

### Generative Approach
- Multiple possible futures exist (a person could turn left or right)
- Averaging in pixel space → **blurry, meaningless prediction**
- The model has no way to represent "either left or right"

</div>
<div class="teal-card text-sm">

### JEPA Approach
- Introduce a **latent variable** $z$ to capture different modes
- $\hat{s}_y = \text{Pred}(s_x, z)$ — different $z$ → different futures
- Each prediction is **sharp and meaningful** in representation space

</div>
</div>

---

# The Crepe-Making Analogy

<img src="/figures/lecun-crepes-multiscale.png" class="mx-auto rounded-lg shadow-lg mt-2" style="max-height:260px" />

<div class="mt-4">

LeCun uses cooking as an analogy for **multi-scale prediction**:

</div>

<div class="grid grid-cols-3 gap-4 mt-2">
<div class="accent-card text-sm">

### Level 1: Milliseconds
Predict exact muscle movements — wrist angle while pouring batter.

*Low-level motor control*

</div>
<div class="teal-card text-sm">

### Level 2: Seconds
Predict task steps — pour, spread, wait, flip.

*Task decomposition*

</div>
<div class="blue-card text-sm">

### Level 3: Minutes
Predict goal state — stack of finished crepes on a plate.

*Goal planning*

</div>
</div>

<div class="accent-card mt-2 text-sm">

**Key insight:** You can predict the **outcome** (crepe on plate) without predicting every pixel of the batter spreading. This is exactly what JEPA enables — prediction at the right level of abstraction.

</div>

---

# The Energy-Based Model Perspective

<div class="mt-2">

LeCun frames JEPA as an **energy-based model (EBM)**. The energy function measures compatibility between inputs.

</div>

<img src="/figures/lecun-energy-landscape-collapse.png" class="mx-auto rounded-lg shadow-lg mt-2" style="max-height:240px" />

<div class="grid grid-cols-2 gap-6 mt-4">
<div class="blue-card text-sm">

### Good Energy Function
- Low energy for **compatible** (x, y) pairs
- High energy for **incompatible** pairs
- Energy landscape has clear valleys at data points

</div>
<div class="accent-card text-sm">

### The Collapse Problem
- Trivial solution: $F(x, y) = 0$ for all inputs
- The model assigns **low energy to everything**
- All information is lost — representations become constant

</div>
</div>

---

# Four Methods to Prevent Collapse

<img src="/figures/lecun-four-approaches-collapse.png" class="mx-auto rounded-lg shadow-lg mt-2" style="max-height:280px" />

<div class="grid grid-cols-2 gap-4 mt-4">
<div class="blue-card text-sm">

### 1. Contrastive (SimCLR, MoCo)
Push negative pairs to high energy. **Problem:** Need exponentially many negatives in high dimensions.

### 2. Regularization (VICReg, Barlow Twins)
Maximize variance + minimize covariance of embeddings. **No negatives needed.**

</div>
<div class="teal-card text-sm">

### 3. Distillation / EMA (BYOL, DINO)
Student-teacher with exponential moving average of weights. **Simple but heuristic.**

### 4. Architectural (Masking / JEPA)
Mask parts of input — forces network to predict, creating an **information bottleneck.**

</div>
</div>

<div class="accent-card mt-2 text-sm text-center">

**JEPA's approach:** Combine **masking** (architectural) + **EMA target encoder** (distillation) + **variance regularization** (VICReg-style)

</div>

---

# Evolution of Self-Supervised Learning

<img src="/figures/lecun-self-supervised-paradigm.png" class="mx-auto rounded-lg shadow-lg mt-2" style="max-height:260px" />

<div class="mt-4">

| Era | Methods | Key Idea | Limitation |
|-----|---------|----------|------------|
| **Contrastive (2018-2020)** | SimCLR, MoCo, CPC | Push/pull positive and negative pairs | Need many negatives; scales poorly |
| **Non-Contrastive (2020-2022)** | BYOL, VICReg, Barlow Twins | Twin networks, no negatives | Still augmentation-based, not predictive |
| **JEPA (2022-present)** | I-JEPA, V-JEPA, V-JEPA 2 | Predict in latent space from masked input | The current frontier |

</div>

---

# Hierarchical JEPA — The Grand Vision

<img src="/figures/lecun-hierarchical-jepa.png" class="mx-auto rounded-lg shadow-lg mt-2" style="max-height:280px" />

<div class="mt-4">

LeCun's ultimate vision: a **hierarchy of JEPA modules** operating at multiple time scales.

</div>

<div class="grid grid-cols-3 gap-4 mt-2">
<div class="accent-card text-sm">

### Level 1
**Millisecond** predictions. Raw sensory processing. Detailed, fast, reactive.

</div>
<div class="teal-card text-sm">

### Level 2
**Second-scale** predictions. Object-level dynamics. Mid-level planning.

</div>
<div class="blue-card text-sm">

### Level 3
**Minute/hour** predictions. Abstract goals. Long-horizon strategy.

</div>
</div>

<div class="purple-card mt-2 text-sm">

Higher levels **set goals** for lower levels. Lower levels **execute** and report back. This is how LeCun envisions hierarchical planning — like a CEO setting strategy and managers executing.

</div>

---

# Quiz: LeCun's Philosophy

<div class="quiz-card mt-4">

### Quick Check

**Q1:** Why does LeCun argue against generative world models?

<v-click>

**A:** They waste resources predicting irrelevant pixel details. Prediction should happen in an abstract representation space where only task-relevant information is kept.

</v-click>

**Q2:** What are the two modes of reasoning in LeCun's architecture?

<v-click>

**A:** System 1 (reactive — direct perception→action, no world model) and System 2 (deliberative — uses the world model to simulate and plan).

</v-click>

**Q3:** What is the "collapse" problem?

<v-click>

**A:** When the model learns a trivial solution (constant output) that assigns low energy everywhere, losing all information. JEPA prevents this through masking, EMA, and variance regularization.

</v-click>

</div>

---
layout: center
---

# Part 2

## The JEPA Framework — Foundations

<div class="mt-4 opacity-60">

Joint Embedding Predictive Architecture

</div>

---

# From Philosophy to Architecture

<div class="mt-4">

Now that we understand **why** LeCun advocates for non-generative world models, let's see **how** JEPA implements this vision.

</div>

<div class="accent-card mt-4">

### The JEPA Principle (3 sentences)

1. **Encode** both input $x$ and target $y$ into representations using separate encoders
2. **Predict** the target's representation from the input's representation (not the raw pixels)
3. **Learn** by matching predicted vs actual representations — never reconstruct pixels

</div>

<div class="mt-4">

$$\text{Loss} = D\big(\underbrace{f_\theta(x)}_{\text{context encoder}},\; \underbrace{g_\phi(y)}_{\text{target encoder}}\big) \quad \text{← both in representation space!}$$

</div>

---

# JEPA Architecture — Detailed

<img src="/figures/jepa-architecture-detailed.png" class="mx-auto rounded-lg shadow-lg mt-2" style="max-height:300px" />

<div class="grid grid-cols-3 gap-4 mt-4">
<div class="accent-card text-sm">

### Context Encoder $f_\theta$
Processes the **visible** (unmasked) portion of the input. Trained by gradient descent.

</div>
<div class="teal-card text-sm">

### Predictor $g_\psi$
Takes context representation + **mask tokens** and predicts target representations. Lightweight — often just a few transformer layers.

</div>
<div class="blue-card text-sm">

### Target Encoder $\bar{f}_\theta$
Processes the **masked** (target) portion. Updated via **EMA** — no gradients flow through it.

</div>
</div>

---

# Why Three Components?

<div class="mt-4">

The three components serve a specific purpose in preventing **collapse**:

</div>

<div class="grid grid-cols-2 gap-6 mt-4">
<div class="accent-card">

### Stop-Gradient + EMA

The target encoder is a **slow-moving copy** of the context encoder:

$$\bar{\theta} \leftarrow \alpha \bar{\theta} + (1 - \alpha) \theta$$

where $\alpha = 0.996 \rightarrow 1.0$ (cosine schedule).

**Why?** If both encoders were trained jointly, they'd collapse to the same constant output. The EMA target provides a **slowly evolving training signal**.

</div>
<div class="teal-card">

### Asymmetric Design

- **Context encoder** sees partial input → must learn to fill in
- **Target encoder** sees the answer → provides the training signal
- **Predictor** bridges the gap — it's smaller than the encoder

The predictor is intentionally kept **small** to prevent it from memorizing shortcuts. The context encoder must learn **meaningful representations**.

</div>
</div>

---

# JEPA vs Other Self-Supervised Methods

<img src="/figures/jepa-core-concept.png" class="mx-auto rounded-lg shadow-lg mt-2" style="max-height:260px" />

<div class="mt-4">

| Method | What it predicts | Space | Limitation |
|--------|-----------------|-------|------------|
| **MAE / BEiT** | Raw pixels | Pixel space | Wastes capacity on textures |
| **DINO / iBOT** | CLS token only | Embedding | No spatial info; augmentation-dependent |
| **Contrastive** (SimCLR) | Same/different | Embedding | Needs negatives; sampling bias |
| **JEPA** | Target **patch** representations | Latent space | Predicts meaningful, spatial features |

</div>

<div class="accent-card mt-2 text-sm">

JEPA's key advantage: It predicts at the **patch level** in **representation space** — capturing spatial structure without wasting capacity on pixel-level reconstruction.

</div>

---

# I-JEPA — JEPA for Images

<div class="mt-4">

**I-JEPA** (Assran et al., CVPR 2023) was the first concrete implementation of the JEPA framework for images.

</div>

<div class="grid grid-cols-2 gap-6 mt-4">
<div class="accent-card">

### How I-JEPA Works

1. Take an image, split into patches (like ViT)
2. **Mask out** a large region (the target)
3. Context encoder processes the **visible patches**
4. Predictor tries to predict the **representations** of masked patches
5. Target encoder (EMA) provides the ground truth representations

</div>
<div class="teal-card">

### Key Results

- **Linear probing on ImageNet:** 77.4% top-1 (ViT-H/14)
- **Competitive** with DINO v2 while being simpler
- **Better low-level features** than contrastive methods
- **Semantic masking:** Learns to predict meaningful content, not textures

</div>
</div>

<div class="blue-card mt-4 text-sm">

**The masking strategy matters enormously.** I-JEPA uses large, contiguous block masks (not random patches) — forcing the model to make high-level semantic predictions rather than just interpolating from nearby patches.

</div>

---

# The Masking Strategy — Why It Matters

<div class="mt-4">

The choice of what to mask determines what the model learns:

</div>

<div class="grid grid-cols-3 gap-4 mt-4">
<div class="accent-card">

### Random Patches
MAE-style random 75% masking.

**Result:** Model learns texture interpolation — low-level features.

*Not what we want.*

</div>
<div class="teal-card">

### Large Block Masks
I-JEPA: 1-4 large contiguous blocks.

**Result:** Model must predict semantics — "what object is there?" — not textures.

*Much better!*

</div>
<div class="blue-card">

### Multi-Block (V-JEPA)
Multiple spatiotemporal blocks in video.

**Result:** Model must predict temporal dynamics and spatial semantics simultaneously.

*Best for video understanding.*

</div>
</div>

---

# Quiz: JEPA Foundations

<div class="quiz-card mt-4">

### Quick Check

**Q1:** In JEPA, what space does prediction happen in?

<v-click>

**A:** **Representation space** (latent space) — not pixel space. The predictor maps from the context encoder's output to the target encoder's output.

</v-click>

**Q2:** Why is the target encoder updated with EMA instead of gradients?

<v-click>

**A:** If both encoders were trained jointly with gradients, they would collapse to a trivial constant solution. The EMA provides a slowly-evolving, stable training signal.

</v-click>

**Q3:** Why use large block masks instead of random patch masking?

<v-click>

**A:** Large blocks force the model to make **semantic predictions** (what object is in this region?) rather than low-level **texture interpolation** from nearby patches.

</v-click>

</div>

---
layout: center
---

# Part 3

## V-JEPA — Extending JEPA to Video

<div class="mt-4 opacity-60">

From static images to spatiotemporal understanding

</div>

---

# Why Video?

<div class="mt-4">

LeCun's vision requires world models that understand **dynamics** — how things change over time. Images alone are not enough.

</div>

<div class="grid grid-cols-2 gap-6 mt-4">
<div class="accent-card">

### What Video Adds

- **Temporal dynamics** — cause and effect
- **Physical intuition** — objects fall, liquids flow
- **Action understanding** — what a robot's action *does*
- **Prediction** — "if this, then what?"

Video is the **dominant modality** for learning world models.

</div>
<div class="teal-card">

### The Challenge

- Videos are **massive** — orders of magnitude more data per second than images
- Need to predict **future representations** — not just fill in missing patches
- Must capture **long-range temporal dependencies**
- Can't afford to generate pixel-level video predictions

</div>
</div>

<div class="blue-card mt-4 text-sm">

This is exactly why JEPA — predicting in representation space, not pixel space — is the right approach for video.

</div>

---

# V-JEPA 1: Video JEPA

<div class="mt-4">

**V-JEPA** (Bardes et al., 2024) extends I-JEPA to video with spatiotemporal masking.

</div>

<div class="grid grid-cols-2 gap-6 mt-4">
<div class="accent-card">

### Architecture Changes from I-JEPA

- Input: **Video clip** (e.g., 16 frames at 224×224)
- Patchification: **3D tubelets** (2×16×16) — space AND time
- Encoder: ViT operating on spatiotemporal tokens
- Masking: **3D spatiotemporal blocks** — mask entire regions across multiple frames
- Prediction: Predict representations of masked spatiotemporal regions

</div>
<div class="teal-card">

### Key Innovations

- **Multi-block masking**: Mask multiple spatiotemporal blocks simultaneously (see next slide)
- **No pixel reconstruction** — stays true to JEPA
- **Feature prediction** is easier than pixel prediction for videos (no need to predict exact motion blur, lighting changes, etc.)

</div>
</div>

---

# V-JEPA Multi-Block Masking

<img src="/figures/vjepa-multiblock-masking.png" class="mx-auto rounded-lg shadow-lg mt-2" style="max-height:300px" />

<div class="mt-4">

The masking strategy is critical for V-JEPA:

</div>

<div class="grid grid-cols-2 gap-6 mt-2">
<div class="accent-card text-sm">

### What Gets Masked
- **Multiple large 3D blocks** in the video volume
- Each block spans several frames and a large spatial region
- Typically masks **~90%** of all spatiotemporal tokens
- Context encoder only sees the remaining ~10%

</div>
<div class="teal-card text-sm">

### Why This Works
- Forces **temporal prediction**: "what happens in these frames?"
- Forces **spatial prediction**: "what's in this region?"
- The model must learn both **appearance** and **dynamics**
- Much harder than image masking — can't just interpolate from nearby frames

</div>
</div>

---

# V-JEPA 1 Results

<div class="mt-4">

V-JEPA 1 demonstrated that non-generative video pretraining could match or beat methods that reconstruct pixels.

</div>

<div class="grid grid-cols-2 gap-6 mt-4">
<div class="accent-card">

### Video Understanding

| Benchmark | V-JEPA 1 | Previous SOTA |
|-----------|----------|---------------|
| Something-Something v2 | 71.4% | 70.8% (VideoMAE v2) |
| Kinetics-400 | 82.0% | 81.5% (InternVideo) |

Competitive with much larger, supervised models.

</div>
<div class="teal-card">

### Key Properties

- **No pixel generation** at any point during training
- **Frozen encoder** evaluation — features are general, not task-specific
- Learns representations useful for both **appearance** and **motion** tasks
- But... still limited in scale (ViT-L, ~300M params)

</div>
</div>

<div class="blue-card mt-4 text-sm">

V-JEPA 1 proved the concept. But the question remained: **Can this approach scale?** That's where V-JEPA 2 comes in.

</div>

---
layout: center
---

# Part 4

## V-JEPA 2 — Scaling Non-Generative Video Models

<div class="mt-4 opacity-60">

"Scaling Non-Generative Video Models" — Meta FAIR, 2025 (arXiv: 2506.09985)

</div>

---

# V-JEPA 2: The Big Idea

<div class="mt-4">

V-JEPA 2 answers the question: **What happens when you scale JEPA aggressively across four dimensions?**

</div>

<img src="/figures/vjepa2-scaling-axes.png" class="mx-auto rounded-lg shadow-lg mt-2" style="max-height:220px" />

<div class="grid grid-cols-4 gap-3 mt-4">
<div class="accent-card text-sm text-center">

### 📊 Data
VideoMix22M — 22 million video clips curated from multiple sources

</div>
<div class="teal-card text-sm text-center">

### 🧠 Model
ViT-g/16 with **1B parameters** — 4× larger than V-JEPA 1

</div>
<div class="blue-card text-sm text-center">

### 📐 Resolution
Progressive training: 224→384→448 with increasing frame count

</div>
<div class="purple-card text-sm text-center">

### ⏱️ Duration
Up to **64 frames** — much longer temporal context

</div>
</div>

---

# V-JEPA 2 Architecture

<img src="/figures/vjepa2-architecture.png" class="mx-auto rounded-lg shadow-lg mt-2" style="max-height:300px" />

<div class="grid grid-cols-2 gap-6 mt-4">
<div class="accent-card text-sm">

### What's New vs V-JEPA 1

- **ViT-g/16**: 1B params, patch size 16×16
- **3D Rotary Position Embeddings (RoPE)**: Separate frequency for height, width, time — enables variable resolution
- **Factored self-attention**: Spatial attention + temporal attention (efficient for long videos)
- **Tubelet embedding**: 2×16×16 — each token covers 2 frames

</div>
<div class="teal-card text-sm">

### Why 3D RoPE?

Traditional position embeddings are **fixed** — the model can only handle one resolution.

3D RoPE encodes position as **rotations** — the model can generalize to:
- Different spatial resolutions (224→384→448)
- Different temporal lengths (16→32→64 frames)
- Any combination at inference time

</div>
</div>

---

# Progressive Resolution Training

<img src="/figures/vjepa2-progressive-training.png" class="mx-auto rounded-lg shadow-lg mt-2" style="max-height:260px" />

<div class="mt-4">

Instead of training at full resolution from the start (expensive), V-JEPA 2 uses a **three-stage progressive schedule**:

</div>

| Stage | Resolution | Frames | Tokens/Video | Duration |
|-------|-----------|--------|-------------|----------|
| **Stage 1** | 224×224 | 16 | ~1,568 | Longest (cheap) |
| **Stage 2** | 384×384 | 32 | ~9,216 | Medium |
| **Stage 3** | 448×448 | 64 | ~25,088 | Short (expensive) |

<div class="accent-card mt-2 text-sm">

**Why this works:** Low-res training learns good **semantic features** cheaply. High-res training fine-tunes **spatial detail**. Total compute is ~3× less than training at full resolution throughout.

</div>

---

# VideoMix22M Dataset

<img src="/figures/vjepa2-videomix22m.png" class="mx-auto rounded-lg shadow-lg mt-2" style="max-height:280px" />

<div class="mt-4">

V-JEPA 2 curates **22 million** video clips from diverse sources:

</div>

<div class="grid grid-cols-2 gap-6 mt-2">
<div class="accent-card text-sm">

### Sources
- **HowTo100M**: Instructional videos (cooking, repair, crafts)
- **Kinetics-710**: Human action recognition
- **Something-Something v2**: Fine-grained object manipulation
- **InternVid**: Web-scale video with captions
- And several more...

</div>
<div class="teal-card text-sm">

### Why Diversity Matters
- No single dataset covers all aspects of the visual world
- Mixing ensures the model learns both **coarse actions** (sports, cooking) and **fine-grained manipulation** (something-something)
- Curriculum: Start with easy (static scenes) → hard (complex dynamics)

</div>
</div>

---

# Training Details

<div class="mt-4">

The full V-JEPA 2 training pipeline:

</div>

<div class="grid grid-cols-2 gap-6 mt-4">
<div class="accent-card">

### Optimization

- **Optimizer:** AdamW, lr=1e-3, weight decay 0.05
- **Batch size:** 2048 videos
- **Total compute:** ~80K GPU-hours on H100s
- **Masking ratio:** 90% of spatiotemporal tokens
- **EMA schedule:** $\tau$ from 0.996 → 1.0 (cosine)

</div>
<div class="teal-card">

### Key Techniques

- **Multi-crop**: Multiple context/target pairs per video
- **Predictor:** 12-layer ViT (much smaller than encoder)
- **Variance-covariance regularization** (VICReg loss) prevents collapse
- **No labels, no text, no contrastive pairs** — pure self-supervised

</div>
</div>

<div class="blue-card mt-4 text-sm">

**Remarkable:** V-JEPA 2 never sees a single label during pretraining. It learns entirely from predicting masked video representations. Yet it achieves SOTA on both video understanding and robot planning.

</div>

---

# V-JEPA 2 Results — Video Understanding

<img src="/figures/vjepa2-understanding-results.png" class="mx-auto rounded-lg shadow-lg mt-2" style="max-height:280px" />

<div class="mt-4">

| Benchmark | V-JEPA 2 | Previous SOTA | Type |
|-----------|----------|---------------|------|
| **Kinetics-400** | 87.5% | 86.5% | Action recognition |
| **Something-Something v2** | 76.2% | 75.0% | Fine-grained temporal |
| **UCF-101** | 98.7% | 98.2% | Action recognition |
| **HMDB-51** | 84.3% | 82.1% | Action recognition |

</div>

<div class="accent-card mt-2 text-sm">

All results with a **frozen encoder** + simple linear probe or attentive probe. The representations are so good that you barely need fine-tuning.

</div>

---

# What V-JEPA 2 Learns

<div class="mt-4">

The representations learned by V-JEPA 2 capture both **semantic** and **temporal** information:

</div>

<div class="grid grid-cols-2 gap-6 mt-4">
<div class="accent-card">

### Semantic Understanding
- Object categories and attributes
- Scene types and layouts
- Fine-grained actions (e.g., "pushing something from left to right" vs "pulling something from right to left")

</div>
<div class="teal-card">

### Temporal Understanding
- Cause-and-effect relationships
- Object permanence (tracking through occlusion)
- Action phases (start, middle, end)
- Speed and direction of motion

</div>
</div>

<div class="blue-card mt-4 text-sm">

This is precisely what LeCun predicted: a non-generative model trained on video learns representations that capture the **structure of the world** — without ever trying to generate a single pixel.

</div>

---

# Energy Landscape Visualization

<img src="/figures/vjepa2-energy-landscape.png" class="mx-auto rounded-lg shadow-lg mt-2" style="max-height:320px" />

<div class="mt-4">

V-JEPA 2's latent space organizes videos by **semantic similarity**. Compatible (input, target) pairs have low energy; incompatible pairs have high energy — exactly the EBM framework LeCun described.

</div>

---

# Quiz: V-JEPA 2

<div class="quiz-card mt-4">

### Quick Check

**Q1:** What are the four scaling axes of V-JEPA 2?

<v-click>

**A:** Data (22M videos), Model (ViT-g, 1B params), Resolution (progressive 224→448), Duration (up to 64 frames).

</v-click>

**Q2:** Why does V-JEPA 2 use 3D RoPE instead of fixed position embeddings?

<v-click>

**A:** 3D RoPE enables **resolution-agnostic** training — the model can handle different spatial resolutions and temporal lengths without retraining. This makes progressive training possible.

</v-click>

**Q3:** What fraction of tokens does V-JEPA 2 mask during training?

<v-click>

**A:** **90%** — the context encoder only sees ~10% of the spatiotemporal tokens. This extreme masking forces the model to learn high-level semantic and temporal features.

</v-click>

</div>

---
layout: center
---

# Part 5

## V-JEPA 2-AC — From Understanding to Robot Action

<div class="mt-4 opacity-60">

Action-Conditioned prediction for zero-shot robot manipulation

</div>

---

# The Bridge: Understanding → Acting

<div class="mt-4">

V-JEPA 2 learns excellent video representations. But how do we use them for **robot control**?

</div>

<div class="grid grid-cols-3 gap-4 mt-4">
<div class="accent-card text-center">

### Step 1: Pretrain
V-JEPA 2 encoder learns video representations on 22M clips.

**No robot data needed.**

</div>
<div class="teal-card text-center">

### Step 2: Fine-tune
Add an action-conditioned predictor that takes (state, action) → next state.

**62 hours of robot data.**

</div>
<div class="blue-card text-center">

### Step 3: Plan
Use the model to search for action sequences that reach a goal.

**Zero-shot at test time.**

</div>
</div>

<div class="purple-card mt-4 text-sm">

This is LeCun's cognitive architecture in practice: the **world model** (V-JEPA 2) predicts; the **actor** (CEM planner) searches for optimal actions; the **cost module** measures goal distance.

</div>

---

# V-JEPA 2-AC Architecture

<img src="/figures/vjepa2-ac-architecture.png" class="mx-auto rounded-lg shadow-lg mt-2" style="max-height:300px" />

<div class="grid grid-cols-2 gap-6 mt-4">
<div class="accent-card text-sm">

### Action-Conditioned Predictor
- Takes: V-JEPA 2 representations $s_t$ + robot action $a_t$
- Predicts: Next state representation $\hat{s}_{t+1}$
- Architecture: 300M parameter transformer
- **Crucially:** V-JEPA 2 encoder stays **frozen** — only the predictor is trained

</div>
<div class="teal-card text-sm">

### Training Data
- **62 hours** of robot teleoperation data
- Robot: Franka Emika Panda arm
- Actions: 7-DoF joint velocities
- Multiple camera views (wrist + external)
- Tasks: picking, placing, pushing, stacking

</div>
</div>

---

# The Loss Function

<div class="mt-4">

V-JEPA 2-AC uses a combination of losses to train the action-conditioned predictor:

</div>

<div class="grid grid-cols-2 gap-6 mt-4">
<div class="accent-card">

### Prediction Loss
$$\mathcal{L}_\text{pred} = \| \hat{s}_{t+1} - \text{sg}(s_{t+1}) \|_2^2$$

Predict the next state's representation. Stop-gradient on the target (just like JEPA pretraining).

</div>
<div class="teal-card">

### Temporal Consistency Loss
$$\mathcal{L}_\text{temp} = \| \hat{s}_{t+1} - \hat{s}_{t+2 \leftarrow t} \|_2^2$$

Multi-step predictions should be **consistent** — predicting 2 steps ahead should match composing two 1-step predictions.

</div>
</div>

<div class="blue-card mt-4">

### Total Loss
$$\mathcal{L} = \mathcal{L}_\text{pred} + \lambda_\text{temp} \mathcal{L}_\text{temp}$$

The temporal consistency loss acts as a **regularizer** — encouraging the predictor to learn smooth, physically plausible dynamics.

</div>

---

# Planning with CEM

<img src="/figures/vjepa2-planning-cem.png" class="mx-auto rounded-lg shadow-lg mt-2" style="max-height:260px" />

<div class="mt-4">

At test time, V-JEPA 2-AC uses **Cross-Entropy Method (CEM)** to plan:

</div>

<div class="grid grid-cols-2 gap-6 mt-2">
<div class="accent-card text-sm">

### CEM Planning Loop

1. **Sample** N random action sequences from current distribution
2. **Roll out** each through the world model: $s_0 \xrightarrow{a_1} \hat{s}_1 \xrightarrow{a_2} \hat{s}_2 \cdots$
3. **Score** each trajectory: how close is $\hat{s}_T$ to the goal representation?
4. **Refit** the action distribution to the **top-K** trajectories
5. **Repeat** for several iterations
6. **Execute** the first action of the best sequence

</div>
<div class="teal-card text-sm">

### Why This Works

- The **world model** replaces real-world interaction with **imagination**
- CEM is derivative-free — works even when the dynamics model isn't differentiable
- Planning horizon: typically **10-20 steps** ahead
- Replanning at every timestep → closed-loop, reactive behavior
- **No task-specific training** — the same model plans for any goal

</div>
</div>

---

# Goal Specification

<div class="mt-4">

How does the robot know what to achieve? V-JEPA 2-AC uses **goal images**:

</div>

<div class="grid grid-cols-2 gap-6 mt-4">
<div class="blue-card">

### Goal Image → Goal Representation

1. Take a **goal image** showing the desired end state
2. Encode it with the frozen V-JEPA 2 encoder: $s_\text{goal} = \text{Enc}(x_\text{goal})$
3. The cost function is simply:

$$C(s_t) = \| s_t - s_\text{goal} \|_2^2$$

The robot plans actions to make its **predicted future state** match the **goal state** in representation space.

</div>
<div class="purple-card">

### Why This is Powerful

- **No reward engineering** — just show a picture of what you want
- **No task-specific training** — the same model works for any goal
- **Representation distance** is more meaningful than pixel distance
  - Two images of "cup on table" are close in V-JEPA 2 space even if camera angle differs
  - In pixel space, they'd look completely different

</div>
</div>

---

# Robot Results — Zero-Shot Manipulation

<img src="/figures/vjepa2-robot-results.png" class="mx-auto rounded-lg shadow-lg mt-2" style="max-height:260px" />

<div class="mt-4">

V-JEPA 2-AC achieves **zero-shot** manipulation without task-specific training:

</div>

| Task | V-JEPA 2-AC | Best Baseline | Improvement |
|------|-------------|---------------|-------------|
| **Pick & Place** | 85% | 62% (R3M) | +23% |
| **Push to Target** | 78% | 55% (MVP) | +23% |
| **Stack Blocks** | 72% | 48% (VIP) | +24% |
| **Open Drawer** | 81% | 59% (R3M) | +22% |

<div class="accent-card mt-2 text-sm">

**"Zero-shot"** means: the robot was never explicitly trained on these specific tasks. It was trained on 62 hours of general teleoperation data. At test time, you just show it a goal image and it plans how to get there.

</div>

---

# Why V-JEPA 2-AC Works So Well

<div class="grid grid-cols-2 gap-6 mt-4">
<div class="accent-card">

### Internet-Scale Pretraining

V-JEPA 2 was pretrained on **22M videos** — it already understands:
- How objects move and interact
- What "pushing" and "grasping" look like
- Physics (gravity, friction, collisions)
- Object permanence and spatial relationships

The robot doesn't need to learn physics from scratch.

</div>
<div class="teal-card">

### Efficient Fine-tuning

Only the **300M predictor** is trained; the **1B encoder** stays frozen.

- 62 hours of robot data is enough
- No task-specific reward functions
- No RL — pure supervised prediction
- Training takes ~24 hours on 8 H100s

</div>
</div>

<div class="blue-card mt-4">

This validates LeCun's thesis: **a world model pretrained on internet video can be efficiently adapted to robot control** — bridging the gap between human-like learning efficiency and current AI.

</div>

---

# V-JEPA 1 vs V-JEPA 2 — Summary

<img src="/figures/vjepa1-vs-vjepa2-summary.png" class="mx-auto rounded-lg shadow-lg mt-2" style="max-height:260px" />

<div class="mt-4">

| Aspect | V-JEPA 1 | V-JEPA 2 |
|--------|----------|----------|
| **Model** | ViT-L (~300M) | ViT-g (~1B) |
| **Data** | ~2M clips | 22M clips (VideoMix22M) |
| **Resolution** | Fixed 224 | Progressive 224→384→448 |
| **Position Embedding** | Learned, fixed | 3D RoPE (flexible) |
| **Max Frames** | 16 | 64 |
| **Video Understanding** | Competitive | **SOTA** |
| **Robot Control** | Not explored | **V-JEPA 2-AC** (zero-shot) |

</div>

---

# The Full Picture — LeCun's Vision Realized

<div class="mt-4">

Let's connect everything back to LeCun's cognitive architecture:

</div>

<div class="grid grid-cols-2 gap-6 mt-4">
<div class="accent-card">

### LeCun's Vision (2022)
- **Perception:** Encode observations
- **World Model:** Predict future states
- **Cost:** Measure goal distance
- **Actor:** Plan optimal actions
- **Learn from video** without generation

</div>
<div class="teal-card">

### V-JEPA 2-AC (2025)
- **Perception:** V-JEPA 2 encoder (frozen)
- **World Model:** Action-conditioned predictor
- **Cost:** L2 distance to goal representation
- **Actor:** CEM planner
- **Trained on 22M videos** + 62h robot data

</div>
</div>

<div class="purple-card mt-4">

V-JEPA 2-AC is the **closest realization** of LeCun's cognitive architecture to date. It proves that:
1. Non-generative self-supervised learning produces **excellent world models**
2. Internet video pretraining **transfers** to robot manipulation
3. Planning in **representation space** is more effective than planning in pixel space

</div>

---

# What's Missing? Open Challenges

<div class="grid grid-cols-2 gap-6 mt-4">
<div class="accent-card">

### Current Limitations

- **No hierarchy**: V-JEPA 2 operates at a single temporal scale (no H-JEPA yet)
- **No language**: Goal specification via images only — no natural language goals
- **CEM planning**: Derivative-free, not very efficient for long horizons
- **Single robot**: Only tested on Franka Panda — generalization to other robots unclear

</div>
<div class="teal-card">

### Future Directions

- **Hierarchical JEPA** (H-JEPA): Multi-scale temporal prediction
- **Language-conditioned planning**: "Pick up the red cup and place it on the shelf"
- **Learned planners**: Replace CEM with a learned policy
- **Multi-robot**: Transfer world model across robot morphologies
- **Real-world deployment**: Beyond lab settings

</div>
</div>

<div class="blue-card mt-4 text-sm">

**The key takeaway:** V-JEPA 2 demonstrates that LeCun's philosophical framework — predict in representation space, not pixel space — is not just a theoretical idea. It works in practice, and it works remarkably well.

</div>

---

# Comparing World Model Approaches

<div class="mt-4">

How does V-JEPA 2 compare to the world models we studied in Part 1?

</div>

| Feature | IRIS | DIAMOND | DINO-WM | V-JEPA 2 |
|---------|------|---------|---------|----------|
| **Generates pixels** | Yes (VQ-VAE) | Yes (diffusion) | No | No |
| **Self-supervised** | No (RL) | No (RL) | Yes (DINO) | Yes (JEPA) |
| **Pretraining data** | Game frames | Game frames | ImageNet | 22M videos |
| **Robot control** | No | No | Limited | Yes (zero-shot) |
| **Scale** | ~100M | ~200M | ~300M | **1B** |
| **Planning** | Imagination | Imagination | Probing | CEM in latent space |

<div class="accent-card mt-4 text-sm">

**Pattern:** The field is moving from generative (IRIS, DIAMOND) to non-generative (DINO-WM, V-JEPA 2) world models, and from game environments to real-robot tasks.

</div>

---

# Recap — What We Learned Today

<div class="grid grid-cols-2 gap-6 mt-4">
<div class="accent-card">

### LeCun's Philosophy
- The **learning efficiency gap** between humans and AI
- **System 1 vs System 2** reasoning
- The **6-module cognitive architecture** with the world model at center
- Why **generative models fail** for world models
- **Energy-based models** and the collapse problem

</div>
<div class="teal-card">

### JEPA → V-JEPA 2
- JEPA: **predict in representation space**, not pixel space
- **Three components**: context encoder, predictor, EMA target encoder
- **V-JEPA**: extend to video with spatiotemporal masking
- **V-JEPA 2**: scale across data, model, resolution, duration
- **V-JEPA 2-AC**: action-conditioned planning for zero-shot robot manipulation

</div>
</div>

<div class="purple-card mt-4">

### The Big Takeaway

LeCun's vision of a non-generative, self-supervised world model trained on video is **not just philosophy** — V-JEPA 2 proves it works. Internet-scale video pretraining + minimal robot fine-tuning enables zero-shot manipulation that outperforms task-specific baselines by 20%+.

</div>

---

# Key Equations Summary

<div class="mt-4">

| Concept | Equation |
|---------|----------|
| **JEPA Prediction** | $\hat{s}_y = \text{Pred}(f_\theta(x))$ |
| **JEPA Loss** | $\mathcal{L} = D(s_y, \hat{s}_y)$ where $s_y = \bar{f}_\theta(y)$ |
| **EMA Update** | $\bar{\theta} \leftarrow \tau \bar{\theta} + (1-\tau)\theta$ |
| **World Model** | $\hat{s}_{t+1} = \text{Pred}(s_t, a_t)$ |
| **Goal Cost** | $C(s) = \|s - s_\text{goal}\|_2^2$ |
| **CEM Planning** | $a^* = \arg\min_{a_{1:T}} \sum_t C(\hat{s}_t)$ |

</div>

---

# Reading List

<div class="grid grid-cols-2 gap-6 mt-4">
<div class="accent-card text-sm">

### Essential Papers

1. **LeCun (2022)** — "A Path Towards Autonomous Machine Intelligence" — The philosophical manifesto
2. **Assran et al. (2023)** — I-JEPA — JEPA for images (CVPR 2023)
3. **Bardes et al. (2024)** — V-JEPA — Extending to video
4. **Meta FAIR (2025)** — V-JEPA 2 — Scaling + robot planning (arXiv: 2506.09985)

</div>
<div class="teal-card text-sm">

### Related Reading

- **VICReg** (Bardes et al., 2022) — Variance-covariance regularization
- **DINO v2** (Oquab et al., 2024) — Self-supervised ViT features
- **BYOL** (Grill et al., 2020) — Bootstrap without negatives
- **3D RoPE** — Rotary position embeddings in 3D

</div>
</div>

---

# Final Quiz

<div class="quiz-card mt-4">

### Test Your Understanding

**Q1:** In one sentence, what is the core idea of JEPA?

<v-click>

**A:** Predict the **representation** of a masked target from the representation of visible context — never reconstruct raw pixels.

</v-click>

**Q2:** How does V-JEPA 2-AC specify goals at test time?

<v-click>

**A:** A **goal image** is encoded by the frozen V-JEPA 2 encoder, and the robot plans actions to minimize the L2 distance between predicted and goal representations.

</v-click>

**Q3:** Why does V-JEPA 2 use progressive resolution training?

<v-click>

**A:** Training at low resolution first is computationally cheap and learns good semantic features. High resolution is added later for spatial detail, reducing total compute by ~3×.

</v-click>

**Q4:** What is LeCun's strongest argument against generative world models?

<v-click>

**A:** They waste capacity predicting irrelevant pixel-level details (textures, lighting, shadows) that are unnecessary for planning and decision-making. Prediction should happen at the level of **abstraction** relevant to the task.

</v-click>

</div>

---
layout: center
---

# Part 6

## LeWorldModel — A Tiny End-to-End JEPA

<div class="mt-4 opacity-60">The opposite bet: no foundation encoder, just 15M parameters from raw pixels</div>

---

# The DINO-WM Ceiling

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### Where DINO-WM hits the wall

<div class="card text-sm mb-3">
<strong>Heavy encoder:</strong> DINOv2-Base is ~86M frozen parameters. Every observation is ~196 patch tokens at 768-dim — <span class="highlight">a lot</span> of latents to predict.
</div>

<div class="card text-sm mb-3">
<strong>Slow planning:</strong> CEM rollouts through DINO-WM take <span class="highlight">~47 seconds per step</span>. Totally unusable for real-time control.
</div>

<div class="card text-sm mb-3">
<strong>Frozen bottleneck:</strong> You cannot fine-tune the encoder for your domain. You're stuck with whatever ImageNet-DINO decided was important.
</div>

</div>
<div>

### The provocative question

<div class="accent-card text-sm">

If a pre-trained foundation encoder gives us such painful costs...

<strong>what if we just threw it away?</strong>

Could we learn a small, fast, from-scratch encoder + predictor that's actually *better*?

</div>

<div class="teal-card text-sm mt-3">
That's the bet LeWorldModel makes. It's not "DINO-WM but bigger" — it's the <strong>opposite philosophy</strong>.
</div>

</div>
</div>

---

# LeWorldModel: The Opposite of DINO-WM

<div class="mt-4">

<div class="grid grid-cols-2 gap-6">
<div class="card">
<h3>DINO-WM (from Part 1 lecture)</h3>
<div class="text-sm mt-2">

- **Frozen** pre-trained DINOv2-Base encoder (~86M params)
- **~200 patch tokens** per frame, 768-dim each
- Predictor learned on top of frozen features
- CEM planning — **~47 s per step**
- Multi-term losses to prevent collapse

</div>
</div>
<div class="accent-card">
<h3>LeWorldModel</h3>
<div class="text-sm mt-2">

- **End-to-end from raw pixels** — no pre-trained weights
- Single <strong>192-dim CLS token</strong> per frame (200× fewer)
- Tiny ViT-Tiny encoder (~5M) + 6-layer predictor (~10M) = <strong>~15M total</strong>
- Planning <strong>&lt;1 s per step — 48× faster</strong>
- <strong>Just 2 loss terms</strong>: prediction + SIGReg

</div>
</div>
</div>

<div class="teal-card mt-4 text-sm text-center">
<strong>LeWM is the first JEPA that trains stably end-to-end from pixels</strong> without exponential moving averages, stop-gradients, or auxiliary supervision.
</div>

</div>

---

# LeWM Architecture

<div class="flex justify-center items-start mt-2" style="padding-top:0.5rem;">
<img src="/figures/leworld-architecture.png" class="rounded-lg" style="max-height:68vh; max-width:90%;" />
</div>

---

# The Two Components

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### Encoder $f_\theta$

<div class="teal-card text-sm mb-3">

- **ViT-Tiny** architecture
- 12 layers · 3 heads · **192-dim**
- Patch size 14
- **~5M parameters**, trained from scratch
- Output = [CLS] token → single-layer MLP + BatchNorm
- One latent $s_t \in \mathbb{R}^{192}$ per frame

</div>

<div class="card text-sm">
<strong>No patch tokens</strong>, no tricks — just a compact global embedding per observation.
</div>

</div>
<div>

### Predictor $g_\phi$

<div class="accent-card text-sm mb-3">

- **6-layer Transformer**, 16 attention heads
- 10% dropout
- **~10M parameters**
- Actions enter via <strong>AdaLN</strong> (Adaptive LayerNorm), initialized to zero for training stability
- Input: $[s_{t-k}, \ldots, s_t]$ + action $a_t$
- Output: predicted next latent $\hat{s}_{t+1}$

</div>

<div class="card text-sm">
Action conditioning through AdaLN (not concatenation) lets the predictor <em>modulate</em> its dynamics based on what the agent is doing.
</div>

</div>
</div>

---

# The SIGReg Loss

<div class="flex justify-center items-start mt-2" style="padding-top:0.5rem;">
<img src="/figures/leworld-sigreg.png" class="rounded-lg" style="max-height:68vh; max-width:90%;" />
</div>

---

# Why SIGReg Matters

<div class="mt-2">

<div class="grid grid-cols-2 gap-4">

<div class="card text-sm mb-3">
<h3>The collapse problem</h3>
Any JEPA can trivially minimize $\|\hat{s}_{t+1} - s_{t+1}\|^2$ by making <em>all</em> embeddings the same point. Then the prediction loss is zero — and the encoder has learned nothing.
</div>

<div class="teal-card text-sm mb-3">
<h3>Prior fixes were fragile</h3>
V-JEPA, I-JEPA, PLDM stack <strong>6 loss terms</strong>, EMAs, stop-gradients, and centering tricks — each adding a hyperparameter you have to tune.
</div>

<div class="accent-card text-sm mb-3">
<h3>LeWM's fix — SIGReg</h3>
Project embeddings onto $M=1024$ random unit directions → test each 1D projection for univariate normality → penalize deviations from $\mathcal{N}(0,1)$. One regularizer, <strong>one hyperparameter</strong> ($\lambda=0.1$).
</div>

<div class="blue-card text-sm mb-3">
<h3>Why it works</h3>
Gaussians are <em>maximum-entropy</em> for fixed variance. A collapsed distribution is nothing like a Gaussian → big penalty → encoder is forced to spread embeddings out.
</div>

</div>

<div class="purple-card mt-3 text-sm text-center">

$$\mathcal{L} = \mathcal{L}_{\text{pred}} + \lambda \cdot \mathrm{SIGReg}(Z), \qquad \lambda = 0.1, \quad M = 1024$$

<strong>Two loss terms total. No EMA. No stop-gradient. No auxiliary supervision.</strong>

</div>

</div>

---

# LeWM vs DINO-WM Side by Side

<div class="flex justify-center items-start mt-2" style="padding-top:0.5rem;">
<img src="/figures/leworld-vs-dinowm.png" class="rounded-lg" style="max-height:68vh; max-width:90%;" />
</div>

---

# The Efficiency Numbers

<div class="flex justify-center items-start mt-2" style="padding-top:0.5rem;">
<img src="/figures/leworld-efficiency.png" class="rounded-lg" style="max-height:68vh; max-width:90%;" />
</div>

---

# Planning with LeWM

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### Receding-horizon MPC

<div class="card text-sm mb-3">

1. Encode current observation to $s_t$
2. Encode goal image to $s_{\text{goal}}$
3. Sample candidate action sequences $\{a_t^{(i)}, \ldots, a_{t+H}^{(i)}\}$
4. Roll each sequence through $g_\phi$ to predict future latents
5. Score: $\|s_{t+H}^{(i)} - s_{\text{goal}}\|^2$
6. Pick best, **execute only $a_t^{(i^\ast)}$**
7. Replan from the new observation

</div>

<div class="teal-card text-sm">
Because a frame is just <strong>1 token</strong>, one rollout is hundreds of times cheaper than DINO-WM. You can sample <em>thousands</em> of candidate action sequences in under a second.
</div>

</div>
<div>

### Results across tasks

<div class="accent-card text-sm mb-3">

| Task | Method | Success |
|---|---|---|
| Push-T | DINO-WM (+proprio) | moderate |
| Push-T | **LeWM (pixels only)** | **+18% vs PLDM, beats DINO-WM** |
| Reacher | **LeWM** | **competitive** |
| Two-Room | **LeWM** | **best** |
| OGBench-Cube | **LeWM** | **competitive** |

</div>

<div class="teal-card text-sm">
<strong>Surprising finding:</strong> LeWM beats DINO-WM on Push-T <em>even without</em> proprioceptive inputs. A tiny from-scratch encoder captures what you need for pixel-only planning.
</div>

</div>
</div>

---

# What LeWorldModel Teaches Us

<div class="mt-4">

<div class="grid grid-cols-2 gap-4">
<div class="teal-card text-sm mb-3">
<h3>Foundation encoders are not mandatory</h3>
DINO-WM was a proof of concept that pre-trained features help. LeWM is a proof of concept that you <em>don't need them</em> if your architecture and loss are right.
</div>
<div class="accent-card text-sm mb-3">
<h3>One good loss beats six fragile ones</h3>
SIGReg replaces EMA + stop-gradient + centering + variance + covariance + invariance losses with a single Gaussian penalty. Simplicity wins.
</div>
</div>

<div class="grid grid-cols-2 gap-4">
<div class="blue-card text-sm mb-3">
<h3>Tiny models still plan</h3>
15M parameters, 1 GPU, a few hours of training — and you can do MPC faster than real-time. The 14B foundation models are not always the answer.
</div>
<div class="purple-card text-sm mb-3">
<h3>But — still action-conditioned</h3>
LeWM still requires action labels for every training trajectory. It can't use unlabeled internet video. The next frontier solves exactly that.
</div>
</div>

<div class="accent-card mt-3 text-sm text-center">
<strong>The next question:</strong> What if we could predict actions AND world states <em>together</em> — and leverage unlimited internet video for the world model?
<br>That's exactly what <strong>DreamZero</strong> does.
</div>

</div>

---
layout: center
---

# Part 7

## DreamZero — Joint World-Action Model

<div class="mt-4 opacity-60">Imagine and act simultaneously — using internet-scale video</div>

---

# The Three Paradigms

<div class="mt-4">

<div class="grid grid-cols-3 gap-4">

<div class="blue-card text-sm">
<h3>Action-Conditioned</h3>

$x' = f(x, a)$

DINO-WM, IRIS, DIAMOND, LeWorld

**Needs actions** for training → can't use internet video

</div>

<div class="card text-sm">
<h3>Video-Only</h3>

$x' = f(x)$, then $a = g(x, x')$

DreamGen, 1x WM

**No actions needed** for WM → but two-stage

</div>

<div class="accent-card text-sm">
<h3>Joint (WAM)</h3>

$(x', a) = f(x)$

**DreamZero**, Fast WAM

**Best of both worlds** — one model, two outputs

**Today's focus**

</div>

</div>

<div class="teal-card mt-4 text-sm text-center">
<strong>Chris Paxton (2025):</strong> "Joint models generalize better than alternatives" — and they address the biggest limitation of action-conditioned models: the need for expensive action labels.
</div>

</div>

---

# Meet DreamZero

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

<div class="card text-sm mb-3">
<strong>Paper:</strong> "DreamZero: A Generalist Joint World-Action Model"<br>
NVIDIA (Feb 2026), arXiv:2602.15922
</div>

<div class="accent-card text-sm mb-3">
<strong>The claim:</strong> One 14B model that jointly denoises future <em>video</em> AND future <em>actions</em> — trained end-to-end with flow matching on robot data.
</div>

<div class="teal-card text-sm">
<strong>The result:</strong>

- <strong>62.2%</strong> task progress on AgiBot G1 (seen tasks) vs 27.4% for best VLA
- <strong>39.5%</strong> on completely unseen tasks (vs 16.3% for VLAs) — 2.4× gap
- <strong>49.0%</strong> on DROID-Franka (vs 33% for pi-0.5, 31% for GR00T N1.6)
- <strong>7 Hz</strong> real-time closed-loop control
</div>

</div>
<div>

### Why it matters

<div class="blue-card text-sm mb-3">
DreamZero is the <strong>first</strong> robot foundation model that treats world modeling and action generation as <strong>one joint distribution</strong>, initialized from a web-scale video diffusion backbone (Wan2.1-I2V-14B).
</div>

<div class="card text-sm mb-3">
It shows the <strong>WAM paradigm works at scale</strong>: a single model can imagine the future <em>and</em> decide what to do, beating specialized VLAs by 2×+ on generalization.
</div>

</div>
</div>

---

# DreamZero Architecture

<div class="flex justify-center items-start mt-2" style="padding-top:0.5rem;">
<img src="/figures/dreamzero-architecture.png" class="rounded-lg" style="max-height:72vh; max-width:92%;" />
</div>

---

# What's Inside the 14B Backbone?

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### Three Input Streams

<div class="teal-card text-sm mb-3">
<strong>1. Visual context</strong><br>
Recent camera frames → VAE encoder (frozen) → visual latent tokens $z_{ctx}$
</div>

<div class="blue-card text-sm mb-3">
<strong>2. Language</strong><br>
Task instruction ("pick up the red cup") → text encoder (frozen) → text tokens $c$
</div>

<div class="accent-card text-sm mb-3">
<strong>3. Robot state</strong><br>
Proprioception (joint angles, gripper) → small state encoder (trained) → state tokens $q$
</div>

</div>
<div>

### The Shared Backbone

<div class="card text-sm mb-3">
<strong>Wan2.1-I2V-14B-480P</strong> — a 14 billion parameter image-to-video Diffusion Transformer, <strong>initialized from web-scale video pre-training</strong>.<br><br>
All DiT blocks are fine-tuned end-to-end. This is not a frozen backbone with LoRA — the entire 14B moves.
</div>

### Two Output Heads

<div class="teal-card text-sm mb-2">
<strong>Video head</strong> → predicted future frames (noisy video latents denoised)
</div>

<div class="accent-card text-sm">
<strong>Action head</strong> → predicted action chunk $a_1 \ldots a_K$ (denoised jointly with video)
</div>

</div>
</div>

---

# The Joint Formulation

<div class="flex justify-center items-start mt-2" style="padding-top:0.5rem;">
<img src="/figures/dreamzero-joint-formulation.png" class="rounded-lg" style="max-height:70vh; max-width:90%;" />
</div>

---

# Why Joint Beats Separate

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

<div class="card text-sm mb-3">
<strong>Direct VLA:</strong> $\pi(a \mid o, \ell)$<br>
Learns <em>what</em> to do, but nothing about <em>how the world evolves</em>. No physics understanding baked in.
</div>

<div class="card text-sm mb-3">
<strong>Video WM + Inverse dynamics:</strong><br>
$x' = f(x), \quad a = g(x, x')$<br>
Two stages. The inverse dynamics model is lossy. Errors compound.
</div>

<div class="accent-card text-sm mb-3">
<strong>DreamZero (joint):</strong>
$$\pi(\text{vid}, \text{act} \mid o, \ell, q) = \pi(\text{vid} \mid o, \ell, q) \cdot \pi(\text{act} \mid \text{vid}, q)$$
<br>
One model, one set of weights. Actions are <em>conditioned on predicted video</em> — implicit inverse dynamics.
</div>

</div>
<div>

### The punchline

<div class="teal-card text-sm mb-3">
Because the action head is conditioned on the predicted video, <strong>the model must learn physics in order to produce good actions</strong>.
</div>

<div class="blue-card text-sm mb-3">
And because video and action share the backbone, <strong>the physics learned for video prediction immediately helps action prediction</strong>.
</div>

<div class="accent-card text-sm">
<strong>Empirical result:</strong> 2.4× better generalization to unseen tasks than the best VLA baselines — with the same action data.
</div>

</div>
</div>

---

# Autoregressive Chunks + KV Cache

<div class="flex justify-center items-start mt-2" style="padding-top:0.5rem;">
<img src="/figures/dreamzero-chunks.png" class="rounded-lg" style="max-height:70vh; max-width:92%;" />
</div>

---

# DreamZero-Flash: 7 Hz Real-Time

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

<div class="card text-sm mb-3">
A 14B DiT doing 50 denoising steps per chunk is <strong>way too slow</strong> for real-time robot control. DreamZero-Flash is the inference-time distillation that makes it work.
</div>

<div class="blue-card text-sm mb-3">
<strong>Step 1 — Beta-distribution noise schedule</strong><br>
Instead of uniform $t \sim U(0,1)$, sample from $\text{Beta}(\alpha, \beta)$ skewed toward low noise.
</div>

<div class="teal-card text-sm mb-3">
<strong>Step 2 — Few-step distillation</strong><br>
Progressive distillation: train a student to match the teacher's trajectory in fewer steps.
</div>

<div class="accent-card text-sm">
<strong>Result:</strong> <strong>38× speedup</strong> over naive sampling → <strong>7 Hz closed-loop control</strong> on real robots, even with a 14B backbone.
</div>

</div>
<div>

### Why this matters

<div class="card text-sm mb-3">
7 Hz is the magic number for manipulation: fast enough for visuomotor feedback, slow enough that the 14B model can run on a single H100.
</div>

<div class="teal-card text-sm mb-3">
Prior video-action models (UniPi, DreamGen) had to cheat — run the video model open-loop and execute many actions between predictions. DreamZero doesn't: every action chunk is re-conditioned on a fresh observation.
</div>

<div class="blue-card text-sm">
<strong>Engineering punchline:</strong> You can have a huge world model AND real-time control — the two are no longer in tension.
</div>

</div>
</div>

---

# The Numbers

<div class="flex justify-center items-start mt-2" style="padding-top:0.5rem;">
<img src="/figures/dreamzero-benchmarks.png" class="rounded-lg" style="max-height:72vh; max-width:92%;" />
</div>

---

# Cross-Embodiment Transfer

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

<div class="card text-sm mb-3">
Every VLA paper shows <strong>one robot</strong>, <strong>one lab</strong>, <strong>one set of tasks</strong>. Generalization to a new embodiment usually means "re-collect hundreds of hours of data on the new arm."
</div>

<div class="blue-card text-sm mb-3">
<strong>DreamZero's result:</strong> Transfer from AgiBot G1 → YAM bimanual with just <strong>20 minutes of video-only play data</strong> (no demonstrations, no action labels, raw video).
</div>

<div class="accent-card text-sm mb-3">
Task progress: <strong>38.3% → 55.4%</strong>. A +17 point improvement from 20 minutes of unpaired video.
</div>

<div class="teal-card text-sm">
<strong>Even wilder:</strong> 12 minutes of <em>human hand</em> video (no robot at all) gets you to <strong>54.3%</strong> — almost the same.
</div>

</div>
<div>

### Why this works

<div class="card text-sm mb-3">
The world head has learned general visual physics from Wan2.1 pre-training + AgiBot G1 fine-tuning. It doesn't need action labels to understand "how objects move."
</div>

<div class="blue-card text-sm mb-3">
When you show it 20 minutes of a new arm (or a hand) manipulating objects, the video loss updates the world head to "understand this new body." The action head then <em>infers</em> what actions would produce that motion.
</div>

<div class="accent-card text-sm">
<strong>This is the end of per-robot data collection.</strong> Pre-train once → adapt to any embodiment with minutes of unpaired video.
</div>

</div>
</div>

---

# DreamZero vs. Everything

<div class="mt-2">

| | **DINO-WM** | **IRIS** | **DIAMOND** | **LeWorld** | **V-JEPA 2** | **DreamZero** |
|---|---|---|---|---|---|---|
| **Generates pixels** | No | Yes | Yes | No | No | **Yes** (joint) |
| **Actions for WM** | Yes | Yes | Yes | Yes | No | **No** |
| **Internet video** | No | No | No | No | Yes | **Yes** |
| **Learned policy** | No (CEM) | Yes | Yes | No (MPC) | No (CEM) | **Yes** |
| **Scale** | ~300M | ~100M | ~200M | ~15M | ~1B | **14B** |
| **Generalization** | Limited | Moderate | Moderate | Good | Good | **Best** |

<div class="accent-card mt-3 text-sm text-center">
<strong>The trajectory:</strong> From action-conditioned + planning (DINO-WM, LeWorld) → non-generative JEPA (V-JEPA 2) → joint prediction leveraging internet-scale data (DreamZero). Each step addresses the previous one's limitations.
</div>

</div>

---

# Recap — The Full Arc

<div class="grid grid-cols-2 gap-6 mt-4">
<div class="accent-card">

### Philosophy & Foundations
- LeCun's **learning efficiency gap** and cognitive architecture
- **JEPA**: predict in representation space, not pixels
- **V-JEPA 2**: scale to 1B params, 22M videos, SOTA understanding
- **V-JEPA 2-AC**: zero-shot robot manipulation via CEM planning

</div>
<div class="teal-card">

### From Theory to Production
- **LeWorld**: tiny 15M end-to-end JEPA, SIGReg, 48× faster than DINO-WM
- **DreamZero**: 14B joint world-action model, flow matching, 7 Hz real-time
- **Cross-embodiment**: 20 min of video → new robot, no action labels
- **The GPT playbook**: pre-train on internet video, fine-tune on robot data

</div>
</div>

<div class="purple-card mt-4 text-sm">

### The Big Takeaway

The field is converging on a clear recipe: **(1)** learn world representations from massive video (JEPA / generative), **(2)** add action conditioning with minimal robot data, **(3)** plan or act directly in learned latent space. V-JEPA 2 proves non-generative JEPA works. DreamZero proves joint generative models scale. Both point to the same future: **robots that learn physics from watching the world**.

</div>

---

# Capstone Project: Build with LeWorld + SO-101

<div class="accent-card mt-4 text-sm">

**Why LeWorld?** At 15M parameters, it trains in **4–8 GPU-hours** on a single A100, runs inference at **>30 FPS on an M4 Pro**, and needs only **50 demonstrations**. It's the most student-accessible world model that actually works.

</div>

<div class="grid grid-cols-3 gap-4 mt-4">

<div class="teal-card text-sm">

### Option A
**"Teach Your Robot to Imagine"**

Train LeWorld end-to-end on SO-101 pick-and-place demos. Deploy CEM planning on your laptop. The robot picks a cube using *imagination alone* — no policy network.

</div>

<div class="blue-card text-sm">

### Option B
**"The Surprise Detector"**

Use LeWorld's **prediction error** as a real-time anomaly signal. Detect task failures, human interventions, and auto-label successful episodes — no human supervisor needed.

</div>

<div class="purple-card text-sm">

### Option C
**"One Model, Four Tasks"**

Train a single LeWorld on all four SO-101 tasks. Switch tasks at inference by changing the **goal image** — no retraining. Test zero-shot transfer to a 5th unseen task.

</div>

</div>

---

# Step 1: Setup — Install LeWorld

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### Repositories

<div class="card text-sm mb-3">

```bash
# Clone LeWorld
git clone https://github.com/lucas-maes/le-wm.git
cd le-wm

# Create environment (Python 3.10)
uv venv --python=3.10
source .venv/bin/activate

# Install stable-worldmodel (training + envs)
uv pip install stable-worldmodel[train,env]
```

</div>

<div class="teal-card text-sm mb-3">
<strong>Three repos work together:</strong><br>
• <code>lucas-maes/le-wm</code> — configs + train/eval scripts<br>
• <code>galilai-group/stable-worldmodel</code> — data, CEM solver, eval<br>
• <code>rbalestr-lab/stable-pretraining</code> — ViT backbone, transforms
</div>

<div class="blue-card text-sm">
<strong>Paper:</strong> arXiv:2603.19312<br>
<strong>Project page:</strong> <code>le-wm.github.io</code>
</div>

</div>
<div>

### Verify: Replicate Push-T

<div class="card text-sm mb-3">

```bash
# Download Push-T dataset (~200MB)
# Extracts to $STABLEWM_HOME/pusht_expert_train.h5
tar --zstd -xvf pusht_expert_train.tar.zst

# Train LeWorld on Push-T (baseline)
python train.py data=pusht

# Evaluate with CEM planning
python eval.py --config-name=pusht \
    policy=pusht/lewm
```

</div>

<div class="accent-card text-sm mb-3">
<strong>Expected result:</strong> Training converges in ~100 epochs. CEM evaluation runs 50 episodes. You should see the Push-T success rate from the paper.
</div>

<div class="purple-card text-sm">
<strong>Checkpoint:</strong> Saved to <code>$STABLEWM_HOME/&lt;job_id&gt;/lewm_epoch_N_object.ckpt</code>
</div>

</div>
</div>

---

# Step 2: Data Pipeline — LeRobot → LeWorld HDF5

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### LeWorld's data format

<div class="card text-sm mb-3">
LeWorld expects a <strong>single HDF5 file</strong> with flat arrays. All episodes are concatenated. Two metadata arrays index into them:
</div>

<div class="teal-card text-sm mb-3">

| HDF5 key | Shape | Type |
|----------|-------|------|
| `ep_len` | `(num_eps,)` | int |
| `ep_offset` | `(num_eps,)` | int |
| `pixels` | `(total_steps, H, W, 3)` | uint8 |
| `action` | `(total_steps, 7)` | float32 |
| `state` | `(total_steps, 7)` | float32 |
| `step_idx` | `(total_steps,)` | int |
| `episode_idx` | `(total_steps,)` | int |

</div>

<div class="blue-card text-sm">
<strong>SO-101 action dim = 7</strong> (6 joint velocities + 1 gripper). Images resized to 224×224 for ViT-Tiny.
</div>

</div>
<div>

### Conversion script

<div class="card text-sm mb-3">

```python
# convert_lerobot_to_h5.py
import h5py, numpy as np
from lerobot.common.datasets import LeRobotDataset

ds = LeRobotDataset("lerobot/svla_so101_pickplace")

with h5py.File("so101_pickplace_train.h5", "w") as f:
    all_px, all_act, all_st = [], [], []
    ep_lens = []

    for ep_idx in range(ds.num_episodes):
        ep = ds.get_episode(ep_idx)
        imgs = ep["observation.images.front"]  # (T,C,H,W)
        # HWC uint8 for LeWorld
        imgs = (imgs.permute(0,2,3,1) * 255).byte()
        acts = ep["action"]            # (T, 7)
        state = ep["observation.state"] # (T, 7)

        all_px.append(imgs.numpy())
        all_act.append(acts.numpy())
        all_st.append(state.numpy())
        ep_lens.append(len(imgs))

    f["pixels"] = np.concatenate(all_px)
    f["action"] = np.concatenate(all_act)
    f["state"] = np.concatenate(all_st)
    f["ep_len"] = np.array(ep_lens)
    f["ep_offset"] = np.cumsum([0]+ep_lens[:-1])
    f["step_idx"] = np.concatenate(
        [np.arange(l) for l in ep_lens])
    f["episode_idx"] = np.concatenate(
        [np.full(l, i) for i, l in enumerate(ep_lens)])
```

</div>

<div class="accent-card text-sm">
Place output at <code>$STABLEWM_HOME/so101_pickplace_train.h5</code>
</div>

</div>
</div>

---

# Step 3: Training Config for SO-101

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### Create data config

<div class="card text-sm mb-3">

```yaml
# config/train/data/so101.yaml
dataset:
  num_steps: ${eval:'${wm.num_preds} + ${wm.history_size}'}
  frameskip: 5          # 30Hz → 6Hz control
  name: so101_pickplace_train
  keys_to_load:
    - pixels
    - action
    - state
  keys_to_cache:
    - action
    - state
```

</div>

<div class="teal-card text-sm mb-3">
<strong>Why frameskip=5?</strong> SO-101 records at 30 Hz. CEM planning at 6 Hz (every 5th frame) is enough for pick-place. Actions in each group are concatenated: <code>action_dim = 7 × 5 = 35</code> per planning step.
</div>

<div class="blue-card text-sm">
<strong>Auto-detection:</strong> <code>action_dim</code> is read from the HDF5 file automatically — you don't set it manually.
</div>

</div>
<div>

### Training command

<div class="card text-sm mb-3">

```bash
# Train LeWorld on SO-101
python train.py data=so101 \
    trainer.max_epochs=100 \
    optimizer.lr=5e-5 \
    loss.sigreg.weight=0.09 \
    loader.batch_size=128 \
    trainer.precision=bf16

# Override for smaller datasets (50 eps)
python train.py data=so101 \
    trainer.max_epochs=200 \
    loader.batch_size=64
```

</div>

<div class="accent-card text-sm mb-3">

### Key hyperparameters

| Parameter | Default | Notes |
|-----------|---------|-------|
| `encoder_scale` | `tiny` | ViT-Tiny, 5M params |
| `wm.history_size` | `3` | 3 past frames as context |
| `wm.num_preds` | `1` | Predict 1 step ahead |
| `wm.embed_dim` | `192` | Latent dimension |
| `predictor.depth` | `6` | 6 transformer layers |
| `loss.sigreg.weight` | `0.09` | The ONE hyperparameter |

</div>

<div class="purple-card text-sm">
<strong>Monitor for collapse:</strong> If <code>sigreg_loss</code> drops to 0 while <code>pred_loss</code> stalls, the encoder collapsed. Increase <code>sigreg.weight</code>.
</div>

</div>
</div>

---

# Step 4: Understanding the Training Loop

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### What happens each step

<div class="card text-sm mb-3">

```
Input batch:
  pixels: (128, 4, 3, 224, 224)   # B, T, C, H, W
  action: (128, 4, 35)             # B, T, act_dim*skip

Step 1: Encode all frames
  ViT-Tiny(pixels) → CLS tokens
  → Projector MLP → emb: (128, 4, 192)

Step 2: Encode all actions
  Conv1D + SiLU MLP → act_emb: (128, 4, 192)

Step 3: Split context / target
  ctx_emb  = emb[:, :3]    # history
  ctx_act  = act_emb[:, :3]
  tgt_emb  = emb[:, 1:]    # shifted target

Step 4: Predict
  ARPredictor(ctx_emb, ctx_act) → pred: (128,3,192)

Step 5: Loss
  pred_loss  = MSE(pred, tgt_emb)
  sigreg     = SIGReg(emb)      # collapse prevention
  total_loss = pred_loss + 0.09 * sigreg
```

</div>

</div>
<div>

### The architecture in one picture

<div class="teal-card text-sm mb-3">

```
pixels ──→ [ViT-Tiny] ──→ [Projector] ──→ emb
              5M params       MLP           (B,T,192)
                                              │
actions ──→ [Embedder] ──────────────→ act_emb│
              Conv1D+MLP                (B,T,192)
                                              │
              ┌───────────────────────────────┘
              ▼
         [AR Predictor]  ←── 6-layer Transformer
           10M params        16 heads, AdaLN
              │
              ▼
         [Pred Projector] ──→ pred_emb (B,T,192)
              MLP
              │
              ▼
         MSE(pred_emb, tgt_emb) + λ·SIGReg(emb)
```

</div>

<div class="accent-card text-sm mb-3">
<strong>Total: ~15M parameters.</strong> The encoder (5M) and predictor (10M) are trained jointly end-to-end. No frozen foundation model. No EMA. No stop-gradient.
</div>

<div class="blue-card text-sm">
<strong>SIGReg in one line:</strong> Project embeddings onto 1,024 random directions. Penalize deviation from $\mathcal{N}(0,1)$. That's it — collapsed embeddings can't be Gaussian.
</div>

</div>
</div>

---

# Step 5: CEM Planning — How the Robot "Imagines"

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### The algorithm

<div class="card text-sm mb-3">

```
Input: current_obs (3 frames), goal_image
Output: action sequence (5 steps)

1. z_current = Encoder(current_obs)   # (1, 3, 192)
   z_goal    = Encoder(goal_image)    # (1, 1, 192)

2. Initialize: μ = zeros(5, 35)
               σ = ones(5, 35)

3. For i = 1 to 30:        # CEM iterations
     # Sample 300 action candidates
     A ~ N(μ, σ²)          # shape: (300, 5, 35)

     # Rollout each candidate through world model
     For each candidate a₁...a₅:
       z₁ = Predictor(z_current, a₁)
       z₂ = Predictor([z₁], a₂)
       ...
       z₅ = Predictor([z₄], a₅)

     # Score: how close is z₅ to z_goal?
     cost = MSE(z₅, z_goal)    # (300,)

     # Keep top 30, update distribution
     elite = top_30_lowest_cost(A)
     μ = mean(elite)
     σ = std(elite)

4. Return μ  # best action sequence
```

</div>

</div>
<div>

### Config

<div class="teal-card text-sm mb-3">

```yaml
# config/eval/solver/cem.yaml
num_samples: 300     # candidates per iteration
n_steps: 30          # CEM iterations
topk: 30             # elite samples
```

```yaml
# config/eval/so101.yaml  (you create this)
plan_config:
  horizon: 5          # plan 5 steps ahead
  receding_horizon: 5 # execute all 5
  action_block: 5     # must match frameskip

eval:
  num_eval: 20
  goal_offset_steps: 25  # goal = 25 steps ahead
  eval_budget: 50         # max planning cycles
```

</div>

<div class="blue-card text-sm mb-3">
<strong>Speed:</strong> 300 candidates × 5 rollout steps × 30 iterations = 45,000 forward passes through the predictor. On M4 Pro: <strong>&lt;1 second total</strong> (predictor is 10M params, 192-dim). On DINO-WM: ~47 seconds (200 tokens per frame, 86M encoder).
</div>

<div class="accent-card text-sm">
<strong>Receding horizon:</strong> Execute 5 actions (at 6 Hz = 0.83 sec of motion), get a new camera frame, re-plan. The robot is constantly re-imagining its future.
</div>

</div>
</div>

---

# Step 6: Deploy on Real SO-101

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### Real-time control loop

<div class="card text-sm mb-3">

```python
# deploy_leworld_so101.py
import torch, cv2, numpy as np
from lerobot.common.robots import SO101Robot

# Load trained model
model = load_lewm_checkpoint("so101/lewm")
model.eval().to("mps")  # or "cuda"

# Connect to SO-101
robot = SO101Robot(cameras=["front"])
robot.connect()

# Capture goal image (show desired end state)
goal_img = capture_and_preprocess(robot, size=224)
z_goal = model.encode_single(goal_img)

# Control loop
history = deque(maxlen=3)  # last 3 frames
for step in range(200):
    frame = robot.get_observation()["images"]["front"]
    frame = preprocess(frame, size=224)
    history.append(frame)

    if len(history) < 3:
        continue

    # CEM planning
    z_ctx = model.encode(stack(history))
    actions = cem_solve(model, z_ctx, z_goal,
                        n_samples=300, n_iters=30,
                        horizon=5, topk=30)

    # Execute first action chunk (5 raw actions)
    for a in actions[0].reshape(5, 7):
        robot.send_action(a)  # 30 Hz
        time.sleep(1/30)
```

</div>

</div>
<div>

### Key implementation details

<div class="teal-card text-sm mb-3">
<strong>Action denormalization:</strong> LeWorld trains with z-scored actions. You must save the normalizer's <code>mean</code> and <code>std</code> from training and apply the inverse transform before sending to the robot.
</div>

<div class="blue-card text-sm mb-3">
<strong>Image preprocessing:</strong> Must match training exactly — resize to 224×224, permute to CHW, ImageNet normalize:
<br><code>mean=[0.485, 0.456, 0.406]</code>
<br><code>std=[0.229, 0.224, 0.225]</code>
</div>

<div class="accent-card text-sm mb-3">
<strong>Goal image:</strong> Before starting, manually place objects in the desired final configuration. Snap a photo. Encode it once. This is the target for all CEM planning.
</div>

<div class="purple-card text-sm">
<strong>Frameskip alignment:</strong> Training used <code>frameskip=5</code>, so each planned action is 5 raw actions concatenated (dim=35). Reshape to <code>(5, 7)</code> and send each at 30 Hz. One planning step = 5/30 = 0.167 seconds of motion.
</div>

</div>
</div>

---

# Option A: "Teach Your Robot to Imagine"

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### Week-by-week plan

<div class="teal-card text-sm mb-3">
<strong>Week 1 — Replicate Push-T:</strong><br>
• Install le-wm, download Push-T dataset<br>
• Run <code>python train.py data=pusht</code><br>
• Run <code>python eval.py --config-name=pusht policy=pusht/lewm</code><br>
• <strong>Checkpoint:</strong> loss converging, CEM planning works in sim
</div>

<div class="blue-card text-sm mb-3">
<strong>Week 2 — SO-101 data + training:</strong><br>
• Convert dataset: <code>python convert_lerobot_to_h5.py</code><br>
• Create <code>config/train/data/so101.yaml</code><br>
• Train: <code>python train.py data=so101 trainer.max_epochs=200</code><br>
• <strong>Checkpoint:</strong> pred_loss ↓, sigreg_loss stable (not zero!)
</div>

<div class="accent-card text-sm mb-3">
<strong>Week 3 — Deploy on real robot:</strong><br>
• Write <code>deploy_leworld_so101.py</code> (previous slide)<br>
• Test CEM planning with goal images<br>
• <strong>Checkpoint:</strong> robot picks cube at least 3/10 trials
</div>

<div class="purple-card text-sm">
<strong>Week 4 — Ablations + report:</strong><br>
• Sweep SIGReg λ: [0.01, 0.05, 0.09, 0.2, 0.5]<br>
• Sweep demo count: [10, 25, 50] episodes<br>
• Sweep CEM: num_samples [100, 300, 500], n_steps [10, 30]<br>
• <strong>Checkpoint:</strong> ablation plots + comparison table
</div>

</div>
<div>

### Deliverables

<div class="card text-sm mb-3">
<strong>1. Trained checkpoint</strong> (~200 MB)<br>
15M params, trained on 50 demos in 4–8 GPU-hours on 1×A100
</div>

<div class="card text-sm mb-3">
<strong>2. Demo video</strong><br>
SO-101 picking a cube using CEM planning — camera feed + latent distance plot overlay showing the planner converging
</div>

<div class="card text-sm mb-3">
<strong>3. Speed benchmark table</strong>

| | LeWorld | DINO-WM |
|--|---------|---------|
| Encoder | 5M (trained) | 86M (frozen) |
| Latents/frame | 1 | ~200 |
| Plan time/step | <1s | ~47s |
| Hardware | M4 Pro | H100 |

</div>

<div class="card text-sm mb-3">
<strong>4. Ablation plots</strong><br>
Success rate vs. λ, demo count, CEM population — 3 clean figures
</div>

<div class="accent-card text-sm">
<strong>Stretch goal:</strong> Webcam goal specification — hold up a photo of the desired end state, encode it live, plan toward it.
</div>

</div>
</div>

---

# Option B: "The Surprise Detector"

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### Core idea

<div class="card text-sm mb-3">
A world model predicts what <strong>should</strong> happen. When reality diverges, that's <strong>surprise</strong>. This is a free signal for failure detection, safety monitoring, and autonomous data labeling.
</div>

### Implementation

<div class="teal-card text-sm mb-3">
<strong>Step 1:</strong> Train LeWorld on 50 successful demos (same as Option A).
</div>

<div class="blue-card text-sm mb-3">
<strong>Step 2:</strong> Define the surprise score:

$$S(t) = \| \text{Enc}(x_{t+1}) - \text{Pred}(s_t, a_t) \|_2$$

```python
# In the control loop:
z_pred = model.predict(z_history, a_emb)  # (1,192)
z_real = model.encode(next_frame)          # (1,192)
surprise = torch.norm(z_pred - z_real).item()
```

</div>

<div class="accent-card text-sm mb-3">
<strong>Step 3:</strong> Collect calibration data:
<br>• 20 episodes where the task succeeds
<br>• 20 episodes where it fails (drop cube, miss target, human intervenes)
<br>• Plot $S(t)$ curves for both groups
<br>• Find threshold $\tau$ using ROC analysis
</div>

<div class="purple-card text-sm">
<strong>Step 4:</strong> Deploy as real-time monitor at 30 Hz alongside any policy (ACT, Diffusion, or even teleoperation).
</div>

</div>
<div>

### Three applications

<div class="card text-sm mb-3">
<strong>App 1 — Failure detection:</strong><br>
When $S(t) > \tau$ → task probably failed → trigger retry. Run alongside Diffusion Policy or ACT — LeWorld monitors, the policy acts.
</div>

<div class="card text-sm mb-3">
<strong>App 2 — Human intervention:</strong><br>
Someone grabs the cube mid-task. LeWorld predicts the cube should still be there — massive surprise spike. Pause execution, re-capture goal, re-plan.
</div>

<div class="accent-card text-sm mb-3">
<strong>App 3 — Auto-labeling for dataset growth:</strong><br>
Robot attempts task autonomously. If max$(S(t)) < \tau$ throughout → auto-label as "success" → add to dataset. If surprise spikes → discard. <strong>Grow your dataset without human supervision.</strong>
</div>

### Deliverables

<div class="teal-card text-sm">
<strong>1.</strong> ROC curve: surprise-based success/failure classification<br>
<strong>2.</strong> AUC comparison: surprise score vs. naive pixel-difference baseline<br>
<strong>3.</strong> Real-time surprise dashboard (plot $S(t)$ live during execution)<br>
<strong>4.</strong> Auto-labeled dataset: N episodes labeled by surprise alone
</div>

</div>
</div>

---

# Option C: "One Model, Four Tasks"

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### Setup

<div class="card text-sm mb-3">
<strong>Hypothesis:</strong> LeWorld learns <strong>physics</strong>, not tasks. One model should plan for any goal image — no task ID needed.
</div>

<div class="teal-card text-sm mb-3">
<strong>Data:</strong> Pool all four SO-101 datasets into one HDF5:

```python
# Same conversion script, but loop over:
datasets = [
    "lerobot/svla_so101_pickplace",   # 50 eps
    "your_org/so101_pour_beads",       # 50 eps
    "your_org/so101_sort_by_color",    # 50 eps
    "your_org/so101_push_plate",       # 50 eps
]
# → so101_multitask_train.h5 (200 eps)
```

</div>

<div class="blue-card text-sm mb-3">
<strong>Training:</strong> Identical config. Same 4–8 GPU-hours — 200 eps is still small data. The model sees a variety of object interactions during training.
</div>

<div class="accent-card text-sm">
<strong>Inference:</strong> Provide a goal image of the desired outcome. CEM minimizes <code>MSE(z_predicted, z_goal)</code>. No task ID, no language conditioning — just "make reality look like this photo."
</div>

</div>
<div>

### Experiments

<div class="card text-sm mb-3">
<strong>1. Task confusion matrix (4×4):</strong><br>
Train on all 4, evaluate on each separately. Does multi-task help or hurt per-task performance vs. single-task models?
</div>

<div class="card text-sm mb-3">
<strong>2. Data scaling curve:</strong><br>
Train on [50, 100, 150, 200] total demos. Plot success rate per task. When does more data stop helping?
</div>

<div class="card text-sm mb-3">
<strong>3. Latent space t-SNE:</strong><br>
Encode 500 frames from each task. t-SNE colored by task. Do tasks form separate clusters? Do "grasping" frames from different tasks overlap?
</div>

<div class="card text-sm mb-3">
<strong>4. Leave-one-task-out transfer:</strong><br>
Train on 3 tasks, test on the 4th. Repeat for all 4. Report zero-shot success rate. This directly tests: <em>did the model learn transferable physics?</em>
</div>

<div class="accent-card text-sm">
<strong>5. Novel task (bonus):</strong> Place objects in a configuration the model never saw (e.g., "push cup to left zone"). Give a goal photo. Does CEM find a plan?
</div>

</div>
</div>

---

# Resources, Compute & Tips

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### Code & Data

<div class="card text-sm mb-3">
<strong>LeWorld:</strong> <code>github.com/lucas-maes/le-wm</code><br>
<strong>Framework:</strong> <code>galilai-group/stable-worldmodel</code><br>
<strong>Paper:</strong> arXiv:2603.19312
</div>

<div class="teal-card text-sm mb-3">
<strong>SO-101 datasets (HuggingFace):</strong><br>
• <code>lerobot/svla_so101_pickplace</code> (50 eps)<br>
• <code>whosricky/so101-megamix-v1</code> (400 eps)<br>
• <code>youliangtan/so101-table-cleanup</code> (80 eps)<br>
Or record your own: <code>python -m lerobot.record</code>
</div>

<div class="blue-card text-sm">
<strong>LeRobot v0.4+:</strong> <code>pip install lerobot</code><br>
Data loading, camera capture, robot control, replay — the full pipeline for SO-101.
</div>

</div>
<div>

### Compute & common pitfalls

<div class="card text-sm mb-3">

| Phase | Hardware | Time | Cost |
|-------|----------|------|------|
| **Training** | 1× A100 | 4–8h | ~$8 |
| **Inference** | M4 Pro / RTX 4060 | >30 FPS | free |
| **CEM plan** | any GPU or CPU | <1s/step | free |

</div>

<div class="accent-card text-sm mb-3">
<strong>Common mistakes:</strong><br>
• Forgetting action denormalization → robot goes wild<br>
• Image normalize mismatch (training vs deploy) → garbage latents<br>
• <code>frameskip</code> ≠ <code>action_block</code> → CEM plans wrong horizon<br>
• SIGReg weight too low → encoder collapses silently
</div>

<div class="purple-card text-sm">
<strong>Start order:</strong> Push-T in sim (free, fast) → verify training loop → then SO-101 data conversion → then real robot. Don't skip the sim step.
</div>

</div>
</div>

---
layout: center
---

# Thank You

<div class="mt-6">
<h2 style="color:var(--claude-accent) !important; font-size:2em !important;">Pre-train once. Adapt to any embodiment from minutes of video.</h2>
</div>

<div class="mt-8">
<span class="opacity-60">That's the promise. Whether it holds at scale is the next chapter of the story.</span>
</div>

<div class="mt-8">
  <span class="px-4 py-2 rounded-lg text-lg" style="background:#c2785c;color:#fff;font-weight:700;">
    Modern Robot Learning from Scratch — V2
  </span>
</div>

<div class="abs-br m-6 flex gap-2">
  <a href="https://vizuara.ai" target="_blank" class="text-sm opacity-50 hover:opacity-100">
    vizuara.ai
  </a>
</div>
