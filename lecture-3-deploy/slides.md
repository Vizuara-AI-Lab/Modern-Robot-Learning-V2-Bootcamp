---
theme: default
title: "From VLAs to Real Robots: SmolVLA, Flow Matching & SO-101 Deployment"
info: |
  Lecture 3 — Modern Robot Learning from Scratch V2 Bootcamp
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
.slidev-layout {
  background: var(--claude-bg) !important;
  color: var(--claude-text) !important;
  overflow-y: auto;
  max-height: 100vh;
}
/* Vizuara logo on every slide */
.slidev-layout::after {
  content: '';
  position: absolute;
  top: 14px;
  right: 18px;
  width: 90px;
  height: 28px;
  background: url('/vizuara-logo.png') no-repeat center / contain;
  opacity: 0.3;
  pointer-events: none;
  z-index: 10;
}
/* Headings — Caveat handwritten font */
.slidev-layout h1 { font-family: 'Caveat', cursive !important; color: var(--claude-accent) !important; font-size: 2.1em !important; font-weight: 700 !important; line-height: 1.2 !important; }
.slidev-layout h2 { font-family: 'Caveat', cursive !important; color: var(--claude-warm) !important; font-size: 1.5em !important; font-weight: 600 !important; }
.slidev-layout h3 { font-family: 'Caveat', cursive !important; color: var(--claude-teal) !important; font-size: 1.25em !important; font-weight: 600 !important; }
/* Links */
.slidev-layout a { color: var(--claude-blue) !important; }
/* Code */
.slidev-layout code { background: var(--claude-surface) !important; color: var(--claude-text) !important; border: 1px solid var(--claude-border); }
.slidev-layout pre { background: var(--claude-surface) !important; border: 1px solid var(--claude-border); border-left: 3px solid var(--claude-accent); border-radius: 0 8px 8px 0 !important; }
.slidev-layout pre code { color: var(--claude-text) !important; background: transparent !important; border: none !important; }
.slidev-layout pre .line span { color: var(--claude-text) !important; }
.shiki, .shiki span { color: var(--claude-text) !important; }
/* Blockquotes */
.slidev-layout blockquote { border-left: 3px solid var(--claude-accent); background: var(--claude-surface); padding: 8px 12px; border-radius: 0 8px 8px 0; }
/* Tables */
.slidev-layout table { border-collapse: collapse; width: 100%; }
.slidev-layout th { background: var(--claude-surface); color: var(--claude-accent); padding: 6px 10px; border-bottom: 2px solid var(--claude-accent); font-family: 'Caveat', cursive; font-size: 1.1em; }
.slidev-layout td { padding: 4px 10px; border-bottom: 1px solid var(--claude-border); }
/* Strong text */
.slidev-layout strong { color: var(--claude-warm); }
/* Cards */
.card { background: var(--claude-card); border-radius: 12px; padding: 16px; border: 1px solid var(--claude-border); }
.accent-card { background: rgba(194,120,92,0.06); border-radius: 12px; padding: 16px; border: 1px solid rgba(194,120,92,0.25); }
.teal-card { background: rgba(106,154,91,0.06); border-radius: 12px; padding: 16px; border: 1px solid rgba(106,154,91,0.25); }
.blue-card { background: rgba(90,127,165,0.06); border-radius: 12px; padding: 16px; border: 1px solid rgba(90,127,165,0.25); }
.purple-card { background: rgba(138,107,170,0.06); border-radius: 12px; padding: 16px; border: 1px solid rgba(138,107,170,0.25); }
.quiz-card { background: rgba(138,107,170,0.06); border-radius: 12px; padding: 16px; border: 2px solid var(--claude-purple); }
.brainstorm-card { background: var(--claude-surface); border-radius: 12px; padding: 32px; border: 2px dashed var(--claude-warm); min-height: 280px; display: flex; align-items: center; justify-content: center; }
.notebook-card { background: rgba(90,127,165,0.06); border-radius: 12px; padding: 16px; border: 1px solid rgba(90,127,165,0.25); }
.highlight { color: var(--claude-accent); font-weight: 600; }
.inline-video { border-radius: 12px; overflow: hidden; }
</style>

# From VLAs to Real Robots

## SmolVLA, Flow Matching & SO-101 Deployment

<div class="pt-8">
  <span class="px-4 py-2 rounded-lg text-lg" style="background:#c2785c;color:#fff;font-weight:700;">
    Modern Robot Learning from Scratch — V2
  </span>
</div>

<div class="pt-4 opacity-60">
  Lecture 3 — Vizuara Bootcamp
</div>

<div class="abs-br m-6 flex gap-2">
  <a href="https://vizuara.ai" target="_blank" class="text-sm opacity-50 hover:opacity-100">
    vizuara.ai
  </a>
</div>



---

<div style="height:1px;"></div>

---

<div style="height:1px;"></div>


---

<div style="height:1px;"></div>


---

<div style="height:1px;"></div>


---

<div style="height:1px;"></div>


---

<div style="height:1px;"></div>


---

<div style="height:1px;"></div>


---

<div style="height:1px;"></div>


---

<div style="height:1px;"></div>

---
layout: center
---

# What You'll Learn Today

<div class="grid grid-cols-3 gap-3 mt-4 text-left text-sm">

<div class="accent-card">

### Part 1: Open-Source VLAs
From pi0 to **OpenVLA** and **SmolVLA** — two architectures you can actually run yourself.
</div>

<div class="teal-card">

### Part 2: Flow Matching from Scratch
The secret behind pi0 and SmolVLA — a **simpler, faster** alternative to DDPM.
</div>

<div class="blue-card">

### Part 3: Meet the SO-101
A **$100 robot arm** you can build at home. Assembly, calibration, cameras — from the box to first motion.
</div>

</div>

<div class="grid grid-cols-2 gap-3 mt-3 text-left text-sm">

<div class="purple-card">

### Part 4: Deploy a VLA on Real Hardware
Record demonstrations → train SmolVLA → run it on your robot. The **full pipeline**.
</div>

<div class="card" style="border: 2px solid var(--claude-accent);">

### Part 5: Live Demo
Watch SmolVLA control an SO-101 arm to **pick up a red cube** — trained from just 50 demonstrations.
</div>

</div>

---

<div style="height:1px;"></div>

---
layout: section
---

# First — A Quick Recap
## What Is a VLA? What Did We Learn in Lecture 2?

---

# Recap: The Journey from Lecture 2

In Lecture 2, we built a **Vision-Language-Action** model from scratch. Here's the path we took:

<v-clicks>

<div class="card mt-3 mb-2 text-center text-sm">

**Step 1:** We built a **mini-VLA** — CNN + GRU + Diffusion duct-taped together. It worked on training data but **failed everywhere else**.

</div>

<div class="card mb-2 text-center text-sm">

**Step 2:** We learned **Transformers from scratch** — self-attention, multi-head, positional encoding. The architecture that fixes the bottleneck.

</div>

<div class="card mb-2 text-center text-sm">

**Step 3:** We learned **Vision Transformers (ViT)** — images as patch sequences, global attention replaces local CNNs.

</div>

<div class="card mb-2 text-center text-sm">

**Step 4:** We combined ViT + LLM → **Vision-Language Model (VLM)** — a model that sees AND understands.

</div>

<div class="accent-card text-center text-lg">

**Step 5:** VLM + Action Expert = **VLA** — a robot that understands the world and acts in it.

</div>

</v-clicks>

---

# What IS a VLA?

<div v-click>
<img src="/figures/vla-recap-diagram.png" class="rounded-lg mx-auto" style="max-height:28vh; max-width:85%;" />
</div>

<v-clicks>

<div class="grid grid-cols-3 gap-3 mt-3 text-sm">

<div class="blue-card text-center">

### V = Vision
Camera images → ViT / SigLIP → visual tokens

The robot **sees** the workspace

</div>

<div class="accent-card text-center">

### L = Language
"Pick up the red cup" → Tokenizer + LLM → language tokens

The robot **understands** instructions

</div>

<div class="teal-card text-center">

### A = Action
Fused understanding → Action Head → joint angles

The robot **moves** to accomplish the task

</div>

</div>

</v-clicks>

<div v-click class="mt-3 purple-card text-center text-sm">

We saw two VLA approaches in Lecture 2: **RT-2** (actions as tokens, 55B) and **pi0** (diffusion-based action expert, 3.3B). Both were closed systems. **Today: open-source VLAs you can actually run.**

</div>

---

<div style="height:1px;"></div>

---
layout: section
---

# Part 1
## Open-Source VLAs — OpenVLA & SmolVLA

---

# The Open-Source Moment

Something remarkable happened in 2024–2025:

<v-clicks>

<div class="card mt-3 mb-2 text-sm">

### The Problem Before
RT-2 required **55 billion parameters** and Google's proprietary data. Pi0 required Physical Intelligence's internal data and compute. You could *read* the papers, but you couldn't *run* the models.

</div>

<div class="teal-card mb-2 text-sm">

### OpenVLA (Stanford/Berkeley, June 2024)
**7B parameters**, fully open-source, trained on Open X-Embodiment data. You can download it, fine-tune it, and run it. Uses the **action tokenization** approach (like RT-2).

</div>

<div class="blue-card mb-2 text-sm">

### SmolVLA (HuggingFace, 2025)
**450M parameters** — small enough to run on a laptop. Uses **flow matching** (like pi0). Designed for the LeRobot ecosystem. Open weights, open data, open code.

</div>

<div class="accent-card text-center">

**Two open-source VLAs, two fundamentally different approaches.** Let's understand both — starting with OpenVLA.

</div>

</v-clicks>

---

# OpenVLA: Architecture Overview

<div class="grid grid-cols-2 gap-6 mt-3">

<div>

<v-clicks>

<div class="card mb-3 text-sm">

### Three Components

1. **Dual Vision Encoder**: SigLIP (400M) + DinoV2 (300M)
2. **Projector**: 2-layer MLP → maps visual features into LLM space
3. **Language Backbone**: Llama 2 7B — the autoregressive decoder

</div>

<div class="accent-card text-sm">

### The Key Idea

Treat action prediction as **language modeling**. The robot's joint angles become "words" in a vocabulary.

**Input:** Image tokens + "pick up the red cup"
**Output:** "147 52 230 89 12 201 155" (7 action tokens)

</div>

</v-clicks>

</div>

<div v-click>

<img src="/figures/openvla-architecture.png" class="rounded-lg" style="max-height:50vh; max-width:100%;" />

</div>

</div>

---

# What Is SigLIP? (Quick Recap from Lecture 2)

You learned SigLIP in Lecture 2 as part of pi0. Here's the key idea:

<v-clicks>

<div class="card mt-3 mb-3 text-sm">

### Contrastive Learning on Image-Text Pairs

SigLIP is trained on **billions** of (image, caption) pairs from the internet. For each pair:
- Encode the image with a ViT → image embedding
- Encode the caption with a text encoder → text embedding
- **Matching** pairs should have high cosine similarity
- **Non-matching** pairs should have low similarity

After training, the vision encoder **understands concepts**: it knows "cup" means cup, "red" means red, regardless of angle or lighting.

</div>

<div class="accent-card text-center text-sm">

**SigLIP gives the robot semantic understanding.** It tells the robot *what* things are. But it's trained to match global image-text pairs — it can lose fine **spatial details** like exact pixel positions.

</div>

</v-clicks>

---

# What Is DinoV2? — The Missing Piece

DinoV2 is something we **haven't** covered yet. It's a fundamentally different kind of vision encoder.

<v-clicks>

<div class="grid grid-cols-2 gap-4 mt-3">

<div class="blue-card text-sm">

### How DinoV2 Is Trained

**Self-supervised** — no text captions at all! Only images.

The training trick: take an image, create two different **augmented views** (crop, rotate, color shift). Train the ViT so both views produce the **same** representation.

This forces the network to learn **geometric invariances** — edges, shapes, spatial layout, object boundaries — because those features are preserved across augmentations.

</div>

<div class="teal-card text-sm">

### What DinoV2 Learns

Without any text labels, DinoV2 discovers:
- **Object boundaries** — precise pixel-level segmentation
- **Spatial layout** — where things are relative to each other
- **Geometric features** — corners, edges, surface normals
- **Depth cues** — relative distances from the camera

It doesn't know a "cup" is called a "cup" — but it knows **exactly where the cup's edge is** down to the pixel.

</div>

</div>

</v-clicks>

---

# SigLIP vs DinoV2: Why OpenVLA Needs BOTH

<div v-click>
<img src="/figures/siglip-vs-dinov2.png" class="rounded-lg mx-auto" style="max-height:32vh; max-width:85%;" />
</div>

<v-clicks>

<div class="grid grid-cols-2 gap-4 mt-2 text-sm">

<div class="blue-card">

### SigLIP Alone
"There's a red cup somewhere in the image."

Knows **what** to grab but is fuzzy about **where exactly** the handle is. Features are aligned with language (great for understanding instructions) but spatially coarse.

</div>

<div class="teal-card">

### DinoV2 Alone
"There's an object with a handle at pixel (312, 247)."

Knows **where** every edge is but doesn't know "cup" from "vase." Precise spatial features but no language grounding.

</div>

</div>

<div class="accent-card mt-2 text-center text-sm">

**Together: "There's a red cup, and its handle is at pixel (312, 247)."** SigLIP provides the *what*, DinoV2 provides the *where*. OpenVLA **concatenates** their patch features channel-wise before projecting into Llama's space.

</div>

</v-clicks>

---

# How the Dual Encoder Works — Step by Step

<v-clicks>

<div class="card mt-3 mb-2 text-sm">

### Step 1: Both encoders process the same image

Image (224×224) → SigLIP ViT → **256 patch tokens**, each 1152-d (semantic)
Image (224×224) → DinoV2 ViT → **256 patch tokens**, each 1024-d (spatial)

</div>

<div class="teal-card mb-2 text-sm">

### Step 2: Concatenate channel-wise

For each of the 256 patches, concatenate the SigLIP and DinoV2 features:
**Patch i → [SigLIP_i (1152-d) | DinoV2_i (1024-d)] = 2176-d per patch**

Now each patch carries both semantic AND spatial information.

</div>

<div class="blue-card mb-2 text-sm">

### Step 3: Project into LLM space

