---
theme: default
title: "World Models Part 2: Scaling to Real Robots"
info: |
  Lecture — Modern Robot Learning from Scratch V2 Bootcamp
  Vizuara — Part 2 (LeWorld + DreamZero)
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

# World Models — Part 2

## Scaling to Real Robots

<div class="pt-8">
  <span class="px-4 py-2 rounded-lg text-lg" style="background:#c2785c;color:#fff;font-weight:700;">
    Modern Robot Learning from Scratch — V2
  </span>
</div>

<div class="pt-4 opacity-60">
  Vizuara Bootcamp — Part 2 continues from the main World Models lecture
</div>

<div class="abs-br m-6 flex gap-2">
  <a href="https://vizuara.ai" target="_blank" class="text-sm opacity-50 hover:opacity-100">
    vizuara.ai
  </a>
</div>

---

# What We'll Cover in Part 2

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### The Journey (Part 2)

<v-clicks>

<div class="accent-card mb-3">
<strong>Part 1:</strong> LeWorldModel — A tiny end-to-end JEPA from raw pixels. The counter-argument to giant foundation encoders.
</div>

<div class="teal-card mb-3">
<strong>Part 2:</strong> DreamZero — The joint world-action model. Leverages internet-scale video, trains policies and world models jointly.
</div>

</v-clicks>

</div>
<div>

### Where This Fits

<div class="card mt-2 text-sm">

In the main <strong>World Models</strong> lecture we covered:

- Why world models (Part 1)
- <strong>DINO-WM</strong> — predict in feature space (Part 2)
- <strong>RL foundations</strong> (Part 3)
- <strong>IRIS</strong> — world as language model (Part 4)
- <strong>DIAMOND</strong> — diffusion for pixel-space dreams (Part 5)
- <strong>Build Your Own WFM</strong> (Part 6)

**Part 2 takes the next step:** beyond games and robot play, toward models that scale to real robots and to internet-scale unlabeled video.

</div>

</div>
</div>

---

<div style="height:1px;"></div>

---
layout: center
---

# Part 1

## LeWorldModel (LeWM)

<div class="mt-4 opacity-60">A tiny end-to-end JEPA from raw pixels</div>

---

# The DINO-WM Ceiling

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### Where DINO-WM hits the wall

<v-clicks>

<div class="card text-sm mb-3">
<strong>Heavy encoder:</strong> DINOv2-Base is ~86M frozen parameters. Every observation is ~196 patch tokens at 768-dim — <span class="highlight">a lot</span> of latents to predict.
</div>

<div class="card text-sm mb-3">
<strong>Slow planning:</strong> CEM rollouts through DINO-WM take <span class="highlight">~47 seconds per step</span>. Totally unusable for real-time control.
</div>

<div class="card text-sm mb-3">
<strong>Frozen bottleneck:</strong> You cannot fine-tune the encoder for your domain. You're stuck with whatever ImageNet-DINO decided was important.
</div>

</v-clicks>

</div>
<div>

<v-click>

### The provocative question

<div class="accent-card text-sm">

If a pre-trained foundation encoder gives us such painful costs...

<strong>what if we just threw it away?</strong>

Could we learn a small, fast, from-scratch encoder + predictor that's actually <em>better</em>?

</div>

<div class="teal-card text-sm mt-3">
That's the bet LeWorldModel makes. It's not "DINO-WM but bigger" — it's the <strong>opposite philosophy</strong>.
</div>

</v-click>

</div>
</div>

---

# LeWorldModel: The Opposite of DINO-WM

<div class="mt-4">

<div class="grid grid-cols-2 gap-6">
<div class="card">
<h3>DINO-WM (main lecture, Part 2)</h3>
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

<v-click>

<div class="teal-card mt-4 text-sm text-center">
<strong>LeWM is the first JEPA that trains stably end-to-end from pixels</strong> without exponential moving averages, stop-gradients, or auxiliary supervision. It's the proof that you don't need a foundation encoder to learn useful world-model features.
</div>

</v-click>

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

<v-click>

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

</v-click>

</div>
<div>

<v-click>

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

</v-click>

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

<v-clicks>

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

</v-clicks>

<v-click>

<div class="purple-card mt-3 text-sm text-center">

$$\mathcal{L} = \mathcal{L}_{\text{pred}} + \lambda \cdot \mathrm{SIGReg}(Z), \qquad \lambda = 0.1, \quad M = 1024$$

