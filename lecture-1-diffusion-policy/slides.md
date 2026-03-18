---
theme: default
title: "Diffusion Policy: Visuo-Motor Policy Learning via Action Diffusion"
info: |
  Lecture 1 — Modern Robot Learning from Scratch V2 Bootcamp
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

# Diffusion Policy

## Visuo-Motor Policy Learning via Action Diffusion

<div class="pt-8">
  <span class="px-4 py-2 rounded-lg text-lg" style="background:#c2785c;color:#fff;font-weight:700;">
    Modern Robot Learning from Scratch — V2
  </span>
</div>

<div class="pt-4 opacity-60">
  Lecture 1 — Vizuara Bootcamp
</div>

<div class="abs-br m-6 flex gap-2">
  <a href="https://vizuara.ai" target="_blank" class="text-sm opacity-50 hover:opacity-100">
    vizuara.ai
  </a>
</div>

---
layout: center
---

# What You'll Learn Today

<div class="grid grid-cols-2 gap-4 mt-6 text-left">

<div class="accent-card">

### Part 1: Diffusion from Scratch
How to generate **anything** from pure noise — using Batman as our example.
</div>

<div class="teal-card">

### Part 2: From Images to Robot Actions
Instead of generating images, generate **robot actions** — this is Diffusion Policy.
</div>

<div class="blue-card">

### Part 3: The Full Architecture
Every component: vision encoder, U-Net, FiLM, receding horizon — step by step.
</div>

<div class="purple-card">

### Part 4: Build It Yourself
Hands-on Colab notebooks — implement and train a Diffusion Policy from scratch.
</div>

</div>

---

<div style="height:1px;"></div>

---
layout: section
---

# Part 1
## Diffusion — Generating from Pure Noise

---

# The Big Idea: Learning to Denoise

Imagine you have a photo of **Batman**:

<v-clicks>

<div class="grid grid-cols-3 gap-6 mt-6">

<div class="card text-center">

### 1. Destroy
Gradually add noise until it becomes pure static

</div>

<div class="card text-center">

### 2. Learn
Train a network to **reverse** the destruction

</div>

<div class="card text-center">

### 3. Create
Start from static → denoise → **new images**

</div>

</div>

</v-clicks>

<div v-click class="mt-4 accent-card text-center">

**This is diffusion.** Destruction is easy (just add noise). If you learn to undo it, you can **create from scratch**.

</div>

---

# The Forward Process: Destroying Batman

We take an image and **progressively add Gaussian noise**:

<div class="flex justify-center mt-4">
<img src="/figures/batman-forward-diffusion.png" class="rounded-lg" style="max-height:50vh;" />
</div>

<div v-click class="mt-3 accent-card text-center text-sm">

At each step, we know **exactly** how much noise was added. The destruction is controlled and mathematical.

</div>

---

# What IS Gaussian Noise?

Before we go further — let's understand "Gaussian noise" with a simple example.

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

### Thermometer Example

The true temperature is **25°C**. Your thermometer isn't perfect:

- Sometimes reads **24.3**, sometimes **25.8**, sometimes **25.1**
- These errors follow a **bell curve** (Gaussian distribution)
- Most errors are small, big errors are rare

<div v-click class="mt-3 teal-card">

**Gaussian = bell-curve-shaped randomness**

</div>

</div>

<div v-click>

### Small vs Large Variance

<img src="/figures/gaussian-comparison.png" class="rounded-lg" style="max-height:28vh;" />

Left: $\mathcal{N}(25, 1)$ — gentle. Right: $\mathcal{N}(25, 100)$ — aggressive.

</div>

</div>

---

# The Two Numbers That Define Gaussian Noise

Every Gaussian is defined by just **two numbers**:

<div class="grid grid-cols-2 gap-6 mt-4">

<div class="accent-card">

### Mean ($\mu$) — the center

> "Where is the average?"

For noise: usually $\mu = 0$ (no bias)

</div>

<div class="teal-card">

### Variance ($\sigma^2$) — the spread

> "How wild are the fluctuations?"

Small $\sigma^2$ = gentle, large $\sigma^2$ = aggressive

</div>

</div>

<div v-click class="mt-4 card text-center">

$$\epsilon \sim \mathcal{N}(0, I)$$

*"$\epsilon$ is randomly sampled from a Gaussian with zero mean and unit variance"*

**For diffusion: we add $\mathcal{N}(0, I)$ noise, increasing the amount from $t=0$ to $t=T$.**

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

# The Forward Process: The Math

The equation that describes exactly how we add noise at any timestep $t$:

<div class="card mt-4 text-center">

$$x_t = \sqrt{\bar\alpha_t}\, x_0 + \sqrt{1 - \bar\alpha_t}\, \epsilon$$

</div>

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

<v-clicks>

- $x_0$ = **original** clean data (Batman)
- $x_t$ = **noisy** version at step $t$
- $\epsilon$ = pure random noise
- $\bar\alpha_t$ = controls **signal vs noise** ratio
  - $\bar\alpha_0 \approx 1$ → almost all signal
  - $\bar\alpha_{T} \approx 0$ → almost all noise

</v-clicks>

</div>

<div v-click>

<img src="/figures/signal-vs-noise.png" class="rounded-lg" style="max-height:26vh;" />

As $t$ increases, noise dominates over signal.

</div>

</div>

---

# Forward Process: A Concrete Example

Let's say $\bar\alpha_{50} = 0.3$ at timestep 50:

<div class="card mt-4 text-center text-lg">

$$x_{50} = \underbrace{\sqrt{0.3}}_{\approx 0.55} \cdot x_0 + \underbrace{\sqrt{0.7}}_{\approx 0.84} \cdot \epsilon$$

</div>

<div class="mt-4">

**Translation**: At $t=50$, the noisy image is **55%** original Batman mixed with **84%** strength noise.

</div>

<div v-click class="mt-4">
<img src="/figures/trajectory-noise-progression.png" class="rounded-lg" style="max-height:28vh;" />
</div>

<div v-click class="mt-2 accent-card text-center text-sm">

This shows the same idea but on a **robot trajectory** — the smooth arc gets progressively noisier.

</div>

---

# The Noise Schedule

How fast do we add noise? The **schedule** $\bar\alpha_t$ controls this.

<div class="flex justify-center mt-4">
<img src="/figures/cosine-vs-linear-schedule.png" class="rounded-lg" style="max-height:40vh;" />
</div>

<div v-click class="mt-3 accent-card text-sm">

**Diffusion Policy uses `squaredcos_cap_v2`** — a cosine schedule that preserves signal longer before rapid drop-off. This produces better quality learned actions.

</div>


---

<div style="height:1px;"></div>


---

<div style="height:1px;"></div>


---

<div style="height:1px;"></div>

---

# The Reverse Process: Learning to Denoise

The forward process **destroys** — the reverse process **creates**.

<div class="grid grid-cols-2 gap-6 mt-4">

<div class="card">

### What the Network Learns

Given noisy data $x_t$ and timestep $t$, predict the noise $\epsilon$:

$$\hat\epsilon = \epsilon_\theta(x_t, t)$$

*"I see this noisy mess — what noise was added?"*

</div>

<div class="card" v-click>

### The Training Loss

$$\mathcal{L} = \|\epsilon - \epsilon_\theta(x_t, t)\|^2$$

Just **MSE** between real and predicted noise. That's it!

1. Pick clean data, pick random $t$, add noise
2. Ask network to predict the noise
3. Compute MSE. Backprop. Done.

</div>

</div>

<div v-click class="mt-3 accent-card text-center">

Once we can predict noise, we can **subtract** it step by step — going from pure static back to clean data.

</div>


---

<div style="height: 1px;"></div>

---

# Why Does This Work? Multi-Scale Learning

<div class="flex justify-center mt-2">
<img src="/figures/diffusion-forward-reverse.png" class="rounded-lg" style="max-height:24vh;" />
</div>

<v-clicks>

<div class="accent-card mt-3 mb-2 text-sm">

**Easy timesteps** ($t \approx 0$): Almost clean — network learns fine details. *"That speckle on the cape? Noise."*

</div>

<div class="teal-card mb-2 text-sm">

**Medium timesteps** ($t \approx 50$): Network learns structure. *"Humanoid shape with pointy head."*

</div>

<div class="blue-card text-sm">

**Hard timesteps** ($t \approx 100$): Network hallucates from nothing. *"This blob could become Batman."*

</div>

</v-clicks>

---

# Quiz: Diffusion Basics (1/3)

<div class="quiz-card mt-2">

<div class="mb-3">

**Q1:** When ᾱₜ = 0, what is xₜ?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">

xₜ = √0 · x₀ + √1 · ε = ε — **pure noise**, zero signal remains.

</div>

<div class="mb-3">

**Q2:** If a diffusion model is trained on cats, will it generate dogs from noise?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">

No! It learned to denoise **toward cats**. Different training data → different outputs.

</div>

<div class="mb-3">

**Q3:** Why add fresh noise (σₜz) during each reverse step?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">

Maintains stochasticity — different seeds → different valid outputs. This gives **multimodality**.

</div>

<div class="mb-3">

**Q4:** What two numbers define a Gaussian distribution?

</div>

<div v-click class="px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">

**Mean** (μ) — the center, and **Variance** (σ²) — the spread. For diffusion noise: N(0, I).

</div>

</div>

---

# Quiz: Diffusion Basics (2/3)

<div class="quiz-card mt-2">

<div class="mb-3">

**Q5:** In xₜ = √ᾱₜ · x₀ + √(1-ᾱₜ) · ε, what does √ᾱₜ control?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">

It controls how much **original signal** survives. When ᾱₜ ≈ 1, most of x₀ is preserved. When ᾱₜ ≈ 0, the signal vanishes.

</div>

<div class="mb-3">

**Q6:** What is the training loss for a diffusion model?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">

L = ‖ε - ε_θ(xₜ, t)‖² — simple **MSE** between the actual noise added and the network's predicted noise.

</div>

<div class="mb-3">

**Q7:** At ᾱ₅₀ = 0.3, roughly what percentage of the original image remains?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">

√0.3 ≈ 0.55, so about **55%** of the original signal remains, mixed with **84%** strength noise (√0.7).

</div>

</div>

---

# Quiz: Diffusion Basics (3/3)

<div class="quiz-card mt-2">

<div class="mb-3">

**Q8:** Why does Diffusion Policy use a cosine schedule instead of linear?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">

Cosine preserves signal **longer** before a rapid drop-off, giving the network more useful training signal at intermediate timesteps → better quality actions.

</div>

<div class="mb-3">

**Q9:** What does the network learn at high-noise timesteps (t ≈ T) vs low-noise (t ≈ 0)?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">

**High noise:** global structure — *"this blob should be a humanoid shape."* **Low noise:** fine details — *"that speckle is noise, not a feature."*

</div>

<div class="mb-3">

**Q10:** Can you jump directly from x₀ to xₜ at any timestep, or must you go step-by-step?

</div>

<div v-click class="px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">

You can jump directly! The formula xₜ = √ᾱₜ · x₀ + √(1-ᾱₜ) · ε lets you compute xₜ at **any** t in one step. Only the **reverse** process must go step-by-step.

</div>

</div>

---

# Notebook: Explore Diffusion Yourself

<div class="notebook-card mt-4">

### Google Colab: Forward & Reverse Diffusion

<div class="grid grid-cols-2 gap-4 mt-2">

<div class="card text-sm">

**What you'll do:**
1. Apply forward process to images at different $t$
2. Visualize the noise schedule ($\bar\alpha_t$)
3. Run the reverse process — watch noise become a trajectory
4. Sample multiple times — see the diversity!

</div>

<div class="card text-sm">

**Focus on these cells:**
- Part 3E: Forward/Reverse Process
- Part 6: Denoising Visualization

