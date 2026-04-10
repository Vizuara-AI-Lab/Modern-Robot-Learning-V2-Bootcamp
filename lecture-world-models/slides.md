---
theme: default
title: "World Models: Teaching Robots to Imagine"
info: |
  Lecture — Modern Robot Learning from Scratch V2 Bootcamp
  Vizuara
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
.slidev-layout blockquote { border-left:3px solid var(--claude-accent); background:var(--claude-surface); padding:8px 12px; border-radius:0 8px 8px 0; }
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

# World Models

## Teaching Robots to Imagine

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

# What We'll Cover Today

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### The Journey

<v-clicks>

<div class="accent-card mb-3">
<strong>Part 1:</strong> Why World Models? — The big picture
</div>

<div class="teal-card mb-3">
<strong>Part 2:</strong> DINO World Model — Predict in feature space
</div>

<div class="blue-card mb-3">
<strong>Part 3:</strong> RL Foundations — Just enough for IRIS
</div>

<div class="purple-card mb-3">
<strong>Part 4:</strong> IRIS World Model — World as language model
</div>

<div class="accent-card mb-3">
<strong>Part 5:</strong> DIAMOND — Diffusion as a world model
</div>

<div class="teal-card mb-3">
<strong>Part 6:</strong> Build Your Own — From scratch pipeline
</div>

</v-clicks>

<div class="card mt-2 text-sm" style="opacity:0.8;">
<strong>Continue in Part 2:</strong> LeWorld (tiny end-to-end JEPAs) and DreamZero (joint world-action models). Separate deck.
</div>

</div>
<div>

### What You'll Walk Away With

<div class="card mt-2 text-sm">

- Understanding of **4 major world model architectures** (DINO-WM, IRIS, DIAMOND, and your own WFM)
- Why world models are an **alternative to VLAs**
- Hands-on notebooks for **DINO-WM**, **IRIS**, and **DIAMOND**
- A roadmap for **building your own** world model from scratch
- The full arc of the field — from feature-space prediction to pixel-space diffusion

</div>

</div>
</div>

---

<div style="height:1px;"></div>

---
layout: center
---

# Part 1

## Why World Models?

<div class="mt-4 opacity-60">The case for imagination in robot learning</div>

---

# The Question That Started It All

<div class="brainstorm-card mt-6">
<div class="text-center">
<h2 style="color:var(--claude-accent) !important; font-size:1.8em !important;">Your robot sees a cup on a table.</h2>
<h2 style="color:var(--claude-accent) !important; font-size:1.8em !important;">If it pushes the cup, what happens?</h2>
<div class="mt-4 opacity-70">A human knows the cup slides... and might fall off the edge.</div>
<div class="mt-2 opacity-70">That prediction? That's a <strong>world model</strong>.</div>
</div>
</div>

---

# The Problem with Reactive Policies

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### What We Built in Lectures 1 & 2

<v-clicks>

<div class="card mb-3 text-sm">
<strong>Diffusion Policy</strong> (Lecture 1)
<br>Observation → denoise → action trajectory
<br><span class="opacity-60">Great for multi-modal actions, but no lookahead</span>
</div>

<div class="card mb-3 text-sm">
<strong>VLA</strong> (Lecture 2)
<br>Image + language → transformer → action
<br><span class="opacity-60">Understands language, but still purely reactive</span>
</div>

<div class="accent-card text-sm">
<strong>The common limitation:</strong> These are all <span class="highlight">stimulus → response</span> systems. They see, they act. They never <em>imagine</em> what happens next.
</div>

</v-clicks>

</div>
<div>

<v-click>

### The Driving Analogy

<div class="teal-card text-sm">

**Reactive policy** = driving while only looking **1 meter ahead**

You can stay in lane, but you'll miss the turn, the red light, the pedestrian...

**World model** = driving while imagining the **next 100 meters**

You anticipate the curve, slow down for the intersection, plan your lane change.

</div>

<div class="mt-4 accent-card text-sm">
<strong>Key insight:</strong> Lookahead requires an internal model of how the world works — a <span class="highlight">world model</span>.
</div>

</v-click>

</div>
</div>

---

# What is a World Model?

<div class="mt-2">

<v-clicks>

<div class="accent-card mb-4">

### The Core Equation

$$s_{t+1} = f(s_t, a_t)$$

Given the current state $s_t$ and an action $a_t$, predict the next state $s_{t+1}$.

**That's it.** A world model is a learned function that predicts what happens next.

</div>

<div class="grid grid-cols-3 gap-4">
<div class="card text-sm text-center">
<h3>Mental Simulator</h3>
Humans do this constantly — we imagine outcomes before acting
</div>
<div class="card text-sm text-center">
<h3>Historical Roots</h3>
STRIPS (1971) → Ha & Schmidhuber (2018) → today's explosion
</div>
<div class="card text-sm text-center">
<h3>Key Insight</h3>
If you can predict the future, you can <strong>plan</strong> instead of just <strong>react</strong>
</div>
</div>

</v-clicks>

</div>

---

# The Three Paradigms

<div class="flex justify-center items-start mt-2" style="padding-top:0.5rem;">
<img src="/figures/three-paradigms.png" class="rounded-lg" style="max-height:68vh; max-width:90%;" />
</div>

---

# Paradigm 1: Action-Conditioned

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### How It Works

$$x_{t+1} = f(x_t, a_t)$$

<v-clicks>

- Feed in observation **+ action** → predict next state
- The "purest" form of world modeling
- Strong theoretical basis for model-based RL

</v-clicks>

<v-click>

<div class="teal-card mt-4 text-sm">
<strong>Examples:</strong> V-JEPA 2 (Meta), DreamerV3 (DeepMind), DINO-WM
</div>

</v-click>

</div>
<div>

<v-click>

### The Trade-Off

<div class="card text-sm">

**Pros:**
- Clean, principled formulation
- Direct use in planning

**Cons:**
- **Needs action labels** — can't use internet video
- Error accumulates over long horizons
- Each prediction uses the previous (possibly wrong) prediction

</div>

</v-click>

</div>
</div>

---

# Paradigm 2: Video World Models

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### How It Works

$$x_{t+1} = f(x_t) \quad \text{then} \quad a_t = g(x_t, x_{t+1})$$

<v-clicks>

- **First** generate plausible future video (no actions needed!)
- **Then** extract actions via inverse dynamics model
- Two-stage pipeline: imagine → act

</v-clicks>

<v-click>

<div class="teal-card mt-4 text-sm">
<strong>Examples:</strong> DreamGen (NVIDIA), 1x World Model, LingBot-VA
</div>

</v-click>

</div>
<div>

<v-click>

### The Trade-Off

<div class="card text-sm">

**Pros:**
- **No action labels needed** for world model training
- Can leverage billions of hours of internet video
- Same idea behind Sora, Cosmos, Genie

**Cons:**
- Two-stage pipeline introduces errors
- Inverse dynamics is lossy — recovering exact actions is hard
- Video generation is expensive

</div>

</v-click>

</div>
</div>

---

# Paradigm 3: Joint World-Action Models

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### How It Works

$$(x_{t+1}, a_t) = f(x_t)$$

<v-clicks>

- **One model** predicts both future state **AND** action
- No chicken-and-egg problem
- Actions and predictions co-evolve during training

</v-clicks>

<v-click>

<div class="teal-card mt-4 text-sm">
<strong>Examples:</strong> DreamZero, Fast WAM, DualWorld
</div>

</v-click>

</div>
<div>

<v-click>

### Why This Might Win

<div class="accent-card text-sm">

**Chris Paxton (2025):**

> "Joint models generalize better than alternatives"

- Pre-train world model on internet video (no actions)
- Fine-tune action head on small robot dataset
- Same scaling argument that made LLMs work: **pre-train on everything, fine-tune on task**

</div>

<div class="card text-sm mt-3">
<strong>Current limitation:</strong> Newest approach — less understood, fewer implementations
</div>

</v-click>

</div>
</div>

---

# World Models vs. VLAs

<div class="flex justify-center items-start mt-2" style="padding-top:0.5rem;">
<img src="/figures/wm-vs-vla.png" class="rounded-lg" style="max-height:68vh; max-width:90%;" />
</div>

---

# Two Roads to Robot Intelligence

<div class="mt-2">

| | **VLA** (Lecture 2) | **World Model** |
|---|---|---|
| **Approach** | Observation → Action (direct) | Observation → Imagine → Plan → Action |
| **Planning** | None — purely reactive | Yes — simulates futures before acting |
| **Data needs** | Large action-labeled datasets | Can use unlabeled video |
| **Speed** | Fast inference (single forward pass) | Slower (multiple imagination steps) |
| **Sample efficiency** | Lower (needs lots of data) | Higher (learns from imagination) |
| **Generalization** | Good with scale | Better with planning |

<v-click>

<div class="accent-card mt-4 text-sm text-center">
<strong>Neither has won.</strong> They're complementary — and the best future systems may combine both.
<br>Chris Paxton: "World models have historically underperformed expectations, but the gap is narrowing rapidly."
</div>