A 2-layer MLP maps each 2176-d concatenated patch → **4096-d** (Llama 2's hidden dimension).

These 256 projected tokens enter the Llama backbone alongside the language tokens.

</div>

<div class="accent-card text-center text-sm">

**The robot now sees with two eyes:** one that understands concepts (SigLIP) and one that understands geometry (DinoV2). Both feed into the same language model that makes decisions.

</div>

</v-clicks>

---

# OpenVLA: The Training Data — Open X-Embodiment

<div class="grid grid-cols-2 gap-6 mt-3">

<div>

<v-clicks>

<div class="card mb-3 text-sm">

### What Is Open X-Embodiment (OXE)?

A **massive collaborative dataset** from 21+ robotics labs worldwide:
- **970,000 robot trajectories**
- **22 different robot embodiments** (Franka, WidowX, Google Robot, UR5, ...)
- Tasks: pick, place, push, open drawer, pour, wipe, fold, ...
- All standardized to a common format

</div>

<div class="teal-card text-sm">

### Curation for OpenVLA

Not all OXE data is useful. OpenVLA curates:
- Only **manipulation** tasks (no navigation)
- At least one **3rd-person camera** view
- Only **single-arm** control (no bimanual)
- **7-DoF end-effector** actions (position + rotation + gripper)

After curation: ~970K trajectories, weighted to balance embodiments.

</div>

</v-clicks>

</div>

<div v-click>

<img src="/figures/oxe-dataset-samples.png" class="rounded-lg" style="max-height:50vh; max-width:100%;" />

</div>

</div>

---

# OpenVLA: How Exactly Is It Trained?

<v-clicks>

<div class="card mt-3 mb-2 text-sm">

### Step 1: Initialize from Prismatic VLM

Start with a **pre-trained VLM** (SigLIP + DinoV2 + Llama 2 7B) that already understands images and text from internet-scale pre-training. This is the foundation — the model can already "see" and "read."

</div>

<div class="teal-card mb-2 text-sm">

### Step 2: Add 256 action tokens to vocabulary

Take the **256 least-used tokens** in Llama's vocabulary and replace them with action bin IDs. Each bin represents a small range of a continuous action value.

Bin boundaries are set using **quantile statistics** (1st–99th percentile) from the training data — not uniform spacing.

</div>

<div class="blue-card mb-2 text-sm">

### Step 3: Fine-tune on robot data

Standard **next-token prediction** loss, but now some of the "next tokens" are **action tokens**:

Image tokens + "pick up the cup" + **[action_147] [action_52] [action_230] ...**

The model learns: "when I see this scene and hear this instruction, the next tokens should be these action bins."

</div>

<div class="accent-card text-center text-sm">

**64 A100 GPUs for 14 days** (21,500 A100-hours). Batch size 2,048. 27 epochs through the dataset.

</div>

</v-clicks>

---

# The Autoregressive Efficiency Problem

Here's where it gets concerning. Let's count the tokens.

<v-clicks>

<div class="card mt-3 mb-3 text-sm">

### Single-Step Actions (Original OpenVLA)

7 action dimensions × 1 token each = **7 tokens** per timestep, decoded **sequentially**.

Each token requires a **full forward pass** through Llama 2 7B. At ~50ms per pass on an A100:
7 × 50ms = **350ms per action** → max ~3 Hz. Usable but slow.

</div>

<div class="card mb-3 text-sm" style="border-left: 3px solid #D4543A;">

### What About Action Chunks? (The Scaling Nightmare)

If we wanted OpenVLA to predict 16-step action chunks (like Diffusion Policy):
16 steps × 7 dimensions = **112 tokens**, all decoded sequentially.

112 × 50ms = **5.6 seconds per chunk**. By the time the robot gets its plan, the world has moved on.

**This is why OpenVLA predicts only 1 timestep at a time** — and why it can't do action chunking.

</div>

<div class="accent-card text-center text-sm">

**Contrast with SmolVLA:** flow matching generates all 50 × 7 = 350 action values **simultaneously** in 10 Euler steps. Same information, but **parallel** instead of sequential. We'll see how shortly.

</div>

</v-clicks>

---

# Visualizing the Sequential Bottleneck

<div v-click>
<img src="/figures/openvla-sequential-bottleneck.png" class="rounded-lg mx-auto" style="max-height:48vh; max-width:90%;" />
</div>

<v-clicks>

<div class="grid grid-cols-2 gap-4 mt-2 text-sm">

<div class="card" style="border-left: 3px solid #D4543A;">

### OpenVLA: Sequential Tokens

**1 step:** 7 tokens × 50ms = 350ms (~3 Hz)
**16 steps (hypothetical chunk):** 112 tokens × 50ms = **5.6 seconds**

Each token requires a **complete 7B forward pass**. There's no way around it — autoregressive means "one at a time."

</div>

<div class="teal-card">

### SmolVLA: Parallel Flow Matching

**50 steps:** 10 Euler steps × 30ms = **300ms** total

All 350 action values (50 steps × 7 joints) are generated **simultaneously** in each Euler step. The 100M action expert processes everything in one pass.

</div>

</div>

<div class="accent-card mt-2 text-center text-sm">

**This is the fundamental architectural difference.** Autoregressive models generate actions like writing words one by one. Flow matching generates the entire trajectory at once, like seeing the whole path in a flash.

</div>

</v-clicks>

---

# OpenVLA: The Results

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

<div class="teal-card text-sm">

| Benchmark | RT-2-X (55B) | OpenVLA (7B) |
|-----------|:---:|:---:|
| BridgeData V2 | Baseline | **+16.5%** |
| New objects | Good | **Better** |
| New phrasing | Good | **Comparable** |
| LoRA fine-tune | N/A | **Works (1.4% params)** |

</div>

<div v-click class="blue-card mt-3 text-sm text-center">

**7x fewer parameters, better results.** The dual encoder (SigLIP + DinoV2) and diverse training data make the difference.

</div>

</div>

<div v-click>

<div class="card text-sm">

### What makes OpenVLA practical

1. **LoRA fine-tuning** — adapt to your robot by updating only **1.4%** of parameters
2. **4-bit quantization** — runs in **7GB VRAM** with zero performance loss
3. **Open weights** — download from HuggingFace, no license restrictions
4. **Common interface** — standard HuggingFace `AutoModelForVision2Seq`

</div>

<div class="accent-card mt-3 text-sm text-center">

**But the fundamental limits remain:** discrete actions (lossy), sequential decoding (slow), single-step prediction (no chunking). Can we do better?

</div>

</div>

</div>

---

<div style="height:1px;"></div>

---

# SmolVLA: The 450M Parameter VLA

<div class="grid grid-cols-2 gap-6 mt-3">

<div>

<v-clicks>

<div class="card mb-3 text-sm">

### Design Philosophy

Take the pi0 recipe (VLM + separate Action Expert + flow matching) and make it **tiny**:
- pi0: 3.3B parameters
- SmolVLA: **450M parameters** (7.3x smaller)

Small enough to run on a **single GPU** or even a Mac.

</div>

<div class="teal-card text-sm">

### Two Modules

1. **VLM Backbone: SmolVLM2** (~350M)
   - Vision: SigLIP encoder
   - Language: SmolLM2 decoder
   - Only **64 visual tokens** per frame (pi0 uses 256+)

2. **Action Expert** (~100M)
   - Compact transformer
   - Trained with **flow matching**
   - Predicts **50 action steps** at once (action chunk)

</div>

</v-clicks>

</div>

<div v-click>

<img src="/figures/smolvla-architecture.png" class="rounded-lg" style="max-height:50vh; max-width:100%;" />

</div>

</div>

---

# Efficiency Trick 1: Only 64 Visual Tokens

Standard VLMs are wasteful with images. SmolVLA fixes this.

<v-clicks>

<div class="grid grid-cols-2 gap-4 mt-3">

<div class="card text-sm">

### The Problem

A standard VLM like PaliGemma produces **256–1024 visual tokens** from a single image. In a transformer, attention cost scales as $O(n^2)$ — doubling tokens **quadruples** the compute.

For a robot control loop running at 10+ Hz, every token costs precious milliseconds.

</div>

<div class="teal-card text-sm">

### SmolVLA's Solution: PixelShuffle

Instead of keeping all patch tokens, SmolVLA applies **PixelShuffle** spatial compression:

512×512 image → SigLIP patches → **PixelShuffle 4×** → only **64 tokens**

Think of it as rearranging 4 adjacent patches into the channel dimension of 1 token. The spatial information is preserved — just packed more densely.

</div>

</div>

<div class="accent-card mt-3 text-center text-sm">

**64 tokens vs 256 = 16× less attention cost.** A robot doesn't need the same visual detail as a chatbot describing a painting. It needs enough to locate objects and plan grasps. 64 tokens is plenty.

</div>

</v-clicks>

---

# PixelShuffle: How It Works

<div v-click>
<img src="/figures/pixelshuffle-compression.png" class="rounded-lg mx-auto" style="max-height:55vh; max-width:90%;" />
</div>

<div v-click class="mt-3 teal-card text-center text-sm">

**PixelShuffle merges 2×2 neighboring patches into a single token with 4× the channels.** Spatial information is preserved — just packed into fewer, richer tokens. 256 tokens × d → 64 tokens × 4d. The attention cost drops by **16×**.

</div>


---

<div style="height:1px;"></div>

---

# Efficiency Trick 2: Layer Skipping

Not all layers are equally useful for robot control.

<v-clicks>

<div class="grid grid-cols-2 gap-4 mt-3">

<div class="card text-sm">

### What different layers learn

In a transformer with N layers:
- **Bottom layers (1 to N/2):** Low-level features — edge detection, spatial layout, object shapes, color. These are the "seeing" layers.
- **Top layers (N/2 to N):** High-level reasoning — compositionality, abstract concepts, complex language understanding. These are the "thinking" layers.

</div>

<div class="teal-card text-sm">

### SmolVLA's insight

For **motor control**, a robot needs:
- Where is the cup? (spatial — bottom layers)
- What does the cup look like? (visual features — bottom layers)
- What does "pick up" mean for my joints? (action mapping — learned by the action expert)

It does NOT need:
- Write a poem about the cup (complex reasoning — top layers)

</div>

</div>

<div class="accent-card mt-3 text-center text-sm">

**SmolVLA discards the top N/2 layers entirely.** The action expert only attends to features from the bottom half of the VLM. This **halves** the VLM forward pass cost with minimal impact on manipulation tasks.

</div>

</v-clicks>

---

# Layer Skipping: What Gets Kept and What Gets Discarded

<div v-click>
<img src="/figures/layer-skipping.png" class="rounded-lg mx-auto" style="max-height:55vh; max-width:90%;" />
</div>

<div v-click class="mt-3 blue-card text-center text-sm">

**Bottom N/2 layers** encode spatial/visual features (where is the cup? what shape is it?). **Top N/2 layers** handle abstract reasoning (write a poem about the cup). For robot control, we only need the bottom half — **50% less VLM compute** with minimal manipulation performance loss.

</div>

---

# Before Trick 3: Let's Talk About Cross-Attention

You already know **self-attention** from Lecture 2. Let's build up to cross-attention step by step.

<v-clicks>

<div class="card mt-3 mb-3 text-sm">

### Self-Attention Recap (What You Know)

In self-attention, **one** sequence provides all three roles:

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right) V$$

- **Q** (Queries), **K** (Keys), **V** (Values) all come from the **same** input tokens
- Each token asks every other token: *"How relevant are you to me?"*
- Result: each token gets a **weighted mix** of all other tokens' values

This is how a transformer processes a sentence — each word attends to all other words.

</div>

<div class="accent-card text-sm">

### The Limitation for Robots

Self-attention works within **one** sequence. But a robot's action expert has a problem: the action tokens need information from a **completely different** source — the VLM's visual/language features. How do action tokens "look at" the observation?

</div>

</v-clicks>

---

# From Self-Attention to Cross-Attention

<div v-click>
<img src="/figures/self-attention-to-cross-attention.png" class="rounded-lg mx-auto" style="max-height:38vh; max-width:90%;" />
</div>

<v-clicks>

<div class="grid grid-cols-2 gap-4 mt-2 text-sm">

<div class="blue-card">

### Self-Attention
**Q, K, V** all from the same sequence.

```
tokens = [action₁, action₂, ..., action₅₀]
Q = W_q × tokens   # ask questions
K = W_k × tokens   # provide answers
V = W_v × tokens   # provide content
```

Each action token attends to **other action tokens**.

</div>

<div class="purple-card">

### Cross-Attention
**Q** from one sequence, **K, V** from another.

```
Q = W_q × action_tokens    # actions ask
K = W_k × vlm_features     # observations answer
V = W_v × vlm_features     # observations provide
```

Each action token attends to **observation features**.

</div>

</div>

<div class="accent-card mt-2 text-center text-sm">

**The only difference: where K and V come from.** In cross-attention, the action tokens "query" the observations. Everything else — softmax, weighted sum, multi-head — is identical.

</div>

</v-clicks>

---

# Why Cross-Attention = Conditioning on Observations

This is a crucial insight. Cross-attention **is** conditioning.

<v-clicks>

<div class="grid grid-cols-2 gap-4 mt-3">

<div class="card text-sm">

### What "Conditioning" Means

When we say the action is **conditioned on the observation**, we mean:

$$P(\text{action} \mid \text{observation})$$

The action depends on (is influenced by, changes based on) what the robot sees. Different observations → different actions.

</div>

<div class="teal-card text-sm">

### What Cross-Attention Does

Each action token computes a **weighted average** of observation features:

$$\text{output}_i = \sum_j \alpha_{ij} \cdot V_j^{\text{obs}}$$

where $\alpha_{ij} = \text{softmax}(Q_i^{\text{act}} \cdot K_j^{\text{obs}} / \sqrt{d})$

**The attention weights $\alpha_{ij}$ are learned.** Action token $i$ learns to look at whichever observation feature is most relevant for that specific action step.

</div>

</div>

<div class="accent-card mt-3 text-center text-sm">

**Cross-attention literally computes a conditional function:** the action output depends on the observation input through learned attention weights. Action step 1 (reaching) attends to the cup's position. Action step 40 (placing) attends to the bowl's position. **Same mechanism, different attention weights.**

</div>

</v-clicks>

<div v-click>
<img src="/figures/cross-attention-conditioning.png" class="rounded-lg mx-auto mt-2" style="max-height:16vh; max-width:75%;" />
</div>


---

<div style="height:1px;"></div>

---

# Efficiency Trick 3: Interleaved Cross-Attention + Self-Attention

This is the most important architectural innovation in SmolVLA.

<v-clicks>