<strong>Two loss terms total. No EMA. No stop-gradient. No auxiliary supervision.</strong>

</div>

</v-click>

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

# Training LeWM

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### The full training loop

<v-clicks>

<div class="card text-sm mb-3">

**1. Encode** a pair of consecutive frames
$$s_t = f_\theta(o_t), \quad s_{t+1} = f_\theta(o_{t+1})$$

**2. Predict** the next embedding given the action
$$\hat{s}_{t+1} = g_\phi(s_t, a_t)$$

**3. Compute prediction loss**
$$\mathcal{L}_{\text{pred}} = \|\hat{s}_{t+1} - s_{t+1}\|^2$$

**4. Compute SIGReg on the batch**
$$\mathcal{L}_{\text{SIGReg}} = \tfrac{1}{M}\sum_{m} \mathrm{test}(u_m^\top Z)$$

**5. Backprop through BOTH encoder and predictor** — the whole network learns jointly from pixels.

</div>

</v-clicks>

</div>
<div>

<v-click>

### Training recipe

<div class="teal-card text-sm mb-3">

| | |
|---|---|
| Data | Trajectories from the target task |
| Batch size | 256 latent pairs |
| Optimizer | AdamW |
| LR | 3e-4 cosine |
| $\lambda_{\text{SIGReg}}$ | 0.1 |
| $M$ (projections) | 1024 |
| Hardware | **1 GPU** (A100 or smaller) |
| Wall time | **A few hours** |

</div>

<div class="accent-card text-sm">
<strong>No pre-training.</strong> No foundation model download. No 8-GPU cluster. Just train the whole thing end-to-end on the task data you have.
</div>

</v-click>

</div>
</div>

---

# Planning with LeWM

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### Receding-horizon MPC

<v-clicks>

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

</v-clicks>

</div>
<div>

<v-click>

### Results across tasks

<div class="accent-card text-sm mb-3">

| Task | Method | Success |
|---|---|---|
| Push-T | DINO-WM (+proprio) | moderate |
| Push-T | **LeWM (pixels only)** | **+18% vs PLDM, beats DINO-WM** |
| Reacher | DINO-WM | competitive |
| Reacher | **LeWM** | **competitive** |
| Two-Room | PLDM | baseline |
| Two-Room | **LeWM** | **best** |
| OGBench-Cube | DINO-WM | competitive |
| OGBench-Cube | **LeWM** | **competitive** |

</div>

<div class="teal-card text-sm">
<strong>Surprising finding:</strong> LeWM beats DINO-WM on Push-T <em>even without</em> proprioceptive inputs. A tiny from-scratch encoder captures what you need for pixel-only planning.
</div>

</v-click>

</div>
</div>

---

# A Bonus: Surprise Detection

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

<v-clicks>

<div class="card text-sm mb-3">

### Violation-of-Expectation

The LeWM encoder learns a meaningful physical structure as a side effect. If you show it a sequence where a ball <em>passes through</em> a wall, the model reports a much larger prediction error than for a physically consistent sequence.

</div>

<div class="teal-card text-sm mb-3">

### Why it matters

- LeWM can flag <strong>physically implausible events</strong> at inference time — a form of intrinsic "surprise" signal.
- This can be used for <strong>anomaly detection</strong>, exploration bonuses, or pre-action safety checks.
- Statistical significance: $p < 0.01$ for perturbed vs. unperturbed sequences.

</div>

</v-clicks>

</div>
<div>

<v-click>

<div class="accent-card text-sm mb-3">

### Latent probing

The paper shows you can <strong>linearly decode</strong> physical quantities (agent position, block position, velocity) from LeWM's 192-dim embedding — matching what DINO-WM gives you despite being 200× smaller.

<br><br>

<strong>Implication:</strong> End-to-end training doesn't throw away physics. It learns a compressed, task-relevant version of it — using orders of magnitude less compute.

</div>

<div class="blue-card text-sm">
This is the same insight that made Dreamer and TD-MPC2 work: <em>small, fast world models built for the task</em> often beat giant general-purpose ones.
</div>

</v-click>

</div>
</div>

---

# What LeWorldModel Teaches Us

<div class="mt-4">

<v-clicks>

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

</v-clicks>

<v-click>

<div class="accent-card mt-3 text-sm text-center">
<strong>The next question:</strong> What if we could predict actions AND world states <em>together</em> — and leverage unlimited internet video for the world model?
<br>That's exactly what <strong>DreamZero</strong> does.
</div>