</v-click>

</div>

---

# The Architectural Zoo

<div class="flex justify-center items-start mt-2" style="padding-top:0.5rem;">
<img src="/figures/architectural-zoo.png" class="rounded-lg" style="max-height:62vh; max-width:90%;" />
</div>

<v-click>

<div class="accent-card mt-2 text-sm text-center">
Today we go deep on <strong>3 architectures</strong>: DINO-WM → IRIS → DIAMOND. Then we <strong>build one from scratch</strong>. (LeWorld &amp; DreamZero are in <strong>Part 2</strong>.)
</div>

</v-click>

---

# Quiz 1: World Model Basics

<div class="quiz-card mt-4">

### Question

A robot needs to pour water from a pitcher into a glass. Which approach would handle this better?

<v-clicks>

**A.** A VLA that maps camera image → pour action directly

**B.** A world model that imagines "if I tilt the pitcher 30°, water flows out... if I tilt 60°, it overflows"

</v-clicks>

<v-click>

<div class="mt-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> The world model (B). Pouring requires predicting fluid dynamics — how water flows, when the glass is full, when it overflows. A reactive policy would need to have seen the exact same pitcher/glass combination during training. The world model can <em>reason about consequences</em> and adjust its pour angle in real time.
</div>

</v-click>

</div>

---

<div style="height:1px;"></div>

---
layout: center
---

# Part 2

## DINO World Model

<div class="mt-4 opacity-60">Predict in feature space, not pixel space</div>

---

# The Key Insight: Don't Predict Pixels

<div class="flex justify-center items-start mt-2" style="padding-top:0.5rem;">
<img src="/figures/pixel-vs-feature-prediction.png" class="rounded-lg" style="max-height:68vh; max-width:90%;" />
</div>

---

# Why Feature Space?

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### Pixel Prediction is Wasteful

<v-clicks>

- 256 × 256 × 3 = **196,608 values** per frame
- Most pixels are irrelevant: shadows, textures, background noise
- The model wastes capacity predicting things that don't matter for actions
- Mode collapse: blurry average predictions

</v-clicks>

</div>
<div>

<v-click>

### DINO Features Capture Semantics

<div class="teal-card text-sm">

**DINOv2** was pre-trained on millions of images via self-supervised learning.

Its features naturally encode:
- **Object identity** — "this is a cup"
- **Spatial layout** — "cup is left of the plate"
- **Pose information** — "the arm is extended"
- **Affordances** — "the handle is graspable"

All in a compact **14 × 14 grid** of feature vectors = **196 vectors**.

</div>

</v-click>

<v-click>

<div class="accent-card mt-3 text-sm">
<strong>196 meaningful features vs. 196,608 noisy pixels.</strong> That's a 1000× reduction in what needs to be predicted!
</div>

</v-click>

</div>
</div>

---

# DINO-WM Architecture

<div class="flex justify-center items-start mt-2" style="padding-top:0.5rem;">
<img src="/figures/dino-wm-architecture.png" class="rounded-lg" style="max-height:68vh; max-width:90%;" />
</div>

---

# The Three Components

<div class="grid grid-cols-3 gap-4 mt-4">

<v-clicks>

<div class="teal-card text-sm">

### 1. Frozen DINO Encoder

- Pre-trained DINOv2 ViT
- **Completely frozen** — no training needed
- Image → 14×14 grid of feature patches
- Each patch = 768-dim vector
- Captures rich semantic information

</div>

<div class="accent-card text-sm">

### 2. Transformer Predictor

- **The only trainable part!**
- Takes: DINO features + action embedding
- Block-causal attention mask
- Spatial + temporal position encodings
- Predicts: next frame's DINO features

</div>

<div class="blue-card text-sm">

### 3. VQ-VAE Decoder

- **Optional** — for visualization only
- Converts DINO features → viewable images
- Vector quantization: features → codebook entries
- Planning doesn't need this at all

</div>

</v-clicks>

</div>

<v-click>

<div class="card mt-4 text-sm text-center">
<strong>Key insight:</strong> Only the Transformer Predictor is trained. The frozen encoder does the heavy lifting of representation, and the decoder is just for human viewing.
</div>

</v-click>

---

# Interactive: DINO Transformer Predictor

<iframe src="https://dino-transformer-predictor-visualiz.vercel.app/" class="w-full rounded-lg mt-1" style="height:72vh;border:none;" />

---

# The Frozen Encoder Advantage

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### Data Efficiency

<v-clicks>

<div class="teal-card mb-3 text-sm">
<strong>DINO-WM:</strong> Works with just <span class="highlight">50–100 trajectories</span>
<br>Pre-trained features = rich representations for free
</div>

<div class="card mb-3 text-sm">
<strong>End-to-end pixel models:</strong> Need <span class="highlight">10,000+ trajectories</span>
<br>Must learn visual representations AND dynamics from scratch
</div>

<div class="accent-card text-sm">
<strong>Why?</strong> DINO was trained on millions of internet images. Those features transfer directly to robot scenes — objects, spatial layout, pose — all for free.
</div>

</v-clicks>

</div>
<div>

<v-click>

### PCA of DINO Feature Space

<div class="card text-sm">

When you visualize DINO features with PCA, you see:

- **Objects cluster by identity** (all cups together, all plates together)
- **Spatial relationships preserved** (nearby objects have nearby features)
- **Smooth trajectories** in feature space (movement = smooth path)

This is why predicting in DINO space works — the features are already "well-organized" for dynamics prediction.

</div>

</v-click>

</div>
</div>

---

# Zero-Shot Planning with CEM

<div class="flex justify-center items-start mt-2" style="padding-top:0.5rem;">
<img src="/figures/cem-planning.png" class="rounded-lg" style="max-height:68vh; max-width:90%;" />
</div>

---

# How CEM Planning Works

<div class="mt-2">

<v-clicks>

<div class="grid grid-cols-2 gap-4">
<div class="card text-sm mb-3">
<h3>Step 1: Sample Random Actions</h3>
Generate many random action sequences (e.g., 64 trajectories of 10 steps each)
</div>
<div class="card text-sm mb-3">
<h3>Step 2: Imagine Outcomes</h3>
Roll out each sequence through the world model — predict what happens for each
</div>
</div>

<div class="grid grid-cols-2 gap-4">
<div class="card text-sm mb-3">
<h3>Step 3: Evaluate Against Goal</h3>
Compare predicted final features to goal features. Rank by distance: closest = best.
</div>
<div class="card text-sm mb-3">
<h3>Step 4: Refine & Repeat</h3>
Keep top-K trajectories, re-sample around them. After 3-5 iterations, execute the best action.
</div>
</div>

</v-clicks>

<v-click>

<div class="accent-card mt-2 text-sm">
<strong>Zero-shot:</strong> No reward function needed — just a goal image! The world model + CEM finds actions that reach the goal purely by imagining futures.
</div>

</v-click>

</div>

---

# Interactive: VQ-VAE Decoder

<iframe src="https://vqvae-decoder-visualizer.vercel.app/" class="w-full rounded-lg mt-1" style="height:72vh;border:none;" />

---

# Notebook: DINO World Model from Scratch

<a href="/notebooks/DINO_World_Model_From_Scratch.ipynb" download class="text-xs px-2 py-1 rounded" style="background:rgba(90,127,165,0.08);color:#5a7fa5;text-decoration:none;border:1px solid rgba(90,127,165,0.2);position:absolute;right:2em;top:4.5em;">
  Notebook: DINO_World_Model_From_Scratch.ipynb
</a>

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### What You'll Build

<div class="notebook-card text-sm">

1. **Ball Arena** environment — colored ball moves on a 2D plane
2. **Frozen DINO encoder** — extract features from each frame
3. **Transformer Predictor** — learn dynamics in feature space
4. **VQ-VAE Decoder** — reconstruct images for visualization
5. **CEM Planner** — zero-shot goal reaching!

</div>

### Key Results

<div class="teal-card text-sm mt-3">

- Train on ~50 episodes
- Ball reaches arbitrary goals it's never seen
- PCA analysis shows clean feature space
- Autoregressive multi-step rollouts

</div>

</div>
<div>

### Also Available

<div class="card text-sm mb-3">
<strong>DINO-WM on Push-T</strong> (real LeRobot data!)
<br>Same approach, but on the Push-T benchmark with 40 expert episodes at 96×96
<br>Pre-encoded DINO features for 5× speedup
</div>

<div class="accent-card text-sm">
<strong>What to look for in the notebook:</strong>
- How little data is needed (frozen features do the heavy lifting)
- The PCA visualization — see how DINO organizes the world
- Autoregressive rollout quality — how far ahead can it predict?
- CEM planning — watch the agent reach goals without any reward function
</div>

</div>
</div>

---

# DINO-WM: Limitations

<div class="mt-4">

<v-clicks>