<a href="/notebooks/Week1_PushT_Diffusion_Policy.ipynb" download class="inline-block mt-2 px-3 py-1 rounded-lg text-sm" style="background:#c2785c;color:#fff;font-weight:600;text-decoration:none;">
  Download Week 1 Notebook
</a>

</div>

</div>

</div>

---

# Brainstorming: From Images to Actions

<div class="brainstorm-card mt-4">
<div class="text-center opacity-40 text-xl">
<p><em>Annotation space — draw and discuss</em></p>
<p><strong>We can generate images from noise. But we're here to build robots.</strong></p>
<p>What if we generated <strong>robot joint angles</strong> instead of pixel values?</p>
<p>What would the "image" be? What would the "noise" be?</p>
</div>
</div>

---
layout: section
---

# Part 2
## From Images to Robot Actions

Instead of denoising pixels, we denoise **motor commands**

---

# Imagine This Task

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

A robot arm holding a teapot needs to **pour tea into a cup**.

<v-clicks>

- The robot sees the scene through a **camera**
- It knows its own **joint positions** (proprioception)
- It needs to output a **sequence of motor commands**

**Question:** Given what the robot sees, what should it do?

$$p(A_t \mid O_t)$$

We want to learn the **probability distribution** of actions given observations.

</v-clicks>

</div>

<div>

<img src="/figures/robot-teapot-pour.png" class="rounded-lg" style="max-height:45vh;" />

</div>

</div>


---

<div style="height:1px;"></div>


---

# Real Robot: Pick & Place from Two Angles

<div class="grid grid-cols-2 gap-4 mt-4">

<div class="card text-center">

### Front View

<video autoplay loop muted playsinline class="inline-video w-full rounded-lg mt-2"
  src="https://huggingface.co/datasets/RajatDandekar/so101_pick_place_red_cube/resolve/main/videos/observation.images.front/chunk-000/file-000.mp4">
</video>

</div>

<div class="card text-center">

### Side View

<video autoplay loop muted playsinline class="inline-video w-full rounded-lg mt-2"
  src="https://huggingface.co/datasets/RajatDandekar/so101_pick_place_red_cube/resolve/main/videos/observation.images.side/chunk-000/file-000.mp4">
</video>

</div>

</div>

<div v-click class="mt-3 accent-card text-center text-sm">

**SO-101 robot arm** performing a pick-and-place task. This is the kind of behavior we want to learn from demonstrations using Diffusion Policy.

</div>


---

# What's Inside the Dataset?

<div class="text-sm mb-3">

From images to actions — at every timestep, the robot records **what it sees** and **what it does**.

</div>

<div class="grid grid-cols-2 gap-4">

<div class="card">

### Observations (Input)

<table class="text-sm">
<tr><th>Channel</th><th>Shape</th></tr>
<tr><td>Front camera</td><td>640 × 480 RGB</td></tr>
<tr><td>Side camera</td><td>640 × 480 RGB</td></tr>
<tr><td>Joint state</td><td>6 values (degrees)</td></tr>
</table>

<div class="mt-2 text-xs" style="color:var(--claude-muted);">2 cameras × 2 frames = 4 images per step</div>

</div>

<div class="accent-card">

### Actions (Output to Predict)

<table class="text-sm">
<tr><th>Joint</th><th>Example (°)</th></tr>
<tr><td style="color:#3B82F6;">Shoulder Pan</td><td><code>-10.37</code></td></tr>
<tr><td style="color:#EF4444;">Shoulder Lift</td><td><code>-81.67</code></td></tr>
<tr><td style="color:#22C55E;">Elbow Flex</td><td><code>77.85</code></td></tr>
<tr><td style="color:#F59E0B;">Wrist Flex</td><td><code>2.68</code></td></tr>
<tr><td style="color:#8B5CF6;">Wrist Roll</td><td><code>123.21</code></td></tr>
<tr><td style="color:#EC4899;">Gripper</td><td><code>6.50</code></td></tr>
</table>

<div class="mt-2 text-xs" style="color:var(--claude-muted);">6 DOF — predict 16 steps ahead</div>

</div>

</div>

<div v-click class="mt-3 teal-card text-center text-sm">

**The shift:** Instead of generating a 256×256 image (65,536 pixels), we generate a **16×6 action chunk** (96 numbers). Same diffusion math, wildly different output.

</div>

---

# The Key Shift: What Are We Generating?

<div class="grid grid-cols-2 gap-6 mt-4">

<div class="accent-card">

### Image Diffusion (Batman)

- $x_0$ = a 256×256×3 image
- Each value = pixel intensity
- Forward: add noise to pixels
- Output: a pretty picture

</div>

<div class="teal-card">

### Diffusion Policy (Ours!)

- $x_0$ = **16 timesteps × 2 actions**
- Each value = a joint angle or position
- Forward: add noise to actions
- Output: an executable trajectory

</div>

</div>

<div v-click class="mt-4 card text-center">

**Same math. Same training. Same denoising.**

The only difference: $x_0$ is a **1D action sequence** instead of a 2D image.

</div>

---

# Forward Process on Robot Actions

What does "noisy robot actions" look like? The smooth trajectory gets destroyed:

<div class="flex justify-center mt-3">
<img src="/figures/trajectory-noise-progression.png" class="rounded-lg" style="max-height:22vh;" />
</div>

<div class="flex justify-center mt-2">
<img src="/figures/joint-angles-forward-diffusion.png" class="rounded-lg" style="max-height:22vh;" />
</div>

<div v-click class="mt-2 accent-card text-center text-sm">

Noise on actions = random joint angles = robot jittering in space. Same formula: $A_t = \sqrt{\bar\alpha_t}\, A_0 + \sqrt{1 - \bar\alpha_t}\, \epsilon$

</div>

---

# Reverse Process: From Chaos to a Plan

Starting from random joint angles → denoise → smooth executable trajectory:

<div class="flex justify-center mt-4">
<img src="/figures/denoising-trajectory.png" class="rounded-lg" style="max-height:32vh;" />
</div>

<div v-click class="mt-3 accent-card text-center">

**Just like images**: pixels resolve into Batman → joint angles resolve into a pour-the-tea trajectory. The network learned the structure of **good robot behavior**.

</div>

---

# Why Not Just Predict Actions Directly?

<div class="mt-2">

The obvious approach: train a network with **MSE loss** to predict the action.

</div>

<v-clicks>

<div class="grid grid-cols-2 gap-6 mt-4">

<div class="card">

### Regression Approach

$$\hat{a} = f_\theta(\text{observation})$$

$$\mathcal{L} = \|\hat{a} - a_{\text{demo}}\|^2$$

*"Minimize the distance to the demonstrated action."*

</div>

<div class="accent-card">

### The Hidden Problem

What if there are **multiple valid actions** for the same observation?

- Go left around the obstacle?
- Go right around the obstacle?
- Both are correct demonstrations!

</div>

</div>

<div class="mt-4 teal-card text-center">

**This is the multimodality problem** — and it's everywhere in robotics.

</div>

</v-clicks>

---

# The Averaging Disaster

<div class="flex justify-center mt-3">
<img src="/figures/multimodality-problem.png" class="rounded-lg" style="max-height:50vh; max-width:90%;" />
</div>

<div v-click class="mt-3 accent-card text-center text-sm">

MSE learns the **mean** of all demonstrations. When two valid paths exist, the average goes **straight through the obstacle**. A perfect loss, a catastrophic policy.

</div>

---

# Diffusion Solves Multimodality

<div class="flex justify-center mt-3">
<img src="/figures/multimodality-demo.png" class="rounded-lg" style="max-height:50vh; max-width:90%;" />
</div>

<div v-click class="mt-3 teal-card text-center text-sm">

Different noise seeds → different valid strategies. Every sample is a **complete, coherent** trajectory. The network never averages across modes.

</div>

---

# Regression vs Diffusion: The Full Picture

<div class="grid grid-cols-2 gap-6 mt-4">

<div class="accent-card">

### Regression (MSE)

- Input: observation → **one** prediction
- Learns the **mean** of demonstrations
- Collapses multiple modes into one
- Averaged path = **unsafe** path

$$\hat{a} = f_\theta(o) \quad \text{(single output)}$$

</div>

<div class="teal-card">

### Diffusion Policy

- Input: observation + **random noise**
- Learns the **full distribution**
- Each sample is a complete, valid plan
- Different seeds = different strategies

$$a \sim p_\theta(a | o) \quad \text{(sample from distribution)}$$

</div>

</div>

<div v-click class="mt-3 card text-center text-sm">

**Bottom line:** Regression answers "what is the average action?" Diffusion answers "what are all the valid actions?" — then picks one.

</div>

---

# Diffusion Policy: Real Robot Results

<div class="grid grid-cols-3 gap-3 mt-4">

<div class="card text-center">

### Push-T

<video autoplay loop muted playsinline class="inline-video w-full mt-1">
  <source src="https://diffusion-policy.cs.columbia.edu/videos/highlight_pusht.mp4" type="video/mp4">
</video>

<div class="text-xs mt-1 opacity-70">2D pushing — "Hello World"</div>

</div>

<div class="card text-center">

### Mug Flipping

<video autoplay loop muted playsinline class="inline-video w-full mt-1">
  <source src="https://diffusion-policy.cs.columbia.edu/videos/highlight_mug.mp4" type="video/mp4">
</video>

<div class="text-xs mt-1 opacity-70">Contact-rich dynamics</div>

</div>

<div class="card text-center">

### Sauce Pour & Spread

<video autoplay loop muted playsinline class="inline-video w-full mt-1">
  <source src="https://diffusion-policy.cs.columbia.edu/videos/highlight_sauce.mp4" type="video/mp4">
</video>

<div class="text-xs mt-1 opacity-70">Deformable objects, multi-step</div>

</div>

</div>

---

# Robustness: It Recovers from Perturbations

<div class="flex justify-center mt-4">
<div class="card" style="max-width:75%;">
<video autoplay loop muted playsinline class="inline-video w-full rounded-lg">
  <source src="https://diffusion-policy.cs.columbia.edu/videos/pusht_robustness_web.mp4" type="video/mp4">
</video>
</div>
</div>

<div v-click class="mt-3 accent-card text-center">

**Why robust?** The policy **re-plans every 8 steps**. When the world changes, the next plan adapts. Action chunking = smooth execution. Receding horizon = adaptability.

</div>

---

# Simulation Benchmark Results

<div class="grid grid-cols-4 gap-2 mt-4 text-center text-sm">

<div class="card">

### Lift
<video autoplay loop muted playsinline class="inline-video w-full mt-1">
  <source src="https://diffusion-policy.cs.columbia.edu/videos/lift.mp4" type="video/mp4">
</video>
</div>

<div class="card">

### Can
<video autoplay loop muted playsinline class="inline-video w-full mt-1">
  <source src="https://diffusion-policy.cs.columbia.edu/videos/can.mp4" type="video/mp4">
</video>
</div>

<div class="card">

### Square
<video autoplay loop muted playsinline class="inline-video w-full mt-1">
  <source src="https://diffusion-policy.cs.columbia.edu/videos/square.mp4" type="video/mp4">
</video>
</div>

<div class="card">

### Tool Hang
<video autoplay loop muted playsinline class="inline-video w-full mt-1">
  <source src="https://diffusion-policy.cs.columbia.edu/videos/tool_hang.mp4" type="video/mp4">
</video>
</div>

</div>

<div class="grid grid-cols-3 gap-2 mt-2 text-center text-sm">

<div class="card">

### Transport
<video autoplay loop muted playsinline class="inline-video w-full mt-1">
  <source src="https://diffusion-policy.cs.columbia.edu/videos/transport.mp4" type="video/mp4">
</video>
</div>

<div class="card">

### Block Push
<video autoplay loop muted playsinline class="inline-video w-full mt-1">
  <source src="https://diffusion-policy.cs.columbia.edu/videos/block_push.mp4" type="video/mp4">