<div class="card mt-3 mb-3 text-sm">

### The Question

The action expert is a transformer that generates robot actions. But it needs to be **grounded** in what the robot sees and hears (VLM features). How should the action tokens interact with the VLM tokens?

</div>

<div class="grid grid-cols-3 gap-3 text-sm">

<div class="card" style="border-left: 3px solid #D4543A;">

### Option A: Self-Attention Only
Concatenate VLM tokens + action tokens, run self-attention over everything.

**Problem:** Action tokens are overwhelmed by the much larger VLM sequence. Expensive — $O((V+A)^2)$.

</div>

<div class="card" style="border-left: 3px solid var(--claude-amber);">

### Option B: Cross-Attention Only
Action tokens attend to VLM tokens, but never to each other.

**Problem:** No temporal coherence. Action at step 30 doesn't know what action step 29 planned. Jerky motions.

</div>

<div class="teal-card">

### Option C: Interleaved (SmolVLA)
Alternate between cross-attention (see the world) and self-attention (coordinate with neighbors).

**Best of both:** grounded in perception AND temporally smooth.

</div>

</div>

</v-clicks>

---

# Why Cross-Attention AND Self-Attention Together?

Let's trace what happens at each layer type:

<v-clicks>

<div class="grid grid-cols-2 gap-4 mt-3">

<div class="blue-card text-sm">

### Cross-Attention Layer (CA)

**Keys & Values** come from VLM features.
**Queries** are the action tokens.

Each action token asks: *"What in the scene is relevant to me?"*

- Action step 1 might attend to the cup's position
- Action step 25 might attend to the bowl's position
- Action step 50 might attend to the instruction "place it in the bowl"

**This is how the action expert "sees" the world.**

</div>

<div class="teal-card text-sm">

### Self-Attention Layer (SA)

**Keys, Values, and Queries** are all action tokens.
With **causal masking**: action $a_t$ can only see $a_1, ..., a_{t-1}$.

Each action token asks: *"What did the previous actions plan?"*

- Action step 25 sees steps 1–24 → smooth continuation
- Action step 50 sees steps 1–49 → consistent trajectory

**This is how the action expert produces smooth, coordinated motions.**

</div>

</div>

<div class="accent-card mt-3 text-center text-sm">

**CA without SA:** The robot sees the world but plans each action independently → jerky, uncoordinated.
**SA without CA:** The robot plans smooth motions but is blind to the scene → wrong direction.
**CA + SA interleaved:** See the world AND plan smooth motions → exactly what a robot needs.

</div>

</v-clicks>

---

# SmolVLA: The Action Expert — Up Close

<div v-click>
<img src="/figures/smolvla-action-expert.png" class="rounded-lg mx-auto" style="max-height:55vh; max-width:90%;" />
</div>

<div v-click class="mt-2 accent-card text-center text-sm">

Each action token alternates: **look at the world** (CA) → **coordinate with neighbors** (SA) → **look at the world** (CA) → **coordinate** (SA). This interleaving runs for 6+ layers, progressively refining the action plan.

</div>


---

<div style="height:1px;"></div>

---

# SmolVLA Attention Mask: What Exactly Can See What?

Let's be precise about the attention patterns.

<div v-click>
<img src="/figures/smolvla-attention-mask.png" class="rounded-lg mx-auto" style="max-height:32vh; max-width:85%;" />
</div>

<v-clicks>

<div class="grid grid-cols-2 gap-4 mt-2 text-sm">

<div class="teal-card">

### Cross-Attention Layers

**Rows:** 50 action tokens (queries)
**Columns:** 64 visual + text tokens from VLM (keys/values)

The mask is **completely full** — every action token can see every VLM token. There's no causal restriction here. Action step 50 gets the same visual information as action step 1.

*Why?* All action steps need the full scene context — the cup position, bowl position, and instruction are all equally relevant.

</div>

<div class="blue-card">

### Self-Attention Layers

**Rows & Columns:** 50 action tokens only

The mask is **lower-triangular (causal)** — action $a_t$ can only see actions $a_1, ..., a_{t-1}$.

*Why?* This ensures **temporal coherence**. Action step 30 must know what steps 1–29 planned, so it can continue the trajectory smoothly. But it shouldn't peek at the "future" — that would leak information.

</div>

</div>

<div class="accent-card mt-2 text-center text-sm">

**These two masks alternate layer by layer:** CA (full rectangular) → SA (causal square) → CA → SA → ... This is fundamentally different from pi0's block-wise attention, where everything lives in one big matrix.

</div>

</v-clicks>

---

# Attention Pattern Comparison: OpenVLA vs pi0 vs SmolVLA

The three architectures handle the Vision ↔ Action interaction completely differently.

<div v-click>
<img src="/figures/attention-pattern-comparison.png" class="rounded-lg mx-auto" style="max-height:35vh; max-width:90%;" />
</div>

<v-clicks>

<div class="grid grid-cols-3 gap-3 mt-2 text-sm">

<div class="accent-card">

### OpenVLA
**No separate action module.** Vision + language + action tokens ALL go through the same Llama decoder with standard causal attention. Actions attend to everything before them.

</div>

<div class="purple-card">

### pi0
**Block-wise attention.** Three blocks concatenated. Bidirectional within blocks, causal between. Actions see VLM tokens, but VLM doesn't see actions. One giant matrix.

</div>

<div class="teal-card">

### SmolVLA
**Interleaved CA+SA.** Action tokens are separate. Alternate between cross-attending to VLM and self-attending among themselves. Cheapest and most focused.

</div>

</div>

</v-clicks>

---

# The Big Comparison

<div class="mt-3">

| | **OpenVLA** | **pi0** | **SmolVLA** |
|---|:---:|:---:|:---:|
| **Parameters** | 7B | 3.3B | **450M** |
| **VLM backbone** | Llama 2 + SigLIP + DinoV2 | PaliGemma 3B | SmolVLM2 350M |
| **Action method** | Tokenization (256 bins) | Flow matching | Flow matching |
| **Action output** | 1 step, 7 tokens (sequential) | 50 steps, all at once | 50 steps, all at once |
| **Precision** | Discrete (lossy) | **Continuous** | **Continuous** |
| **Attention pattern** | Causal (LLM-style) | Block-wise | Interleaved CA+SA |
| **Visual tokens** | ~256 (SigLIP + DinoV2) | ~256+ | **64** |
| **Training data** | 970K trajectories (OXE) | 10,000 hours | 22.9K episodes |
| **Can you run it?** | Yes (7GB w/ quantization) | Difficult | **Yes (laptop)** |

</div>

<div v-click class="mt-2 accent-card text-center text-sm">

**SmolVLA is the sweet spot for learning:** small enough to run, modern enough to work (flow matching + action chunking), and integrated with LeRobot.

</div>

---

# SmolVLA: Real-World Results

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

<div class="teal-card text-sm">

### SO-100 Tasks (78.3% success with pretraining)

| Task | Without PT | With PT |
|------|:---:|:---:|
| Pick & Place | 60% | **85%** |
| Stack | 35% | **70%** |
| Pour | 40% | **75%** |
| Sort | 45% | **80%** |

*PT = pre-training on the 487 LeRobot community datasets*

</div>

<div v-click class="blue-card mt-3 text-sm text-center">

**Pre-training matters.** SmolVLA pre-trained on diverse robot data learns a foundation to master new tasks from just 50 demos.

</div>

</div>

<div v-click>

<div class="card text-sm">

### But Wait — There's More

SmolVLA also introduces **asynchronous inference**: the VLM processes the next observation while the robot executes the current actions. Result: **30% faster** task completion (9.7s vs 13.7s).

We'll cover this in detail in the next slides.

</div>

<div class="accent-card mt-3 text-sm text-center">

**450M parameters, 78% success, runs on consumer hardware.** This is what democratized robotics looks like.

</div>

</div>

</div>

---

# SmolVLA's Secret Weapon: Asynchronous Inference

The naive way to run a VLA is **synchronous**: observe → think → act → wait → observe → think → act. SmolVLA does something smarter.

<v-clicks>

<div class="card mt-3 mb-3 text-sm" style="border-left: 3px solid #D4543A;">

### The Synchronous Problem

In synchronous mode, the robot's control loop looks like:

1. **Capture image** (5ms)
2. **Run VLM encoder** — SigLIP + SmolLM2 bottom layers (~200ms)
3. **Run flow matching** — 10 Euler steps through action expert (~100ms)
4. **Execute 15 of the 50 actions** (~500ms at 30 Hz)
5. **Robot sits idle** while we go back to step 1

Total cycle: ~800ms. But the robot is **idle for 300ms** every cycle while the VLM thinks. That's wasted time!

</div>

<div class="teal-card text-center text-sm">

### The Asynchronous Insight

**Action chunking gives us a buffer.** We predict 50 actions but only execute 15 before re-planning. Those 15 actions take ~500ms to execute. The VLM encoding only takes ~300ms. **The VLM can think while the robot moves!**

</div>

</v-clicks>

---

# How Asynchronous Inference Works — Step by Step

<div v-click>
<img src="/figures/smolvla-async-inference.png" class="rounded-lg mx-auto" style="max-height:35vh; max-width:90%;" />
</div>

<v-clicks>

<div class="grid grid-cols-2 gap-4 mt-2 text-sm">

<div class="card" style="border-left: 3px solid #D4543A;">

### Synchronous (Naive)

```
Time 0ms:    [Observe + Encode: 300ms]
Time 300ms:  [Flow Match: 100ms]
Time 400ms:  [Execute 15 actions: 500ms]
Time 900ms:  [Observe + Encode: 300ms]  ← robot idle!
Time 1200ms: [Flow Match: 100ms]
Time 1300ms: [Execute: 500ms]
```

**Total per cycle: ~900ms.** Robot waits 300ms each cycle.

</div>

<div class="teal-card">

### Asynchronous (SmolVLA)

```
Time 0ms:    [Execute chunk N: 500ms]
             [Observe + Encode N+1: 300ms] ← parallel!
Time 300ms:  [Flow Match N+1: 100ms]
Time 400ms:  (buffer ready, waiting for execution)
Time 500ms:  [Execute chunk N+1: 500ms]
             [Observe + Encode N+2: 300ms] ← parallel!
```

**Total per cycle: ~500ms.** Robot **never waits!**

</div>

</div>

<div class="accent-card mt-2 text-center text-sm">

**Result: 9.7s per task (async) vs 13.7s (sync) — 30% faster.** The trick is simple: while hands move, the brain already prepares the next plan. Just like how you reach for a cup while your eyes are already looking at the coffee machine.

</div>

</v-clicks>


---

<div style="height:1px;"></div>

---

# Interactive Deep-Dive: SmolVLA Async Inference

Explore the full async inference pipeline interactively — action queue dynamics, chunk merging, sync vs async race, and real performance numbers.

<div class="mt-4">

<div class="card text-sm mb-3" style="border-left: 3px solid #6a9a5b;">

### What's Inside the Visualizer

- **Action Queue Simulator** — watch the queue fill/drain in real time, trigger threshold-based observation dispatch
- **Chunk Overlap & Aggregation** — adjust merge weights (0.3×old + 0.7×new) and see how trajectories blend
- **Sync vs Async Race** — two robots race to place 5 cubes, one sync, one async — see the 30% speed difference live
- **Architecture Walkthrough** — step through the 6 stages: capture → threshold check → VLM → flow match → gRPC → queue merge

</div>

<div class="teal-card text-center">