<div class="grid grid-cols-2 gap-4">
<div class="card text-sm mb-3">
<h3>1. Error Compounds</h3>
Single-frame prediction → each step uses the <em>previous prediction</em> → errors grow exponentially over long horizons
</div>
<div class="card text-sm mb-3">
<h3>2. No Learned Policy</h3>
CEM planning requires many forward passes per action (slow!). Must re-plan from scratch every step.
</div>
</div>

<div class="grid grid-cols-2 gap-4">
<div class="card text-sm mb-3">
<h3>3. Frozen = No Adaptation</h3>
DINO features are general-purpose but can't adapt to task-specific details. Some fine-grained information may be lost.
</div>
<div class="card text-sm mb-3">
<h3>4. Simple Dynamics Only</h3>
Works great for simple tasks (ball arena, push-T) but struggles with complex multi-object interactions.
</div>
</div>

</v-clicks>

<v-click>

<div class="accent-card mt-3 text-sm text-center">
These limitations motivate two extensions: <strong>IRIS</strong> (learn everything from scratch, train policy in dreams) and <strong>DIAMOND</strong> (diffusion in pixel space — visual details preserved).
<br>But first — we need to understand RL fundamentals for IRIS.
</div>

</v-click>

</div>

---

# Quiz 2: DINO-WM

<div class="quiz-card mt-4">

### Question

Why does DINO-WM only need ~50 training trajectories, while pixel-based world models need 10,000+?

<v-clicks>

**A.** DINO-WM uses a simpler environment

**B.** The frozen DINO encoder provides rich pre-trained representations, so only the small dynamics model needs to be trained

**C.** DINO-WM uses data augmentation

**D.** The VQ-VAE decoder generates additional training data

</v-clicks>

<v-click>

<div class="mt-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> (B) The frozen DINO encoder. DINOv2 was pre-trained on millions of images and already "understands" objects, spatial layout, and visual semantics. This transfers directly to the robot domain. The Transformer Predictor only needs to learn <em>dynamics</em> (how things move), not <em>perception</em> (what things are). That's 1% of the total learning problem.
</div>

</v-click>

</div>

---

<div style="height:1px;"></div>

---
layout: center
---

# Part 3

## RL Foundations

<div class="mt-4 opacity-60">Just enough reinforcement learning to understand IRIS</div>

---

# Why RL? Why Now?

<div class="mt-4">

<div class="accent-card mb-4 text-sm">
<strong>IRIS</strong> does something remarkable: it trains an RL agent <em>entirely inside its own imagination</em>.
<br><br>
To understand why this is powerful, we need to know: What is an RL agent? What is a policy? What is an actor-critic? This section covers the minimum — if you want more, check out the <strong>RL from Scratch</strong> video series.
</div>

<v-click>

<div class="grid grid-cols-3 gap-4">
<div class="card text-sm text-center">
<h3>What is RL?</h3>
Agent interacts with environment, learns from reward signals
</div>
<div class="card text-sm text-center">
<h3>What is Actor-Critic?</h3>
Actor decides, Critic evaluates — they improve together
</div>
<div class="card text-sm text-center">
<h3>What is Dream Learning?</h3>
Train in imagination instead of reality — IRIS's key trick
</div>
</div>

</v-click>

</div>

---

# The RL Loop

<div class="flex justify-center items-start mt-2" style="padding-top:0.5rem;">
<img src="/figures/rl-agent-environment.png" class="rounded-lg" style="max-height:52vh; max-width:80%;" />
</div>

<v-click>

<div class="grid grid-cols-2 gap-4 mt-4">
<div class="card text-sm">
<h3>The Loop</h3>

1. Agent observes state $s_t$
2. Agent takes action $a_t$ based on policy $\pi(a|s)$
3. Environment transitions to $s_{t+1}$
4. Agent receives reward $r_{t+1}$
5. Repeat

</div>
<div class="accent-card text-sm">
<h3>The Goal</h3>

Maximize the **cumulative discounted return**:

$$G_t = r_t + \gamma r_{t+1} + \gamma^2 r_{t+2} + \ldots$$

$\gamma \in [0,1]$ is the **discount factor** — future rewards are worth less than immediate ones.

</div>
</div>

</v-click>

---

# Policy & Value Functions

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### Policy: Your Instincts

<v-clicks>

<div class="accent-card mb-3 text-sm">
$\pi(a|s)$ = probability of taking action $a$ in state $s$

The policy is what the agent has **learned to do** — its strategy.

**Example:** In chess, the policy says "in this position, move the queen to d5 with 60% probability."
</div>

### Value Function: Your Judgment

<div class="blue-card text-sm">
$V(s)$ = expected return from state $s$ under policy $\pi$

"How good is it to be in this state?"

**Example:** Being ahead in material in chess → high value. Being in checkmate → $V = 0$.
</div>

</v-clicks>

</div>
<div>

<v-click>

### Q-Function: Action Evaluation

<div class="teal-card mb-3 text-sm">
$Q(s,a)$ = expected return from state $s$, taking action $a$, then following $\pi$

"How good is this specific action in this state?"
</div>

### The Bellman Equation (Intuition)

<div class="purple-card text-sm">