</video>
</div>

<div class="card">

### Kitchen
<video autoplay loop muted playsinline class="inline-video w-full mt-1">
  <source src="https://diffusion-policy.cs.columbia.edu/videos/kitchen.mp4" type="video/mp4">
</video>
</div>

</div>

---

# Quiz: Images → Actions (1/3)

<div class="quiz-card mt-2">

<div class="mb-3">

**Q1:** In Diffusion Policy, what is x₀ (the clean data)?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">

A sequence of **actions** — e.g., x₀ ∈ ℝ^(16×6) for SO-101 (16 timesteps, 6 joint angles).

</div>

<div class="mb-3">

**Q2:** Starting from different random noise, will Diffusion Policy produce the same trajectory?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">

No! Different noise = different valid trajectories. This is **multimodality** — the key advantage over regression.

</div>

<div class="mb-3">

**Q3:** Why does MSE regression fail for multimodal tasks?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">

MSE minimizes average error, so it **averages** across modes. Two valid paths (left and right) become one invalid path (straight through the obstacle).

</div>

<div class="mb-3">

**Q4:** What are the two inputs to the Diffusion Policy denoiser at inference?

</div>

<div v-click class="px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">

**Random noise** x_T ~ N(0, I) and the current **observation** (camera images + joint state). The observation conditions the denoising.

</div>

</div>

---

# Quiz: Images → Actions (2/3)

<div class="quiz-card mt-2">

<div class="mb-3">

**Q5:** Why predict 16 actions at once instead of 1?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">

**Action chunking** → smoother trajectories. Predicting one action at a time causes jittery, inconsistent behavior because each prediction is independent.

</div>

<div class="mb-3">

**Q6:** If we predict 16 actions, why only execute 8?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">

**Receding horizon** — execute 8 steps, then re-observe and re-plan. Balances trajectory smoothness with adaptability to changes in the scene.

</div>

<div class="mb-3">

**Q7:** Our SO-101 dataset has 6 DOF. What does each action value represent?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">

A **target joint angle in degrees** for each of the 6 joints: Shoulder Pan, Shoulder Lift, Elbow Flex, Wrist Flex, Wrist Roll, Gripper.

</div>

</div>

---

# Quiz: Images → Actions (3/3)

<div class="quiz-card mt-2">

<div class="mb-3">

**Q8:** How many total numbers does Diffusion Policy generate in one denoising pass for SO-101?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">

16×6 = 96 numbers — 16 timesteps × 6 joint angles. Compare this to generating a 256×256 image (65,536 pixels). Same math, much smaller output.

</div>

<div class="mb-3">

**Q9:** What observations does the robot use? (Hint: there are two types.)

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">

**Visual** — camera images (front + side, 640×480 RGB), and **proprioceptive** — its own joint angles (6 values). Together, they tell the robot what it sees and where its arm is.

</div>

<div class="mb-3">

**Q10:** Can Diffusion Policy handle a new obstacle it hasn't seen in training?

</div>

<div v-click class="px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">

Only if similar situations appeared in training data. It learns from **demonstrations**, not physics. But its multimodal nature makes it more **robust** — it can recover from perturbations by re-planning.

</div>

</div>

---
layout: section
---

# Part 3
## The Full Architecture

Every component, step by step — no black boxes, no hand-waving

---

# Imagine This Task

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

A robot arm is holding a **teapot** and needs to **pour tea into a cup**.

Think about what the robot needs:

<v-clicks>

- It needs to **see** the scene (where is the cup?)
- It needs to know its **own arm position**
- It needs to **plan a sequence of movements**
- It needs to **actually execute** those movements

</v-clicks>

<div v-click class="mt-3 accent-card">

**Our goal**: Build a system that takes in what the robot sees and outputs a smooth, executable motion plan.

</div>

</div>

<div>

<img src="/figures/robot-teapot-pour.png" class="rounded-lg" style="max-height:48vh;" />

</div>

</div>

---

# What Does the Robot See?

The robot has **two types of input** — let's understand each one.

<div class="grid grid-cols-2 gap-6 mt-4">

<div class="accent-card">

### 1. Camera Image

A single RGB image from a camera looking at the workspace.

- Resolution: **96 × 96 pixels** (downscaled for speed)
- Shows: the teapot, the cup, the table, the arm
- **Problem**: This is 96×96×3 = **27,648 numbers**. Way too many for direct use!

</div>

<div class="teal-card" v-click>

### 2. Robot Joint State

The robot knows where its own arm is.

- For PushT: just $(x, y)$ position → **2 numbers**
- For a real 6-DOF arm: 6 joint angles → **6 numbers**

This is called **proprioception** — the robot's sense of its own body.

</div>

</div>

<div v-click class="mt-3 card text-center">

**Together**: observation $o_t$ = (camera image, joint state). We get this at every timestep.

</div>

---

# Visualize: Robot Observations

<div class="text-sm opacity-60 -mt-2 mb-1">Camera image + joint positions = everything the robot knows about the world.</div>

<div class="flex justify-center items-start">
<img src="/figures/robot-observations.png" class="rounded-lg" style="max-height:72vh; max-width:85%;" />
</div>

---

# What Does the Robot Need to Output?

The robot needs to output **actions** — motor commands that move its arm.

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

### A Single Action

For PushT: $a_t = (x, y)$ — where to move next.

For a 6-DOF arm: $a_t = (\theta_1, \theta_2, ..., \theta_6)$ — target joint angles.

### Why Not Just One Action?

<div v-click class="accent-card mt-2">

Predicting **one action at a time** leads to jittery, uncoordinated motion — like giving driving directions one meter at a time.

Instead, we predict a **whole plan**: the next **16 actions** at once.

</div>

</div>

<div v-click>

### An Action Trajectory (Our Output)

$$A = \begin{bmatrix} a_{t-1} \\ a_t \\ a_{t+1} \\ \vdots \\ a_{t+14} \end{bmatrix} \in \mathbb{R}^{16 \times d_a}$$

For PushT: $16 \times 2 = 32$ numbers total.

This is what diffusion generates — $x_0$ in our diffusion model **is this action trajectory**.

</div>

</div>


---

<div style="height:1px;"></div>

---

# Visualize: Action Trajectory Output

<div class="text-sm opacity-60 -mt-2 mb-1">16 timesteps of motor commands — the robot's complete movement plan generated by diffusion.</div>

<div class="flex justify-center items-start">
<img src="/figures/action-trajectory-output.png" class="rounded-lg" style="max-height:72vh; max-width:85%;" />
</div>

---

# The Three Horizons

The robot operates with three important time windows:

<div class="flex justify-center mt-3">
<img src="/figures/three-horizons.png" class="rounded-lg" style="max-height:22vh;" />
</div>

<div class="grid grid-cols-3 gap-4 mt-3">

<div class="blue-card text-center">

### $T_o = 2$
**Observation Horizon**

Look at the current frame and previous frame.

*"What just happened?"*

</div>

<div class="teal-card text-center">

### $T_p = 16$
**Prediction Horizon**

Plan the next 16 timesteps.

*"What's my full plan?"*

</div>

<div class="accent-card text-center">

### $T_a = 8$
**Execution Horizon**

Execute only the first 8, then re-plan.

*"Trust for 0.8s, then reassess."*

</div>

</div>

---

# Architecture Overview: The Big Picture

Here is the complete pipeline. We'll zoom into **every box** one at a time.

<div class="flex justify-center mt-3">
<img src="/figures/architecture-overview.png" class="rounded-lg" style="max-height:38vh;" />
</div>

<div class="grid grid-cols-4 gap-2 mt-3 text-center text-xs">

<div class="accent-card">
<strong>A</strong> — Vision Encoder
</div>

<div class="teal-card">
<strong>B</strong> — 1D U-Net (Denoiser)
</div>

<div class="blue-card">
<strong>C</strong> — FiLM Conditioning
</div>

<div class="purple-card">
<strong>D</strong> — Receding Horizon
</div>

</div>

---

# Step A: The Vision Problem

The robot sees a **96×96 RGB image**. But the denoiser needs a **compact vector of numbers**.

How do we convert an image into something useful?

<div class="grid grid-cols-3 gap-4 mt-6">

<div class="card text-center" v-click>

### Option 1: Use Raw Pixels?

27,648 numbers per image.

Way too large. Mostly irrelevant info (background, lighting).

</div>

<div class="card text-center" v-click>

### Option 2: Handcrafted Features?

Manually detect edges, colors, object positions...

Too brittle. Doesn't generalize.

</div>

<div class="accent-card text-center" v-click>

### Option 3: Learn Features!

Use a **pretrained CNN** to extract meaningful features automatically.

This is what we do.

</div>

</div>

---

# Visualize: The Vision Problem

<div class="text-sm opacity-60 -mt-2 mb-2">Raw pixels vs. handcrafted features vs. learned features — why we choose a pretrained CNN.</div>

<div class="flex justify-center items-start">
<img src="/figures/vision-problem-options.png" class="rounded-lg" style="max-height:72vh; max-width:85%;" />
</div>

---

# What is a CNN? (Quick Refresher)

<a href="/notebooks/Component_ResNet18.ipynb" download class="text-xs px-2 py-1 rounded" style="background:rgba(90,127,165,0.08);color:#5a7fa5;text-decoration:none;border:1px solid rgba(90,127,165,0.2);position:absolute;right:2em;top:4.5em;">Notebook: Component_ResNet18.ipynb</a>

A **Convolutional Neural Network** learns to detect patterns in images.

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

### How It Works

A small **filter** (e.g., 3×3) slides across the image:

- **Early layers** detect simple things: edges, corners, colors
- **Middle layers** combine these: textures, shapes
- **Deep layers** recognize objects: "this is a mug handle"

Each layer produces a **feature map** — a grid showing "where did I find this pattern?"

</div>

<div v-click>

### ResNet18

We use **ResNet18** — a CNN pretrained on ImageNet (1.2M images).