**[Open Interactive Visualizer →](https://smolvla-async-inference-visualizer.vercel.app)**

<span class="text-xs opacity-70">Opens in browser · Single-file HTML · No dependencies</span>

</div>

</div>

---

# Why Async Inference Only Works with Action Chunking

<v-clicks>

<div class="card mt-4 mb-3 text-sm">

### The Key Requirement: A Buffer of Future Actions

Async inference **requires** the robot to have a queue of actions to execute while the VLM thinks. This is only possible because SmolVLA predicts **50 actions** at once (an action chunk).

If you predict only 1 action (like OpenVLA), there's nothing to execute while thinking → **you're stuck with synchronous**.

</div>

<div class="grid grid-cols-3 gap-3 text-sm">

<div class="card" style="border-left: 3px solid #D4543A;">

### OpenVLA
Predicts **1 action step**

No buffer → no async possible

Must stop → think → move → stop

**Fundamentally synchronous**

</div>

<div class="purple-card">

### pi0
Predicts **50 action steps**

Can buffer, but pi0 paper uses synchronous inference

Async possible in theory

</div>

<div class="teal-card">

### SmolVLA
Predicts **50 action steps**

Executes 15, queues the rest

VLM runs in parallel with execution

**30% faster than sync**

</div>

</div>

<div class="accent-card mt-3 text-center text-sm">

**Action chunking isn't just about smooth motions — it enables a completely different execution paradigm.** The chunk acts as a buffer between perception and execution, letting both run concurrently.

</div>

</v-clicks>

---

# But Wait — What Is "Flow Matching"?

We keep saying SmolVLA uses **flow matching** instead of DDPM. You learned DDPM in Lecture 1. But what is this new thing?

<v-clicks>

<div class="card mt-4 mb-3 text-sm">

In Lecture 2, we mentioned that pi0's Action Expert uses DDPM to generate actions from noise. That was a simplification. Pi0 actually uses **flow matching** — a newer, cleaner alternative.

</div>

<div class="accent-card text-center">

**Flow matching is to DDPM what a highway is to a winding mountain road.** Both get you from A to B, but one takes a much straighter path. Let's build it from scratch.

</div>

</v-clicks>


---

<div style="height:1px;"></div>


---

<div style="height:1px;"></div>


---

<div style="height:1px;"></div>

---

<div style="height:1px;"></div>

---
layout: section
---

# Part 2
## Flow Matching from Scratch — The Straight Path from Noise to Action

---

# Recall: DDPM from Lecture 1

Let's recap what you already know:

<v-clicks>

<div class="grid grid-cols-2 gap-4 mt-3">

<div class="card text-sm">

### Forward Process (Destroy)

Gradually add Gaussian noise over **T steps** (T = 50 or 1000):

$$x_t = \sqrt{\bar{\alpha}_t} \cdot x_0 + \sqrt{1 - \bar{\alpha}_t} \cdot \epsilon$$

where $\epsilon \sim \mathcal{N}(0, I)$

After T steps: $x_T \approx$ pure noise

</div>

<div class="card text-sm">

### Reverse Process (Create)

A neural network predicts the noise $\hat{\epsilon}$, then subtract:

$$x_{t-1} = \frac{1}{\sqrt{\alpha_t}}\left(x_t - \frac{1-\alpha_t}{\sqrt{1-\bar{\alpha}_t}} \hat{\epsilon}\right) + \sigma_t z$$

Repeat T times: pure noise → clean sample

</div>

</div>

<div class="accent-card mt-3 text-center text-sm">

**It works beautifully.** But there are two things about it that bother us...

</div>

</v-clicks>

---

# The Two Problems with DDPM

<v-clicks>

<div class="card mt-4 mb-4" style="border-left: 3px solid #D4543A;">

### Problem 1: Too Many Steps

DDPM needs **50–1000 denoising steps** to generate a clean sample. Each step is a full forward pass through the neural network.

For robot control at 10 Hz, you have **100ms** to generate an action. 50 forward passes in 100ms is brutal.

**DDIM** (Lecture 1) helps — it cuts to ~10 steps. But can we do even better?

</div>

<div class="card" style="border-left: 3px solid #D4543A;">

### Problem 2: The Paths Are Curved

Watch what happens when DDPM denoises: the sample takes a **winding, stochastic path** from noise to data. Why? Because at each step, we add a random perturbation ($\sigma_t z$).

Curved paths are hard to follow with few steps — like trying to navigate a winding mountain road by only looking at the map every 5 kilometers. You'll miss the turns.

**What if the path from noise to data was a straight line?**

</div>

</v-clicks>

---

# The Big Idea: Walk in a Straight Line

<v-clicks>

<div class="grid grid-cols-2 gap-6 mt-4">

<div class="card text-sm">

### DDPM: The Winding Path

Start at noise. Take a small step. Add a bit of randomness. Take another step. Wiggle. Step. Wiggle. Step...

After 50 wiggly steps, you arrive at the data.

**Stochastic** — each run gives a slightly different path.
**Slow** — many steps needed to follow the curves.

</div>

<div class="teal-card text-sm">

### Flow Matching: The Highway

Start at noise. **Walk in a straight line** toward the data.

No wiggling. No randomness. Just a **smooth, deterministic** path.

**Deterministic** — same starting point, same ending point.
**Fast** — a straight path needs only 5–10 steps.

</div>

</div>

</v-clicks>

<div v-click>
<img src="/figures/ddpm-vs-flow-paths.png" class="rounded-lg mx-auto mt-3" style="max-height:30vh; max-width:80%;" />
</div>

---

# Step 1: The Simplest Possible Path

Forget neural networks for a moment. What's the simplest way to go from noise to data?

<v-clicks>

<div class="accent-card mt-4 mb-3 text-sm">

### Linear Interpolation

If $x_0$ is a noise sample and $x_1$ is a data sample, then at any time $\tau \in [0, 1]$:

$$x_\tau = (1 - \tau) \cdot x_0 + \tau \cdot x_1$$

- At $\tau = 0$: $x_0$ = **pure noise**
- At $\tau = 0.5$: halfway between noise and data
- At $\tau = 1$: $x_1$ = **clean data**

That's it. A straight line from noise to data.

</div>

<div class="card text-sm text-center">

Compare with DDPM's forward process: $x_t = \sqrt{\bar{\alpha}_t} \cdot x_0 + \sqrt{1 - \bar{\alpha}_t} \cdot \epsilon$

Both **mix** noise and data. But DDPM uses a complicated square-root schedule. Flow matching uses a **linear** mix. Much simpler.

</div>

</v-clicks>

---

# Flow Matching: Linear Interpolation — Visualized

<div v-click>
<img src="/figures/flow-matching-interpolation.png" class="rounded-lg mx-auto" style="max-height:55vh; max-width:90%;" />
</div>

<div v-click class="mt-2 teal-card text-center text-sm">

At every time $\tau$, the point $x_\tau$ sits on the straight line between noise ($x_0$) and data ($x_1$). The **velocity** along this path is constant: $v = x_1 - x_0$.

</div>

---

# Step 2: The Velocity Field

If we know the path, what's the **speed and direction** at any point?

<v-clicks>

<div class="card mt-3 mb-3 text-sm">

### The Derivative

Take the derivative of our linear path with respect to time:

$$\frac{dx_\tau}{d\tau} = x_1 - x_0$$

This is the **velocity** — it tells us: "to go from noise to data, move in the direction $x_1 - x_0$."

For a straight line, the velocity is **constant** — it doesn't change with $\tau$.

</div>

<div class="teal-card mb-3 text-sm">

### The Goal

We want to learn a neural network $v_\theta(\tau, x_\tau)$ that predicts this velocity.

Given a noisy point $x_\tau$ and the time $\tau$, the network should output the direction to walk: $\hat{v} \approx x_1 - x_0$.

</div>

<div class="accent-card text-center text-sm">

**DDPM learns to predict noise $\hat{\epsilon}$.** Flow matching learns to predict **velocity $\hat{v}$** — the direction from noise toward data. Conceptually simpler.

</div>

</v-clicks>

---

# Step 3: The Training Objective

Now we can write the loss function:

<v-clicks>

<div class="card mt-4 mb-3">

### The Flow Matching Loss

$$\mathcal{L}(\theta) = \mathbb{E}_{\tau,\, x_0,\, x_1} \left[ \| v_\theta(\tau, x_\tau) - (x_1 - x_0) \|^2 \right]$$

In words:
1. Sample a time $\tau \sim \text{Uniform}[0, 1]$
2. Sample noise $x_0 \sim \mathcal{N}(0, I)$ and data $x_1$ from the dataset
3. Compute $x_\tau = (1-\tau) \cdot x_0 + \tau \cdot x_1$ (the noisy point on the path)
4. Ask the network: "what direction should we go?" → $v_\theta(\tau, x_\tau)$
5. The answer should be $x_1 - x_0$ → penalize the squared error

</div>

<div class="accent-card text-center text-sm">

**This is just MSE.** No complex noise schedules ($\alpha_t$, $\bar{\alpha}_t$, $\beta_t$). No variance terms. Just: "predict the direction from noise to data." That's the entire loss.

</div>

</v-clicks>

---

# A Concrete Example

Let's trace through flow matching with **robot actions**.

<v-clicks>

<div class="card mt-3 mb-2 text-sm">

### Setup
- **Data $x_1$:** A 50-step action chunk from a demo → `[0.3, 0.5, -0.1, 0.8, ...]` (50 × 7 = 350 numbers)
- **Noise $x_0$:** Random Gaussian → `[-1.2, 0.4, 0.7, -0.3, ...]` (350 random numbers)
- **Time $\tau$:** Sampled as 0.3

</div>

<div class="teal-card mb-2 text-sm">

### Step 1: Create the noisy sample
$$x_{0.3} = 0.7 \cdot [-1.2, 0.4, 0.7, -0.3, ...] + 0.3 \cdot [0.3, 0.5, -0.1, 0.8, ...] = [-0.75, 0.43, 0.46, 0.03, ...]$$

</div>

<div class="blue-card mb-2 text-sm">

### Step 2: Compute the target velocity
$$v^* = x_1 - x_0 = [0.3-(-1.2),\ 0.5-0.4,\ -0.1-0.7,\ 0.8-(-0.3),\ ...] = [1.5, 0.1, -0.8, 1.1, ...]$$

</div>

<div class="accent-card text-sm">

### Step 3: Train
Feed $(x_{0.3},\ \tau=0.3)$ into the network, get prediction $\hat{v}$, compute MSE loss with target $[1.5, 0.1, -0.8, 1.1, ...]$.

</div>

</v-clicks>

---

# Flow Matching: The Training Loop

<div v-click>
<img src="/figures/flow-matching-training.png" class="rounded-lg mx-auto" style="max-height:55vh; max-width:90%;" />
</div>

<div v-click class="mt-2 card text-center text-sm">

**Training is almost identical to DDPM.** Sample noise, mix with data, predict the target. The only difference: predict **velocity** ($x_1 - x_0$) instead of **noise** ($\epsilon$).

</div>

---

# Step 4: Inference — Walking the Path

At inference time, we start from noise and follow the velocity field:

<v-clicks>

<div class="card mt-3 mb-3 text-sm">

### Euler Integration (the simplest ODE solver)

Start with $x_0 \sim \mathcal{N}(0, I)$, choose a step size $\Delta\tau = 0.1$:

$$x_{\tau + \Delta\tau} = x_\tau + \Delta\tau \cdot v_\theta(\tau, x_\tau)$$

**Step 1:** $x_{0.1} = x_0 + 0.1 \cdot v_\theta(0, x_0)$
**Step 2:** $x_{0.2} = x_{0.1} + 0.1 \cdot v_\theta(0.1, x_{0.1})$
...
**Step 10:** $x_{1.0} = x_{0.9} + 0.1 \cdot v_\theta(0.9, x_{0.9})$ ← **clean actions!**

</div>

<div class="accent-card text-center text-sm">

**10 steps.** Not 50. Not 1000. Just 10 forward passes through the network and you have a full 50-step action trajectory. That's why SmolVLA and pi0 are fast enough for real-time robot control.

</div>

</v-clicks>

---

# Flow Matching: Inference — Visualized

<div v-click>
<img src="/figures/flow-matching-inference.png" class="rounded-lg mx-auto" style="max-height:55vh; max-width:90%;" />
</div>

<div v-click class="mt-2 teal-card text-center text-sm">

Starting from noise (left), each Euler step moves the point along the learned velocity field. After 10 steps, we have clean robot actions (right). The path is nearly straight.

</div>

---

# Why Straight Paths Need Fewer Steps

This is the core insight behind flow matching's speed advantage.

<v-clicks>

<div class="grid grid-cols-2 gap-4 mt-3">

<div class="card text-sm" style="border-left: 3px solid #D4543A;">

### Curved Path (DDPM)

Imagine driving a winding mountain road. If you only check the GPS every 5 km, you'll fly off a cliff at the first sharp turn.

**More curves → more GPS checks → more denoising steps.**

With 50 steps, the errors from missing the curves still accumulate.

</div>

<div class="teal-card text-sm">

### Straight Path (Flow Matching)

Now imagine driving a highway. Even if you only check the GPS every 50 km, you'll stay on the road.

**Straight path → fewer checkpoints → fewer Euler steps.**

With 10 steps (or even 5!), the straight path has almost zero discretization error.

</div>

</div>

<div class="accent-card mt-3 text-center text-sm">

**Perfectly straight paths could be solved in a SINGLE step:** $x_1 = x_0 + 1.0 \cdot v_\theta(0, x_0)$. In practice, paths aren't perfectly straight (the network isn't perfect), so we use 5–10 steps.

</div>

</v-clicks>

---

# The Conditional Flow Matching Trick

There's a subtle problem with what we described. Let's address it.

<v-clicks>

<div class="card mt-3 mb-3 text-sm" style="border-left: 3px solid var(--claude-amber);">

### The Problem: Path Crossings

In a batch, different data points $x_1^{(a)}$ and $x_1^{(b)}$ are paired with random noise $x_0^{(a)}$ and $x_0^{(b)}$.

Sometimes the straight paths **cross each other**. At the crossing point, the network sees the same $(\tau, x_\tau)$ but is told to go in **two different directions**. Conflicting gradients → poor learning.

</div>

<div class="teal-card mb-3 text-sm">

### The Fix: Conditional Flow Matching (CFM)

Instead of learning the global velocity field directly (intractable), learn the velocity **conditioned on each data point** $x_1$:

$$\mathcal{L}_{\text{CFM}}(\theta) = \mathbb{E}_{\tau,\, x_1,\, x_\tau | x_1} \left[ \| v_\theta(\tau, x_\tau) - (x_1 - x_0) \|^2 \right]$$

**The key insight** (Lipman et al., 2023): This conditional loss has the **exact same gradients** as the marginal loss. So we can train with conditional pairs (which is what we showed before!) and the network learns the correct global field.

</div>

<div class="accent-card text-center text-sm">

**You've been doing CFM all along!** The training loop we described (sample $x_0$, sample $x_1$, mix, predict velocity) **is** conditional flow matching. The theory just explains why it works.

</div>

</v-clicks>

---

# Optimal Transport: Making Paths Even Straighter

<v-clicks>

<div class="card mt-3 mb-3 text-sm">

### The Pairing Problem

When we randomly pair noise samples with data samples, some paths cross. Even with CFM, this creates conflicting training signals in regions where paths overlap.

</div>

<div class="teal-card mb-3 text-sm">

### Optimal Transport (OT) Coupling

Instead of random pairing, find the **minimum-cost assignment** between noise and data in each mini-batch:

"Which noise sample is **closest** to which data sample?"

Pair nearby noise with nearby data → **paths are shorter, less likely to cross**.

</div>

<div class="blue-card text-sm">

### In Practice

For a mini-batch of B noise samples and B data samples:
1. Compute the B × B distance matrix
2. Solve the linear assignment problem (Hungarian algorithm, $O(B^3)$)
3. Use the optimal pairs for training

**Cost:** negligible — $O(B^3)$ for B=64 is microseconds.
**Benefit:** straighter paths, faster convergence, better few-step inference.

</div>

</v-clicks>

---

# DDPM vs Flow Matching: The Complete Comparison

<div class="mt-3 text-sm">

| | **DDPM** | **Flow Matching** |
|---|---|---|
| **What we learn** | Predict noise $\hat{\epsilon}$ | Predict velocity $\hat{v}$ |
| **Forward process** | $x_t = \sqrt{\bar{\alpha}_t} x_0 + \sqrt{1-\bar{\alpha}_t} \epsilon$ | $x_\tau = (1-\tau) x_0 + \tau x_1$ |
| **Training target** | $\epsilon$ (the noise that was added) | $x_1 - x_0$ (the direction to data) |
| **Inference** | Stochastic reverse SDE (wiggling) | Deterministic ODE (smooth) |
| **Steps needed** | 50–1000 (or 10–50 with DDIM) | **5–10** |
| **Noise schedule** | Complex ($\beta_t$, $\alpha_t$, $\bar{\alpha}_t$) | **None** (linear interpolation) |
| **Path shape** | Curved, stochastic | **Straight, deterministic** |
| **Loss function** | $\|\hat{\epsilon} - \epsilon\|^2$ | $\|\hat{v} - (x_1 - x_0)\|^2$ |

</div>

<div v-click class="mt-3 accent-card text-center text-sm">