$$V(s) = r + \gamma \cdot V(s')$$

"The value of a state = the immediate reward + the discounted value of the next state."

This recursive definition is the foundation of ALL value-based RL.
</div>

</v-click>

</div>
</div>

---

# Actor-Critic Methods

<div class="flex justify-center items-start mt-2" style="padding-top:0.5rem;">
<img src="/figures/actor-critic-architecture.png" class="rounded-lg" style="max-height:52vh; max-width:85%;" />
</div>

<v-click>

<div class="grid grid-cols-3 gap-4 mt-3">
<div class="accent-card text-sm">
<strong>Actor</strong> (Policy Network)
<br>Decides what to do: $\pi(a|s)$
<br>"I should move left"
</div>
<div class="blue-card text-sm">
<strong>Critic</strong> (Value Network)
<br>Evaluates states: $V(s)$
<br>"This state is worth +7.2"
</div>
<div class="teal-card text-sm">
<strong>Advantage</strong>
<br>$A(s,a) = Q(s,a) - V(s)$
<br>"This action was 3.1 better than average"
</div>
</div>

</v-click>

---

# The Dream: Learning Without Reality

<div class="flex justify-center items-start mt-2" style="padding-top:0.5rem;">
<img src="/figures/dream-learning.png" class="rounded-lg" style="max-height:68vh; max-width:90%;" />
</div>

---

# Why Dream Learning Changes Everything

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### Traditional RL

<v-clicks>

<div class="card text-sm mb-3">

- Must interact with **real environment**
- Each episode takes minutes/hours
- Robot might **break things** while exploring
- Need expensive hardware running 24/7
- 50M steps for Atari? That's **38 days** of real-time play

</div>

</v-clicks>

</div>
<div>

<v-click>

### Model-Based RL (Dream Learning)

<div class="teal-card text-sm mb-3">

- Collect a **small amount** of real data
- Learn a **world model** from that data
- Generate **unlimited imagined experiences**
- Train policy **entirely in dreams**
- 100K real steps + 10M imagined steps = same result!

</div>

<div class="accent-card text-sm">
<strong>The catch:</strong> The world model must be accurate. If the model is wrong, the policy learns wrong things.

> "All models are wrong, but some are useful."

The model doesn't need to be perfect — just good enough for the policy to learn useful behaviors.
</div>

</v-click>

</div>
</div>

---

# From DINO-WM to IRIS

<div class="mt-4">

<div class="grid grid-cols-2 gap-6">
<div class="card">
<h3>DINO-WM (Part 2)</h3>
<div class="text-sm mt-2">

- Used **CEM planning** — no learned policy
- Re-plans from scratch every step (slow)
- World model predicts features, but no agent learns from them

</div>
</div>
<div class="accent-card">
<h3>IRIS (Part 4, up next)</h3>
<div class="text-sm mt-2">

- Trains a full **actor-critic** inside the world model
- Policy runs instantly at test time (fast!)
- Agent learns entirely from **imagined experience**
- No real environment needed for policy training

</div>
</div>
</div>

<v-click>

<div class="teal-card mt-4 text-sm text-center">
<strong>IRIS combines world modeling with RL:</strong> it learns a world model (as a language model!) and trains an agent entirely in its dreams. Let's see how.
</div>

</v-click>

</div>

---

<div style="height:1px;"></div>

---
layout: center
---

# Part 4

## IRIS World Model

<div class="mt-4 opacity-60">The world as a language model</div>

---

# The Big Insight: Frames Are Sentences

<div class="mt-4">

<div class="grid grid-cols-2 gap-6">
<div>

### Language Modeling

<v-clicks>

<div class="card text-sm mb-3">
<strong>Input:</strong> "The cat sat on the..."
<br><strong>Predict:</strong> "mat" (next word)
<br><strong>Method:</strong> $P(w_{t+1} | w_1, \ldots, w_t)$
</div>

### World Modeling

<div class="accent-card text-sm">
<strong>Input:</strong> [game frame tokens + action]
<br><strong>Predict:</strong> [next game frame tokens]
<br><strong>Method:</strong> $P(\text{tok}_{t+1} | \text{tok}_1, \ldots, \text{tok}_t)$
</div>

</v-clicks>

</div>
<div>

<v-click>

<div class="teal-card text-sm">

### The IRIS Insight

What if we **tokenize images** into discrete "words"?

Then:
- **Predicting the next frame** = predicting the next sentence
- **Same architecture** (GPT) works for both
- **Same training** (cross-entropy) applies
- **Same scaling laws** should hold

**If you understand GPT, you understand IRIS.**

</div>

<div class="blue-card text-sm mt-3">
<strong>Why discrete?</strong> Discrete tokens enable exact likelihoods, categorical predictions, and avoid the mode collapse that plagues continuous models. Same reason text works with discrete tokens — they're a natural fit for sequence modeling.
</div>

</v-click>

</div>
</div>

</div>

---

# Step 1: Image Tokenization with VQ-VAE

<div class="flex justify-center items-start mt-2" style="padding-top:0.5rem;">
<img src="/figures/iris-vqvae-tokenization.png" class="rounded-lg" style="max-height:68vh; max-width:90%;" />
</div>

---

# How VQ-VAE Tokenization Works

<div class="mt-2">

<v-clicks>

<div class="grid grid-cols-3 gap-4">
<div class="card text-sm">
<h3>1. Encode</h3>
Game frame (e.g. 64×64 Atari) → CNN encoder → continuous latent grid (e.g. 4×4 = 16 vectors)
</div>
<div class="accent-card text-sm">
<h3>2. Quantize</h3>
Each continuous vector **snaps** to its nearest entry in a learned codebook (e.g. 512 entries). Like rounding — but learned.
</div>
<div class="teal-card text-sm">
<h3>3. Decode</h3>
The 16 discrete token IDs → lookup codebook entries → CNN decoder → reconstructed image
</div>
</div>

</v-clicks>

<v-click>

<div class="grid grid-cols-2 gap-4 mt-4">
<div class="blue-card text-sm">
<strong>Key numbers:</strong>
- Each image → **16 discrete tokens**
- Codebook size: **512 entries**
- Each token is an integer: 0, 1, ..., 511
- Reconstruction quality: good enough for RL (not photo-realistic)
</div>
<div class="purple-card text-sm">
<strong>Straight-Through Estimator:</strong>
Quantization is not differentiable (argmin). The STE trick: in the forward pass, snap to nearest codebook entry. In the backward pass, copy gradients straight through as if quantization didn't happen.
</div>
</div>

</v-click>

</div>

---

# Step 2: Sequence Construction

<div class="flex justify-center items-start mt-2" style="padding-top:0.5rem;">
<img src="/figures/iris-sequence-construction.png" class="rounded-lg" style="max-height:68vh; max-width:90%;" />
</div>

---

# The Sequence Layout

<div class="mt-4">

<v-clicks>

<div class="accent-card mb-4 text-sm">

### One Timestep = 19 Tokens

| Token Type | Count | Description |
|---|---|---|
| **Reward** | 1 | Discretized reward (gold) |
| **Done** | 1 | Episode ended? (gray) |
| **Action** | 1 | Which button pressed (rust) |
| **Observation** | 16 | VQ-VAE image tokens (teal) |
| **Total** | **19** | One complete game step |

</div>

<div class="teal-card text-sm">
<strong>Multiple timesteps concatenated:</strong> 3 steps = 57 tokens. 10 steps = 190 tokens.

This is just like a text document — but the "words" are game states. The **GPT-style Transformer** predicts the next token in this sequence.
</div>

</v-clicks>

</div>

---

# Step 3: The World Model Transformer

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### Architecture

<v-clicks>

<div class="card text-sm mb-3">
<strong>Standard GPT-style causal Transformer</strong>
- Input: sequence of past tokens
- Causal mask: each token attends only to previous tokens
- Output: next-token prediction (cross-entropy loss)
</div>

<div class="accent-card text-sm mb-3">
<strong>At inference (dreaming):</strong>
1. Feed current tokens + chosen action
2. Autoregressively generate 16 observation tokens
3. Generate reward and done tokens
4. → One complete imagined timestep!
5. Repeat for as many steps as you want
</div>

</v-clicks>

</div>
<div>

<v-click>

### What the Model Learns

<div class="teal-card text-sm">

The world model Transformer learns **simultaneously**:
- **Physics**: ball bounces off walls, paddle moves left/right
- **Game rules**: brick disappears when hit, score increases
- **Reward structure**: hitting bricks = positive reward
- **Termination**: ball falls below paddle = game over

All from **next-token prediction** — just like GPT learning language, grammar, and world knowledge from predicting the next word.
</div>

</v-click>

</div>
</div>

---

# Interactive: IRIS World Model Architecture

<iframe src="https://iris-world-model-visualizer.vercel.app/" class="w-full rounded-lg mt-1" style="height:72vh;border:none;" />

---

# Step 4: Actor-Critic in Imagination

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### Training the Agent in Dreams

<v-clicks>

<div class="card text-sm mb-3">
<strong>1. World model generates imagined trajectory</strong>
<br>Start from a real state → world model predicts next 15 steps → complete imagined episode
</div>

<div class="accent-card text-sm mb-3">
<strong>2. Actor observes imagined states</strong>
<br>$\pi(a|s_{\text{imagined}})$ — picks actions in the dream world
</div>

<div class="blue-card text-sm mb-3">
<strong>3. Critic evaluates imagined states</strong>
<br>$V(s_{\text{imagined}})$ — estimates value of each dream state
</div>

<div class="teal-card text-sm">
<strong>4. Both improve from imagined rewards</strong>
<br>World model provides rewards → compute advantages → update actor & critic
</div>

</v-clicks>

</div>
<div>

<v-click>

### The Key Insight

<div class="purple-card text-sm">

**The real environment is only used to collect data for the world model.**

The policy is trained **entirely in dreams**.

- Real data: ~100K environment steps (2 hours of gameplay)
- Imagined data: millions of steps (seconds of GPU time)
- Result: human-level Atari performance!

</div>

<div class="accent-card text-sm mt-3">
<strong>Why this works:</strong> The world model has learned accurate game dynamics from 100K real steps. The actor-critic can then practice endlessly in this accurate simulation without ever touching the real game.
</div>

</v-click>

</div>
</div>

---

# IRIS Training Pipeline

<div class="flex justify-center items-start mt-2" style="padding-top:0.5rem;">
<img src="/figures/iris-training-pipeline.png" class="rounded-lg" style="max-height:68vh; max-width:90%;" />
</div>

---

# Results: Playing Atari in Dreams

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### The Numbers

<v-clicks>

<div class="accent-card mb-3 text-sm">
<strong>Sample efficiency:</strong> Human-level on several Atari games with only **100K real steps** (2 hours of gameplay)

Model-free methods need **50M steps** for the same result.

That's **500× more sample efficient.**
</div>

<div class="teal-card text-sm">
<strong>Dream quality:</strong> Imagined rollouts look strikingly similar to real gameplay. The model has learned:
- Ball physics (bouncing angles)
- Paddle movement effects
- Brick destruction patterns
- Score accumulation
</div>

</v-clicks>

</div>
<div>

<v-click>

### Why Discrete Tokens Work

<div class="blue-card text-sm mb-3">

**Intuition says:** Discretization should lose information.

**Reality:** VQ-VAE learns an efficient codebook that preserves what matters:
- 512 codebook entries capture the visual diversity of Atari games
- Discrete tokens = exact likelihoods (no blurry averages)
- Categorical predictions avoid mode collapse
- Same reason text works with discrete tokens

</div>

<div class="card text-sm">
<strong>Connection to LLMs:</strong> Just as GPT captures the "rules of English" from next-word prediction, IRIS captures the "rules of the game" from next-token prediction. Language model scaling laws apply!
</div>

</v-click>

</div>
</div>

---

# Notebook: IRIS World Model from Scratch

<a href="/notebooks/IRIS_World_Model_From_Scratch.ipynb" download class="text-xs px-2 py-1 rounded" style="background:rgba(90,127,165,0.08);color:#5a7fa5;text-decoration:none;border:1px solid rgba(90,127,165,0.2);position:absolute;right:2em;top:4.5em;">
  Notebook: IRIS_World_Model_From_Scratch.ipynb
</a>

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### What You'll Build

<div class="notebook-card text-sm">

1. **Catch environment** — ball falls, paddle catches
2. **VQ-VAE** — tokenize 5×5 frames into discrete tokens
3. **World Model Transformer** — GPT-style next-token prediction
4. **Actor-Critic** — trained entirely in imagined rollouts
5. **Evaluation** — catch rate >70%, all from dreams!

</div>

</div>
<div>

### Key Takeaways

<div class="teal-card text-sm mb-3">

- VQ-VAE training: watch codebook utilization
- Sequence construction: see how tokens concatenate
- Dream rollouts: compare imagined vs real trajectories
- Actor-critic curves: policy improves purely from imagination!

</div>

<div class="accent-card text-sm">
<strong>The "aha" moment:</strong> The agent achieves >70% catch rate having **never played the real game** after the initial data collection. All skill was learned in dreams.
</div>

</div>
</div>

---

# IRIS: Limitations

<div class="mt-4">

<v-clicks>

<div class="grid grid-cols-2 gap-4">
<div class="card text-sm mb-3">
<h3>1. Discrete = Low Fidelity</h3>
VQ-VAE reconstructions are blocky. Fine for Atari, not for real-world manipulation with subtle visual cues.
</div>
<div class="card text-sm mb-3">
<h3>2. Autoregressive = Slow</h3>
Generating one frame = 16 sequential token predictions. Long rollouts are computationally expensive.
</div>
</div>

<div class="grid grid-cols-2 gap-4">
<div class="card text-sm mb-3">
<h3>3. Discrete Actions Only</h3>
Works great with button presses (Atari). Struggles with continuous control (robot joints with infinite action space).
</div>
<div class="card text-sm mb-3">
<h3>4. No Pre-trained Features</h3>
Learns everything from scratch — VQ-VAE, dynamics, policy. Less data-efficient than DINO-WM for small datasets.
</div>
</div>

</v-clicks>

<v-click>

<div class="accent-card mt-3 text-sm text-center">
<strong>Next up:</strong> DIAMOND keeps the "learn in dreams" idea but swaps discrete tokens for <em>continuous pixel-space diffusion</em> — preserving the 1-2 pixel details that IRIS's tokenizer blurs away.
</div>

</v-click>

</div>

---

# Quiz 3: IRIS

<div class="quiz-card mt-4">

### Question

In IRIS, what is the role of the VQ-VAE?

<v-clicks>

**A.** It generates the reward signal for the RL agent

**B.** It converts continuous images into discrete tokens so the world model can use language modeling (next-token prediction)

**C.** It is the world model itself that predicts future states

**D.** It trains the actor-critic policy

</v-clicks>

<v-click>

<div class="mt-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> (B) The VQ-VAE is the <strong>tokenizer</strong> — it converts images into discrete tokens (like converting text to word IDs). This is what enables the world model to be a GPT-style Transformer. The world model is a separate component that predicts the next tokens in the sequence.
</div>

</v-click>

</div>

---

<div style="height:1px;"></div>

---
layout: center
---

# Part 5

## DIAMOND

<div class="mt-4 opacity-60">Diffusion as a model of environment dreams</div>

---

# From Discrete Tokens to Pixel-Space Diffusion

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### The IRIS bottleneck

<v-clicks>

<div class="card text-sm mb-3">
<strong>Lossy tokenizer:</strong> IRIS compresses 64×64 Atari frames into a 8×8 grid of 512-entry codebook indices. That's ~<span class="highlight">3× compression</span> — and it's lossy.
</div>

<div class="card text-sm mb-3">
<strong>Tiny sprites disappear:</strong> In <em>Asterix</em>, a 1–2 pixel chili sprite is worth the entire reward. The tokenizer averages it into the background.
</div>

<div class="card text-sm mb-3">
<strong>Mode averaging:</strong> When next-frame prediction is stochastic, the conditional-mean decoder produces blurred outputs. The agent then reads the blur as noise.
</div>

</v-clicks>

</div>
<div>

### DIAMOND's thesis

<v-click>

<div class="teal-card text-sm mb-3">
<strong>Visual details matter.</strong> In Atari, reward signals often ride on a handful of pixels. Blur them → lose the reward → policy can't learn.
</div>

</v-click>

<v-click>

<div class="accent-card text-sm mb-3">
Keep the <strong>entire pixel tensor</strong>. Model the stochastic distribution over next frames with a <strong>diffusion denoiser</strong> in RGB space. No tokenizer. No quantization. No mode collapse.
</div>

</v-click>

<v-click>

<div class="card text-sm">
<strong>Result:</strong> 1.46 mean human-normalized score on Atari 100K — new SOTA for agents trained entirely in a world model (NeurIPS 2024 spotlight).
</div>

</v-click>

</div>
</div>

---

# DIAMOND at a Glance

<div class="flex justify-center items-start mt-2" style="padding-top:0.5rem;">
<img src="/figures/diamond-big-picture.png" class="rounded-lg" style="max-height:68vh; max-width:90%;" />
</div>

---

# Where DIAMOND Sits in the Map

<div class="grid grid-cols-3 gap-4 mt-4">
<div class="card">
<h3>Discrete-Token</h3>
<div class="text-xs mt-2 opacity-70">IRIS, TWM, STORM</div>
<div class="text-xs mt-3">
VQ-VAE → transformer → codebook indices. Fast inference. Lossy on details.
</div>
</div>

<div class="accent-card" style="border-width:2px;">
<h3>Continuous Pixel</h3>
<div class="text-xs mt-2 opacity-70"><strong>DIAMOND</strong>, GameNGen</div>
<div class="text-xs mt-3">
Diffusion denoiser directly on RGB pixels. Preserves 1-2 pixel details. 3 NFE per frame with EDM.
</div>
</div>

<div class="card">
<h3>Continuous Latent</h3>
<div class="text-xs mt-2 opacity-70">DINO-WM, Dreamer, PlaNet</div>
<div class="text-xs mt-3">
Pre-trained or learned latent space. JEPA-style prediction. No pixel reconstruction.
</div>
</div>
</div>

<v-click>

<div class="teal-card mt-4 text-sm text-center">
DIAMOND is the <strong>first</strong> world model to show that <em>pure pixel-space diffusion</em> works as an RL environment — at ~4.4M parameters, and as few as <strong>3 denoising steps per frame</strong>.
</div>

</v-click>

---

# The DIAMOND Denoiser

<div class="flex justify-center items-start mt-2" style="padding-top:0.5rem;">
<img src="/figures/diamond-architecture.png" class="rounded-lg" style="max-height:68vh; max-width:90%;" />
</div>

---

# Architecture: A Small, Honest U-Net

<div class="grid grid-cols-2 gap-4 mt-3 text-sm">
<div>

<v-clicks>

<div class="card mb-2">
<strong>Backbone:</strong> a 4-level 2D Conv U-Net with <strong>64 channels</strong> per level, 2 residual blocks each. No attention at 64×64.
</div>

<div class="card mb-2">
<strong>Past frames (conditioning):</strong> the last <strong>L = 4</strong> observations are <em>stacked along the channel dimension</em> → 12 input channels.
</div>

<div class="card mb-2">
<strong>Noisy target:</strong> 3 more channels (the frame the model is trying to denoise) → 15 channels in, 3 channels out.
</div>

</v-clicks>

</div>
<div>

<v-clicks>

<div class="teal-card mb-2">
<strong>Past actions:</strong> embedded into a 256-dim vector and injected into every residual block via <strong>Adaptive GroupNorm</strong>.
</div>

<div class="teal-card mb-2">
<strong>Noise level σ:</strong> sinusoidal embedding (c_noise = ¼ · ln σ), fed through the same AdaGN path as actions.
</div>

<div class="accent-card mb-2">
<strong>Total: ~4.4M parameters.</strong> Smaller than the IRIS transformer. No attention, no tokenizer, no codebook — just a convnet that knows how to dream frames.
</div>

</v-clicks>

</div>
</div>

---

# Why DDPM Fails at Low Steps

<div class="flex justify-center items-start mt-2" style="padding-top:0.5rem;">
<img src="/figures/diamond-edm-vs-ddpm.png" class="rounded-lg" style="max-height:68vh; max-width:90%;" />
</div>

---

# The EDM Preconditioning Trick

<div class="grid grid-cols-2 gap-6 mt-3">
<div>

<v-click>

<div class="card text-sm mb-3">
<strong>DDPM parameterization</strong> predicts the noise ε directly. When σ is large, "predict ε" collapses to "predict the input" — the clean-image estimate <span class="highlight">becomes useless</span>. You need many steps to recover.
</div>

</v-click>

<v-click>

<div class="teal-card text-sm">
<strong>EDM (Karras 2022):</strong> reparameterize the denoiser so the network's target is <em>always</em> the clean image, regardless of σ.
</div>

</v-click>

</div>
<div>

<v-click>

<div class="card text-sm mb-3">
$$D_\theta(x; \sigma) = c_{skip}(\sigma)\,x + c_{out}(\sigma)\,F_\theta\big(c_{in}(\sigma)\,x,\; c_{noise}(\sigma)\big)$$
</div>

</v-click>

<v-click>

<div class="accent-card text-sm mb-3">
DIAMOND uses: <code>σ_data = 0.5</code>, <code>σ_offset_noise = 0.3</code>, training noise distribution <code>ln σ ∼ 𝒩(-0.4, 1.2²)</code>.
</div>

</v-click>

<v-click>

<div class="card text-sm">
<strong>Payoff:</strong> training is stable across the whole σ range, and rollouts need only <strong>3 Euler steps per frame</strong> — about 5× cheaper than DDPM.
</div>

</v-click>

</div>
</div>

---

# Why Exactly 3 Denoising Steps?

<div class="flex justify-center items-start mt-2" style="padding-top:0.5rem;">
<img src="/figures/diamond-mode-collapse.png" class="rounded-lg" style="max-height:68vh; max-width:90%;" />
</div>

---

# 1 Step vs 3 Steps: The Mode Problem

<div class="grid grid-cols-2 gap-6 mt-3 text-sm">
<div>

### 1 step → averaging

<v-clicks>

<div class="card mb-2">
A single Euler jump from pure noise to prediction is just the <strong>conditional mean</strong> of the next frame. If the world is stochastic, the mean is a <em>blur</em>.
</div>

<div class="card mb-2">
On <em>Boxing</em>, the opponent's moves are unpredictable. 1-step DIAMOND shows <strong>three ghost copies</strong> of the opponent overlapping — the mean of all possible next positions.
</div>

</v-clicks>

</div>
<div>

### 3 steps → mode selection

<v-clicks>

<div class="teal-card mb-2">
The first step commits to a "seed" — a particular region of the distribution. Later steps refine <em>that</em> mode. Output is crisp and committed.
</div>

<div class="teal-card mb-2">
Empirically, 3 steps is the sweet spot: crisper than 1, essentially indistinguishable from 10. 5× cheaper than the 16+ steps DDPM would need.
</div>

<div class="accent-card">
Across an entire rollout, each step samples a <em>different</em> possible future, so stochasticity is preserved at the trajectory level — not at the pixel level.
</div>

</v-clicks>

</div>
</div>

---

# The Full Training Loop

<div class="flex justify-center items-start mt-2" style="padding-top:0.5rem;">
<img src="/figures/diamond-training-loop.png" class="rounded-lg" style="max-height:68vh; max-width:90%;" />
</div>

---

# Dreaming the Policy Update

<div class="flex justify-center items-start mt-2" style="padding-top:0.5rem;">
<img src="/figures/diamond-rollout-timeline.png" class="rounded-lg" style="max-height:68vh; max-width:90%;" />
</div>

---

# Training in Numbers

<div class="grid grid-cols-2 gap-4 mt-3 text-sm">
<div>

<v-clicks>

<div class="card mb-2">
<strong>Data budget:</strong> 100K real environment steps per game (≈ 2 hours of gameplay). The classic "Atari 100K" benchmark.
</div>

<div class="card mb-2">
<strong>Denoiser loss:</strong> L2 between D_θ(x_σ; σ) and the clean frame, weighted by EDM uncertainty weighting.
</div>

<div class="card mb-2">
<strong>Reward &amp; termination:</strong> a small CNN-LSTM trained on the same buffer, separately from the denoiser.
</div>

</v-clicks>

</div>
<div>

<v-clicks>

<div class="teal-card mb-2">
<strong>Actor-critic:</strong> REINFORCE with value baseline + <strong>λ-returns Bellman target</strong>. γ = 0.985, λ = 0.95. Horizon = 15 imagined steps.
</div>

<div class="teal-card mb-2">
<strong>Optimizer:</strong> AdamW, lr = 1e-4, batch 32. 400 grad steps per epoch, 100 real steps per epoch.
</div>

<div class="accent-card">
<strong>Total wall-clock:</strong> ~2.9 days per game on <em>a single RTX 4090</em>. No cluster needed.
</div>

</v-clicks>

</div>
</div>

---

# DIAMOND vs IRIS on Atari 100K

<div class="flex justify-center items-start mt-2" style="padding-top:0.5rem;">
<img src="/figures/diamond-vs-iris-results.png" class="rounded-lg" style="max-height:68vh; max-width:90%;" />
</div>

---

# The Headline Numbers

<div class="grid grid-cols-2 gap-4 mt-3 text-sm">
<div>

<div class="card mb-3">

| Metric | IRIS (2023) | DIAMOND (2024) |
|---|---|---|
| Mean HNS | 1.05 | **1.46** |
| Asterix | 853 | **3698** |
| Breakout | 83 | **132** |
| Road Runner | 9614 | **20673** |

</div>

</div>
<div>

<v-clicks>

<div class="teal-card mb-2">
<strong>Asterix:</strong> 4.3× better. This is the archetypal case — tiny sprites carry reward, and IRIS's tokenizer blurs them into the background.
</div>

<div class="accent-card mb-2">
<strong>Smaller model:</strong> DIAMOND's denoiser is ~4.4M parameters vs IRIS's ~100M transformer + tokenizer. Continuous pixel-space is more parameter-efficient <em>when details matter</em>.
</div>

<div class="card">
<strong>Same budget, better policy.</strong> Both use 100K real env steps. The difference is <em>entirely</em> in how the world model represents the frame.
</div>

</v-clicks>

</div>
</div>

---

# Scaling Up: DIAMOND on CS:GO

<div class="flex justify-center items-start mt-2" style="padding-top:0.5rem;">
<img src="/figures/diamond-csgo.png" class="rounded-lg" style="max-height:68vh; max-width:90%;" />
</div>

---

# The Recipe Transfers

<div class="grid grid-cols-2 gap-6 mt-3 text-sm">
<div>

<v-clicks>

<div class="card mb-2">
<strong>Same recipe, 80× bigger.</strong> Two-stage diffusion: a 330M <em>dynamics</em> model at 56×30 + a 51M <em>upsampler</em> to 280×150. Still EDM, still 3 denoising steps at the dynamics stage.
</div>

<div class="card mb-2">
<strong>Data:</strong> 87 hours of human Counter-Strike: Global Offensive deathmatch gameplay (~5.5M frames, action-labeled mouse + keyboard).
</div>

</v-clicks>

</div>
<div>

<v-clicks>

<div class="teal-card mb-2">
<strong>Training:</strong> 12 days on a <em>single RTX 4090</em>. Inference: <strong>10 FPS real-time</strong> on an RTX 3090 — players actually walk around, aim, shoot, open doors inside the neural world model.
</div>

<div class="accent-card">
<strong>The message:</strong> DIAMOND isn't an Atari trick. The same pixel-space diffusion recipe scales from 4.4M to 381M parameters and produces a playable 3D FPS — a strong signal that diffusion world models generalize.
</div>

</v-clicks>

</div>
</div>

---

# What DIAMOND Teaches Us

<div class="grid grid-cols-2 gap-6 mt-4 text-sm">
<div>

<v-clicks>

<div class="card mb-2">
<strong>1. Tokenization is a choice, not a law.</strong> IRIS tokenized because transformers ate discrete sequences well. DIAMOND shows you can drop that step entirely.
</div>

<div class="card mb-2">
<strong>2. Loss design beats architecture.</strong> The magic isn't the U-Net — it's EDM preconditioning. Same U-Net with DDPM would need 16+ steps and wouldn't reach SOTA.
</div>

<div class="card mb-2">
<strong>3. Details are not cosmetic.</strong> In sparse-reward games, a 1-pixel sprite <em>is</em> the reward signal. Preserving pixels is a fundamental requirement, not a visual bonus.
</div>

</v-clicks>

</div>
<div>

<v-clicks>

<div class="teal-card mb-2">
<strong>4. Step count is a trade-off lever.</strong> 1 step = mode averaging (blur). 3 steps = mode selection (sharp). More steps = diminishing returns. Tune this per task.
</div>

<div class="teal-card mb-2">
<strong>5. Small world models still work.</strong> You do not need a 14B backbone for a 64×64 pixel environment. A 4M-parameter conv net is enough.
</div>

<div class="accent-card">
<strong>The trajectory:</strong> DINO-WM showed <em>latents</em> are enough for planning. IRIS showed <em>tokens</em> are enough for dream RL. DIAMOND shows <em>pixels themselves</em> are enough — and they're sometimes necessary.
</div>

</v-clicks>

</div>
</div>

---

# What DIAMOND Can't Do (Yet)

<div class="grid grid-cols-2 gap-6 mt-4 text-sm">
<div>

<v-clicks>

<div class="card mb-2">
<strong>Action labels required.</strong> Every training trajectory must come with actions. DIAMOND can't use unlabeled internet video directly.
</div>

<div class="card mb-2">
<strong>Short context.</strong> Only the last 4 frames are used. Long-horizon physics (a ball rolling off-screen and returning) is weak.
</div>

</v-clicks>

</div>
<div>

<v-clicks>

<div class="card mb-2">
<strong>Per-game training.</strong> Unlike DreamZero, there's no internet pre-training. Every new game/environment starts from scratch.
</div>

<div class="card mb-2">
<strong>Compute per rollout.</strong> 3 denoising steps × 15 rollout steps = 45 net forward passes per imagined trajectory. Real-robot inference is still expensive.
</div>

</v-clicks>

<v-click>

<div class="teal-card mt-2">
Part 2 of this lecture covers two answers: <strong>LeWorld</strong> (tiny end-to-end JEPA) and <strong>DreamZero</strong> (joint world-action models with internet pre-training).
</div>

</v-click>

</div>
</div>

---

# Quiz: DIAMOND

<div class="text-sm">

**Q:** Why does DIAMOND use 3 denoising steps per frame instead of 1?

<v-clicks>

**A.** Because 1-step diffusion is computationally cheaper

**B.** Because 1-step diffusion produces the *mean* of the conditional distribution (blur), while 3 steps iteratively commit to a single mode (sharp), preserving the details that carry reward

**C.** Because EDM requires at least 3 steps mathematically

**D.** Because the U-Net can't handle high noise levels

</v-clicks>

<v-click>

<div class="accent-card mt-4">
<strong>A:</strong> (B). Single-step sampling returns the conditional mean of next-frame distributions, which on stochastic tasks like Atari <em>Boxing</em> produces ghost-copy blur. Iterative sampling lets the denoiser collapse to one particular mode per rollout, keeping pixels sharp. Across many rollouts, stochasticity is preserved at the <em>trajectory</em> level rather than inside a single frame. 3 is the empirical sweet spot — any more steps give diminishing returns.
</div>

</v-click>

</div>

---

<div style="height:1px;"></div>


---
layout: center
---

# Part 6

## Building a World Model from Scratch

<div class="mt-4 opacity-60">The complete pipeline — with real code and real numbers</div>

---

# The Full Pipeline

<div class="flex justify-center items-start mt-2" style="padding-top:0.5rem;">
<img src="/figures/wfm-full-pipeline.png" class="rounded-lg" style="max-height:68vh; max-width:90%;" />
</div>

---

# Phase 1: Data — You Need Lots of Video

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### Sources (2.3 TB total)

<v-clicks>

<div class="card text-sm mb-2">
<strong>Kinetics-700:</strong> 754 GB
<br>Human activities — cooking, sports, daily life
</div>

<div class="card text-sm mb-2">
<strong>Bridge V2:</strong> 443 GB
<br>Robot manipulation — pick, place, push
</div>

<div class="card text-sm mb-2">
<strong>Open X-Embodiment:</strong> 1.1 TB
<br>Multi-robot, multi-task manipulation data
</div>

</v-clicks>

</div>
<div>

<v-click>

### Filtering Pipeline

<div class="accent-card text-sm">

**1.67M raw clips → 1.44M curated clips**

1. **Motion filter** — remove static clips (no movement)
2. **Aesthetics filter** — remove low-quality frames
3. **Text overlay filter** — remove watermarked/annotated clips
4. **Captioning** — Qwen2.5-VL-7B generates descriptions for each clip

**Result:** 1.44M high-quality, captioned video clips ready for training.

**Total compute cost: ~$50** on RunPod H100s.

</div>

</v-click>

</div>
</div>

---

# Phase 2: Video Tokenizer

<div class="flex justify-center items-start mt-2" style="padding-top:0.5rem;">
<img src="/figures/video-tokenizer-compression.png" class="rounded-lg" style="max-height:52vh; max-width:85%;" />
</div>

<v-click>

<div class="grid grid-cols-2 gap-4 mt-3">
<div class="teal-card text-sm">
<strong>Why tokenize?</strong> Raw video is too large for Transformers. 25 frames × 256×256 × 3 = 5 MB per clip. We need 38× compression to make training feasible.
</div>
<div class="accent-card text-sm">
<strong>NVIDIA Cosmos CV8×8×8:</strong> Compresses 8× in time, 8× in height, 8× in width. Latent shape: [1, 16, 4, 32, 32]. Quality: 34-41 dB PSNR (near-lossless).
</div>
</div>

</v-click>

---

# The Tokenizer Journey

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### From Scratch Attempt

<v-clicks>

<div class="card text-sm mb-3">
<strong>We built a custom tokenizer:</strong>
- ~105M parameters
- Trained for 50K iterations on 2× A100
- **Result: 17.34 dB PSNR, 0.737 SSIM**
- Cost: ~$19
- Curve still rising — needed 250K+ iterations
</div>

<div class="accent-card text-sm">
<strong>The lesson:</strong> Building a video tokenizer from scratch requires significant compute. The loss was still decreasing — we'd need 5-10× more training.
</div>

</v-clicks>

</div>
<div>

<v-click>

### The Pivot: Pretrained Cosmos

<div class="teal-card text-sm mb-3">
<strong>NVIDIA's pretrained tokenizer:</strong>
- 408 MB model (freely downloadable)
- **OXE data: 40.77 dB / 0.9834 SSIM**
- **Bridge V2: 34.38 dB / 0.9442 SSIM**
- Far exceeds our 30 dB target!
</div>

<div class="blue-card text-sm">
<strong>Pre-tokenization results:</strong>
- Bridge V2: 39,553 latents (4.9 GB)
- OXE: 201,657 latents (~24 GB)
- **Total: 241,210 latents (~29 GB)**
- Each latent: ~132 KB (vs. ~5 MB raw)

Stored on Backblaze B2 — ready for Phase 3.
</div>

</v-click>

</div>
</div>

---

# Phase 3: Diffusion World Model (DiT)

<div class="flex justify-center items-start mt-2" style="padding-top:0.5rem;">
<img src="/figures/dit-architecture.png" class="rounded-lg" style="max-height:68vh; max-width:90%;" />
</div>

---

# The DiT Architecture in Detail

<div class="mt-2">

<v-clicks>

<div class="grid grid-cols-2 gap-4">
<div class="accent-card text-sm mb-3">
<h3>3D Patchify</h3>
Latent [1, 16, 4, 32, 32] → divide into 3D patches of (1, 2, 2) → 2048 patch tokens. Each patch = a small spatiotemporal cube.
</div>
<div class="teal-card text-sm mb-3">
<h3>3D RoPE</h3>
Rotary Position Encoding extended to 3D: encodes (time, height, width) position for each token. The model knows WHERE each patch is in space and time.
</div>
</div>

<div class="grid grid-cols-2 gap-4">
<div class="blue-card text-sm mb-3">
<h3>AdaLN-LoRA</h3>
Adaptive Layer Norm with Low-Rank Adaptation. Conditions each transformer layer on the noise level σ — tells the model how noisy the input is and what scale of detail to predict.
</div>
<div class="purple-card text-sm mb-3">
<h3>Cross-Attention to Text</h3>
Frozen T5 encoder converts captions to embeddings. Cross-attention injects text conditioning into every layer — the model learns to generate video matching the text description.
</div>
</div>

</v-clicks>

<v-click>

<div class="card mt-2 text-sm text-center">
<strong>Total: 1.56B parameters</strong> — 16 layers, d=2048, 16 attention heads, QK-normalization, SwiGLU MLP.
</div>

</v-click>

</div>

---

# Training: EDM Framework

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### How Diffusion Training Works

<v-clicks>

<div class="card text-sm mb-3">
<strong>EDM (Elucidated Diffusion Models):</strong>

1. Take a clean video latent $x$
2. Sample noise level $\sigma \sim \text{LogNormal}(-1.2, 1.2^2)$
3. Add Gaussian noise: $x_\sigma = x + \sigma \cdot \epsilon$
4. Train model to predict the noise: $\hat{\epsilon} = D(x_\sigma, \sigma, \text{caption})$
5. Loss: weighted MSE with uncertainty weighting
</div>

<div class="accent-card text-sm">
<strong>Key trick: Video noise √T scaling</strong>
<br>The noise level is scaled by $\sqrt{T}$ where T is the number of frames. This ensures temporal consistency — without it, the model treats each frame independently and generates flickery video.
</div>

</v-clicks>

</div>
<div>

<v-click>

### PoC Results

<div class="teal-card text-sm mb-3">
<strong>Proof-of-Concept training:</strong>
- **500 steps** on single A100
- Loss: **3.06 → 0.65** (converging!)
- Speed: **4.04 iterations/second**
- VRAM: **16.1 GB** (batch=2)
- Architecture is correct and learning

</div>

<div class="blue-card text-sm">
<strong>Bugs fixed along the way:</strong>
- TimestepEmbed dtype mismatch (float32 vs bfloat16)
- RoPE dim%6 assertion (use 21 pairs/axis, not 22)
- EDM preconditioning dtype precision
- Memory: activation checkpointing essential

<br>
<strong>Building from scratch is hard!</strong> But it teaches you everything.
</div>

</v-click>

</div>
</div>

---

# Interactive: WFM Showcase

<iframe src="https://wfm-showcase.vercel.app/" class="w-full rounded-lg mt-1" style="height:72vh;border:none;" />

---

# From Video Model to Robot World Model

<div class="mt-4">

<v-clicks>

<div class="grid grid-cols-3 gap-4">
<div class="card text-sm">
<h3>Step 1: Video Pre-training</h3>
Train on massive internet video + robot video. Learn general physics, object interactions, scene dynamics. (This is what we've done in Phase 3.)
</div>
<div class="accent-card text-sm">
<h3>Step 2: Action Conditioning</h3>
Add action embeddings to the model. Concatenate with the latent input. Fine-tune on robot data where actions are available. Now: $\hat{x}_{t+1} = D(x_t, a_t, \sigma, \text{text})$
</div>
<div class="teal-card text-sm">
<h3>Step 3: Robot Fine-tuning</h3>
Fine-tune on target robot embodiment (e.g., SO-101 data). The pre-trained video understanding transfers. Small dataset is enough.
</div>
</div>

<div class="accent-card mt-4 text-sm text-center">
<strong>This is the DreamZero strategy in practice:</strong> Pre-train on everything → add actions → fine-tune on your robot. The video pre-training provides a world understanding that transfers to any embodiment.
</div>

</v-clicks>

</div>

---

# What We Learned Building This

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### Hard Lessons

<v-clicks>

<div class="card text-sm mb-3">
<strong>Data is 80% of the work.</strong> Downloading, splitting, filtering, captioning 2.3 TB of video took weeks. The model training is the easy part.
</div>

<div class="card text-sm mb-3">
<strong>Tokenizer quality matters enormously.</strong> Our from-scratch tokenizer at 17 dB would have made the diffusion model useless. The pretrained Cosmos at 34-41 dB made everything work.
</div>

<div class="card text-sm">
<strong>dtype bugs are deadly.</strong> Three separate dtype issues caused NaN losses that looked like architecture bugs. Always check your dtypes (float32 vs bfloat16 mixing).
</div>

</v-clicks>

</div>
<div>

<v-click>

### Honest Assessment

<div class="accent-card text-sm">

**What worked:**
- Architecture is correct (loss converges)
- Pre-tokenization saved enormous compute
- The PoC validated the approach in <500 steps

**What's next:**
- Extended training: 10K-50K steps
- T5 caption pre-encoding for efficiency
- Stage 1 full training: 200K iterations on 8× H100
- Action conditioning for robot control
- Evaluation: FVD, FID, IS metrics

**Total project cost so far: ~$90** (data + tokenizer + PoC)

</div>

</v-click>

</div>
</div>

---

<div style="height:1px;"></div>

---
layout: center
---

# Recap & The Road Ahead

---

# The World Models We Covered

<div class="flex justify-center items-start mt-2" style="padding-top:0.5rem;">
<img src="/figures/world-models-summary-comparison.png" class="rounded-lg" style="max-height:68vh; max-width:90%;" />
</div>

---

# The Narrative Arc

<div class="mt-2">

<v-clicks>

<div class="grid grid-cols-4 gap-3">
<div class="teal-card text-sm text-center" style="padding:10px;">
<strong>DINO-WM</strong>
<br><span class="opacity-70">Predict in feature space</span>
<br>→ errors compound
</div>
<div class="accent-card text-sm text-center" style="padding:10px;">
<strong>IRIS</strong>
<br><span class="opacity-70">World as language model</span>
<br>→ tokens blur details
</div>
<div class="blue-card text-sm text-center" style="padding:10px;">
<strong>DIAMOND</strong>
<br><span class="opacity-70">Diffusion in pixels</span>
<br>→ per-game, action-labelled
</div>
<div class="card text-sm text-center" style="padding:10px; border:2px solid var(--claude-accent);">
<strong>Your WFM</strong>
<br><span class="opacity-70">Build from scratch</span>
<br>→ the frontier!
</div>
</div>

</v-clicks>

<v-click>

<div class="accent-card mt-4 text-sm">
<strong>Each model solved the previous one's limitation:</strong>
- DINO-WM's compounding errors → IRIS trains in imagination, no multi-step rollout needed
- IRIS's lossy tokenizer blurs details → DIAMOND keeps pixels and uses EDM diffusion
- DIAMOND still needs action labels and trains per-game → <strong>Part 2</strong> covers LeWorld &amp; DreamZero
- All of them limited by training data → Diffusion WFM scales to internet video
</div>

</v-click>

</div>

---

# What We Didn't Cover (Future Lectures)

<div class="grid grid-cols-3 gap-4 mt-4">

<div class="card text-sm">
<h3>DreamerV3</h3>
Recurrent State-Space Model (RSSM). Imagination-based RL. First to get diamonds in Minecraft from scratch. 150+ tasks with one set of hyperparameters.
</div>

<div class="card text-sm" style="border:2px solid var(--claude-accent);">
<h3>→ Part 2: LeWorld &amp; DreamZero</h3>
The natural follow-ups to DIAMOND: LeWorld (tiny end-to-end JEPAs from pixels) and DreamZero (14B joint world-action models trained on internet video). Separate deck.
</div>

<div class="card text-sm">
<h3>TD-MPC2</h3>
Implicit world model + MPC. No reconstruction — just latent planning. 300+ pre-trained checkpoints. Completely different philosophy.
</div>

<div class="card text-sm">
<h3>V-JEPA 2</h3>
LeCun's non-generative world model. Predicts in abstract latent space, not pixels. Transfers zero-shot to real robots with 62 hours of data.
</div>

<div class="card text-sm">
<h3>Oasis</h3>
Neural game engine. A diffusion transformer generates Minecraft gameplay in real time from keyboard inputs. The entire "game engine" is a neural network.
</div>

<div class="card text-sm">
<h3>Genie 3</h3>
DeepMind's text-to-world model. Generates interactive 3D environments from text descriptions. The next frontier of world models.
</div>

</div>

---

# Your Toolkit

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### Notebooks

<div class="notebook-card text-sm mb-3">

- **DINO World Model from Scratch** — Ball Arena, CEM planning, PCA analysis
- **IRIS World Model from Scratch** — Catch env, VQ-VAE, GPT world model, dream RL
- **DIAMOND from Scratch** — Atari Breakout, EDM U-Net denoiser, 3-step dream rollouts
- **DINO-WM on Push-T** — Real LeRobot data, 40 expert episodes

</div>

### Interactive Visualizations

<div class="teal-card text-sm">

- [IRIS World Model Architecture](https://iris-world-model-visualizer.vercel.app)
- [DINO Transformer Predictor](https://dino-transformer-predictor-visualiz.vercel.app)
- [VQ-VAE Decoder](https://vqvae-decoder-visualizer.vercel.app)
- [WFM Showcase](https://wfm-showcase.vercel.app)

</div>

</div>
<div>

### Code to Explore

<div class="card text-sm mb-3">

**WFM Codebase (in this repo):**
- `cosmos_tokenizer/` — Video tokenizer (custom + pretrained)
- `diffusion_wfm/` — 1.56B DiT world model
- `scripts/` — Data filtering pipeline

</div>

### Papers to Read

<div class="accent-card text-sm">

1. **DINO-WM** — Ding et al., 2024
2. **IRIS** — Micheli et al., ICLR 2023
3. **DIAMOND** — Alonso et al., NeurIPS 2024 (spotlight)
4. **EDM** — Karras et al., NeurIPS 2022 (preconditioning)
5. **Cosmos** — NVIDIA, 2025
6. *Part 2:* **LeWorld** &amp; **DreamZero**

</div>

</div>
</div>

---

# Final Quiz: The Big Picture

<div class="quiz-card mt-4">

### Question

A startup wants to build a general-purpose robot brain that can handle many tasks. They have: (a) 100 hours of internet cooking videos, (b) 5 hours of their robot doing pick-and-place. Which approach should they use?

<v-clicks>

**A.** Train DINO-WM on the 5 hours of robot data (action-conditioned, no internet video)

**B.** Train IRIS on the 5 hours of robot data (dream RL, but limited data)

**C.** Pre-train a video world model on 100 hours of cooking video, then fine-tune with actions on 5 hours of robot data (DreamZero/WAM approach)

</v-clicks>

<v-click>

<div class="mt-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> (C). This is the DreamZero approach. The 100 hours of cooking video teaches the world model about object physics, pouring, grasping, and spatial relationships — <em>without any action labels</em>. Then the 5 hours of robot data teaches the action head how the specific robot moves. The pre-trained world understanding transfers. Options A and B can only use the 5 hours, wasting 100 hours of valuable physics knowledge.
</div>

</v-click>

</div>

---
layout: center
---

# The Best Way to Understand World Models...

<div class="mt-6">
<h2 style="color:var(--claude-accent) !important; font-size:2em !important;">...is to build one.</h2>
</div>

<div class="mt-8">
<span class="opacity-60">You now have the theory, the code, and the notebooks. Start dreaming.</span>
</div>

<div class="mt-8 flex gap-4 justify-center">
<a href="https://vizuara.ai" target="_blank" class="text-sm px-4 py-2 rounded-lg" style="background:var(--claude-accent);color:#fff;text-decoration:none;">
  vizuara.ai
</a>
</div>