</v-click>

</div>

---

<div style="height:1px;"></div>

---
layout: center
---

# Part 2

## DreamZero

<div class="mt-4 opacity-60">Imagine and act simultaneously</div>

---

# The Three Paradigms Revisited

<div class="mt-4">

<div class="grid grid-cols-3 gap-4">

<div class="blue-card text-sm">
<h3>Action-Conditioned</h3>

$x' = f(x, a)$

DINO-WM, IRIS, DIAMOND, LeWorld

**Needs actions** for training → can't use internet video

Covered in main lecture + LeWorld above ✓

</div>

<div class="card text-sm">
<h3>Video-Only</h3>

$x' = f(x)$, then $a = g(x, x')$

DreamGen, 1x WM

**No actions needed** for WM → but two-stage

Mentioned in main lecture Part 1

</div>

<div class="accent-card text-sm">
<h3>Joint (WAM)</h3>

$(x', a) = f(x)$

**DreamZero**, Fast WAM

**Best of both worlds** — one model, two outputs

**Today's focus** ↓

</div>

</div>

<v-click>

<div class="teal-card mt-4 text-sm text-center">
<strong>Chris Paxton (2025):</strong> "Joint models generalize better than alternatives" — and they address the biggest limitation of action-conditioned models: the need for expensive action labels.
</div>

</v-click>

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
- <strong>49.0%</strong> on DROID-Franka (vs 33% for π₀.₅, 31% for GR00T N1.6)
- <strong>7 Hz</strong> real-time closed-loop control
</div>

</div>
<div>

<v-click>

### Why it matters

<div class="blue-card text-sm mb-3">
DreamZero is the <strong>first</strong> robot foundation model that treats world modeling and action generation as <strong>one joint distribution</strong>, initialized from a web-scale video diffusion backbone (Wan2.1-I2V-14B).
</div>

<div class="card text-sm mb-3">
It shows the <strong>WAM paradigm works at scale</strong>: a single model can imagine the future <em>and</em> decide what to do, beating specialized VLAs by 2×+ on generalization.
</div>

<div class="accent-card text-sm">
<strong>This is the architecture the WFM project (main lecture Part 6) is building toward.</strong>
</div>

</v-click>

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

<v-clicks>

<div class="teal-card text-sm mb-3">
<strong>1. Visual context</strong><br>
Recent camera frames → VAE encoder (frozen ❄) → visual latent tokens $z_{ctx}$
</div>

<div class="blue-card text-sm mb-3">
<strong>2. Language</strong><br>
Task instruction ("pick up the red cup") → text encoder (frozen ❄) → text tokens $c$
</div>

<div class="accent-card text-sm mb-3">
<strong>3. Robot state</strong><br>
Proprioception (joint angles, gripper) → small state encoder (trained 🔥) → state tokens $q$
</div>

</v-clicks>

</div>
<div>

<v-click>

### The Shared Backbone

<div class="card text-sm mb-3">
<strong>Wan2.1-I2V-14B-480P</strong> — a 14 billion parameter image-to-video Diffusion Transformer, <strong>initialized from web-scale video pre-training</strong>.<br><br>
All DiT blocks are fine-tuned end-to-end. This is not a frozen backbone with LoRA — the entire 14B moves.
</div>

</v-click>

<v-click>

### Two Output Heads

<div class="teal-card text-sm mb-2">
<strong>Video head</strong> → predicted future frames (noisy video latents denoised)
</div>

<div class="accent-card text-sm">
<strong>Action head</strong> → predicted action chunk $a_1 \ldots a_K$ (denoised jointly with video)
</div>

</v-click>

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

<v-clicks>

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
One model, one set of weights. Actions are <em>conditioned on predicted video</em> → implicit inverse dynamics.
</div>

</v-clicks>

</div>
<div>

<v-click>

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

</v-click>

</div>
</div>

---

# Flow Matching Training

<div class="mt-2">

<div class="card text-sm mb-3">
DreamZero uses <strong>flow matching</strong> — the same continuous-time objective used in Stable Diffusion 3 and Wan2.1. Instead of predicting noise (DDPM), it predicts a <strong>velocity field</strong> that transports noise to data.
</div>

<v-clicks>

<div class="grid grid-cols-2 gap-4 mt-2">
<div class="blue-card text-sm">

### Forward (training)

1. Sample clean video + action latents $(z, a)$
2. Sample timestep $t \sim \text{schedule}$ and noise $\epsilon$
3. Interpolate: $z_t = (1-t)\,z + t\,\epsilon$
4. Target velocity: $v = \epsilon - z$
</div>

<div class="teal-card text-sm">

### The loss

$$\mathcal{L}(\theta) = \mathbb{E}\Big[\tfrac{1}{K}\!\sum_{k=1}^{K} w(t_k)\,\big\|\, u_\theta([z_{t_k}, a_{t_k}]; C_k, c, q_k, t_k) - v^k\,\big\|^2\Big]$$

where $u_\theta$ is the shared DiT, $K$ is the number of chunks, $C_k$ is the KV cache of prior chunks.
</div>
</div>

<div class="accent-card text-sm mt-3">
<strong>Key detail:</strong> video and action latents are concatenated along the token axis and denoised <strong>together</strong> in the same forward pass — not as two separate decoders operating on shared features.
</div>

</v-clicks>

</div>

---

# Autoregressive Chunks + KV Cache

<div class="flex justify-center items-start mt-2" style="padding-top:0.5rem;">
<img src="/figures/dreamzero-chunks.png" class="rounded-lg" style="max-height:70vh; max-width:92%;" />
</div>

---

# Why Chunk-wise?

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

<v-clicks>

<div class="card text-sm mb-3">
<strong>Naïve bidirectional diffusion:</strong> Denoise the full video+action sequence at once. Every generation redoes all the compute. Slow, cannot stream.
</div>

<div class="blue-card text-sm mb-3">
<strong>DreamZero's trick:</strong> Split the sequence into <strong>chunks</strong> of a few frames each. All frames in one chunk share a timestep $t_k$, but different chunks have <strong>independent</strong> timesteps.
</div>

<div class="teal-card text-sm mb-3">
<strong>Why it matters:</strong>

- Past chunks are clean → go in the KV cache
- Current chunk is being denoised
- Future chunks are noise
- One chunk can condition on all earlier clean chunks
</div>

</v-clicks>

</div>
<div>

<v-clicks>

<div class="accent-card text-sm mb-3">
<strong>Teacher forcing during training:</strong> Because timesteps are independent per chunk, the model is forced to handle "past clean, present noisy" contexts naturally. This is what makes autoregressive rollout work.
</div>

<div class="card text-sm mb-3">
<strong>KV cache reuse at inference:</strong> Once a chunk is fully denoised, its keys and values are cached. The next chunk only recomputes its own tokens.<br><br>
<strong>3–4× faster</strong> than bidirectional for long rollouts.
</div>

<div class="teal-card text-sm">
<strong>Variable-length training:</strong> The same architecture handles any sequence length at inference, even though training uses fixed chunk counts.
</div>

</v-clicks>

</div>
</div>

---

# Closed-Loop: Predicted → Real

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

<div class="card text-sm mb-3">
The big risk with video world models is <strong>drift</strong>: small prediction errors compound as you autoregress, and after a few seconds the dream diverges from reality.
</div>

<v-clicks>

<div class="accent-card text-sm mb-3">
<strong>DreamZero's fix — observation replacement:</strong><br><br>
After each action chunk executes on the real robot, the <strong>actually observed</strong> frame replaces the previously <em>predicted</em> frame in the KV cache.
</div>

<div class="blue-card text-sm mb-3">
<strong>Effect:</strong> The world model never has to commit to a long-horizon hallucination. At every step, the past KV cache is grounded in real observations.
</div>

</v-clicks>

</div>
<div>

<v-click>

### The loop

<div class="teal-card text-sm mb-3">

1. Encode recent real frames → $z_{ctx}$
2. Denoise next chunk: predict future video + action
3. Execute the action on the robot
4. Observe the real next frame
5. <strong>Replace</strong> the predicted frame with the real one in the KV cache
6. Go to step 2

</div>

<div class="accent-card text-sm">
This is why the same trained DiT can serve as both a <strong>dreamer</strong> (open-loop imagination for planning) AND a <strong>policy</strong> (closed-loop control grounded in reality).
</div>

</v-click>

</div>
</div>

---

# DreamZero-Flash: 7 Hz Real-Time

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

<div class="card text-sm mb-3">
A 14B DiT doing 50 denoising steps per chunk is <strong>way too slow</strong> for real-time robot control. DreamZero-Flash is the inference-time distillation that makes it work.
</div>

<v-clicks>

<div class="blue-card text-sm mb-3">
<strong>Step 1 — Beta-distribution noise schedule</strong><br>
Instead of uniform $t \sim U(0,1)$, sample from $\text{Beta}(\alpha, \beta)$ skewed toward low noise. Gives better denoisers on the timesteps that matter at inference.
</div>

<div class="teal-card text-sm mb-3">
<strong>Step 2 — Few-step distillation</strong><br>
Progressive distillation: train a student to match the teacher's trajectory in fewer steps. DreamZero-Flash runs in just a handful of denoising iterations per chunk.
</div>

<div class="accent-card text-sm">
<strong>Result:</strong> <strong>38× speedup</strong> over naïve sampling → <strong>7 Hz closed-loop control</strong> on real robots, even with a 14B backbone.
</div>

</v-clicks>

</div>
<div>

<v-click>

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

</v-click>

</div>
</div>

---

# The Training Data

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### AgiBot G1 (main)

<div class="card text-sm mb-3">
<strong>500 hours</strong> of real robot demonstrations on the AgiBot G1 humanoid, collected across <strong>22 environments</strong> and dozens of tasks: cleaning, cooking prep, tool use, tidying, manipulation.
</div>

<div class="blue-card text-sm mb-3">
Paired with language instructions and proprioceptive state. One of the largest manipulation datasets on a humanoid to date.
</div>

### DROID-Franka (cross-lab)

<div class="teal-card text-sm">
The most heterogeneous tabletop benchmark — 564 scenes across 52 buildings, collected by 50+ research labs with different cameras and lighting.
</div>

</div>
<div>

### Cross-embodiment data

<v-clicks>

<div class="accent-card text-sm mb-3">
<strong>YAM bimanual robot</strong> — 20 minutes of "play" data (free interaction with objects, no task demonstrations).
</div>

<div class="card text-sm mb-3">
<strong>Human hand videos</strong> — 12 minutes of a person manipulating similar objects, no robot at all.
</div>

<div class="blue-card text-sm mb-3">
<strong>The test:</strong> Can DreamZero, pre-trained on AgiBot G1, transfer to a totally different embodiment (different arm kinematics, different camera setup) from just a few minutes of unpaired video?
</div>

<div class="teal-card text-sm">
Yes. See the numbers next.
</div>

</v-clicks>

</div>
</div>

---

# The Numbers

<div class="flex justify-center items-start mt-2" style="padding-top:0.5rem;">
<img src="/figures/dreamzero-benchmarks.png" class="rounded-lg" style="max-height:72vh; max-width:92%;" />
</div>

---

# Cross-Embodiment Is the Big One

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

<div class="card text-sm mb-3">
Every VLA paper shows <strong>one robot</strong>, <strong>one lab</strong>, <strong>one set of tasks</strong>. Generalization to a new embodiment usually means "re-collect hundreds of hours of data on the new arm."
</div>

<v-clicks>

<div class="blue-card text-sm mb-3">
<strong>DreamZero's result:</strong> Transfer from AgiBot G1 → YAM bimanual with just <strong>20 minutes of video-only play data</strong> (no demonstrations, no action labels, raw video).
</div>

<div class="accent-card text-sm mb-3">
Task progress on the new arm goes from <strong>38.3% → 55.4%</strong>. A +17 point absolute improvement from 20 minutes of unpaired video.
</div>

<div class="teal-card text-sm">
<strong>Even wilder:</strong> 12 minutes of <em>human hand</em> video (no robot at all) gets you to <strong>54.3%</strong> — almost the same.
</div>

</v-clicks>

</div>
<div>

<v-click>

### Why this works

<div class="card text-sm mb-3">
The world head has learned general visual physics from Wan2.1 pre-training + AgiBot G1 fine-tuning. It doesn't need action labels to understand "how objects move."
</div>

<div class="blue-card text-sm mb-3">
When you show it 20 minutes of a new arm (or a hand) manipulating objects, the video loss updates the world head to "understand this new body." The action head then <em>infers</em> what actions would produce that motion.
</div>

<div class="accent-card text-sm">
<strong>This is the end of per-robot data collection.</strong> Pre-train once → adapt to any embodiment with minutes of unpaired video. The GPT playbook, applied to robotics.
</div>

</v-click>

</div>
</div>

---

# Why DreamZero May Win

<div class="mt-4">

<v-clicks>

<div class="accent-card mb-4">

### The Scaling Argument

<div class="text-sm">

| Data Source | Size | Actions? | Cost |
|---|---|---|---|
| Internet video | Billions of hours | No | Free |
| Robot demonstrations | Thousands of hours | Yes | Expensive |

**The internet has near-infinite video but almost no action labels.**

DreamZero can use ALL that video for world model pre-training, then only needs a small robot dataset for action fine-tuning. **Same strategy that made GPT work** — pre-train on everything, fine-tune on task.
</div>

</div>

<div class="grid grid-cols-2 gap-4">
<div class="teal-card text-sm">
<h3>Zero-Shot Generalization</h3>
"Dream" = imagines futures. "Zero" = generalizes to new tasks without task-specific training. The joint representation captures physics + affordances + action effects.
</div>
<div class="blue-card text-sm">
<h3>No Planning Needed</h3>
Unlike DINO-WM (CEM) and LeWorld (MPC), DreamZero has a <strong>learned policy</strong>. At test time: one forward pass → action. Fast!
</div>
</div>

</v-clicks>

</div>

---

# DreamZero vs. Everything

<div class="mt-2">

| | **DINO-WM** | **IRIS** | **DIAMOND** | **LeWorld** | **DreamZero** |
|---|---|---|---|---|---|
| **Actions for WM?** | Yes | Yes | Yes | Yes | **No** (just video) |
| **Learned policy?** | No (CEM) | Yes (A-C) | Yes (A-C) | No (MPC) | **Yes** (joint head) |
| **Plans at test time?** | Yes (slow) | No (fast) | No (fast) | Yes (slow) | **No** (fast) |
| **Internet video?** | No | No | No | No | **Yes** |
| **Space** | Features | Discrete tokens | Continuous pixels | Global latent | Joint latent |
| **Generalization** | Limited | Moderate | Moderate | Good | **Best** |
| **Data efficiency** | High (frozen DINO) | Moderate | High | High | Highest |
| **Maturity** | Well-studied | Well-studied | Recent | Recent | **Newest** |

<v-click>

<div class="accent-card mt-3 text-sm text-center">
<strong>The trajectory is clear:</strong> From action-conditioned + planning (DINO-WM, LeWorld) → discrete tokens + dream RL (IRIS) → continuous diffusion (DIAMOND) → joint prediction leveraging internet-scale data (DreamZero). Each step addresses the previous one's limitations.
</div>

</v-click>

</div>

---

# The Bigger Picture

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### World Models = The LLM Moment for Robots?

<v-clicks>

<div class="card text-sm mb-3">
<strong>LLMs succeeded because:</strong>
1. Massive pre-training on internet text
2. Small fine-tuning on specific tasks
3. Emergent capabilities from scale
</div>

<div class="accent-card text-sm mb-3">
<strong>World models could follow the same path:</strong>
1. Massive pre-training on internet video
2. Small fine-tuning on robot data
3. Emergent physical reasoning from scale
</div>

<div class="teal-card text-sm">
<strong>This is exactly what NVIDIA Cosmos, Sora, and Genie are betting on.</strong> And it's what the WFM project in the main lecture (Part 6) was building.
</div>

</v-clicks>

</div>
<div>

<v-click>

### Connection to Your WFM Project

<div class="blue-card text-sm">

**What the main lecture built:**
1. **Data pipeline** — 1.44M curated video clips
2. **Video tokenizer** — Cosmos CV8×8×8 (241K latents)
3. **Diffusion WFM** — 1.56B DiT (PoC validated)

This IS the DreamZero Phase 1 approach:
- Pre-train a video world model on massive data
- Add action conditioning later for robot control

**You're already building this.**
</div>

</v-click>

</div>
</div>

---

# Quiz: DreamZero

<div class="quiz-card mt-4">

### Question

What is the key advantage of DreamZero (joint world-action models) over action-conditioned world models like DINO-WM or DIAMOND?

<v-clicks>

**A.** DreamZero uses larger neural networks

**B.** DreamZero can pre-train the world model on internet video without action labels, then fine-tune the action head on small robot data

**C.** DreamZero has better image quality

**D.** DreamZero doesn't need a GPU

</v-clicks>

<v-click>

<div class="mt-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> (B). The critical advantage is data utilization. The internet has billions of hours of video but almost no action labels. DreamZero can leverage ALL that video for world model pre-training. Action-conditioned models (DINO-WM, IRIS, DIAMOND, LeWorld) can only use data that has paired actions — a tiny fraction of available video data.
</div>

</v-click>

</div>

---

<div style="height:1px;"></div>

---
layout: center
---

# Recap: Part 2

---

# What We Covered in Part 2

<div class="mt-4">

<div class="grid grid-cols-2 gap-6">

<div class="accent-card">
<h3>Part 1: LeWorldModel</h3>
<div class="text-sm mt-2">

- The opposite bet to DINO-WM: end-to-end from pixels, no foundation encoder
- **~15M parameters**, 1 GPU, hours of training
- <strong>SIGReg</strong>: a single Gaussian regularizer replaces 6 fragile collapse-prevention tricks
- 48× faster planning than DINO-WM; competitive on Push-T, Reacher, Two-Room, OGBench-Cube
- **Bonus:** built-in surprise detection via violation-of-expectation

</div>
</div>

<div class="teal-card">
<h3>Part 2: DreamZero</h3>
<div class="text-sm mt-2">

- The joint world-action paradigm: $(x', a) = f(x)$
- 14B DiT, initialized from web-scale video pre-training
- Flow matching with autoregressive chunks + KV cache
- **Closed-loop at 7 Hz** via DreamZero-Flash distillation
- 62.2% on seen tasks, **39.5% on unseen** (2.4× best VLA)
- 17-point transfer gain from **20 minutes** of unpaired video on a new embodiment

</div>
</div>

</div>

<v-click>

<div class="accent-card mt-6 text-sm text-center">
<strong>The arc of Part 2:</strong> LeWorld proves small end-to-end models work. DreamZero proves joint pre-training on unlabeled video scales. Together they bracket the design space for world models that actually run on real robots.
</div>

</v-click>

</div>

---

# How Part 1 and Part 2 Connect

<div class="mt-4">

<v-clicks>

<div class="grid grid-cols-5 gap-2">
<div class="teal-card text-sm text-center" style="padding:10px;">
<strong>DINO-WM</strong>
<br><span class="opacity-70">(main lecture)</span>
<br>Frozen encoder
<br>→ heavy, slow planning
</div>
<div class="accent-card text-sm text-center" style="padding:10px;">
<strong>IRIS</strong>
<br><span class="opacity-70">(main lecture)</span>
<br>Discrete tokens
<br>→ lossy quantization
</div>
<div class="blue-card text-sm text-center" style="padding:10px;">
<strong>DIAMOND</strong>
<br><span class="opacity-70">(main lecture)</span>
<br>Continuous diffusion
<br>→ visual details preserved
</div>
<div class="purple-card text-sm text-center" style="padding:10px; border:2px solid var(--claude-purple);">
<strong>LeWorld</strong>
<br><span class="opacity-70">(Part 2)</span>
<br>Tiny end-to-end
<br>→ still action-conditioned
</div>
<div class="card text-sm text-center" style="padding:10px; border:2px solid var(--claude-accent);">
<strong>DreamZero</strong>
<br><span class="opacity-70">(Part 2)</span>
<br>Joint WAM + video
<br>→ the frontier
</div>
</div>

</v-clicks>

<v-click>

<div class="accent-card mt-4 text-sm">
<strong>Each model solved the previous one's limitation:</strong>
- DINO-WM's heavy encoder → LeWorld's end-to-end 15M-param training
- IRIS's discrete tokenization → DIAMOND's continuous pixel diffusion
- Everyone's need for action labels → DreamZero pre-trains on unlabeled video
- Planning latency of MPC/CEM → DreamZero's learned policy head
</div>

</v-click>

</div>

---
layout: center
---

# The End of Per-Robot Data Collection?

<div class="mt-6">
<h2 style="color:var(--claude-accent) !important; font-size:2em !important;">Pre-train once. Adapt to any embodiment from minutes of video.</h2>
</div>

<div class="mt-8">
<span class="opacity-60">That's the promise. Whether it holds at scale is the next chapter of the story.</span>
</div>

<div class="mt-8 flex gap-4 justify-center">
<a href="https://vizuara.ai" target="_blank" class="text-sm px-4 py-2 rounded-lg" style="background:var(--claude-accent);color:#fff;text-decoration:none;">
  vizuara.ai
</a>
</div>