**Both are MSE losses on the same network architecture.** The magic is in the training scheme — flow matching's linear interpolation naturally produces straighter paths that need fewer integration steps.

</div>

---

# Why Flow Matching for Robot Actions

<v-clicks>

<div class="grid grid-cols-2 gap-3 mt-3">

<div class="card mb-2 text-sm">

### 1. Speed
10 Euler steps vs 50 DDIM steps = **5x faster**. At 10 Hz control, that's the difference between real-time and unusable.

</div>

<div class="card mb-2 text-sm">

### 2. Determinism
ODE integration is deterministic — same starting noise, same actions. No stochastic jitter in the robot's motions.

</div>

<div class="card mb-2 text-sm">

### 3. Simplicity
No noise schedule to tune. No variance terms. Just linear interpolation and MSE. Fewer hyperparameters, less debugging.

</div>

<div class="card text-sm">

### 4. Multimodality
Multiple valid grasping strategies → the velocity field naturally handles this through different noise starting points flowing to different modes.

</div>

</div>

<div class="accent-card mt-3 text-center text-sm">

**This is why both pi0 and SmolVLA chose flow matching over DDPM.** Same expressiveness, less compute, simpler code.

</div>

</v-clicks>

---

# The Flow Matching Training Loop in Code

```python {all|1-3|5-7|9-12|14-16|all}
def train_step(model, action_chunk, observation, optimizer):
    """One training step of flow matching for a VLA action expert."""
    batch_size = action_chunk.shape[0]

    # 1. Sample noise and time
    x0 = torch.randn_like(action_chunk)           # noise
    tau = torch.rand(batch_size, 1)                # time in [0, 1]

    # 2. Create noisy actions via linear interpolation
    x_tau = (1 - tau) * x0 + tau * action_chunk    # the "noisy" point
    target_velocity = action_chunk - x0            # direction: noise → data

    # 3. Predict velocity, conditioned on observation
    predicted_velocity = model(x_tau, tau, observation)

    # 4. MSE loss — that's it!
    loss = F.mse_loss(predicted_velocity, target_velocity)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    return loss.item()
```

<div v-click class="mt-2 teal-card text-center text-sm">

**15 lines of meaningful code.** Compare with DDPM's noise schedules, variance computation, and complex reverse sampling. Flow matching is embarrassingly simple.

</div>

---

# The Flow Matching Inference Loop in Code

```python {all|1-4|6-9|11-13|all}
def generate_actions(model, observation, n_steps=10):
    """Generate a 50-step action chunk from noise using flow matching."""
    # Start from pure noise
    x = torch.randn(1, 50, 7)   # [batch, timesteps, action_dim]

    # Walk from tau=0 to tau=1 in n_steps
    dt = 1.0 / n_steps
    for i in range(n_steps):
        tau = torch.tensor([i * dt])

        # Predict velocity and take one Euler step
        v = model(x, tau, observation)
        x = x + dt * v

    return x   # clean action chunk!
```

<div v-click class="mt-2 accent-card text-center text-sm">

**10 forward passes through the network** → a full 50-step action trajectory. At 30ms per forward pass on a Mac M4, that's **300ms** for 50 action steps = effectively **166 Hz** throughput.

</div>

---

<div style="height:1px;"></div>

---

# Quiz: Flow Matching (1/3)

<div class="quiz-card mt-2">

<div class="mb-3">

**Q1:** In DDPM, we train the network to predict ___. In flow matching, we train it to predict ___. Fill in the blanks.

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> DDPM: <strong>noise</strong> ($\epsilon$). Flow matching: <strong>velocity</strong> ($x_1 - x_0$, the direction from noise to data). Both are trained with MSE loss, but the target is fundamentally different.
</div>

<div class="mb-3">

**Q2:** Why does flow matching need only 10 inference steps while DDPM needs 50+?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> Flow matching produces <strong>straight paths</strong> from noise to data (via linear interpolation). Straight paths have low discretization error even with large step sizes. DDPM produces <strong>curved, stochastic paths</strong> that require many small steps to follow accurately — skip a step and you miss a turn.
</div>

<div class="mb-3">

**Q3:** Write the linear interpolation formula. What does $x_\tau$ look like at $\tau = 0$, $\tau = 0.5$, and $\tau = 1$?

</div>

<div v-click class="px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> $x_\tau = (1-\tau) \cdot x_0 + \tau \cdot x_1$. At $\tau=0$: pure noise ($x_0$). At $\tau=0.5$: equal mix of noise and data. At $\tau=1$: clean data ($x_1$). The formula traces a straight line from noise to data.
</div>

</div>

---

# Quiz: Flow Matching (2/3)

<div class="quiz-card mt-2">

<div class="mb-3">

**Q4:** What is the "conditional" in Conditional Flow Matching? Why is it needed?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> "Conditional" means we condition on a <strong>specific data point</strong> $x_1$ when computing the velocity target. It's needed because the global (marginal) velocity field is intractable — but the conditional velocity (direction from $x_0$ to a specific $x_1$) is trivially $x_1 - x_0$. The mathematical trick: the conditional loss has the same gradients as the intractable marginal loss.
</div>

<div class="mb-3">

**Q5:** SmolVLA generates 50 action steps in 10 Euler steps. How many total neural network forward passes is that? How does this compare to OpenVLA generating 7 action tokens autoregressively?

</div>

<div v-click class="px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> SmolVLA: <strong>10 forward passes</strong> through a 100M network → 50 action steps (all dimensions simultaneously). OpenVLA: <strong>7 forward passes</strong> through a 7B network → 1 action step (one dimension per pass). SmolVLA gets 50x more actions from a 70x smaller model, despite using 10 passes vs 7. The total compute is vastly lower.
</div>

</div>

---

# Quiz: Flow Matching (3/3)

<div class="quiz-card mt-2">

<div class="mb-3">

**Q6:** Optimal Transport (OT) coupling pairs noise with data to make paths straighter. In a mini-batch of 64 samples, what is the computational cost? Is it worth it?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> The Hungarian algorithm solves the assignment in $O(B^3) = O(64^3) \approx 262K$ operations — <strong>microseconds</strong> on a GPU. Completely negligible compared to the neural network forward pass. Worth it: straighter paths mean better few-step generation and faster convergence.
</div>

<div class="mb-3">

**Q7:** Could you replace flow matching with DDPM in SmolVLA's action expert without changing the neural network architecture? What would change?

</div>

<div v-click class="px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> <strong>Yes</strong> — the architecture stays the same (it's just a transformer that takes noisy input + time and outputs a prediction). What changes: (1) Training target: predict noise instead of velocity. (2) Inference: need 50+ denoising steps instead of 10 Euler steps. (3) Need to define a noise schedule ($\beta_t$, $\alpha_t$). The model would be ~5x slower at inference for similar quality.
</div>

</div>

---

# Brainstorm: Flow Matching

<div class="brainstorm-card">
<div class="text-center">

**Now that you understand both DDPM and flow matching, consider this:**

If flow matching is simpler and faster, why was DDPM invented first? What made people think of the more complex approach before the simpler one?

*Hint: The history of science is full of cases where the complicated solution came first. Think about what insights were needed to arrive at flow matching.*

</div>
</div>

---

<div style="height:1px;"></div>

---
layout: section
---

# Part 3
## The Real Implementation — SmolVLA on SO-101


---

<div style="height:1px;"></div>

---

# Our Actual Task: Box-to-Bowl Pick-and-Place

<v-clicks>

<div class="grid grid-cols-2 gap-6 mt-3">

<div>

<div class="card mb-3 text-sm">

### What the Robot Does

Given a natural language instruction like *"Pick up the box and place it in the blue bowl"*, the robot must:

1. **Visually locate** the box on the table
2. **Grasp** it with the gripper
3. **Transport** it to the correct colored bowl
4. **Place** it inside and **release**

</div>

<div class="accent-card text-sm">

### The Semantic Grounding Magic

The robot was trained with **literal color names** only ("red bowl", "green bowl", "blue bowl"). But at inference time:

| What you say | What happens |
|---|---|
| "the ocean-colored bowl" | → blue bowl |
| "the grassy bowl" | → green bowl |
| "the one that looks like blood" | → red bowl |

**Zero-shot generalization** from SmolVLA's VLM backbone!

</div>

</div>

<div v-click>

<img src="/figures/setup-photo.jpg" class="rounded-lg" style="max-height:50vh; max-width:100%;" />

<div class="text-xs text-center mt-1 opacity-60">Our actual workspace: SO-101 follower arm, 3 colored bowls, box, overhead camera, Mac</div>

</div>

</div>

</v-clicks>


---

<div style="height:1px;"></div>

---

# The Workspace: What You See from the Camera

<div class="grid grid-cols-3 gap-3 mt-4">

<div v-click>
<img src="/figures/webcam-blue-bowl.jpg" class="rounded-lg" style="max-height:25vh;" />
<div class="text-xs text-center mt-1">"Place it in the blue bowl"</div>
</div>

<div v-click>
<img src="/figures/webcam-green-bowl.jpg" class="rounded-lg" style="max-height:25vh;" />
<div class="text-xs text-center mt-1">"Place it in the green bowl"</div>
</div>

<div v-click>
<img src="/figures/webcam-red-bowl.jpg" class="rounded-lg" style="max-height:25vh;" />
<div class="text-xs text-center mt-1">"Place it in the red bowl"</div>
</div>

</div>

<v-click>

<div class="card mt-4 text-sm">

### Workspace Layout (Critical for Reproducibility)

1. **Follower arm** — mounted at table edge, within reach of all bowls
2. **3 colored bowls** (red, green, blue) — arranged in a row
3. **Box** — placed in center, within easy grasp reach
4. **Overhead webcam** (camera index 0) — bird's-eye view on tripod
5. **Wrist camera** (camera index 1) — attached to robot's wrist
6. **Leader arm** — nearby for teleoperation during data collection
7. **Mac** — connected to both arms + cameras via USB

</div>

</v-click>

---

# Hardware: The SO-101 Setup

<v-clicks>

<div class="grid grid-cols-2 gap-6 mt-3">

<div>

<div class="card mb-3 text-sm">

### The Robot

| Spec | Detail |
|------|--------|
| DOF | 6 (shoulder_pan, shoulder_lift, elbow_flex, wrist_flex, wrist_roll, gripper) |
| Actuators | Feetech STS3215 serial bus servos |
| Control | 30 Hz position control via USB serial |
| Cost | ~$100 in parts |

</div>

<div class="teal-card text-sm">

### Dual Camera Setup

| Camera | LeRobot Name | SmolVLA Expects |
|--------|-------------|-----------------|
| Overhead webcam | `webcam` (index 0) | `camera1` |
| Wrist camera | `arm_cam` (index 1) | `camera2` |

**Both at 640×480 @ 30fps** — native resolution. SmolVLA handles resizing internally.

</div>

</div>

<div>

<img src="/figures/so101-overview.png" class="rounded-lg" style="max-height:50vh; max-width:100%;" />

</div>

</div>

</v-clicks>

---

# Step 1: Plug In and Find Ports

<v-clicks>

<div class="card mt-4 mb-3 text-sm">

### Detect Robot Ports

```bash
source activate.sh        # Activate the LeRobot environment
lerobot-find-port         # Discover connected USB devices
```

You'll see port paths like:
- **Follower:** `/dev/tty.wchusbserial5AE60830811`
- **Leader:** `/dev/tty.wchusbserial5A7C1167331`

</div>

<div class="teal-card mb-3 text-sm">

### Test Your Cameras

```bash
python show_cameras.py    # Opens live feed windows for both cameras
```

This shows side-by-side views: **"Webcam (Kreo Owl)"** + **"Arm Camera (USB2.0_CAM1)"**. Press Q to quit.

</div>

<div class="accent-card text-center text-sm">

**If you don't see the device:** check the USB cable (must be a **data** cable, not charge-only), try a different port, and on Linux run `sudo chmod 666 /dev/ttyACM0`. On macOS, ports are `/dev/tty.usbmodem*` or `/dev/tty.wchusbserial*`.

</div>

</v-clicks>

---

# Step 2: Calibration

Calibrate both arms before first use. This only needs to be done **once** — calibration files are saved.

<v-clicks>

<div class="card mt-3 mb-3 text-sm">

### Calibrate the Follower Arm

```bash
lerobot-calibrate \
  --robot.type=so101_follower \
  --robot.port=/dev/tty.wchusbserial5AE60830811 \
  --robot.id=my_follower
```

Follow the on-screen instructions to move each joint to its limits.

</div>

<div class="teal-card mb-3 text-sm">

### Calibrate the Leader Arm

```bash
lerobot-calibrate \
  --teleop.type=so101_leader \
  --teleop.port=/dev/tty.wchusbserial5A7C1167331 \
  --teleop.id=my_leader
```

Calibration files saved as `my_follower` and `my_leader`. **Back these up!**

</div>

<div class="accent-card text-center text-sm">

Each Feetech servo reads raw encoder values (0–4095). Calibration maps these to meaningful joint angles. Without it, the robot might try to rotate a joint 360° and **break the frame**.

</div>

</v-clicks>

---

# Step 3: Test Cameras & Verify Everything

<v-clicks>

<div class="card mt-3 mb-3 text-sm">

### Quick Hardware Test

```bash
python test_so101.py --port /dev/tty.wchusbserial5AE60830811
```

This runs a 5-step check: imports → port exists → connect → read joint positions → disconnect cleanly.

</div>

<div class="teal-card mb-3 text-sm">

### Camera Resolution: Use Native!

Cameras **must** be at **640×480 native resolution**. Do NOT set them to 224×224 or 512×512.

```python
# WRONG — camera driver will fail
{"width": 224, "height": 224}

# RIGHT — SmolVLA's preprocessor handles resizing internally
{"width": 640, "height": 480, "fps": 30}
```

</div>

<div class="blue-card text-sm">

### Install LeRobot with SmolVLA Support

```bash
cd lerobot
pip install -e ".[smolvla]"    # Installs feetech + smolvla deps
```

On Apple Silicon: use Python 3.10+ (MPS backend for inference).

</div>

</v-clicks>

---

<div style="height:1px;"></div>

---
layout: section
---

# Part 4
## The Full Pipeline — Recording, Training, Deployment

---

# The Pipeline: Our Actual Numbers

<v-clicks>

<div class="grid grid-cols-4 gap-3 mt-6 text-center">

<div class="accent-card">

### 1. Record
Teleoperate → 2 cameras + joints at 30 Hz

**45 episodes** (15 per bowl color)

</div>