- It already knows how to see! We don't train it from scratch.
- We **remove the classification head** (we don't need "this is a dog")
- We keep the **feature extraction layers**

<div class="accent-card mt-3 text-sm">

**Input**: 96×96×3 image

**Output**: 512×3×3 feature map

512 channels, each a 3×3 spatial grid.

</div>

</div>

</div>

---

# Visualize: CNN Filter Sliding

<div class="text-sm opacity-60 -mt-2 mb-2">A 3×3 filter slides across the image, detecting edges and patterns at each position.</div>

<div class="grid grid-cols-2 gap-4 mt-1">

<div class="flex items-start justify-center">
<img src="/figures/cnn-filter-sliding.png" class="rounded-lg" style="max-height:65vh; max-width:100%;" />
</div>

<div class="flex flex-col items-center gap-4">

<video controls class="rounded-lg" style="max-height:46vh; max-width:100%;">
  <source src="/animations/Scene01_CNNFilterSliding.mp4" type="video/mp4">
</video>

<a href="/notebooks/Component_ResNet18.ipynb" download class="card text-sm px-4 py-2 text-center" style="text-decoration:none;color:var(--claude-text);">
Download: <code>Component_ResNet18.ipynb</code>
</a>

</div>

</div>

---

# ResNet18: From Image to Feature Map

Let's trace the teapot image through ResNet18:

<div class="card mt-4 text-center">

$$\text{96×96×3 image} \xrightarrow{\text{ResNet18}} \text{512×3×3 feature map}$$

</div>

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

### What does 512×3×3 mean?

- **512 channels**: 512 different "pattern detectors"
  - Channel 47 might detect "round objects"
  - Channel 183 might detect "handle-like shapes"
  - Channel 301 might detect "edges on the left"
- **3×3 spatial grid**: each channel has a rough map of where its pattern appears

</div>

<div v-click>

### Next Problem

We have a 512×3×3 = **4,608** number feature map.

We need to compress this into something compact — ideally **64 numbers** per image.

<div class="accent-card mt-3">

**How?** We need a **pooling** method that preserves the most important information.

This is where SpatialSoftmax comes in...

</div>

</div>

</div>

---

# Visualize: ResNet18 Pipeline

<div class="text-sm opacity-60 -mt-2 mb-2">From raw pixels to a compact feature map — 96×96×3 → 512×3×3.</div>

<div class="grid grid-cols-2 gap-4 mt-1">

<div class="flex items-start justify-center">
<img src="/figures/resnet18-pipeline.png" class="rounded-lg" style="max-height:65vh; max-width:100%;" />
</div>

<div class="flex flex-col items-center gap-4">

<video controls class="rounded-lg" style="max-height:46vh; max-width:100%;">
  <source src="/animations/Scene02_ResNet18Pipeline.mp4" type="video/mp4">
</video>

<a href="/notebooks/Component_ResNet18.ipynb" download class="card text-sm px-4 py-2 text-center" style="text-decoration:none;color:var(--claude-text);">
Download: <code>Component_ResNet18.ipynb</code>
</a>

</div>

</div>

---

# The Pooling Problem

<a href="/notebooks/Component_SpatialSoftmax.ipynb" download class="text-xs px-2 py-1 rounded" style="background:rgba(90,127,165,0.08);color:#5a7fa5;text-decoration:none;border:1px solid rgba(90,127,165,0.2);position:absolute;right:2em;top:4.5em;">Notebook: Component_SpatialSoftmax.ipynb</a>

We have 512×3×3 features. How do we compress them?

<div class="grid grid-cols-2 gap-6 mt-4">

<div class="card">

### Global Average Pooling (Standard)

Average all spatial positions for each channel.

$$512 \times 3 \times 3 \rightarrow 512$$

**What it tells you:** *"Channel 47 has high activation"* → "There's a round object **somewhere**."

<div class="accent-card mt-3">

**Problem for robots:** It loses **WHERE** things are! If the mug is on the left vs. right, the average is the same. But the robot needs to reach to a specific location!

</div>

</div>

<div class="teal-card" v-click>

### SpatialSoftmax (Our Choice)

For each channel, find the **expected (x, y) position** of its activation.

$$512 \times 3 \times 3 \rightarrow 32 \times 2 = 64$$

**What it tells you:** *"The round object pattern peaks at position (0.3, 0.7)"*

**This gives spatial coordinates** — the robot knows exactly WHERE each feature is. Crucial for reaching, grasping, pouring!

</div>

</div>

---

# Visualize: GAP vs SpatialSoftmax

<div class="text-sm opacity-60 -mt-2 mb-2">Average pooling loses position. SpatialSoftmax preserves WHERE features are — critical for reaching and grasping.</div>

<div class="grid grid-cols-2 gap-4 mt-1">

<div class="flex items-start justify-center">
<img src="/figures/gap-vs-spatialsoftmax.png" class="rounded-lg" style="max-height:65vh; max-width:100%;" />
</div>

<div class="flex flex-col items-center gap-4">

<video controls class="rounded-lg" style="max-height:46vh; max-width:100%;">
  <source src="/animations/Scene03_GAPvsSpatialSoftmax.mp4" type="video/mp4">
</video>

<a href="/notebooks/Component_SpatialSoftmax.ipynb" download class="card text-sm px-4 py-2 text-center" style="text-decoration:none;color:var(--claude-text);">
Download: <code>Component_SpatialSoftmax.ipynb</code>
</a>

</div>

</div>

---

# SpatialSoftmax: How It Works

<div class="grid grid-cols-2 gap-6 mt-3">

<div>

### Step by Step

1. Take the 512×3×3 feature map
2. Add a **Conv2d(512 → 32)** layer to reduce to 32 channels
3. Now we have **32 feature maps**, each 3×3

For **each** of the 32 channels:

4. Apply **softmax** over the 3×3 grid → turns activations into probabilities
5. Compute the **expected (x, y)** position:

$$\text{keypoint}_c = \sum_{i,j} \text{softmax}(f_c)_{i,j} \cdot (x_i, y_j)$$

This gives one $(x, y)$ coordinate per channel.

**32 keypoints × 2 coords = 64 floats per image**

</div>

<div>

<img src="/figures/spatialsoftmax-keypoints.png" class="rounded-lg" style="max-height:48vh;" />

</div>

</div>

---

# Example: SpatialSoftmax Calculation

Let's trace real numbers through SpatialSoftmax on a **3×3 feature map** for one channel.

<div class="grid grid-cols-3 gap-4 mt-3">

<div class="card text-center">

### Step 1: Raw Activations

| | col 0 | col 1 | col 2 |
|---|:---:|:---:|:---:|
| **row 0** | 0.1 | 0.3 | 0.2 |
| **row 1** | 0.8 | **2.5** | 0.4 |
| **row 2** | 0.1 | 0.6 | 0.3 |

The highest value (2.5) is at position (1, 1).

</div>

<div class="accent-card text-center" v-click>

### Step 2: Softmax → Probabilities

$$p_{i,j} = \frac{e^{f_{i,j}}}{\sum e^{f_{k,l}}}$$

| | col 0 | col 1 | col 2 |
|---|:---:|:---:|:---:|
| **row 0** | 0.04 | 0.05 | 0.04 |
| **row 1** | 0.08 | **0.46** | 0.05 |
| **row 2** | 0.04 | 0.07 | 0.05 |

Sum = 1.0. Most mass at (1, 1).

</div>

<div class="teal-card text-center" v-click>

### Step 3: Weighted Average

$$x = \sum p_{i,j} \cdot x_j = 0.46 \times 0.5 + ... = \mathbf{0.52}$$

$$y = \sum p_{i,j} \cdot y_i = 0.46 \times 0.5 + ... = \mathbf{0.47}$$

**Keypoint = (0.52, 0.47)**

This is very close to the center where the peak was — but it's a soft, differentiable estimate!

</div>

</div>

<div v-click class="mt-3">

<img src="/figures/example-spatialsoftmax-calc.png" class="rounded-lg mx-auto" style="max-height:35vh;" />

</div>

---

# SpatialSoftmax: What the Keypoints Mean

Think of the 32 keypoints as 32 "landmark detectors" that the network learns:

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

<v-clicks>

- Keypoint 1 might track: **mug handle position**
- Keypoint 7 might track: **cup rim center**
- Keypoint 15 might track: **robot gripper tip**
- Keypoint 23 might track: **table edge**

The network **learns** which landmarks are useful — we don't specify them!

</v-clicks>

<div v-click class="accent-card mt-3">

**Why this matters:** When the mug moves from $(0.3, 0.4)$ to $(0.5, 0.4)$, the keypoint coordinates change. The robot can track objects as they move.

</div>

<img src="/figures/keypoints-on-scene.png" class="rounded-lg mt-2" style="max-height:30vh;" />

</div>

<div v-click>

### Per Image vs Two Images

We look at **two frames** ($T_o = 2$):

- Frame at $t-1$: 32 keypoints → **64 floats**
- Frame at $t$: 32 keypoints → **64 floats**

Total from vision: **128 floats**

<div class="teal-card mt-3 text-sm">

**Why two frames?** The difference between $t-1$ and $t$ tells the robot about **motion** — is the cup moving? Is the arm swinging? This temporal context is critical.

</div>

</div>

</div>

---

# Quiz: Vision Encoder (1/3)

<div class="quiz-card mt-2">

**Q1:** Why can't we feed raw pixels directly to the denoiser? Why do we need a CNN encoder?

<div v-click class="mb-3 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> A 96×96 RGB image has 27,648 values — far too high-dimensional. The CNN compresses this into ~64 meaningful features that capture object positions, shapes, and relationships, making the denoiser's job tractable.
</div>

**Q2:** What is the output shape of ResNet18 for a 96×96 input, and what does 512×3×3 mean?

<div v-click class="mb-3 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> 512 feature channels, each a 3×3 spatial grid = 4,608 values. Each channel detects a different visual feature (edges, textures, object parts), and the 3×3 grid retains coarse spatial information about WHERE that feature appears.
</div>

**Q3:** Why is SpatialSoftmax better than Global Average Pooling for robotics?

<div v-click class="mb-3 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> GAP averages each channel into one number — losing WHERE objects are. An object at position (0.3, 0.7) and (0.8, 0.2) produce the same average. SpatialSoftmax outputs (x, y) coordinates, preserving spatial location — essential for reaching and grasping.
</div>

**Q4:** How many keypoints does SpatialSoftmax produce, and what is the total output dimension?

<div v-click class="mb-3 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> A 1×1 conv reduces 512 channels to 32 channels. Each channel produces one (x, y) keypoint = 2 values. Total: 32 × 2 = 64 values per image.
</div>

</div>

---

# Quiz: Vision Encoder (1/3) — continued

<div class="quiz-card mt-2">

**Q5:** What is a "residual connection" in ResNet18, and why does it help?

<div v-click class="mb-3 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> The input to each block is added to the output: y = F(x) + x. This creates a shortcut for gradients to flow backward, solving the vanishing gradient problem and allowing deeper networks to train stably.
</div>

**Q6:** The backbone is pretrained on ImageNet. Why use ImageNet weights for a robot task?

<div v-click class="mb-3 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> ImageNet pretraining teaches low-level features (edges, textures, shapes) that transfer well to any visual domain. The robot fine-tunes these general features to recognize task-specific objects like cups, T-blocks, and grippers.
</div>

**Q7:** Each ResNet block doubles channels and halves spatial resolution. Trace the dimensions: 64×48×48 → ?

<div v-click class="mb-3 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> Layer 1: 64×24×24 (no downsampling in first block), Layer 2: 128×12×12, Layer 3: 256×6×6, Layer 4: 512×3×3. The input 96×96 becomes 48×48 after conv1+maxpool, then halves at layers 2-4.
</div>

**Q8:** What is the softmax function doing spatially in SpatialSoftmax?

<div v-click class="mb-3 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> Softmax converts the 3×3 feature map into a probability distribution over the 9 spatial positions. The highest activation gets the most weight. The expected value of this distribution gives the (x, y) coordinate — like a "center of mass" of the feature.
</div>

</div>

---

# Quiz: Vision Encoder (1/3) — continued

<div class="quiz-card mt-2">

**Q9:** The policy observes at t-1 and t. Each image produces 64 features. What's the total visual feature count?

<div v-click class="mb-3 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> 2 images × 64 features = 128 visual features. These are concatenated to form part of the conditioning vector. Note: the two images share the same ResNet18 weights (weight sharing).
</div>

**Q10:** Could you use a Vision Transformer (ViT) instead of ResNet18? What would change?

<div v-click class="mb-3 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> Yes — ViT splits the image into patches and uses self-attention. It captures global relationships better than CNNs but requires more data and compute. The output would be patch tokens instead of a spatial feature map, so you'd replace SpatialSoftmax with a different pooling strategy (like CLS token or attention pooling).
</div>

</div>

---

# The Timestep Embedding

<a href="/notebooks/Component_Timestep_Embedding.ipynb" download class="text-xs px-2 py-1 rounded" style="background:rgba(90,127,165,0.08);color:#5a7fa5;text-decoration:none;border:1px solid rgba(90,127,165,0.2);position:absolute;right:2em;top:4.5em;">Notebook: Component_Timestep_Embedding.ipynb</a>

Remember: diffusion denoises step by step from $t=99$ to $t=0$. The network needs to know **which step it's at**.

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

### Why not just feed the number $t$?

If we feed $t = 50$ as a single number, the network has almost no information to work with.

<div v-click class="accent-card mt-3">

**Solution: Sinusoidal Embedding**

Convert the scalar $t$ into a **128-dimensional vector** using sine and cosine waves at different frequencies.

$$\text{emb}(t) = [\sin(t/f_1),\, \cos(t/f_1),\, \ldots,\, \cos(t/f_{64})]$$

Then pass through a small **MLP** to get the final 128-dim embedding.

</div>

</div>

<div v-click>

### Why 128 Dimensions?

- **Nearby timesteps** get similar embeddings (t=50 ≈ t=51)
- **Distant timesteps** get very different embeddings (t=5 ≠ t=95)
- The network can learn **different behaviors** for different noise levels

<div class="teal-card mt-3 text-sm">

At $t=99$ (very noisy): "Ignore details, just find the rough direction"

At $t=5$ (almost clean): "Fine-tune the exact joint angles"

The embedding gives the network this context.

</div>

</div>

</div>

---

# Visualize: Sinusoidal Timestep Embedding

<div class="text-sm opacity-60 -mt-2 mb-2">Converting a scalar timestep into a rich 128-dimensional fingerprint using sine and cosine waves.</div>

<div class="grid grid-cols-2 gap-4 mt-1">

<div class="flex items-start justify-center">
<img src="/figures/sinusoidal-embedding.png" class="rounded-lg" style="max-height:65vh; max-width:100%;" />
</div>

<div class="flex flex-col items-center gap-4">

<video controls class="rounded-lg" style="max-height:46vh; max-width:100%;">
  <source src="/animations/Scene04_TimestepEmbedding.mp4" type="video/mp4">
</video>

<a href="/notebooks/Component_Timestep_Embedding.ipynb" download class="card text-sm px-4 py-2 text-center" style="text-decoration:none;color:var(--claude-text);">
Download: <code>Component_Timestep_Embedding.ipynb</code>
</a>

</div>

</div>

---

# Example: Timestep Embedding Calculation

Let's compute the embedding for **$t = 50$** with dimension $d = 128$.

<div class="grid grid-cols-2 gap-6 mt-3">

<div class="card">

### The Formula

$$PE(t, 2i) = \sin\left(\frac{t}{10000^{2i/d}}\right)$$
$$PE(t, 2i+1) = \cos\left(\frac{t}{10000^{2i/d}}\right)$$

### First 6 Values for t=50

| Dim | Frequency | Value |
|:---:|---|:---:|
| 0 | $\sin(50/1.0)$ | **−0.262** |
| 1 | $\cos(50/1.0)$ | **0.965** |
| 2 | $\sin(50/1.93)$ | **0.846** |
| 3 | $\cos(50/1.93)$ | **−0.534** |
| 4 | $\sin(50/3.73)$ | **−0.447** |
| 5 | $\cos(50/3.73)$ | **0.895** |

</div>

<div v-click>

### Key Properties

<div class="teal-card mb-3 text-sm">

**Nearby timesteps are similar:**

$\text{sim}(t{=}49, t{=}50) \approx 0.98$

$\text{sim}(t{=}51, t{=}50) \approx 0.98$

</div>

<div class="accent-card mb-3 text-sm">

**Distant timesteps are different:**

$\text{sim}(t{=}1, t{=}50) \approx 0.12$

$\text{sim}(t{=}99, t{=}50) \approx 0.15$

</div>

This is why the network can learn different behaviors for different noise levels — the embedding gives it a rich, unique fingerprint for each timestep.

<img src="/figures/example-timestep-embedding.png" class="rounded-lg mt-2" style="max-height:30vh;" />

</div>

</div>

---

# Building the Conditioning Vector

<a href="/notebooks/Component_Conditioning_Vector.ipynb" download class="text-xs px-2 py-1 rounded" style="background:rgba(90,127,165,0.08);color:#5a7fa5;text-decoration:none;border:1px solid rgba(90,127,165,0.2);position:absolute;right:2em;top:4.5em;">Notebook: Component_Conditioning_Vector.ipynb</a>

Now we combine everything into one **260-dimensional vector**:

<div class="card mt-4 text-center">

$$\underbrace{64}_{\text{img}_{t-1}} + \underbrace{64}_{\text{img}_t} + \underbrace{2}_{\text{st}_{t-1}} + \underbrace{2}_{\text{st}_t} + \underbrace{128}_{\text{step}} = \mathbf{260}$$

</div>

<div class="flex justify-center mt-3">
<img src="/figures/observation-pipeline.png" class="rounded-lg" style="max-height:34vh;" />
</div>

<div v-click class="mt-2 accent-card text-center text-sm">

This 260-dim vector is the **complete context** — it tells the denoiser everything: what the robot sees, where it is, and what noise level to denoise at.

</div>

---

# Example: The 260 Values, Unpacked

Here's exactly what the conditioning vector contains for one real observation:

<div class="flex justify-center mt-3">
<img src="/figures/example-conditioning-assembly.png" class="rounded-lg" style="max-height:35vh;" />
</div>

<div class="card mt-3 text-sm">

| Section | Dims | Source | Example Values |
|---|:---:|---|---|
| Image $t-1$ features | **64** | ResNet18 + SpatialSoftmax on frame at $t-1$ | `[0.31, -0.12, 0.85, ...]` |
| Image $t$ features | **64** | ResNet18 + SpatialSoftmax on frame at $t$ | `[0.33, -0.10, 0.87, ...]` |
| State $t-1$ | **2** | Robot $(x, y)$ position at $t-1$ | `[0.45, 0.62]` |
| State $t$ | **2** | Robot $(x, y)$ position at $t$ | `[0.47, 0.63]` |
| Timestep embedding | **128** | Sinusoidal encoding of diffusion step $t$ | `[-0.26, 0.97, 0.85, ...]` |
| **Total** | **260** | | |

</div>

<div v-click class="mt-2 accent-card text-center text-sm">

Notice: image features change **slowly** between $t-1$ and $t$ (the scene barely moves in 0.1s). But state values change more — that **difference** encodes motion direction and speed.

</div>

---

# Brainstorming: The Conditioning Vector

<div class="brainstorm-card mt-4">
<div class="text-center opacity-40 text-xl">
<p><em>Annotation space — draw and discuss</em></p>
<p><strong>The 260-dim vector: 64 + 64 + 2 + 2 + 128</strong></p>
<p>1. Why TWO images? What info does the time difference give us?</p>
<p>2. Why 128-dim timestep embedding, not just the number t?</p>
<p>3. If we had 3 cameras instead of 1, how would 260 change?</p>
</div>
</div>

---

# Step B: We Need a Denoiser

We have a 260-dim conditioning vector. Now we need the **actual denoiser** — the neural network that takes noisy actions and predicts the noise.

<div class="grid grid-cols-2 gap-6 mt-4">

<div class="card">

### The Input

- **Noisy action trajectory**: 16 timesteps × 2 dims = 32 numbers
- **Conditioning vector**: 260 dims (from Step A)

### The Output

- **Predicted noise**: 16 timesteps × 2 dims = 32 numbers

Same shape as the input — for every noisy action value, predict how much noise was added.

</div>

<div class="accent-card" v-click>

### What Architecture?

We need something that:

1. Takes a **sequence** (16 timesteps) as input
2. Outputs a **sequence** of the same length
3. Can be **conditioned** on the 260-dim vector
4. Produces **smooth** outputs (no sudden jumps)

**Answer: a 1D U-Net**

</div>

</div>

---

# Visualize: Denoiser Input/Output

<div class="text-sm opacity-60 -mt-2 mb-2">Noisy actions in, predicted noise out — same shape [16×2], different meaning.</div>

<div class="flex justify-center items-start">
<img src="/figures/denoiser-io.png" class="rounded-lg" style="max-height:72vh; max-width:85%;" />
</div>

---

# What is a U-Net?

<a href="/notebooks/Component_1D_UNet.ipynb" download class="text-xs px-2 py-1 rounded" style="background:rgba(90,127,165,0.08);color:#5a7fa5;text-decoration:none;border:1px solid rgba(90,127,165,0.2);position:absolute;right:2em;top:4.5em;">Notebook: Component_1D_UNet.ipynb</a>

A U-Net is an **encoder-decoder** architecture with **skip connections**.

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

### The Shape

```
Input (16 timesteps)
  ↓ Encoder (compress)
    ↓ Bottleneck (smallest)
  ↑ Decoder (expand)
Output (16 timesteps)
```

- **Encoder**: Compresses the sequence, finding high-level patterns
- **Decoder**: Expands back to full resolution
- **Skip connections**: Copy detail from encoder → decoder (arrows across the U)

</div>

<div v-click>

### Why U-Net?

<div class="teal-card mb-3">

**Without skip connections**: The bottleneck loses fine detail. The output is blurry/imprecise.

</div>

<div class="accent-card">

**With skip connections**: Fine details are preserved. The encoder captures "what" and "where", the decoder uses both to produce precise output.

</div>

This is why U-Nets dominate in diffusion models — they preserve both global structure AND local detail.

</div>

</div>

---

# Visualize: U-Net Encoder-Decoder

<div class="text-sm opacity-60 -mt-2 mb-2">Compress, process, expand — with skip connections to preserve both global structure and local detail.</div>

<div class="grid grid-cols-2 gap-4 mt-1">

<div class="flex items-start justify-center">
<img src="/figures/unet-encoder-decoder.png" class="rounded-lg" style="max-height:65vh; max-width:100%;" />
</div>

<div class="flex flex-col items-center gap-4">

<video controls class="rounded-lg" style="max-height:46vh; max-width:100%;">
  <source src="/animations/Scene05_1DUNetFlow.mp4" type="video/mp4">
</video>

<a href="/notebooks/Component_1D_UNet.ipynb" download class="card text-sm px-4 py-2 text-center" style="text-decoration:none;color:var(--claude-text);">
Download: <code>Component_1D_UNet.ipynb</code>
</a>

</div>

</div>

---

# Why 1D, Not 2D?

In image diffusion, the U-Net uses **2D convolutions** (sliding over height × width). But our data is different.

<div class="grid grid-cols-2 gap-6 mt-4">

<div class="card">

### Image Diffusion: 2D

Input: 256×256×3 image

Convolutions slide in **two spatial dimensions** (height and width).

Makes sense — images have 2D structure.

</div>

<div class="accent-card">

### Our Case: 1D

Input: **16 timesteps × 2 actions**

Rearranged to: `[batch, 2, 16]` — 2 channels, 16 time positions.

Convolutions slide along **one dimension** (time).

<div class="mt-2 text-sm">

**This makes sense:** Action $a_5$ is related to $a_4$ and $a_6$ (nearby in time), but not especially to $a_1$ (far away). 1D convolutions capture this **temporal locality**.

</div>

</div>

</div>

---

# Visualize: 1D vs 2D Convolutions

<div class="text-sm opacity-60 -mt-2 mb-2">Images need 2D convolutions (height × width). Time-series trajectories need 1D (along time).</div>

<div class="flex flex-col items-center" style="margin-top:0;">
<img src="/figures/1d-vs-2d-conv.png" class="rounded-lg" style="max-height:68vh; max-width:85%;" />

<a href="/notebooks/Component_1D_UNet.ipynb" download class="card text-sm px-4 py-2 mt-3 text-center" style="text-decoration:none;color:var(--claude-text);">
Download: <code>Component_1D_UNet.ipynb</code>
</a>

</div>

---

# The 1D U-Net Architecture

<div class="flex justify-center mt-2">
<img src="/figures/unet-1d-architecture.png" class="rounded-lg" style="max-height:32vh;" />
</div>

<div v-click class="card mt-3 text-sm">

| Block | Channels | Temporal Size | What Happens |
|-------|----------|:---:|---|
| Input | 2 | 16 | Raw noisy actions |
| Down 1 | 512 | 16 | Extract low-level temporal patterns |
| Down 2 | 1024 | 8 | Downsample, find medium-scale patterns |
| Down 3 | 2048 | 4 | Compress to high-level representation |
| Up 1 | 1024 | 8 | Expand back with skip connection |
| Up 2 | 512 | 16 | Restore temporal resolution |
| Output | 2 | 16 | Predicted noise (same shape as input) |

</div>

---

# Why CNNs for Robot Trajectories?

The choice of 1D CNNs has a powerful **inductive bias** for robot actions.

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

### The Sliding Window

A 1D convolution with kernel size 5 looks at **5 consecutive timesteps** at once:

$$[\,a_{t-2},\, a_{t-1},\, a_t,\, a_{t+1},\, a_{t+2}\,]$$

This naturally produces outputs that are **consistent with neighbors** — i.e., **smooth trajectories**.

<div class="accent-card mt-3">

A sudden jump from $a_t = 0.3$ to $a_{t+1} = 5.7$ would be physically dangerous for a real robot. The CNN's locality bias prevents this.

</div>

</div>

<div v-click>

### Compare to Alternatives

<div class="card mb-3 text-sm">

**Fully connected network**: Treats step 1 and step 16 equally. No notion of temporal locality. Can produce jagged outputs.

</div>

<div class="teal-card text-sm">

**Transformer**: Attends to all timesteps equally. Very powerful but doesn't have a built-in smoothness bias. The paper also tested a Transformer variant — CNN performed better on most tasks.

</div>

</div>

</div>

---

# Visualize: CNN Smoothness Bias

<div class="text-sm opacity-60 -mt-2 mb-2">Convolutional locality naturally produces smooth trajectories — each output depends on its neighbors.</div>

<div class="flex justify-center items-start">
<img src="/figures/cnn-smoothness.png" class="rounded-lg" style="max-height:72vh; max-width:85%;" />
</div>

---

# Step C: The Conditioning Problem

The U-Net takes noisy actions and outputs predicted noise. But there's a critical question:

<div class="mt-4">

<div class="accent-card mb-3">

**Without conditioning**: The U-Net sees `[16 × 2]` noisy actions and the timestep. But it has NO IDEA what the robot is looking at. It would generate random motions with no purpose — "denoise toward... what?"

</div>

<div class="teal-card" v-click>

**With conditioning**: The U-Net also receives the 260-dim vector that encodes the camera view and robot state. Now it knows: "The cup is on the left, the robot arm is here" → it denoises toward a trajectory that reaches the cup.

</div>

</div>

<div v-click class="mt-3 card text-center">

**How do we inject this 260-dim vector into the U-Net?** We could concatenate it... but there's a much better way: **FiLM**.

</div>

---

# Visualize: Blind vs Conditioned Denoising

<div class="text-sm opacity-60 -mt-2 mb-2">Without observations, the denoiser plans in the dark. With conditioning, it knows where to reach.</div>

<div class="flex justify-center items-start">
<img src="/figures/blind-vs-conditioned.png" class="rounded-lg" style="max-height:72vh; max-width:85%;" />
</div>

---

# FiLM: Feature-wise Linear Modulation

<a href="/notebooks/Component_FiLM.ipynb" download class="text-xs px-2 py-1 rounded" style="background:rgba(90,127,165,0.08);color:#5a7fa5;text-decoration:none;border:1px solid rgba(90,127,165,0.2);position:absolute;right:2em;top:4.5em;">Notebook: Component_FiLM.ipynb</a>

FiLM is an elegant way to **condition** a neural network on external information.

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

### The Idea

At **every layer** of the U-Net, we modify the hidden features:

$$h' = \gamma \cdot h + \beta$$

- $h$ = the hidden activation (what the U-Net computed so far)
- $\gamma$ = **scale** (learned from the 260-dim vector)
- $\beta$ = **shift** (learned from the 260-dim vector)

<div v-click class="mt-3 card text-sm">

$\gamma$ and $\beta$ are produced by a small **linear layer** that takes the 260-dim conditioning vector and outputs the right number of scale/shift values for each U-Net layer.

</div>

</div>

<div v-click>

### Why Not Just Concatenate?

<div class="card mb-3 text-sm">

**Concatenation**: Adds the conditioning as extra input channels. The network must learn to use it. Works OK but limited.

</div>

<div class="accent-card text-sm">

**FiLM**: Directly **scales and shifts** every feature at every layer. This is much more powerful because:

- Scale can **amplify** relevant features
- Scale can **suppress** irrelevant features
- It happens at **every layer**, not just the input

It's like adjusting the volume and tone on every instrument in an orchestra, not just adding another instrument.

</div>

</div>

</div>

---

# Visualize: FiLM Conditioning

<div class="text-sm opacity-60 -mt-2 mb-2">Scale and shift every feature at every layer — the U-Net "sees" through the camera via FiLM.</div>

<div class="grid grid-cols-2 gap-4 mt-1">

<div class="flex items-start justify-center">
<img src="/figures/film-mechanism.png" class="rounded-lg" style="max-height:65vh; max-width:100%;" />
</div>

<div class="flex flex-col items-center gap-4">

<video controls class="rounded-lg" style="max-height:46vh; max-width:100%;">
  <source src="/animations/Scene06_FiLMConditioning.mp4" type="video/mp4">
</video>

<a href="/notebooks/Component_FiLM.ipynb" download class="card text-sm px-4 py-2 text-center" style="text-decoration:none;color:var(--claude-text);">
Download: <code>Component_FiLM.ipynb</code>
</a>

</div>

</div>

---

# Example: FiLM Calculation

Let's trace real numbers through FiLM at one U-Net layer.

<div class="grid grid-cols-2 gap-6 mt-3">

<div class="card">

### The Inputs

**Hidden features** $h$ (what the U-Net computed):

$$h = [0.5, \;-0.3, \;0.8, \;1.2, \;-0.5]$$

**From conditioning** (260d → linear layer):

$$\gamma = [2.0, \;0.1, \;1.5, \;0.0, \;3.0]$$
$$\beta = [0.0, \;0.0, \;0.3, \;1.0, \;-0.2]$$

### The Computation

$$h' = \gamma \cdot h + \beta$$

</div>

<div class="accent-card" v-click>

### Element by Element

| Feature | $h$ | $\gamma$ | $\beta$ | $h' = \gamma h + \beta$ | Effect |
|:---:|:---:|:---:|:---:|:---:|---|
| 1 | 0.5 | **2.0** | 0.0 | **1.0** | Amplified ×2 |
| 2 | −0.3 | **0.1** | 0.0 | **−0.03** | Suppressed ×0.1 |
| 3 | 0.8 | 1.5 | **0.3** | **1.5** | Scaled + shifted |
| 4 | 1.2 | **0.0** | **1.0** | **1.0** | Zeroed + replaced |
| 5 | −0.5 | 3.0 | −0.2 | **−1.7** | Amplified + shifted |

<div class="mt-2 text-sm">

$\gamma = 2.0$ → "This feature is important, amplify it!"

$\gamma = 0.0$ → "This feature is irrelevant, suppress it completely"

</div>

</div>

</div>

<div v-click class="mt-2">
<img src="/figures/example-film-calc.png" class="rounded-lg mx-auto" style="max-height:30vh;" />
</div>

---

# FiLM: The Teapot Analogy

<div class="grid grid-cols-2 gap-6 mt-3">

<div>

### Imagine the U-Net Is a Brain

The U-Net is trying to plan: "How should I move the arm?"

**Without FiLM** (blind):

The brain plans in the dark. *"I'll move... somewhere? Maybe left? Maybe right?"* It has no idea where the cup is.

<div v-click class="accent-card mt-3">

**With FiLM** (sighted):

The camera sees the cup on the **LEFT**. The FiLM layer:
- **Boosts** ($\gamma > 1$) the "Move Left" features
- **Suppresses** ($\gamma < 1$) the "Move Right" features
- **Shifts** ($\beta$) the trajectory toward the correct region

→ The brain correctly plans to pour into the cup on the left!

</div>

</div>

<div v-click>

<img src="/figures/film-conditioning.png" class="rounded-lg" style="max-height:46vh;" />

</div>

</div>

---

# Quiz: Denoiser & Conditioning (2/3)

<div class="quiz-card mt-2">

**Q1:** What are the input and output shapes of the 1D U-Net for PushT?

<div v-click class="mb-3 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> Input: noisy actions [16×2] (16 timesteps, 2D actions). Output: predicted noise [16×2] — same shape. The U-Net preserves the temporal dimension.
</div>

**Q2:** Why does the U-Net use 1D convolutions instead of 2D?

<div v-click class="mb-3 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> The input is a 1D sequence (time axis only), not a 2D image. Each timestep has an action vector — we convolve along the time dimension to capture temporal patterns. 2D convs would require a spatial grid.
</div>

**Q3:** What does FiLM stand for, and what are the two operations it performs?

<div v-click class="mb-3 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> Feature-wise Linear Modulation. It applies γ ⊙ h + β — element-wise scale (γ) and shift (β) to feature activations. The γ and β values are predicted from the conditioning vector.
</div>

**Q4:** Without FiLM conditioning, the U-Net is "blind." What does this mean practically?

<div v-click class="mb-3 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> The U-Net would generate trajectories without knowing what the robot sees or what timestep it's at. It would produce generic denoising, not goal-directed plans — like navigating with your eyes closed.
</div>

</div>

---

# Quiz: Denoiser & Conditioning (2/3) — continued

<div class="quiz-card mt-2">

**Q5:** The U-Net encoder path has dimensions [256, 512, 1024]. What happens to the temporal dimension at each stage?

<div v-click class="mb-3 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> It halves: 16 → 8 → 4 → 2. The decoder then upsamples back: 2 → 4 → 8 → 16, with skip connections from the encoder at each level.
</div>

**Q6:** What are the three components concatenated to form the 260d conditioning vector?

<div v-click class="mb-3 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> (1) Visual features from SpatialSoftmax: 128d (64 per image × 2 timesteps), (2) robot joint state: 4d (2 per timestep × 2), (3) timestep embedding: 128d. Total: 128 + 4 + 128 = 260d.
</div>

**Q7:** Why use sinusoidal embedding for the timestep instead of just feeding k directly as a number?

<div v-click class="mb-3 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> A single scalar k gives the network very little information. Sinusoidal embedding creates a 128d fingerprint where each dimension oscillates at a different frequency — the network can distinguish nearby timesteps and detect multi-scale patterns.
</div>

**Q8:** How does kernel size 5 in the 1D conv help produce smooth trajectories?

<div v-click class="mb-3 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> Kernel size 5 means each output depends on 5 neighboring timesteps. This creates a locality bias — the predicted noise at timestep t must be consistent with timesteps t-2 through t+2, naturally preventing jerky motion.
</div>

</div>

---

# Quiz: Denoiser & Conditioning (2/3) — continued

<div class="quiz-card mt-2">

**Q9:** Skip connections in the U-Net concatenate encoder features with decoder features. Why is this critical?

<div v-click class="mb-3 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> The encoder bottleneck compresses 16 timesteps down to 2, losing fine-grained temporal detail. Skip connections pass the original high-resolution features directly to the decoder, preserving both local detail (exact action values) and global structure (overall trajectory shape).
</div>

**Q10:** FiLM is applied at every residual block in the U-Net. Why condition at every layer rather than just the input?

<div v-click class="mb-3 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> Different layers operate at different scales — early layers handle fine details (exact positions), deep layers handle global structure (trajectory shape). FiLM at every layer lets the observation influence the denoising at all scales simultaneously.
</div>

</div>

---

# Step D: Why Predict 16 but Execute Only 8?

<a href="/notebooks/Component_Receding_Horizon.ipynb" download class="text-xs px-2 py-1 rounded" style="background:rgba(90,127,165,0.08);color:#5a7fa5;text-decoration:none;border:1px solid rgba(90,127,165,0.2);position:absolute;right:2em;top:4.5em;">Notebook: Component_Receding_Horizon.ipynb</a>

We could execute all 16 predicted actions. Why don't we?

<div class="flex justify-center mt-3">
<img src="/figures/receding-horizon.png" class="rounded-lg" style="max-height:22vh;" />
</div>

<div class="grid grid-cols-2 gap-4 mt-3">

<div class="accent-card">

### The Problem with Executing All 16

- The world might **change** during execution (someone moves the cup)
- Actions 12-16 are predictions for 1.2-1.6 seconds in the future — increasingly uncertain
- If something goes wrong at step 5, the remaining 11 actions are useless

</div>

<div class="teal-card" v-click>

### Receding Horizon: Execute 8, Re-plan

- Execute **first 8** actions (0.8 seconds)
- Take **new observation** (the world may have changed)
- Generate a **new 16-step plan**
- Execute the first 8 of the new plan
- Repeat!

This balances **smoothness** (8-step commitment) with **adaptability** (frequent re-planning).

</div>

</div>

---

# The Complete Control Loop

Here's the full closed-loop system, step by step:

<div class="card mt-4 text-sm">

```
Step 1: OBSERVE
  → Capture camera frame at t-1 and t (96×96 each)
  → Read robot joint state at t-1 and t

Step 2: ENCODE
  → ResNet18 + SpatialSoftmax → 128 visual features
  → Concatenate with 4 state values + 128 timestep embedding → 260d

Step 3: DENOISE (the diffusion part!)
  → Sample random noise: [16 × 2] random numbers
  → Run 100 denoising steps through the 1D U-Net with FiLM
  → Output: clean action trajectory [16 × 2]

Step 4: EXECUTE
  → Send first 8 actions to the robot motors
  → Wait 0.8 seconds as the robot moves

Step 5: REPEAT from Step 1!
```

</div>

<div v-click class="mt-2 accent-card text-center text-sm">

This loop runs continuously. Every 0.8 seconds, the robot gets a fresh plan based on what it currently sees.

</div>

---

# Visualize: The Complete Control Loop

<div class="text-sm opacity-60 -mt-2 mb-2">Observe → Encode → Denoise → Execute 8 of 16 → Repeat every 0.8 seconds.</div>

<div class="flex flex-col items-center" style="margin-top:0;">
<img src="/figures/control-loop.png" class="rounded-lg" style="max-height:68vh; max-width:85%;" />

<a href="/notebooks/Component_Receding_Horizon.ipynb" download class="card text-sm px-4 py-2 mt-3 text-center" style="text-decoration:none;color:var(--claude-text);">
Download: <code>Component_Receding_Horizon.ipynb</code>
</a>

</div>

---

# Example: One Complete Forward Pass

Let's trace **one camera frame** through the entire pipeline, watching the tensor shapes transform.

<div class="flex justify-center mt-2">
<img src="/figures/example-forward-pass.png" class="rounded-lg" style="max-height:35vh;" />
</div>

<div class="card mt-3 text-sm">

| Step | Operation | Shape | Values |
|:---:|---|:---:|:---:|
| 1 | Camera frame | **96 × 96 × 3** | 27,648 floats |
| 2 | ResNet18 backbone | **512 × 3 × 3** | 4,608 floats |
| 3 | Conv2d(512 → 32) | **32 × 3 × 3** | 288 floats |
| 4 | SpatialSoftmax | **32 × 2** | 64 floats |
| 5 | ×2 images (t−1, t) | — | 128 floats |
| 6 | + state (t−1, t) | — | +4 floats |
| 7 | + timestep embedding | — | +128 floats |
| 8 | **Conditioning vector** | **260** | **260 floats** |
| 9 | FiLM → 1D U-Net | **[16 × 2]** | 32 floats out |
| 10 | Execute first 8 | **[8 × 2]** | 16 motor commands |

</div>

<div v-click class="mt-2 accent-card text-center text-sm">

**27,648 pixels → 260 features → 16 motor commands.** The network compresses 27K inputs into the 16 numbers that actually move the robot.

</div>

---

# The Training Objective: Beautifully Simple

Despite the complex architecture, training is remarkably simple.

<div class="card mt-4">

```python
for batch in dataloader:
    clean_actions = batch['action']                    # Expert trajectory [B, 16, 2]
    t = random_timestep()                              # Random t ∈ {0, ..., 99}
    noise = torch.randn_like(clean_actions)            # ε ~ N(0, I)
    noisy_actions = scheduler.add_noise(clean_actions, noise, t)
    predicted_noise = unet(noisy_actions, t, conditioning)
    loss = MSE(predicted_noise, noise)                 # How wrong?
    loss.backward()
```

</div>

<div v-click class="mt-3 accent-card text-center">

**That's it.** Add noise to expert actions → ask the network to predict the noise → MSE loss → backprop. The complexity is in the architecture, not the training.

</div>

---

# Visualize: Training Pipeline

<div class="text-sm opacity-60 -mt-2 mb-2">Add noise to expert actions, predict the noise, compute MSE loss, backprop. Beautifully simple.</div>

<div class="grid grid-cols-2 gap-4 mt-1">

<div class="flex items-start justify-center">
<img src="/figures/training-pipeline.png" class="rounded-lg" style="max-height:65vh; max-width:100%;" />
</div>

<div class="flex flex-col items-center gap-4">

<video controls class="rounded-lg" style="max-height:55vh; max-width:100%;">
  <source src="/animations/Scene07_TrainingLoop.mp4" type="video/mp4">
</video>

</div>

</div>

---

# Quiz: Training, Control & End-to-End (3/3)

<div class="quiz-card mt-2">

**Q1:** Why do we predict 16 actions but only execute the first 8?

<div v-click class="mb-3 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> The last 8 predicted actions degrade in quality (they're furthest from the observation). Executing only the first 8 and re-planning gives the robot fresh observations, combining commitment (smooth motion) with adaptability.
</div>

**Q2:** What is the training loss function, and what exactly are its two arguments?

<div v-click class="mb-3 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> MSE loss between the actual noise ε that was added to the clean actions, and the predicted noise ε̂ output by the U-Net. Both are [16×2] tensors.
</div>

**Q3:** Walk through the complete inference pipeline: camera image → executed motor commands.

<div v-click class="mb-3 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> 96×96 image → ResNet18 (512×3×3) → SpatialSoftmax (64d) → concat with state + timestep embedding = 260d → FiLM conditions 1D U-Net → denoise 100 steps → 16-step trajectory → execute first 8 → re-observe → repeat.
</div>

**Q4:** During training, does the model ever run the denoising loop (100 steps)?

<div v-click class="mb-3 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> No. Training is a single forward pass: pick random timestep k, add noise to clean actions at that level, predict the noise. The 100-step loop only happens at inference.
</div>

</div>

---

# Quiz: Training, Control & End-to-End (3/3) — continued

<div class="quiz-card mt-2">

**Q5:** What is the receding horizon frequency? How often does the robot re-plan?

<div v-click class="mb-3 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> Every 8 action steps. At 10 Hz control, that's every 0.8 seconds. The robot executes 8 steps, takes a new observation, and generates a fresh 16-step plan.
</div>

**Q6:** Why does the model observe at both t-1 and t (two timesteps) instead of just the current frame?

<div v-click class="mb-3 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> Two frames give the model velocity/motion information — it can infer which direction objects are moving and how fast. A single frame only shows position, not dynamics.
</div>

**Q7:** The training randomly samples a timestep k ∈ [0, 100]. Why random and not sequential?

<div v-click class="mb-3 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> Random sampling ensures the network learns to denoise at all noise levels equally. If we trained sequentially, it would overfit to certain noise levels and fail at others.
</div>

**Q8:** What happens if you increase Tₐ from 8 to 16 (execute all predicted actions)?

<div v-click class="mb-3 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> The robot commits to longer plans without re-observing. This makes motion smoother but less reactive — if something changes (object moves, disturbance), the robot can't adapt for 1.6 seconds instead of 0.8.
</div>

</div>

---

# Quiz: Training, Control & End-to-End (3/3) — continued

<div class="quiz-card mt-2">

**Q9:** At inference, the model starts from pure Gaussian noise. Where does this noise come from?

<div v-click class="mb-3 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> <code>torch.randn(1, 16, 2)</code> — 32 random numbers from a standard normal distribution N(0, I). Different random seeds produce different valid trajectories — this is the stochasticity that solves multimodality.
</div>

**Q10:** The full system runs at 10 Hz. If denoising takes 100 U-Net forward passes, is this fast enough?

<div v-click class="mb-3 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> Each U-Net pass takes ~1ms on a GPU, so 100 passes = ~100ms. Combined with encoding (~5ms), total inference is ~105ms per plan. Since we only re-plan every 8 steps (800ms), this easily fits within the budget.
</div>

</div>

---

# 3D Interactive: The Full Diffusion Policy

<div class="mt-1 text-center text-sm opacity-60">

Watch noise transform into a trajectory, then see the SO-101 arm execute it.

</div>

<iframe src="https://diffusion-policy-3d-viz.vercel.app/" class="w-full rounded-lg mt-1" style="height:72vh;border:none;" />

---

# 2D Interactive: Training Walkthrough

<div class="mt-1 text-center text-sm opacity-60">

Trace ONE example through every step of the training pipeline with real numbers.

</div>

<iframe src="https://diffusion-policy-training.vercel.app/" class="w-full rounded-lg mt-1" style="height:72vh;border:none;" />

---

# 2D Interactive: Diffusion Policy Visualizer

<div class="mt-1 text-center text-sm opacity-60">

Tea-pouring images, SVG trajectory overlays, and a noise slider.

</div>

<iframe src="https://diffusion-policy-visualizer.vercel.app/" class="w-full rounded-lg mt-1" style="height:72vh;border:none;" />

---

# Comparison: Diffusion Policy vs Baselines

<div class="grid grid-cols-2 gap-4 mt-3">

<div class="card">

<video autoplay loop muted playsinline class="inline-video w-full rounded-lg">
  <source src="https://diffusion-policy.cs.columbia.edu/videos/all_pusht_wide_web.mp4" type="video/mp4">
</video>

</div>

<div>

| Method | Push-T Score |
|--------|:---:|
| Random Policy | ~5% |
| IBC (Energy-Based) | ~60% |
| BC-RNN (Recurrent) | ~72% |
| **Diffusion (CNN)** | **~91%** |
| **Diffusion (Transformer)** | **~87%** |

<div v-click class="mt-2 accent-card text-sm">

**Why diffusion wins:**
1. Captures multimodal distributions
2. Action chunking prevents jitter
3. 100-step denoising = expressive
4. Noise = regularization

</div>

</div>

</div>

---
layout: section
---

# Part 4
## Hands-On Implementation

Train a Diffusion Policy from scratch on PushT — then scale to real robot tasks

---

# The Simulation Environments

These are the tasks you'll work with across the bootcamp. Each one tests a different capability of Diffusion Policy.

<div class="grid grid-cols-3 gap-3 mt-4">

<div class="card text-center">

### Week 1: PushT

<video autoplay loop muted playsinline class="inline-video w-full mt-1 rounded-lg">
  <source src="https://diffusion-policy.cs.columbia.edu/videos/highlight_pusht.mp4" type="video/mp4">
</video>

<div class="text-xs mt-1">2D pushing — your "Hello World" for diffusion policy. 205 demos, 2D actions.</div>

</div>

<div class="card text-center" v-click>

### Week 2: ALOHA

<video autoplay loop muted playsinline class="inline-video w-full mt-1 rounded-lg">
  <source src="https://diffusion-policy.cs.columbia.edu/videos/highlight_sauce.mp4" type="video/mp4">
</video>

<div class="text-xs mt-1">Bimanual manipulation — 14 DOF, dual arms, real-world teleoperation data.</div>

</div>

<div class="card text-center" v-click>

### Week 3: LIBERO

<video autoplay loop muted playsinline class="inline-video w-full mt-1 rounded-lg">
  <source src="https://diffusion-policy.cs.columbia.edu/videos/kitchen.mp4" type="video/mp4">
</video>

<div class="text-xs mt-1">Multi-task with language — 130 tasks, language-conditioned policies.</div>

</div>

</div>

---

# Week 1: What You'll Build

Your goal this week: **train a working Diffusion Policy on PushT from scratch** using the LeRobot framework.

<div class="grid grid-cols-2 gap-4 mt-3">

<div>

### Step-by-Step Workflow

<div class="card text-sm">

1. **Load PushT** — 205 expert demos at 10 FPS via `lerobot`
2. **Explore the data** — visualize obs images, states, action trajectories
3. **Build the architecture** — ResNet18 → SpatialSoftmax → 1D U-Net + FiLM
4. **Train for 5000 steps** (~1-2 hrs on T4 GPU)
5. **Evaluate** — run the trained policy in the PushT simulator
6. **Visualize denoising** — watch noise become a trajectory
7. **Test multimodality** — same observation, 20 different trajectories
8. **Run ablations** — break things on purpose to understand why they work

</div>

</div>

<div v-click>

### The Notebook

<div class="accent-card text-sm mb-3">

**`Week1_PushT_Diffusion_Policy.ipynb`** — a single end-to-end Colab notebook. All 8 steps above are in sequential cells. Just run top to bottom.

</div>

<div class="card text-sm mb-2">

**Runtime**: Google Colab T4 GPU (free tier works)

**Framework**: LeRobot v0.4.4

**Time**: ~3 hours total (1-2 hrs training, rest is exploration)

</div>

<a href="/notebooks/Week1_PushT_Diffusion_Policy.ipynb" download class="inline-block px-3 py-1 rounded-lg text-sm" style="background:#c2785c;color:#fff;font-weight:600;text-decoration:none;">
  Download Week 1 Notebook
</a>

</div>

</div>

---

# The PushT Task: Your Training Ground

<div class="grid grid-cols-2 gap-4 mt-3">

<div>

<div class="card text-sm">

```python
import gymnasium as gym
import gym_pusht

env = gym.make(
    "gym_pusht/PushT-v0",
    obs_type="pixels_agent_pos",
    render_mode="rgb_array",
)
obs, info = env.reset(seed=42)
print(obs['pixels'].shape)   # (384, 384, 3)
print(obs['agent_pos'])      # [x, y]
```

</div>

A blue circle pushes a T-block onto a green target. **205 expert demos** at 10 FPS.

</div>

<div v-click>

### Why PushT is Deceptively Hard

<div class="accent-card mb-2 text-sm">

**Multiple valid strategies** — approach from left, right, above → MSE averages them → crashes

</div>

<div class="teal-card mb-2 text-sm">

**Precise spatial reasoning** — T-block must be rotated and positioned exactly → needs SpatialSoftmax

</div>

<div class="blue-card text-sm">

**Temporal coordination** — sequence of pushes, not one action → needs action chunking

</div>

</div>

</div>

---

# Robosuite Benchmarks: Where Diffusion Policy Excels

<div class="grid grid-cols-4 gap-2 mt-4 text-center text-sm">

<div class="card">

### Lift
<video autoplay loop muted playsinline class="inline-video w-full mt-1">
  <source src="https://diffusion-policy.cs.columbia.edu/videos/lift.mp4" type="video/mp4">
</video>
<div class="text-xs mt-1">Pick up a cube</div>
</div>

<div class="card">

### Can
<video autoplay loop muted playsinline class="inline-video w-full mt-1">
  <source src="https://diffusion-policy.cs.columbia.edu/videos/can.mp4" type="video/mp4">
</video>
<div class="text-xs mt-1">Pick and place a can</div>
</div>

<div class="card">

### Square
<video autoplay loop muted playsinline class="inline-video w-full mt-1">
  <source src="https://diffusion-policy.cs.columbia.edu/videos/square.mp4" type="video/mp4">
</video>
<div class="text-xs mt-1">Insert square peg</div>
</div>

<div class="card">

### Tool Hang
<video autoplay loop muted playsinline class="inline-video w-full mt-1">
  <source src="https://diffusion-policy.cs.columbia.edu/videos/tool_hang.mp4" type="video/mp4">
</video>
<div class="text-xs mt-1">Hardest — hang a tool</div>
</div>

</div>

<div v-click class="mt-3 accent-card text-center text-sm">

These Robosuite environments are where diffusion policy was originally benchmarked. In Week 4 projects, you can train on any of these.

</div>

---

# Key Config: `delta_timestamps`

The most confusing config for newcomers — let's demystify it.

<div class="card mt-3 text-sm">

```python
delta_timestamps = {
    "observation.image": [-0.1, 0.0],           # 2 frames: t-1 and t
    "observation.state": [-0.1, 0.0],            # 2 states: t-1 and t
    "action": [-0.1, 0.0, 0.1, ..., 1.4],       # 16 actions: t-1 to t+14
}
```

</div>

<div class="grid grid-cols-3 gap-3 mt-3 text-center">

<div class="accent-card text-sm">

**Images**: 2 frames

$[-0.1, 0.0]$ sec

*"What just happened?"*

</div>

<div class="teal-card text-sm">

**States**: 2 positions

$[-0.1, 0.0]$ sec

*"Where was I? Where am I?"*

</div>

<div class="blue-card text-sm">

**Actions**: 16 steps

$[-0.1 \text{ to } 1.4]$ sec

*"Plan for next 1.5 seconds"*

</div>

</div>

<div v-click class="mt-3 purple-card text-sm text-center">

At 10 FPS: 0.1s = 1 frame. So `[-0.1, 0.0]` = previous frame + current frame.

</div>

---

# Notebook Part 6: The Denoising Visualization

This is the most illuminating part — noise becoming a trajectory in real time.

<div class="card mt-3 text-sm">

```python
for t in noise_scheduler.timesteps:   # 99, 98, ..., 0
    predicted_noise = unet(noisy_actions, t, global_cond)
    noisy_actions = scheduler.step(predicted_noise, t, noisy_actions)
```

</div>

<div class="flex justify-center mt-3">
<img src="/figures/denoising-trajectory.png" class="rounded-lg" style="max-height:24vh;" />
</div>

<div v-click class="mt-2 teal-card text-center text-sm">

**Run this 20 times** with different noise seeds (Part 7) → 20 DIFFERENT valid trajectories from the same observation. **Multimodality in action!**

</div>

---

# Notebook Part 8: Ablation Experiments

**Pick 2-3 and compare.** This builds real understanding of each architectural choice.

<div class="grid grid-cols-2 gap-3 mt-3">

<div class="card text-sm">

| Experiment | What to Expect |
|-----------|----------------|
| **DDIM (10 steps)** | 10x faster inference, similar quality |
| **8 keypoints** | Reduced spatial precision, faster |
| **Small U-Net** | Faster training, maybe worse |

</div>

<div class="card text-sm">

| Experiment | What to Expect |
|-----------|----------------|
| **No FiLM scale** | Weaker visual conditioning |
| **1 obs step** | No temporal context |
| **Short horizon (8)** | Less planning ahead |

</div>

</div>

<div class="card mt-3 text-sm">

```python
# Example: Train with 8 keypoints instead of 32
losses_8kp, _, _, _ = train_ablation(
    {"spatial_softmax_num_keypoints": 8}, steps=2000, label="8-keypoints"
)
```

</div>

<div v-click class="mt-2 accent-card text-sm">

**Week 1 Deliverables**: Trained checkpoint, eval video, loss curves, denoising viz, 2-3 ablation comparisons.

</div>

---

# Brainstorming: Design Trade-offs

<div class="brainstorm-card mt-4">
<div class="text-center opacity-40 text-xl">
<p><em>Annotation space — draw and discuss</em></p>
<p>1. To = 2 → what if To = 5? More context but more compute.</p>
<p>2. Predict 16, execute 8 → what if we execute all 16? Or only 1?</p>
<p>3. 100 denoising steps. DDIM can do 10. What breaks at 1?</p>
<p>4. ResNet18 vs ResNet50 vs ViT? Trade-offs?</p>
</div>
</div>

---
layout: section
---

# Part 5
## Looking Ahead

---

# The Roadmap

<div class="grid grid-cols-4 gap-3 mt-6">

<div class="accent-card text-center text-sm">

### Week 1
**Diffusion Policy**

PushT — learn action generation via denoising

*You are here*

</div>

<div class="teal-card text-center text-sm" v-click>

### Week 2
**ALOHA**

Bimanual manipulation — 14 DOF, dual arms

</div>

<div class="blue-card text-center text-sm" v-click>

### Week 3
**LIBERO**

Multi-task — 130 tasks with language conditioning

</div>

<div class="purple-card text-center text-sm" v-click>

### Week 4
**Projects**

DP3, DPPO, ManiSkill3, or cross-env transfer

</div>

</div>

---

# Diffusion Policy → pi0

Everything you learned today is the foundation for next-gen robot policies.

| | Diffusion Policy (Today) | pi0 (Future) |
|--|---|---|
| **Vision** | ResNet18 + SpatialSoftmax | SigLIP-So400M |
| **Language** | None | PaliGemma 3B |
| **Action gen** | DDPM (100 steps) | Flow matching (10 steps) |
| **Architecture** | 1D U-Net | Transformer (MoE) |
| **Multi-task** | Per-task model | Single model, many tasks |

<div v-click class="mt-3 accent-card text-sm">

**The trend**: Larger VLMs + lightweight action heads = better generalization. But the **core idea** — denoise noise into actions — remains at the heart of both.

</div>

---

# Deliverables

<div class="grid grid-cols-2 gap-4 mt-3">

<div>

### Required

1. **Complete Week 1 notebook** (Parts 0-7)
   - Train 5000+ steps
   - Evaluation video
   - Denoising visualization (Part 6)
   - Multimodality plot (Part 7)

2. **Run 2-3 ablations** (Part 8)

3. **Short report** (1 page) — what did you learn?

</div>

<div>

### Resources

<div class="card mb-2 text-sm">

**Paper**: [diffusion-policy.cs.columbia.edu](https://diffusion-policy.cs.columbia.edu/)

</div>

<div class="card mb-2 text-sm">

**Code**: [github.com/huggingface/lerobot](https://github.com/huggingface/lerobot)

</div>

<div class="card mb-2 text-sm">

**3D Viz**: [diffusion-policy-3d-viz.vercel.app](https://diffusion-policy-3d-viz.vercel.app)

</div>

<div class="card mb-2 text-sm">

**Training**: [diffusion-policy-training.vercel.app](https://diffusion-policy-training.vercel.app)

</div>

<div class="card text-sm">

**Visualizer**: [diffusion-policy-visualizer.vercel.app](https://diffusion-policy-visualizer-hzzuks7f0-rajatdandekars-projects.vercel.app)

</div>

</div>

</div>

---

# Final Discussion

<div class="brainstorm-card mt-4">
<div class="text-center opacity-40 text-xl">
<p><em>Open discussion — annotate together</em></p>
<p>1. What was the single most surprising idea today?</p>
<p>2. Is 100 denoising steps too slow for real-time control? How to speed up?</p>
<p>3. MSE loss produces sophisticated behavior — why does something so simple work?</p>
<p>4. What would YOU improve? Vision backbone? More observations? Different schedule?</p>
</div>
</div>

---
layout: center
class: text-center
---

# Let's Build

<div class="mt-6 text-lg" style="color:var(--claude-muted);">

Download the Week 1 notebook, upload to Google Colab, and start exploring.

</div>

<div class="mt-6">
<a href="/notebooks/Week1_PushT_Diffusion_Policy.ipynb" download class="inline-block px-6 py-3 rounded-xl text-lg" style="background:#c2785c;color:#fff;font-weight:700;text-decoration:none;">
  Download Week 1 Notebook
</a>
</div>

<div class="mt-8 text-sm" style="color:var(--claude-muted);">

Diffusion Policy — Chi et al., RSS 2023 | Built with Vizuara

</div>