<div class="teal-card">

### 2. Upload
Auto-pushed to HuggingFace Hub

`RajatDandekar/so101_box_to_bowl`

</div>

<div class="blue-card">

### 3. Train
Fine-tune on RunPod A100

**30K steps, ~2 hours**

</div>

<div class="purple-card">

### 4. Deploy
Mac M4 Pro, MPS backend

**30 Hz, real-time!**

</div>

</div>

</v-clicks>

<div v-click class="mt-5 card text-center text-sm">

**Three HuggingFace resources:** Dataset → `RajatDandekar/so101_box_to_bowl` | Trained model → `RajatDandekar/smolvla_box_to_bowl` | Base model → `lerobot/smolvla_base`

</div>

---

# Step 1: Recording Demonstrations

Record ~45 teleoperation episodes — **15 per bowl color**. A human moves the leader arm, the follower mirrors, and both camera streams + joint positions are recorded at 30 Hz.

<v-clicks>

<div class="card mt-3 mb-3 text-sm">

### The Recording Commands (One Color at a Time)

```bash
./record_box_to_bowl.sh red      # Creates the dataset, 15 episodes
./record_box_to_bowl.sh green    # Appends with --resume=true, 15 more
./record_box_to_bowl.sh blue     # Appends with --resume=true, 15 more
```

Each command sets the task string: `"Pick up the box and place it in the {color} bowl"`

</div>

<div class="teal-card text-sm">

### Recording Parameters

| Parameter | Value |
|-----------|-------|
| Episodes per color | 15 |
| Total episodes | ~45 |
| Episode duration | 60 seconds max |
| Reset time | 15 seconds between episodes |
| Recording FPS | 30 Hz |
| Cameras | 2 (overhead + wrist) at 640×480 |

</div>

</v-clicks>

---

# What Gets Recorded Per Timestep

<v-clicks>

<div class="card mt-4 mb-3 text-sm">

### Data Format (at 30 Hz)

```
observation.state:          [6 floats]   → shoulder_pan, shoulder_lift, elbow_flex,
                                           wrist_flex, wrist_roll, gripper
observation.images.webcam:  [480×640×3]  → overhead camera frame (RGB)
observation.images.arm_cam: [480×640×3]  → wrist camera frame (RGB)
action:                     [6 floats]   → leader arm joint positions (target)
task:                       string       → "Pick up the box and place it in the {color} bowl"
```

</div>

<div class="grid grid-cols-2 gap-4">

<div>
<img src="/figures/dataset-structure.png" class="rounded-lg" style="max-height:30vh; max-width:100%;" />
</div>

<div class="accent-card text-sm">

### The Dataset is Auto-Pushed

The recording script automatically pushes to HuggingFace as `RajatDandekar/so101_box_to_bowl`. No manual upload needed — LeRobot handles it.

This means you can record on your Mac and train on a cloud GPU without copying files.

</div>

</div>

</v-clicks>

---

# Tips for Good Demonstrations

<v-clicks>

<div class="grid grid-cols-2 gap-4 mt-3">

<div class="teal-card text-sm">

### DO This

- **Smooth, deliberate motions** — no jerking the leader arm
- **Consistent approach angles** and grasp positions across episodes
- **Complete the full task** — box must be **fully inside** the bowl before ending
- **Vary slightly** — small differences in box position teach generalization
- **Reset workspace** completely during the 15-second reset window
- **Discard bad episodes** — if you mess up, re-record that one

</div>

<div class="card text-sm" style="border-left: 3px solid #D4543A;">

### DON'T Do This

- **Fast, jerky motions** — the policy learns to be jerky
- **Inconsistent start positions** — confuses normalization
- **Partial tasks** — stopping before the box is in the bowl
- **Poor lighting** — shadows confuse the vision encoder
- **Move the camera** between recording sessions — keep it fixed!
- **Record all colors at once** — do one color batch at a time

</div>

</div>

<div class="accent-card mt-3 text-center text-sm">

**You are the expert teacher.** The robot will mimic your demonstrations exactly. Smooth, consistent demos → smooth, consistent robot behavior. **Garbage in, garbage out.**

</div>

</v-clicks>

---

# Step 2: Training on RunPod

Fine-tune the pretrained `lerobot/smolvla_base` on your recorded demonstrations. The VLM backbone retains its language understanding — only the action head learns your robot's joint space.

<v-clicks>

<div class="card mt-3 mb-3 text-sm">

### Setup on RunPod (Run Once After Pod Starts)

```bash
apt-get update && apt-get install -y ffmpeg
pip install "lerobot[smolvla]"
huggingface-cli login --token $HF_TOKEN
```

</div>

<div class="grid grid-cols-2 gap-4">

<div class="teal-card text-sm">

### GPU Options

| GPU | VRAM | Batch Size | Training Time |
|-----|------|-----------|---------------|
| **A100 80GB** | 80 GB | **64** | **~2 hours** |
| A40 48GB | 48 GB | 32 | ~3.5 hours |
| 4090 24GB | 24 GB | 16 | ~5 hours |

</div>

<div class="blue-card text-sm">

### Training Command

```bash
lerobot-train \
  --policy.path=lerobot/smolvla_base \
  --policy.repo_id="RajatDandekar/
    smolvla_box_to_bowl" \
  --policy.device=cuda \
  --policy.use_amp=true \
  --dataset.repo_id="RajatDandekar/
    so101_box_to_bowl" \
  --batch_size=64 \
  --steps=30000
```

</div>

</div>

</v-clicks>

---

# The Rename Map — A Critical Detail

<v-clicks>

<div class="card mt-4 mb-3 text-sm" style="border-left: 3px solid #D4543A;">

### The Problem

Your dataset has cameras named `webcam` and `arm_cam`. But SmolVLA's pretrained checkpoint expects `camera1` and `camera2`.

**If you forget the rename map:** the policy silently receives wrong/empty camera inputs → trains on garbage → model looks converged but produces random actions. **This is a silent failure.**

</div>

<div class="teal-card mb-3 text-sm">

### The Fix — Add to BOTH Training AND Inference

```bash
--rename_map='{"observation.images.webcam": "observation.images.camera1",
               "observation.images.arm_cam": "observation.images.camera2"}'
```

This must be present in **every** command that touches the model — training, inference, evaluation. Miss it once → broken pipeline.

</div>

<div class="accent-card text-center text-sm">

The trained model is automatically pushed to HuggingFace as `RajatDandekar/smolvla_box_to_bowl`. Train in the cloud, deploy locally.

</div>

</v-clicks>

---

# Step 3: Inference — Running the Robot Autonomously

<v-clicks>

<div class="card mt-3 mb-3 text-sm">

### The Basic Inference Command

```bash
lerobot-record \
  --robot.type=so101_follower \
  --robot.port="/dev/tty.wchusbserial5AE60830811" \
  --robot.id=my_follower \
  --robot.cameras='{"webcam": {"type": "opencv", "index_or_path": 0,
    "width": 640, "height": 480, "fps": 30},
    "arm_cam": {"type": "opencv", "index_or_path": 1,
    "width": 640, "height": 480, "fps": 30}}' \
  --policy.path="RajatDandekar/smolvla_box_to_bowl" \
  --policy.device=mps \
  --dataset.single_task="Pick up the box and place it in the bowl
    which has the same color as that of the ocean"
```

Note the semantic test: **"ocean"** → the robot goes to the **blue** bowl!

</div>

<div class="accent-card text-sm">

### What Happens at 30 Hz

1. Cameras capture frames at 640×480
2. SmolVLA receives images + language instruction
3. Model outputs an **action chunk of 50 future joint positions**
4. Actions queued and executed one per control step (33ms each)
5. When queue empties (~1.7 seconds), model runs again
6. Continues for the episode duration (default: 600 seconds)

</div>

</v-clicks>


---

<div style="height:1px;"></div>

---

# Voice-Controlled Inference

A background thread continuously listens via **Whisper STT**. Speak a new instruction at any time — the robot changes behavior on the **very next control step** with zero downtime.

<v-clicks>

<div class="grid grid-cols-2 gap-4 mt-3">

<div class="card text-sm">

### How It Works

1. **Main thread** (30 Hz): read cameras → SmolVLA forward pass → send actions
2. **Background thread** (continuous): microphone → Whisper STT → transcript
3. Transcript updates a thread-safe `TaskState` object
4. Next control step reads new task → SmolVLA adjusts behavior

```bash
# Voice mode (requires microphone)
python voice_inference.py

# Text mode (type instructions)
python voice_inference.py --text_mode
```

</div>

<div class="teal-card text-sm">

### Semantic Grounding Examples

| What you say | What happens |
|---|---|
| "Put the box in the blue bowl" | Literal → blue |
| "Move it to the ocean-colored bowl" | Semantic → blue |
| "The grassy bowl" | Semantic → green |
| "The one that looks like blood" | Semantic → red |
| "The emerald one" | Semantic → green |

The robot runs for up to **60 minutes** continuously. Just speak to redirect it.

</div>

</div>

</v-clicks>

---

# Intent Classification — Robust Voice Control

For noisy speech environments, map free-form transcripts to **exact canonical task strings** using sentence-transformers semantic similarity.

<v-clicks>

<div class="card mt-3 mb-3 text-sm">

### The Pipeline

```
Voice Input → Whisper STT → "put it in the leafy one"
                                      ↓
              Sentence Transformer → encode to embedding
                                      ↓
              Cosine similarity vs reference embeddings:
                  green: ["green", "grass", "leaves", "lime", "emerald", "forest"]
                  blue:  ["blue", "sky", "ocean", "sapphire", "azure"]
                  red:   ["red", "blood", "fire", "ruby"]
                                      ↓
              Best match: green (similarity: 0.87)
                                      ↓
              Canonical: "Pick up the box and place it in the green bowl"
```

</div>

<div class="accent-card text-sm">

### Why This Matters

SmolVLA performs best when the inference-time task string **exactly matches** the training-time task string. Free-form voice input like "put it in the leafy one" might confuse the model. Intent classification ensures the **exact canonical string** reaches SmolVLA every time.

```bash
python intent_inference.py              # Voice mode with video recording
python intent_inference.py --text_mode  # Keyboard mode
```

</div>

</v-clicks>

---

<div style="height:1px;"></div>

---
layout: section
---

# Part 5
## 10 Critical Bugs & Integration Lessons

---

# The 10 Bugs That Almost Broke Everything

These bugs cost us **days** of debugging. Each one is a silent failure — the code runs, no error messages, but the robot does garbage. If you're building a similar system, **read these carefully**.

<v-clicks>

<div class="grid grid-cols-2 gap-3 mt-3 text-sm">

<div class="accent-card">

### Hardware-Side Bugs
1. State Vector Order (THE BIGGEST)
2. Camera Rename Map
3. Camera Resolution
4. Episode Length Too Short
5. LeRobot Import Paths

</div>

<div class="teal-card">

### Software-Side Bugs
6. Action Chunking (Must Use Queue)
7. Do NOT Call .float()
8. Features Not Populated
9. Missing Preprocessor/Postprocessor
10. torch.load Allowlist

</div>

</div>

<div class="card mt-3 text-center text-sm" style="border: 2px solid var(--claude-accent);">

**Every single one of these is a silent failure.** The code runs, the model loads, training "converges" — but the robot moves randomly. That's what makes them so dangerous.

</div>

</v-clicks>

---

# Bug #1: State Vector Order (THE BIGGEST BUG)

<v-clicks>

<div class="card mt-3 mb-3 text-sm" style="border-left: 4px solid #D4543A;">

### The Problem

Using `sorted()` on joint names produces **alphabetical** order:

```
elbow_flex, gripper, shoulder_lift, shoulder_pan, wrist_flex, wrist_roll
```

But the model was trained with **motor-definition** order:

```
shoulder_pan, shoulder_lift, elbow_flex, wrist_flex, wrist_roll, gripper
```

Per-element normalization applies mean/std to the **wrong joints** → every joint gets the wrong normalization → garbage model input → **erratic robot motion**.

</div>

<div class="teal-card mb-3 text-sm">

### The Fix — Build State Vector Explicitly

```python
JOINT_NAMES = ["shoulder_pan", "shoulder_lift", "elbow_flex",
               "wrist_flex", "wrist_roll", "gripper"]
state = [obs.get(f"{j}.pos", 0.0) for j in JOINT_NAMES]
```

**Never** rely on dictionary iteration order or `sorted()` for joint names.

</div>

<div class="accent-card text-center text-sm">

**Why it's so dangerous:** No error message. The robot moves — just to the wrong places. Training loss still converges. You think the model is bad, but it's the **data pipeline** that's broken.

</div>

</v-clicks>

---

# Bug #2: Action Chunking — Must Use Action Queue

<v-clicks>

<div class="card mt-3 mb-3 text-sm" style="border-left: 4px solid #D4543A;">

### The Problem

Calling `policy.sample_actions()` **every step** (30 Hz) and using `action[0]` each time generates a brand new 50-step trajectory every 33ms. The robot always jumps to the **start** of a new trajectory → **violent jerking**.

</div>

<div class="teal-card mb-3 text-sm">

### The Fix

Use `predict_action()` from `lerobot.utils.control_utils` — the **exact same function** that `lerobot-record` uses internally.

It manages an internal action **deque** of 50 actions. The model is only queried when the queue is empty (~every 1.7 seconds).

```python
from lerobot.utils.control_utils import predict_action
action = predict_action(observation, policy, device, preprocessor,
                        postprocessor, task=task, robot_type=robot.robot_type)
```

</div>

<div class="accent-card text-center text-sm">

**The difference between smooth motion and dangerous jerking is one function call.** This is the single most important API choice in the entire deployment.

</div>

</v-clicks>

---

# Bug #3: Do NOT Call .float() on SmolVLA

<v-clicks>

<div class="card mt-3 mb-3 text-sm" style="border-left: 4px solid #D4543A;">

### The Problem

```python
# WRONG:
smolvla_policy.to(device).float()
```

This converts the **entire model** to float32. `lerobot-record` does NOT do this. It changes the model's numerical behavior and produces **different (wrong) outputs**.

SmolVLA internally uses mixed precision — some layers are bfloat16, some are float32. Forcing everything to float32 breaks the carefully tuned numerical behavior.

</div>

<div class="teal-card text-sm">

### The Fix

```python
# RIGHT:
smolvla_policy.to(device)    # NO .float()!
```

Just `.to(device)` — **never** `.float()`, `.half()`, or `.bfloat16()`. Let the model manage its own dtypes.

</div>

</v-clicks>

---

# Bug #4: Features Not Populated by from_pretrained

<v-clicks>

<div class="card mt-3 mb-3 text-sm" style="border-left: 4px solid #D4543A;">

### The Problem

`SmolVLAPolicy.from_pretrained()` does NOT populate `input_features`, `output_features`, or `image_features` from the HuggingFace config. Methods like `prepare_images()` fail with: **"All image features are missing."**

</div>

<div class="teal-card text-sm">

### The Fix — Manually Set Features

```python
from lerobot.configs.types import FeatureType, PolicyFeature

smolvla_config.input_features = {
    "observation.state": PolicyFeature(type=FeatureType.STATE, shape=(6,)),
    "observation.images.camera1": PolicyFeature(type=FeatureType.VISUAL, shape=(3, 256, 256)),
    "observation.images.camera2": PolicyFeature(type=FeatureType.VISUAL, shape=(3, 256, 256)),
}
smolvla_config.output_features = {
    "action": PolicyFeature(type=FeatureType.ACTION, shape=(6,)),
}
```

Set these **before** loading the model weights.

</div>

</v-clicks>

---

# Bug #5: Missing Preprocessor/Postprocessor

<v-clicks>

<div class="card mt-3 mb-3 text-sm" style="border-left: 4px solid #D4543A;">

### The Problem

The postprocessor contains **normalization stats** (mean/std from the training dataset). Without it, raw model outputs are in **normalized space** — meaningless numbers to the robot.

The robot receives actions like `[-0.3, 0.7, 0.1, ...]` when it expects degree values like `[45.0, 120.0, 30.0, ...]`.

</div>

<div class="teal-card text-sm">

### The Fix — Load from Pretrained Checkpoint

```python
from lerobot.processor import PolicyProcessorPipeline

preprocessor = PolicyProcessorPipeline.from_pretrained(
    pretrained_model_name_or_path=smolvla_path,
    config_filename="policy_preprocessor.json",
    overrides={"device_processor": {"device": device},
               "rename_observations_processor": {"rename_map": rename_map}},
)
postprocessor = PolicyProcessorPipeline.from_pretrained(
    pretrained_model_name_or_path=smolvla_path,
    config_filename="policy_postprocessor.json",
)
```

These contain the exact mean/std from your training dataset. **Without them, actions are gibberish.**

</div>

</v-clicks>

---

# Bugs #6–8: Camera, Resolution, Episode Length

<v-clicks>

<div class="card mt-3 mb-2 text-sm" style="border-left: 4px solid #D4543A;">

### Bug #6: Camera Rename Map Required

Camera names `webcam`/`arm_cam` don't match policy expectation `camera1`/`camera2`. The rename map must be present in **both** training and inference. **Forgetting it causes silent failures** — the model trains/infers on mismatched camera inputs.

</div>

<div class="card mb-2 text-sm" style="border-left: 4px solid #D4543A;">

### Bug #7: Camera Resolution — Use Native

Setting camera config to 224×224 or 512×512 **fails** because the webcam doesn't support those resolutions natively. Always capture at **640×480** (native). SmolVLA's `prepare_images()` handles resizing to 512×512 with padding **internally**.

</div>

<div class="card mb-2 text-sm" style="border-left: 4px solid #D4543A;">

### Bug #8: Episode Length — 50 Steps Is Not Enough

Default `steps_per_episode=50` gives ~1.7 seconds at 30 Hz. Pick-and-place needs **30-50 seconds**.

```bash
--dataset.episode_time_s=60         # 60 seconds per episode (recording)
--steps_per_episode 1500            # 50 seconds at 30Hz (inference)
```

</div>

</v-clicks>

---

# Bugs #9–10: Serialization and Import Paths

<v-clicks>

<div class="card mt-3 mb-3 text-sm" style="border-left: 4px solid #D4543A;">

### Bug #9: torch.load Needs NormalizationMode Allowlisted

Checkpoints contain `NormalizationMode` enum which `weights_only=True` blocks by default.

```python
from lerobot.configs.types import NormalizationMode
torch.serialization.add_safe_globals([NormalizationMode])
```

Without this, loading any checkpoint crashes with a cryptic serialization error.

</div>

<div class="card mb-3 text-sm" style="border-left: 4px solid #D4543A;">

### Bug #10: LeRobot Import Paths

It's `so_follower`, **NOT** `so101_follower`:

```python
from lerobot.robots.so_follower.config_so_follower import SOFollowerRobotConfig
from lerobot.cameras.opencv.configuration_opencv import OpenCVCameraConfig
```

Camera config uses `index_or_path` (not `camera_index`). Robot/leader IDs must **match existing calibration files**.

</div>

<div class="accent-card text-center text-sm">

**The Golden Rule:** To match `lerobot-record` inference exactly, use `predict_action()` from `lerobot.utils.control_utils`. Don't try to manually replicate the pipeline — there are too many subtle details that must match exactly.

</div>

</v-clicks>

---

# Summary: The DOs and DON'Ts

<v-clicks>

<div class="grid grid-cols-2 gap-4 mt-3">

<div class="teal-card text-sm">

### DO

- Use `predict_action()` for inference — never reimplement
- Use `lerobot-record` in policy mode for deployment
- Capture cameras at **640×480 native** resolution
- Build state vector with **explicit joint order**
- Load preprocessor/postprocessor from checkpoint
- Add rename map to **every** command
- Set episode length to 50+ seconds
- Back up calibration files
- Use cloud GPU for training, local Mac for inference

</div>

<div class="card text-sm" style="border-left: 3px solid #D4543A;">

### DON'T

- Call `sample_actions()` every control step
- Call `.float()` on SmolVLA
- Use `sorted()` for joint name ordering
- Set camera resolution to 224×224 or 512×512
- Forget the camera rename map
- Leave `steps_per_episode` at default (50)
- Use `so101_follower` (it's `so_follower`)
- Skip the preprocessor/postprocessor loading
- Assume `from_pretrained()` sets all features
- Use `weights_only=True` without allowlisting

</div>

</div>

</v-clicks>

---

# RLT: Reinforcement Learning from Trajectory (Experimental)

An extension that adds **RL fine-tuning** on top of SmolVLA's frozen embeddings for precision phases.

<v-clicks>

<div class="grid grid-cols-2 gap-4 mt-3">

<div class="card text-sm">

### Stage 1: Train RLT Encoder (Offline)

Train an encoder-decoder on SmolVLA's embeddings from demonstration data.

```bash
python scripts/train_rlt_stage1.py
```

Encoder loss: 0.707 (converged)

### Stage 2: Online RL with Human Intervention

Robot runs SmolVLA autonomously. When it makes mistakes, **grab the leader arm** to correct it. These corrections create high-quality RL transitions.

</div>

<div class="teal-card text-sm">

### VLA ↔ Actor Switching

```bash
./run_rlt_inference.sh
```

- Starts in **VLA mode** (normal SmolVLA)
- Press **SPACE** → RL actor takes over (precision phase)
- Press **SPACE** again → back to VLA
- The actor **replaces** VLA during critical phases (not blending)

### Current Status

| Metric | Value |
|--------|-------|
| Stage 2 episodes | 20 |
| RL updates | 630 |
| Status | Needs gradient clipping + more episodes |

</div>

</div>

</v-clicks>


---

<div style="height:1px;"></div>

---

<div style="height:1px;"></div>

---
layout: section
---

# Part 6
## Live Demo — SmolVLA Picking and Placing

---

# The Demo: Box-to-Bowl with Language Control

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

<v-clicks>

<div class="card mb-3 text-sm">

### Task
"Pick up the box and place it in the {color} bowl"

3 targets: red, green, blue — selected by natural language.

</div>

<div class="card mb-3 text-sm">

### Our Actual Setup
- **Robot:** SO-101 follower arm
- **Cameras:** 2 (overhead + wrist) at 640×480
- **Policy:** SmolVLA fine-tuned on **45 episodes** (30K steps)
- **Compute:** Mac M4 Pro (MPS backend)
- **Control rate:** 30 Hz
- **Action chunk:** 50 steps (~1.7 seconds lookahead)

</div>

<div class="accent-card text-sm">

### The Full Path

45 teleoperation demos → auto-push to HuggingFace → fine-tune on RunPod A100 (2 hours) → download → deploy on Mac → robot picks and places!

</div>

</v-clicks>

</div>

<div v-click>

<img src="/figures/setup-photo.jpg" class="rounded-lg" style="max-height:50vh; max-width:100%;" />

<div class="text-xs text-center mt-1 opacity-60">The actual hardware setup used in our demo</div>

</div>

</div>

---

# What Worked

<v-clicks>

<div class="grid grid-cols-2 gap-4 mt-4">

<div class="teal-card text-sm">

### Semantic Grounding Is Real
Training with literal colors **generalizes to metaphors**: "ocean" → blue, "grass" → green, "blood" → red. VLM pre-training delivers zero-shot language understanding.

</div>

<div class="teal-card text-sm">

### 45 Episodes Is Enough
With SmolVLA's pretrained backbone, ~45 demos sufficed for reliable 3-target pick-and-place. The pretrained VLM already understands objects — fine-tuning only teaches your robot's kinematics.

</div>

<div class="teal-card text-sm">

### Cloud Train, Local Deploy
2 hours on A100 ($2-3), deploy on M4 Pro at 30 Hz. HuggingFace Hub makes the cloud→local handoff completely seamless.

</div>

<div class="teal-card text-sm">

### Voice Control Works Live
Speak a new instruction → behavior changes on the **very next control step**. No stopping, no restart, no episode boundaries. Continuous 60-minute operation.

</div>

</div>

</v-clicks>

---

# What Didn't Work (Yet)

<v-clicks>

<div class="grid grid-cols-2 gap-4 mt-4">

<div class="card text-sm" style="border-left: 3px solid #D4543A;">

### Precision Grasping
The gripper sometimes misses the box or doesn't close firmly enough. The 6-DOF arm lacks force feedback — the policy can't "feel" when it has a solid grasp. **Fix:** RLT actor for precision phases.

</div>

<div class="card text-sm" style="border-left: 3px solid #D4543A;">

### Recovery from Drops
If the gripper fails to grasp and the box falls, the robot continues executing the planned trajectory as if it succeeded. **Fix:** Closed-loop re-planning with grasp detection.

</div>

<div class="card text-sm" style="border-left: 3px solid #D4543A;">

### RL Actor Still Unstable
After 20 episodes and 630 RL updates, the actor's critic loss exploded to ~4 trillion. Needs gradient clipping and 100+ more episodes.

</div>

<div class="card text-sm" style="border-left: 3px solid #D4543A;">

### Lighting Sensitivity
Camera auto-exposure changes with sunlight → image distribution shifts → policy struggles. **Fix:** Record demos under varied lighting conditions, or disable auto-exposure.

</div>

</div>

<div class="accent-card mt-3 text-center text-sm">

**These are all solvable.** The architecture works. The bugs were in the integration, not the model. With more data and the RLT pipeline, reliability will improve significantly.

</div>

</v-clicks>

---

<div style="height:1px;"></div>

---
layout: section
---

# Part 7
## Bimanual Inference — Two Arms, One Brain

---

# Why Bimanual Manipulation?

Single-arm pick-and-place is impressive, but the real world demands **two-arm coordination**.

<v-clicks>

<div class="grid grid-cols-3 gap-3 mt-3">

<div class="card text-sm">

### Handover Tasks
One arm holds or presents an object, the other picks from it.

<img src="https://arxiv.org/html/2410.24164v1/assets/x8.png" class="rounded-lg mt-2" style="max-height:14vh;" />

<div class="text-xs text-center mt-1 opacity-60">pi0: multi-stage bimanual tasks (laundry, bussing, box assembly)</div>

</div>

<div class="card text-sm">

### Assembly Tasks
One arm stabilizes, the other inserts or attaches. Requires **synchronized timing**.

<img src="https://arxiv.org/html/2410.13126v1/assets/x1.png" class="rounded-lg mt-2" style="max-height:14vh;" />

<div class="text-xs text-center mt-1 opacity-60">ALOHA Unleashed: shirt hanging + shoelace tying</div>

</div>

<div class="card text-sm">

### Large Object Manipulation
Both arms grip and move together — folding cloth, lifting trays.

<img src="https://arxiv.org/html/2410.24164v1/assets/figures/fig2_final.jpeg" class="rounded-lg mt-2" style="max-height:14vh;" />

<div class="text-xs text-center mt-1 opacity-60">pi0: mobile manipulator folding laundry</div>

</div>

</div>

<div class="accent-card mt-3 text-center text-sm">

**The key challenge:** A single policy must learn **coordinated 12-DOF control** (6 joints x 2 arms) from shared visual input, deciding what *each* arm should do at every timestep.

</div>

</v-clicks>

---

# Bimanual in the Wild — pi0 & ALOHA

<div class="grid grid-cols-2 gap-4 mt-3">

<div v-click>

<video autoplay muted loop playsinline style="max-height:25vh; width:100%; border-radius:8px; object-fit:cover;">
<source src="https://website.pi-asset.com/v2/upload/lowres_processed2xspeed_apartment_folding_4_13min.mp4" type="video/mp4">
</video>
<div class="text-xs text-center mt-1 opacity-60">pi0: autonomous bimanual laundry folding (13 min continuous)</div>

</div>

<div v-click>

<video autoplay muted loop playsinline style="max-height:25vh; width:100%; border-radius:8px; object-fit:cover;">
<source src="https://aloha-unleashed.github.io/assets/LaceMessy.mp4" type="video/mp4">
</video>
<div class="text-xs text-center mt-1 opacity-60">ALOHA Unleashed: tying shoelaces with two arms</div>

</div>

</div>

<v-clicks>

<div class="grid grid-cols-2 gap-4 mt-3">

<div class="card text-sm">

### What These Systems Proved
- A **single VLA policy** can control two 7-DOF arms simultaneously
- Language-conditioned bimanual tasks ("fold the shirt", "tie the laces")
- The same **flow matching** backbone we covered in Part 2
- No explicit coordination logic — learned end-to-end from demos

</div>

<div class="teal-card text-sm">

### Why This Matters for Us
- The action expert simply outputs a **larger action vector** (14-DOF)
- **SmolVLA has the same architecture** — if pi0 can do it, SmolVLA can too
- ALOHA showed bimanual works on **low-cost hardware**
- We just need to extend our SO-101 setup to two arms

</div>

</div>

</v-clicks>


---

<div style="height:1px;"></div>

---

# pi0's Bimanual Results: The Bar We're Chasing

<div class="grid grid-cols-2 gap-4 mt-3">

<div v-click>

<video autoplay muted loop playsinline style="max-height:22vh; width:100%; border-radius:8px; object-fit:cover;">
<source src="https://website.pi-asset.com/v2/upload/lowres_processed1xspeed_build_box_3.mp4" type="video/mp4">
</video>
<div class="text-xs text-center mt-1 opacity-60">pi0: bimanual box assembly</div>

</div>

<div v-click>

<video autoplay muted loop playsinline style="max-height:22vh; width:100%; border-radius:8px; object-fit:cover;">
<source src="https://website.pi-asset.com/v2/upload/lowres_processed2xspeed_bussing_2.mp4" type="video/mp4">
</video>
<div class="text-xs text-center mt-1 opacity-60">pi0: table bussing (bimanual coordination)</div>

</div>

</div>

<v-clicks>

<div class="grid grid-cols-3 gap-3 mt-3">

<div class="card text-sm">

<img src="https://arxiv.org/html/2410.24164v1/assets/x2.png" class="rounded-lg" style="max-height:16vh;" />

<div class="text-xs text-center mt-1 opacity-60">pi0 trains on 7 different robot embodiments — including bimanual</div>

</div>

<div class="teal-card text-sm text-center">

### pi0's Scale
- **10,000+** hours of training data
- **7 robot platforms** (single + bimanual)
- **3B parameters**
- Complex multi-stage tasks

**We'll do it with 5 demos and 450M params.**

</div>

<div class="card text-sm">

<img src="https://arxiv.org/html/2410.13126v1/assets/x4.png" class="rounded-lg" style="max-height:16vh;" />

<div class="text-xs text-center mt-1 opacity-60">ALOHA Unleashed: learned bimanual behaviors</div>

</div>

</div>

</v-clicks>

---

# Our Bimanual Task: Box Pass Between Arms

<v-clicks>

<div class="card mt-3 text-sm" style="border-left: 3px solid var(--claude-accent);">

### The Task

**"Right arm passes the red bowl with the box to the left arm. Left arm picks up the box and places it in the green bowl."**

This is a true bimanual coordination task — neither arm can complete it alone. The right arm must **present** the bowl while the left arm **reaches in and picks** from it.

</div>

<div class="grid grid-cols-2 gap-4 mt-3">

<div class="teal-card text-sm">

### Hardware: 4 Arms + 3 Cameras

| Component | Count |
|-----------|-------|
| Follower arms (autonomous) | 2 (left + right) |
| Leader arms (teleoperation) | 2 (left + right) |
| Cameras | 3 (left wrist, right wrist, overhead) |
| Action dimensions | **12** (6 per arm) |
| USB connections | 7 total |

</div>

<div class="blue-card text-sm">

### vs Single-Arm Setup

| | Single Arm | Bimanual |
|--|-----------|----------|
| Arms | 1 follower + 1 leader | 2 + 2 |
| Cameras | 2 | **3** |
| Action DOF | 6 | **12** |
| Coordination | None | Required |
| Teleoperation | One hand | **Both hands** |

</div>

</div>

</v-clicks>

---

# The Bimanual Pipeline: Our Numbers

<v-clicks>

<div class="grid grid-cols-4 gap-3 mt-6 text-center">

<div class="accent-card">

### 1. Record
Bimanual teleoperation — both leader arms simultaneously

**5 episodes**

</div>

<div class="teal-card">

### 2. Upload
Auto-pushed to HuggingFace Hub

`RajatDandekar/so101_bimanual_box_pass`

</div>

<div class="blue-card">

### 3. Train
Fine-tune on RunPod A100

**10K steps, ~1 hour**

</div>

<div class="purple-card">

### 4. Deploy
Mac Apple Silicon, MPS backend

**~2.7 Hz inference**

</div>

</div>

</v-clicks>

<div v-click class="mt-4 card text-center text-xs" style="padding: 8px 12px; line-height: 1.6;">

**HuggingFace Resources:**<br>
Dataset → `RajatDandekar/so101_bimanual_box_pass`<br>
Trained model → `RajatDandekar/smolvla_bimanual_box_pass`<br>
Base model → `lerobot/smolvla_base`

</div>

---

# The Triple-Camera Naming Trap

The biggest bimanual-specific bug: **double-prefixed camera names**.

<v-clicks>

<div class="card mt-4 mb-3 text-sm" style="border-left: 3px solid #D4543A;">

### The Problem

`BiSOFollower` adds `left_`/`right_` prefixes to ALL keys — including camera names that already have a prefix. The left wrist camera, named `left_wrist` in the arm config, becomes `left_left_wrist` in the observation dict.

</div>

<div class="teal-card mb-3 text-sm">

### The Rename Map (Must Be Exact)

| Physical Camera | Bimanual Key | SmolVLA Expects |
|----------------|-------------|-----------------|
| Left wrist cam | `left_left_wrist` | `camera1` |
| Right wrist cam | `right_right_wrist` | `camera2` |
| Overhead webcam | `right_webcam` | `camera3` |

</div>

<div class="accent-card text-center text-sm">

**This rename map must be identical in training AND inference.** A mismatch means the model receives garbage images and outputs erratic actions — with no error message.

</div>

</v-clicks>

---

# Bimanual Teleoperation: The Hard Part

<v-clicks>

<div class="grid grid-cols-2 gap-4 mt-4">

<div class="card text-sm" style="border-left: 3px solid #D4543A;">

### Why It's Difficult
- Operating **two leader arms simultaneously** requires motor coordination most people don't have
- Early demos had jerky, uncoordinated motion that confused the model
- You need consistent approach angles, grasp positions, and handover timing across all episodes
- With only **5 episodes**, every demo must be high quality

</div>

<div class="teal-card text-sm">

### Tips That Worked

1. **Practice 5–10 times** without recording
2. **Sequential, not simultaneous** — right arm moves first, then left
3. **Slow and deliberate** — fast bimanual motions confuse the model
4. **Discard bad episodes freely** — quality >> quantity
5. **Label your USB cables** — with 7 USB connections, port confusion is constant

</div>

</div>

<div class="blue-card mt-4 text-sm">

### What Gets Recorded Per Timestep

```
observation.state:                     [12 floats]  → 6 joints x 2 arms
observation.images.left_left_wrist:    [480x640x3]  → left wrist camera
observation.images.right_right_wrist:  [480x640x3]  → right wrist camera
observation.images.right_webcam:       [480x640x3]  → overhead camera
action:                                [12 floats]  → target joint positions for both arms
```

</div>

</v-clicks>

---

# Demo: Our Bimanual Inference in Action

The trained SmolVLA model autonomously controls both SO-101 arms:

<div class="grid grid-cols-2 gap-3 mt-3">

<div v-click>

<video controls muted playsinline style="max-height:28vh; width:100%; border-radius:8px;">
<source src="/videos/bimanual_demo_1.mp4" type="video/mp4">
</video>
<div class="text-xs text-center mt-1 opacity-60">Run 1 — right arm passes bowl, left arm picks box</div>

</div>

<div v-click>

<video controls muted playsinline style="max-height:28vh; width:100%; border-radius:8px;">
<source src="/videos/bimanual_demo_2.mp4" type="video/mp4">
</video>
<div class="text-xs text-center mt-1 opacity-60">Run 2 — full bimanual coordination sequence</div>

</div>

<div v-click>

<video controls muted playsinline style="max-height:28vh; width:100%; border-radius:8px;">
<source src="/videos/bimanual_demo_3.mp4" type="video/mp4">
</video>
<div class="text-xs text-center mt-1 opacity-60">Run 3 — box placed in green bowl</div>

</div>

<div v-click>

<video controls muted playsinline style="max-height:28vh; width:100%; border-radius:8px;">
<source src="/videos/bimanual_demo_4.mp4" type="video/mp4">
</video>
<div class="text-xs text-center mt-1 opacity-60">Run 4 — consistent handover behavior</div>

</div>

</div>

<div v-click class="mt-2 card text-center text-sm">

**5 demos → 10K training steps → autonomous bimanual coordination.** Full code: [github.com/RajatDandekar/SmolVLA_MRL2Bootcamp_Bimanual](https://github.com/RajatDandekar/SmolVLA_MRL2Bootcamp_Bimanual)

</div>

---

<div style="height:1px;"></div>

---

# What We've Learned Today

<div class="grid grid-cols-3 gap-3 mt-4 text-sm">

<div class="accent-card">

### Part 1: Open-Source VLAs
OpenVLA (7B, action tokens, DinoV2+SigLIP) and SmolVLA (450M, flow matching, efficiency tricks). Attention patterns compared across all three VLAs.

</div>

<div class="teal-card">

### Part 2: Flow Matching
Linear interpolation → velocity field → MSE loss. Straighter paths than DDPM → fewer steps → faster inference. **The engine behind pi0 and SmolVLA.**

</div>

<div class="blue-card">

### Parts 3–4: Real Implementation
45 demos, 3 bowl colors, dual cameras, RunPod training, Mac deployment. Voice control with Whisper. Intent classification with sentence-transformers.

</div>

</div>

<div class="grid grid-cols-2 gap-3 mt-3 text-sm">

<div class="purple-card">

### Part 5: 10 Critical Bugs
State vector order, action chunking, .float(), rename maps, preprocessors, camera resolution. Each one a silent failure. **Read these before you build.**

</div>

<div class="card" style="border: 2px solid var(--claude-accent);">

### Part 6: Live Demo
Box-to-bowl pick-and-place. Semantic grounding ("ocean" → blue). Voice control with zero-downtime task switching.

</div>

</div>

<div class="grid grid-cols-1 gap-3 mt-3 text-sm">

<div class="card" style="border: 2px solid var(--claude-teal);">

### Part 7: Bimanual Inference
Two SO-101 arms, one SmolVLA policy, 12-DOF coordinated control. 5 demos → 10K steps → autonomous box handover between arms.

</div>

</div>


---

<div style="height:1px;"></div>


---

<div style="height:1px;"></div>

---

# The Journey So Far

<v-clicks>

<div class="card mt-3 mb-2 text-center text-sm">

**Lecture 1:** Diffusion from scratch → noise to actions → U-Net + FiLM + receding horizon

</div>

<div class="card mb-2 text-center text-sm">

**Lecture 2:** Language encoding (BoW → GRU → Transformer) → mini-VLA (fails) → ViT + VLM → RT-2 → pi0

</div>

<div class="accent-card mb-2 text-center text-sm">

**Lecture 3 (Today):** OpenVLA + SmolVLA → flow matching from scratch → real SO-101 implementation → 10 critical bugs → voice-controlled demo → bimanual two-arm coordination

</div>

<div class="card mb-2 text-center text-lg">

**You now have the complete picture:** from the math of diffusion and flow matching, through VLA architectures, all the way to a **working robot on your desk** — with all the real-world bugs documented.

</div>

</v-clicks>

---

# Resources & Further Reading

<div class="grid grid-cols-2 gap-4 mt-4 text-sm">

<div class="card">

### Papers
- **OpenVLA** (Kim et al., 2024) — 7B open-source VLA
- **SmolVLA** (HuggingFace, 2025) — 450M efficient VLA
- **Flow Matching** (Lipman et al., 2023) — The straight-path framework
- **pi0** (Black et al., 2024) — Diffusion-based VLA with flow matching
- **FAST Tokenizer** (Pertsch et al., 2025) — Better action tokenization

</div>

<div class="card">

### Hands-On Resources
- [Single-Arm Repo](https://github.com/RajatDandekar/SmolVLA_MRL2Bootcamp)
- [Bimanual Repo](https://github.com/RajatDandekar/SmolVLA_MRL2Bootcamp_Bimanual)
- [LeRobot GitHub](https://github.com/huggingface/lerobot)
- [SmolVLA on HuggingFace](https://huggingface.co/lerobot/smolvla_base)
- [Our Dataset](https://huggingface.co/datasets/RajatDandekar/so101_box_to_bowl)
- [Our Trained Model](https://huggingface.co/RajatDandekar/smolvla_box_to_bowl)
- [Bimanual Dataset](https://huggingface.co/datasets/RajatDandekar/so101_bimanual_box_pass)
- [Bimanual Model](https://huggingface.co/RajatDandekar/smolvla_bimanual_box_pass)
- [SO-101 Build Guide](https://github.com/TheRobotStudio/SO-ARM100)

</div>

</div>

<div class="accent-card mt-4 text-sm">

### Notebooks from Today

| Notebook | What You'll Build |
|----------|------------------|
| **Flow_Matching_From_Scratch** | Velocity fields, Euler integration, OT coupling, conditioned robot actions |
| **Cross_Attention_And_VLA_Architectures** | Cross-attention from scratch, action tokenization, 3-way attention mask comparison |
| **SmolVLA_Efficiency_Tricks** | PixelShuffle, layer skipping, async inference simulation |
| **SmolVLA_Deployment_Simulation** | Dataset exploration, action chunking, voice pipeline, intent classification |
| **The_10_Bugs_Interactive_Debugging** | All 10 critical bugs as hands-on exercises |

</div>

---

# Thank You!

<div class="mt-8 text-center">
  <span class="px-4 py-2 rounded-lg text-lg" style="background:#c2785c;color:#fff;font-weight:700;">
    Modern Robot Learning from Scratch — V2
  </span>
</div>

<div class="mt-6 text-center opacity-60">

**Lecture 3: From VLAs to Real Robots — SmolVLA, Flow Matching & SO-101 Deployment**

</div>

<div class="grid grid-cols-3 gap-4 mt-8 text-center text-sm">

<div class="card">

### Your Assignment
Clone the [SmolVLA repo](https://github.com/RajatDandekar/SmolVLA_MRL2Bootcamp). Record 45 demos. Fine-tune SmolVLA. Show us a working robot at the next session.

</div>

<div class="card">

### Practice
Run the flow matching notebook. Study the 10 critical bugs. Read `RLT_STAGE2_LEARNINGS.md` in the repo.

</div>

<div class="card">

### Explore
Try training on a **new task** — sorting, pouring, stacking. Add voice control. Push the limits.

</div>

</div>

<div class="abs-br m-6 flex gap-2">
  <a href="https://vizuara.ai" target="_blank" class="text-sm opacity-50 hover:opacity-100">
    vizuara.ai
  </a>
</div>
