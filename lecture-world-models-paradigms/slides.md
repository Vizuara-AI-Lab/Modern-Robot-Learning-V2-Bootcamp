---
theme: default
title: "Two Paradigms of World Models — Video-First vs. Joint World-Action"
info: |
  Lecture — Modern Robot Learning from Scratch V2
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
.slidev-layout h1 { font-family: 'Caveat', cursive !important; color: var(--claude-accent) !important; font-size: 2.1em !important; font-weight: 700 !important; line-height: 1.2 !important; }
.slidev-layout h2 { font-family: 'Caveat', cursive !important; color: var(--claude-warm) !important; font-size: 1.5em !important; font-weight: 600 !important; }
.slidev-layout h3 { font-family: 'Caveat', cursive !important; color: var(--claude-teal) !important; font-size: 1.25em !important; font-weight: 600 !important; }
.slidev-layout a { color: var(--claude-blue) !important; }
.slidev-layout code { background: var(--claude-surface) !important; color: var(--claude-text) !important; border: 1px solid var(--claude-border); }
.slidev-layout pre { background: var(--claude-surface) !important; border: 1px solid var(--claude-border); border-left: 3px solid var(--claude-accent); border-radius: 0 8px 8px 0 !important; }
.slidev-layout pre code { color: var(--claude-text) !important; background: transparent !important; border: none !important; }
.slidev-layout blockquote { border-left: 3px solid var(--claude-accent); background: var(--claude-surface); padding: 8px 12px; border-radius: 0 8px 8px 0; }
.slidev-layout table { border-collapse: collapse; width: 100%; }
.slidev-layout th { background: var(--claude-surface); color: var(--claude-accent); padding: 6px 10px; border-bottom: 2px solid var(--claude-accent); font-family: 'Caveat', cursive; font-size: 1.1em; }
.slidev-layout td { padding: 4px 10px; border-bottom: 1px solid var(--claude-border); }
.slidev-layout strong { color: var(--claude-warm); }
.card { background: var(--claude-card); border-radius: 12px; padding: 16px; border: 1px solid var(--claude-border); }
.accent-card { background: rgba(194,120,92,0.06); border-radius: 12px; padding: 16px; border: 1px solid rgba(194,120,92,0.25); }
.teal-card { background: rgba(106,154,91,0.06); border-radius: 12px; padding: 16px; border: 1px solid rgba(106,154,91,0.25); }
.blue-card { background: rgba(90,127,165,0.06); border-radius: 12px; padding: 16px; border: 1px solid rgba(90,127,165,0.25); }
.purple-card { background: rgba(138,107,170,0.06); border-radius: 12px; padding: 16px; border: 1px solid rgba(138,107,170,0.25); }
.warn-card { background: rgba(212,84,58,0.06); border-radius: 12px; padding: 16px; border: 1px solid rgba(212,84,58,0.25); }
.quiz-card { background: rgba(138,107,170,0.06); border-radius: 12px; padding: 16px; border: 2px solid var(--claude-purple); }
.highlight { color: var(--claude-accent); font-weight: 600; }
</style>

# Two Paradigms of World Models

## Video-First vs. Joint World-Action Models

<div class="pt-8">
  <span class="px-4 py-2 rounded-lg text-lg" style="background:#c2785c;color:#fff;font-weight:700;">
    Modern Robot Learning from Scratch — V2
  </span>
</div>

<div class="pt-4 opacity-60">
  Vizuara Lecture — UniPi · SuSIE · HiP · GR-1 · Cosmos · DreamZero + SO-101 build
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

<div style="height:1px;"></div>

---
layout: center
---

# What You'll Learn Today

<div class="grid grid-cols-3 gap-3 mt-6 text-left">

<div class="accent-card">
<strong>Paradigm A — Video → Inverse Dynamics</strong>
<ul class="text-sm mt-2">
<li>UniPi — video as the plan</li>
<li>SuSIE — single goal image</li>
<li>HiP — LLM + video + ID composition</li>
<li>GR-1 / GR-2 — video pretraining is robot pretraining</li>
<li>VPP — video latents as policy features</li>
</ul>
</div>

<div class="teal-card">
<strong>Paradigm B — Joint World-Action Models</strong>
<ul class="text-sm mt-2">
<li>Cosmos — NVIDIA's foundation world model</li>
<li>DreamZero — joint video + action flow matching</li>
<li>The end of per-robot data collection</li>
</ul>
</div>

<div class="blue-card">
<strong>Our own build — DreamZero-SO101</strong>
<ul class="text-sm mt-2">
<li>Patching DreamZero for a new embodiment</li>
<li>715 episodes from HuggingFace → GEAR format</li>
<li>LoRA fine-tune on 4×H100</li>
<li>The bugs we hit and how we fixed them</li>
</ul>
</div>

</div>

---
layout: center
---

# Where We've Been

<div class="grid grid-cols-2 gap-4">

<div class="blue-card">
<strong>Classical Model-Based RL (covered previously)</strong>
<ul class="text-sm mt-2">
<li><strong>Dreamer V1/V2/V3</strong> — RSSM world model + actor/critic, RL in imagination</li>
<li><strong>DINO-WM</strong> — latent world model in DINO-v2 space, planning via MPC</li>
<li><strong>IRIS</strong> — transformer world model for sample-efficient RL</li>
<li><strong>DIAMOND</strong> — diffusion world model, RL in imagination</li>
</ul>
</div>

<div class="accent-card">
<strong>Common pattern in all four</strong>
<ul class="text-sm mt-2">
<li>Two <em>separate</em> networks: world model + policy</li>
<li>World model predicts observations (in latent or pixel space)</li>
<li>Policy is a distinct MLP trained via RL or MPC</li>
<li>They are <em>coupled</em> but never <em>fused</em></li>
</ul>
</div>

</div>

<div class="pt-6 text-center" style="font-family:'Caveat',cursive;font-size:1.5em;color:var(--claude-accent)">
Today: two <em>other</em> families that collapse this separation — each in a different way.
</div>

---
layout: center
---

# The Three Categories

<div class="flex justify-center">
  <img src="/figures/three-categories-taxonomy.png" class="max-h-80 rounded-lg" />
</div>

<div class="grid grid-cols-3 gap-3 text-xs mt-4">
<div class="accent-card">
<strong>Paradigm A</strong><br/>
Video → Inverse Dynamics<br/>
<em>Two separate models — pixels then actions</em>
</div>
<div class="blue-card">
<strong>Model-Based RL</strong><br/>
World model + separate RL policy<br/>
<em>Covered earlier: Dreamer, DINO-WM, IRIS, DIAMOND</em>
</div>
<div class="teal-card">
<strong>Paradigm B</strong><br/>
Joint world-action models<br/>
<em>One network predicts obs AND actions</em>
</div>
</div>

---
layout: center
---

# Paradigm A at a glance

<div class="flex justify-center">
  <img src="/figures/paradigm-a-pipeline.png" class="max-h-80 rounded-lg" />
</div>

<div class="mt-4 text-center" style="font-family:'Caveat',cursive;font-size:1.5em;color:var(--claude-warm)">
Dream the video. Then read off the actions.
</div>

<div class="accent-card mt-4">
<strong>Two-stage pipeline:</strong>
<ol class="text-sm mt-2">
<li><strong>Visual planner</strong> (video/image diffusion): <code>text + current image → imagined future frames</code></li>
<li><strong>Inverse dynamics</strong> (small MLP): <code>(o_t, o_{t+1}) → action a_t</code></li>
</ol>
</div>

---
layout: center
---

# Why Would You Ever Do This?

<div class="grid grid-cols-2 gap-4">

<div class="teal-card">
<strong>Three concrete wins</strong>
<ol class="text-sm mt-2">
<li><strong>Internet-scale pretraining works</strong> — the video model can be pretrained on YouTube/Ego4D with no actions. Action-free video is trillions of tokens.</li>
<li><strong>Combinatorial generalization</strong> — pixel-level composition of objects + verbs generalizes to unseen combinations.</li>
<li><strong>Long-horizon planning is tractable</strong> — predicting 16 frames with diffusion beats autoregressing 200 action tokens.</li>
</ol>
</div>

<div class="warn-card">
<strong>What you give up</strong>
<ul class="text-sm mt-2">
<li>Two models to train and keep consistent</li>
<li>Inverse dynamics failure ⇒ broken control</li>
<li>Pixel hallucinations (floating objects, wrong physics) corrupt the plan</li>
<li>Video generation is slow at inference</li>
</ul>
</div>

</div>

<div class="pt-4 text-sm text-center opacity-70">
Paradigm A is a bet that <strong>intelligence lives in the pixel prior</strong>, and action decoding is a shallow readout.
</div>

---

# UniPi — "Learning Universal Policies via Text-Conditioned Video Generation"

<div class="grid grid-cols-[3fr_2fr] gap-4">

<div>

<div class="accent-card">
<strong>Du, Yang, Florence, Xia, Wahid, Chen, Abbeel, Mordatch — NeurIPS 2023 (Google / MIT)</strong>
</div>

<div class="mt-3 p-3" style="background:var(--claude-surface);border-radius:8px">
<strong>The whole paper in one idea:</strong><br/>
<em style="color:var(--claude-accent)">What if the policy is a video generator, and the "plan" is a synthesized video of the robot completing the task?</em>
</div>

<div class="pt-3 text-sm">

**Old view of a policy:**
$$\pi(a_t \mid s_t) : \text{state} \to \text{action}$$

**UniPi's view:**
$$p(\tau \mid o_0, x) : \text{(image, text)} \to \text{video trajectory}$$
Then extract actions post-hoc via inverse dynamics.

</div>
</div>

<div class="flex items-center justify-center">
  <img src="/figures/unipi-overview.png" class="max-h-80 rounded-lg" />
</div>

</div>

---

# UniPi — The Two-Stage Architecture

<div class="grid grid-cols-2 gap-4">

<div class="accent-card">
<strong>Stage 1 — The Dreamer</strong><br/>
<code>text + first frame → 16-frame video</code>
<ul class="text-sm mt-2">
<li>3D U-Net video diffusion (space + time)</li>
<li>Text conditioning via T5 + cross-attention</li>
<li>First frame concatenated channel-wise as "image conditioning"</li>
<li>Resolution: 24×40, horizon: 16 frames</li>
</ul>
</div>

<div class="teal-card">
<strong>Stage 2 — The Interpreter</strong><br/>
<code>(o_t, o_{t+1}) → a_t</code>
<ul class="text-sm mt-2">
<li>Small MLP — a few million params</li>
<li>Pure supervised learning on robot demos</li>
<li>Trained independently of video model</li>
<li>Deliberately tiny — capacity bet lives in the video model</li>
</ul>
</div>

</div>

<div class="mt-4 text-center" style="font-family:'Caveat',cursive;font-size:1.3em;color:var(--claude-warm)">
The video IS the plan. Actions are a cheap post-hoc readout.
</div>

<div class="flex justify-center mt-2">
  <img src="/figures/unipi-architecture.png" class="max-h-48 rounded-lg" />
</div>


---

<div style="height:1px;"></div>

---

# UniPi — Hierarchical Temporal Super-Resolution

<div class="grid grid-cols-[3fr_2fr] gap-4">

<div>

A single 16-frame clip is too short for long-horizon tasks. UniPi stacks <strong>coarse-to-fine video diffusion</strong>:

<div class="accent-card mt-2 text-sm">
<ol>
<li>Generate a <strong>coarse</strong> 16-frame plan sparsely sampled across the full task (1 frame / 2 sec).</li>
<li>Second diffusion model does <strong>temporal super-resolution</strong> — fills 4 intermediate frames between each adjacent pair.</li>
<li>Repeat once more → dense video.</li>
</ol>
</div>

<div class="teal-card mt-3 text-sm">
<strong>The deep analogy:</strong> this is exactly hierarchical planning — pick coarse waypoints, then refine — but now the hierarchy is <em>emergent in pixel space</em> rather than hand-designed.
</div>

</div>

<div class="flex items-center justify-center">
  <img src="/figures/unipi-hierarchical.png" class="max-h-80 rounded-lg" />
</div>

</div>

---

# UniPi — The Combinatorial Result

<div class="grid grid-cols-2 gap-4">

<div>

<div class="accent-card text-sm">
<strong>The setup</strong><br/>
Tasks of the form:
<code>place [color] [shape] on [color] [shape]</code><br/>
8 colors × 5 shapes = 40 atoms.<br/>
Train on a subset. Test on <strong>held-out combinations</strong>.
</div>

<div class="mt-3 grid grid-cols-2 gap-2 text-sm">
<div class="warn-card">
<strong>Transformer BC baseline</strong><br/>
~20% held-out combos
</div>
<div class="teal-card">
<strong>UniPi</strong><br/>
~80% held-out combos
</div>
</div>

<div class="mt-3 text-xs">
Why? The video generator sees <em>objects and verbs as compositional pixel primitives</em>. "Blue triangle on green cube" is just a novel pixel rearrangement. A policy bakes the task directly into action space and can't recombine.
</div>

</div>

<div class="flex items-center justify-center">
  <img src="/figures/unipi-combinatorial.png" class="max-h-80 rounded-lg" />
</div>

</div>

<div class="mt-3 text-center" style="font-family:'Caveat',cursive;font-size:1.4em;color:var(--claude-accent)">
Empirical signature that pixel-space planning is fundamentally different from action-space learning.
</div>

---

# UniPi — The Lasting Reframe

<div class="purple-card">
<strong>UniPi's deeper claim:</strong><br/>
Every control problem becomes <em>conditional video synthesis</em>.
</div>

<div class="grid grid-cols-2 gap-3 mt-4 text-sm">
<div class="card">Condition on <strong>language</strong> → task-conditioned policy</div>
<div class="card">Condition on <strong>first frame</strong> → goal-reaching</div>
<div class="card">Condition on <strong>first + last frame</strong> → goal-conditioned manipulation</div>
<div class="card">Condition on <strong>reward</strong> → reward-shaped behavior</div>
</div>

<div class="mt-4 accent-card">
<strong>This reframing is what unlocks the next wave of papers:</strong><br/>
SuSIE, UniSim, HiP, RoboDreamer, GR-1/GR-2. They all take the "video-as-plan" skeleton and push on a different axis.
</div>

---

# SuSIE — "Don't Dream the Video. Dream the Goal."

<div class="grid grid-cols-[3fr_2fr] gap-4">

<div>

<div class="accent-card">
<strong>Black, Nakamoto, Atreya, Walke, Finn, Kumar, Levine — ICLR 2024 (Berkeley)</strong><br/>
<em>"Zero-Shot Robotic Manipulation with Pretrained Image-Editing Diffusion Models"</em>
</div>

<div class="mt-3 warn-card text-sm">
<strong>The rebellion against UniPi:</strong><br/>
Generating 16 coherent future frames is expensive and error-prone. Middle frames drift. Physics gets weird. <em>You're paying huge compute for information the policy doesn't need.</em>
</div>

<div class="mt-3 teal-card text-sm">
<strong>SuSIE's fix in one line:</strong><br/>
Generate <em>just one future image</em> — a subgoal ~2 seconds ahead — via an <strong>image-editing diffusion model</strong>. A small goal-conditioned policy closes the gap.
</div>

</div>

<div class="flex items-center justify-center">
  <img src="/figures/susie-overview.png" class="max-h-80 rounded-lg" />
</div>

</div>

---

# SuSIE — The InstructPix2Pix Trick

<div class="grid grid-cols-2 gap-4">

<div>

<div class="purple-card text-sm">
<strong>The lead innovation isn't the hierarchy — it's reusing an internet-scale pretrained image editor as the subgoal generator.</strong>
</div>

<div class="mt-3 text-sm">

**InstructPix2Pix** (Brooks et al., 2023) was trained on millions of
  `(image, text-edit-instruction, edited-image)`
triplets scraped from the internet:
- *"make it winter"*
- *"add a dog"*
- *"move the cup left"*

It already knows how images change in response to language.

</div>

<div class="mt-3 accent-card text-sm">
SuSIE fine-tunes it on robot data where the edit is <em>"the scene 2 seconds later, given this task."</em>
<br/>The image prior transfers from Photoshop edits into manipulation.
</div>

</div>

<div class="flex items-center justify-center">
  <img src="/figures/susie-instructpix2pix.png" class="max-h-80 rounded-lg" />
</div>

</div>

---

# SuSIE — Low-Level Policy (NOT MPC)

<div class="grid grid-cols-2 gap-4">

<div class="teal-card">
<strong>What the low-level policy does</strong>
<ul class="text-sm mt-2">
<li>Inputs: current image + subgoal image (+ proprio)</li>
<li>Output: <strong>action chunk</strong> of ~4 steps</li>
<li>Architecture: diffusion policy (Chi et al. 2023)</li>
<li>Training: goal-conditioned behavior cloning</li>
<li>Inference: one forward denoise per chunk, then replan</li>
</ul>
</div>

<div class="warn-card">
<strong>NOT MPC (contrast with DINO-WM)</strong>
<ul class="text-sm mt-2">
<li>No world model at inference time</li>
<li>No candidate action rollouts</li>
<li>No CEM / MPPI optimization</li>
<li>Pure amortized feedforward — "planning" distilled into weights</li>
<li>Upper level (subgoal regen every 2s) is MPC-<em>ish</em> replanning, but no search</li>
</ul>
</div>

</div>

<div class="mt-3 accent-card text-sm text-center">
<strong>DINO-WM</strong> = chess engine (search at play time) · <strong>SuSIE</strong> = grandmaster's intuition (trained once, reflexive)
</div>


---

<div style="height:1px;"></div>

---

# SuSIE — Bridge V2 Results & Failure Modes

<div class="grid grid-cols-2 gap-4">

<div class="teal-card text-sm">
<strong>Generalization wins</strong>
<ul class="mt-2">
<li><strong>Novel objects</strong> — "sushi", "orange towel" zero-shot</li>
<li><strong>Novel scenes</strong> — lighting, backgrounds from internet</li>
<li><strong>Novel skills</strong> — composable edits never seen in robot data</li>
<li>Beats RT-2-X (55B params) on held-out scenes</li>
</ul>
</div>

<div class="warn-card text-sm">
<strong>Known failure modes</strong>
<ul class="mt-2">
<li><strong>Physically implausible subgoals</strong> — InstructPix2Pix doesn't know gravity. Floating blocks happen.</li>
<li><strong>Capped by low-level horizon</strong> — if policy can't close 2 seconds, the whole hierarchy collapses.</li>
<li><strong>No temporal coherence</strong> — each subgoal is a static image; no sense of velocity or intermediate dynamics.</li>
</ul>
</div>

</div>

<div class="mt-4 purple-card">
<strong>The meta-lesson of UniPi → SuSIE:</strong><br/>
Both outsource semantics to a pretrained internet-data model. They only disagree on <em>what form that pretrained model takes</em>: full video vs. single keyframe. This axis keeps shifting as the field progresses.
</div>

---

# HiP — Compositional Foundation Models

<div class="grid grid-cols-[3fr_2fr] gap-4">

<div>

<div class="accent-card">
<strong>Ajay, Han, Du, Li, Gupta, Jaakkola, Tenenbaum, Kaelbling, Srivastava, Agrawal — NeurIPS 2023 (MIT)</strong><br/>
<em>"Compositional Foundation Models for Hierarchical Planning"</em>
</div>

<div class="mt-3 text-sm">

**The reframe:** long-horizon tasks need <strong>three kinds of reasoning</strong> — language-level planning, visual planning, motor control.

> Use a <em>different</em> foundation model for each, and compose them at test time.

</div>

<div class="mt-3 teal-card text-sm">
Three levels, each a pretrained foundation model:
<ol class="mt-1">
<li><strong>LLM</strong> — proposes language subgoals</li>
<li><strong>Video diffusion</strong> — renders each subgoal</li>
<li><strong>Inverse dynamics</strong> — extracts actions</li>
</ol>
</div>

</div>

<div class="flex items-center justify-center">
  <img src="/figures/hip-three-levels.png" class="max-h-80 rounded-lg" />
</div>

</div>

---

# HiP — Iterative Refinement Across Levels

<div class="grid grid-cols-2 gap-4">

<div>

<div class="warn-card text-sm">
<strong>Open-loop composition fails:</strong>
<ul class="mt-2">
<li>LLM proposes subgoals the scene can't support</li>
<li>Video model dreams unreachable motions</li>
<li>Errors compound across levels</li>
</ul>
</div>

<div class="mt-3 teal-card text-sm">
<strong>HiP's fix — iterative consistency:</strong>
<ol class="mt-2">
<li>LLM proposes subgoal in language</li>
<li>Video model dreams a video of it</li>
<li>VLM scores video against LLM subgoal</li>
<li>Action-conditioned dynamics model scores physical feasibility</li>
<li>If low score → resample, repeat until all three agree</li>
</ol>
</div>

<div class="mt-3 purple-card text-xs">
<strong>Ablation:</strong> removing consistency scoring drops success by <strong>20–30%</strong>. Refinement is the decisive ingredient.
</div>

</div>

<div class="flex items-center justify-center">
  <img src="/figures/hip-iterative-refinement.png" class="max-h-80 rounded-lg" />
</div>

</div>

---

# HiP — Why This Is MPC-Flavored

<div class="grid grid-cols-2 gap-4">

<div class="accent-card text-sm">
<strong>HiP vs. classical MPC</strong>
<ul class="mt-2">
<li><strong>MPC:</strong> roll candidate action sequences through a world model, score by cost, pick best</li>
<li><strong>HiP:</strong> roll candidate <em>plans</em> (LLM prompts + video samples) through three models, score by <em>consistency</em>, pick best</li>
<li>Both are test-time optimization over plans</li>
<li>Search space is language + pixel space, not action sequences</li>
</ul>
</div>

<div class="teal-card text-sm">
<strong>The three priors being composed</strong>
<ul class="mt-2">
<li><strong>LLM</strong> → commonsense task decomposition (internet text)</li>
<li><strong>Video diffusion</strong> → physical dynamics + visual semantics (internet video)</li>
<li><strong>VLM (CLIP)</strong> → language-vision alignment (image-text pairs)</li>
<li><strong>Robot data</strong> → tiny inverse dynamics head only</li>
</ul>
</div>

</div>

<div class="mt-4 text-center" style="font-family:'Caveat',cursive;font-size:1.4em;color:var(--claude-accent)">
Maximalist Paradigm-A: almost zero robot data, almost all internet priors, composed at test time.
</div>

---

# GR-1 — "Video Pretraining IS Robot Pretraining"

<div class="grid grid-cols-[3fr_2fr] gap-4">

<div>

<div class="accent-card">
<strong>Wu, Jiang, Yu, Chen, Gao, Yang, Zhang — ICLR 2024 (ByteDance)</strong><br/>
<em>"Unleashing Large-Scale Video Generative Pre-training for Visual Robot Manipulation"</em>
</div>

<div class="mt-3 warn-card text-sm">
<strong>The bet:</strong><br/>
Stop using <em>two</em> networks. One causal transformer. Pretrained on internet video (predict next frame). Fine-tuned on robot data (predict next frame + next action).
</div>

<div class="mt-3 text-sm">

The **GPT playbook** applied to embodied learning:
- GPT: pretrain on internet text → predict next token
- GR-1: pretrain on internet video → predict next frame
- Fine-tune with an action head for downstream control

</div>

</div>

<div class="flex items-center justify-center">
  <img src="/figures/gr1-architecture.png" class="max-h-80 rounded-lg" />
</div>

</div>

---

# GR-1 — Architecture & Two Heads

<div class="grid grid-cols-2 gap-4">

<div class="teal-card text-sm">
<strong>Single causal transformer</strong><br/>
Input token stream:

```
[lang, o_1, s_1, a_1, o_2, s_2, a_2, ...]
```

- `lang` — CLIP text embedding of instruction (once)
- `o_t` — MAE-pretrained ViT patch tokens (~196/frame)
- `s_t` — proprioceptive state
- `a_t` — action

</div>

<div class="purple-card text-sm">
<strong>Two prediction heads, shared backbone:</strong>
<ul class="mt-2">
<li><strong>Pixel head</strong> — predicts next image (video prediction loss)</li>
<li><strong>Action head</strong> — predicts next action</li>
</ul>

$$\mathcal{L} = \mathcal{L}_{\text{pixel}} + \lambda \cdot \mathcal{L}_{\text{action}}$$

<div class="mt-2 text-xs">
Video prediction is an <strong>auxiliary loss</strong> that regularizes the representation AND lets pretraining use action-free data.
</div>
</div>

</div>

<div class="mt-3 accent-card text-xs">
<strong>vs UniPi:</strong> same model generates both frames and actions. vs Dreamer: single network, joint loss. vs DreamZero (coming up): two heads instead of one joint denoiser — the paradigm divider.
</div>

---

# GR-1 — The Two-Stage Training Recipe

<div class="grid grid-cols-2 gap-4">

<div class="accent-card text-sm">
<strong>Stage 1 — Video Pretraining on Ego4D</strong>
<ul class="mt-2">
<li>~800K egocentric human video clips</li>
<li>Only the pixel loss is active</li>
<li>No action labels exist</li>
<li>Learns how hands move, how objects respond, how pouring looks</li>
</ul>
</div>

<div class="teal-card text-sm">
<strong>Stage 2 — Joint Fine-Tuning on Robot Data</strong>
<ul class="mt-2">
<li>CALVIN, RT-1 datasets</li>
<li>Both pixel and action loss active</li>
<li>Action head trained from scratch here</li>
<li>Video head continues to refine on robot domain</li>
</ul>
</div>

</div>

<div class="flex justify-center mt-4">
  <img src="/figures/gr1-two-stage.png" class="max-h-60 rounded-lg" />
</div>

---

# GR-1 — The CALVIN Result

<div class="grid grid-cols-2 gap-4">

<div>

<div class="accent-card text-sm">
<strong>CALVIN benchmark</strong><br/>
Execute <strong>chains of 5 subtasks</strong> in sequence:
<em>"open drawer, then push red block left, then turn on light, then..."</em><br/>
Success = all 5 correct.
</div>

<div class="mt-3 warn-card text-sm">
<strong>Best prior (HULC):</strong> ~47% chain success
</div>

<div class="mt-2 teal-card text-sm">
<strong>GR-1:</strong> ~94% chain success
</div>

<div class="mt-3 purple-card text-sm">
<strong>Ablation reveals:</strong> <strong>60-70% of the gain comes from Ego4D pretraining</strong>, not the architecture. Remove the pretrain, GR-1 sits at baseline.
</div>

<div class="mt-3 text-xs opacity-70">
The prior is where the intelligence lives.
</div>

</div>

<div class="flex items-center justify-center">
  <img src="/figures/gr1-calvin-results.png" class="max-h-80 rounded-lg" />
</div>

</div>

---

# GR-2 — Scale Up

<div class="grid grid-cols-2 gap-4">

<div class="accent-card text-sm">
<strong>Cheang et al., 2024 (ByteDance)</strong><br/>
<em>"A Generative Video-Language-Action Model with Web-Scale Knowledge"</em>
</div>

<div class="teal-card text-sm">
<strong>Key changes from GR-1</strong>
<ul class="mt-2">
<li><strong>38M video clips</strong> (Ego4D + Something-Something + HowTo100M + internal)</li>
<li><strong>VQ-VAE video tokens</strong> — discrete, stable scaling</li>
<li><strong>Action chunks</strong> of 10-20 (ACT-style)</li>
<li><strong>Trajectory-level post-training</strong> — self-correction loop</li>
<li>Deployed on bi-manual dual-arm platform, 100+ tasks</li>
</ul>
</div>

</div>

<div class="mt-4 purple-card">
<strong>The killer result:</strong> success rate <strong>barely drops</strong> from "objects seen in both Ego4D + robot data" to "objects seen only in Ego4D."<br/>
<em>Strongest evidence to date that internet video pretraining transfers to physical manipulation.</em>
</div>

---

# VPP — Video Prediction Policy

<div class="grid grid-cols-[3fr_2fr] gap-4">

<div>

<div class="accent-card">
<strong>Hu et al., ICML 2025 (Tsinghua)</strong><br/>
<em>"Video Prediction Policy: A Generalist Robot Policy with Predictive Visual Representations"</em>
</div>

<div class="mt-3 purple-card text-sm">
<strong>The claim:</strong> don't generate the video to completion. Use its <em>intermediate features</em> as representations for a diffusion action policy.
</div>

<div class="mt-3 text-sm">

**Pipeline:**
1. Pretrained Stable Video Diffusion / similar.
2. One forward pass conditioned on (current image, language) — stop at intermediate denoising step.
3. Extract internal features = compressed "imagined future."
4. Feed to a downstream diffusion action policy.

</div>

<div class="mt-3 teal-card text-sm">
<strong>Why this matters:</strong> internet-scale prior without paying full video generation cost at inference. The <em>latent</em> of imagination is enough.
</div>

</div>

<div class="flex items-center justify-center">
  <img src="/figures/vpp-features.png" class="max-h-80 rounded-lg" />
</div>

</div>

---
layout: center
---

# Paradigm A — The Full Arc

<div class="grid grid-cols-5 gap-2 text-xs">

<div class="card">
<strong>UniPi (2023)</strong><br/>
Two models: video diffusion + inverse dynamics. Video is the plan.
</div>

<div class="card">
<strong>SuSIE (2024)</strong><br/>
One goal image (from InstructPix2Pix) + goal-conditioned policy.
</div>

<div class="card">
<strong>HiP (2023)</strong><br/>
LLM + video + ID composed via test-time iterative refinement.
</div>

<div class="card">
<strong>GR-1/2 (2024)</strong><br/>
Single transformer, video pretrain + action fine-tune.
</div>

<div class="card">
<strong>VPP (2025)</strong><br/>
Video diffusion latents as conditioning for action policy.
</div>

</div>

<div class="mt-6 purple-card">
<strong>The trajectory:</strong> from "two separate models" (UniPi) → "compose three specialists at test time" (HiP) → "single model, two heads" (GR-1) → "use the latent, not the pixels" (VPP).<br/>
<em>Paradigm A is progressively erasing the boundary between video generation and action generation.</em>
</div>

<div class="mt-3 text-center" style="font-family:'Caveat',cursive;font-size:1.5em;color:var(--claude-accent)">
The next step is to erase it entirely. That's Paradigm B.
</div>

---
layout: center
---

# The Three Categories — Clarified

<table class="text-sm">
<thead>
<tr><th>Category</th><th>What "joint" means</th><th>Examples</th></tr>
</thead>
<tbody>
<tr>
<td><strong>Paradigm A</strong><br/>Video → Inverse Dynamics</td>
<td>Two separate models: generate pixels, decode actions post-hoc</td>
<td>UniPi, SuSIE, HiP, GR-1, VPP</td>
</tr>
<tr>
<td><strong>Model-Based RL</strong></td>
<td>Two separate networks (world model + policy MLP), trained in coupled loop, policy uses imagined rollouts</td>
<td>Dreamer V1-V3, DINO-WM, IRIS, DIAMOND</td>
</tr>
<tr>
<td><strong>Paradigm B</strong><br/>Joint World-Action Models</td>
<td><strong>One</strong> network predicts next observation AND next action in the same forward pass — shared weights, shared representation</td>
<td><strong>Cosmos, DreamZero</strong> (our focus today)</td>
</tr>
</tbody>
</table>

<div class="mt-6 accent-card">
<strong>Strict definition of Paradigm B:</strong> one neural network, jointly-denoised (observation, action) pairs — <em>not</em> two networks coupled through training.
</div>

---
layout: center
---

# Paradigm B — The Core Shift

<div class="grid grid-cols-2 gap-4">

<div class="warn-card">
<strong>Paradigm A DNA</strong><br/>
Semantics lives in a big pretrained video model. Action decoding is a cheap add-on.
<ul class="text-sm mt-2">
<li>Plan in pixels, act via readout</li>
<li>Two models, two stages</li>
<li>Bet on internet-video priors</li>
</ul>
</div>

<div class="teal-card">
<strong>Paradigm B DNA</strong><br/>
Observation and action live in the same generative distribution. One model, jointly denoised.
<ul class="text-sm mt-2">
<li>Plan and act in the same breath</li>
<li>One model, one representation</li>
<li>Bet on joint generative modeling</li>
</ul>
</div>

</div>

<div class="mt-6 purple-card">
<strong>The reframe:</strong> control becomes <em>conditional trajectory synthesis</em>. Every query — simulate, act, counterfactual — is a different conditioning mask on
$$p(o_{1:T}, a_{1:T} \mid \text{context})$$
</div>

---

# Cosmos — NVIDIA's Foundation World Model

<div class="grid grid-cols-[3fr_2fr] gap-4">

<div>

<div class="accent-card">
<strong>NVIDIA, 2024–2025</strong><br/>
<em>"Cosmos World Foundation Model Platform for Physical AI"</em>
</div>

<div class="mt-3 text-sm">

The **video foundation model** that underpins modern joint world-action robotics. Shipped as:

- **Cosmos Predict** — autoregressive next-frame prediction
- **Cosmos Diffusion** — action/text-conditioned video diffusion
- **Cosmos Tokenizer** — CV8×8×8 / DV8×16×16 (the compressor everything uses)

</div>

<div class="mt-3 teal-card text-sm">
<strong>The training corpus:</strong> <strong>20M+ hours of video</strong>, filtered for physical-world content (manipulation, driving, navigation, human activity, simulations).
</div>

<div class="mt-3 purple-card text-sm">
<strong>Role in the ecosystem:</strong> Cosmos is the <em>backbone</em>. DreamZero, GR00T Dreams, and a dozen other robotics models are Cosmos derivatives — fine-tuned for action conditioning.
</div>

</div>

<div class="flex items-center justify-center">
  <img src="/figures/cosmos-overview.png" class="max-h-80 rounded-lg" />
</div>

</div>

---

# Cosmos — The Tokenizer Is the Workhorse

<div class="grid grid-cols-2 gap-4">

<div class="blue-card text-sm">
<strong>Cosmos-Tokenizer CV8×8×8</strong>
<ul class="mt-2">
<li>8× compression in time, 8× in H, 8× in W</li>
<li>Continuous latents (VAE, not VQ)</li>
<li>25 frames at 256×256 → <strong>latent shape [1, 16, 4, 32, 32]</strong></li>
<li>Each latent file ~132 KB (vs ~30 MB raw video)</li>
<li><strong>408 MB model, freely downloadable</strong> (non-gated)</li>
</ul>
</div>

<div class="teal-card text-sm">
<strong>Why everyone uses it</strong>
<ul class="mt-2">
<li>On robot data: <strong>OXE 40.77 dB PSNR</strong>, Bridge V2 34.38 dB</li>
<li>Far exceeds the 30 dB threshold for downstream training</li>
<li>Pre-tokenize once → train diffusion world models on compressed latents</li>
<li>Cuts WFM training cost by ~100×</li>
</ul>

<div class="mt-2 text-xs opacity-70">
Our WFM Phase 2 pipeline uses this: 241K pre-tokenized latents on B2.
</div>
</div>

</div>

<div class="mt-4 accent-card">
<strong>The practical point:</strong> you can't afford to train a world model on raw pixels at 256×256 × 25 frames (~5M values per sample). Cosmos Tokenizer makes the Paradigm-B dream tractable.
</div>

---

# Cosmos — What Comes Out of the Box

<div class="grid grid-cols-3 gap-3">

<div class="accent-card text-sm">
<strong>Cosmos Predict1 / Predict2</strong><br/>
Autoregressive video prediction.
<ul class="mt-2 text-xs">
<li>Next-frame token prediction</li>
<li>GAIA-1-style interactive use</li>
<li>Conditioning: text, image, action</li>
</ul>
</div>

<div class="teal-card text-sm">
<strong>Cosmos Transfer1</strong><br/>
Video-to-video transfer.
<ul class="mt-2 text-xs">
<li>Sim-to-real: render → realistic video</li>
<li>Style transfer for data augmentation</li>
<li>Used by GR00T for synthetic robot data</li>
</ul>
</div>

<div class="blue-card text-sm">
<strong>Cosmos Reason1</strong><br/>
Video + language reasoning.
<ul class="mt-2 text-xs">
<li>VLM trained on physical video</li>
<li>Scene understanding for planning</li>
<li>Complements world model in agentic loops</li>
</ul>
</div>

</div>

<div class="mt-4 purple-card text-sm">
<strong>The platform thesis:</strong> NVIDIA bets that <em>physical AI</em> needs its own foundation stack — separate from LLMs and image models. Cosmos is that stack.<br/>
DreamZero is how it turns into a <strong>joint world-action model</strong>.
</div>

---

# Meet DreamZero

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

<div class="card text-sm mb-3">
<strong>Paper:</strong> "DreamZero: A Generalist Joint World-Action Model"<br/>
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

<div class="blue-card text-sm mb-3">
<strong>Why it matters:</strong><br/>
DreamZero is the <strong>first</strong> robot foundation model that treats world modeling and action generation as <strong>one joint distribution</strong>, initialized from a web-scale video diffusion backbone (Wan2.1-I2V-14B).
</div>

<div class="card text-sm mb-3">
It shows the Paradigm B bet <strong>works at scale</strong>: a single model imagines the future <em>and</em> decides what to do, beating specialized VLAs by 2×+ on generalization.
</div>

<div class="accent-card text-sm">
<strong>This is the architecture our SO-101 fine-tune is built on.</strong>
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

**1. Visual context**

Recent camera frames → VAE encoder (frozen ❄) → visual latent tokens $z_{ctx}$

</div>

<div class="blue-card text-sm mb-3">

**2. Language**

Task instruction ("pick up the red cup") → text encoder (frozen ❄) → text tokens $c$

</div>

<div class="accent-card text-sm mb-3">

**3. Robot state**

Proprioception (joint angles, gripper) → small state encoder (trained 🔥) → state tokens $q$

</div>

</div>
<div>

### The Shared Backbone

<div class="card text-sm mb-3">
<strong>Wan2.1-I2V-14B-480P</strong> — a 14 billion parameter image-to-video Diffusion Transformer, <strong>initialized from web-scale video pre-training</strong>.<br/><br/>
All DiT blocks are fine-tuned end-to-end. Not a frozen backbone with LoRA — the entire 14B moves.
</div>

### Two Output Heads

<div class="teal-card text-sm mb-2">

**Video head** → predicted future frames (noisy video latents denoised)

</div>

<div class="accent-card text-sm">

**Action head** → predicted action chunk $a_1 \ldots a_K$ (denoised *jointly* with video)

</div>

</div>
</div>


---

<div style="height:1px;"></div>

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

**Direct VLA:** $\pi(a \mid o, \ell)$

Learns *what* to do, but nothing about *how the world evolves*. No physics understanding baked in.

</div>

<div class="card text-sm mb-3">

**Video WM + Inverse dynamics (Paradigm A):**

$x' = f(x), \quad a = g(x, x')$

Two stages. The inverse dynamics model is lossy. Errors compound.

</div>

<div class="accent-card text-sm mb-3">

**DreamZero (joint):**

$$\pi(\text{vid}, \text{act} \mid o, \ell, q) = \pi(\text{vid} \mid o, \ell, q) \cdot \pi(\text{act} \mid \text{vid}, q)$$

One model, one set of weights. Actions are *conditioned on predicted video* → implicit inverse dynamics.

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

# Flow Matching Training

<div class="mt-2">

<div class="card text-sm mb-3">
DreamZero uses <strong>flow matching</strong> — the same continuous-time objective used in Stable Diffusion 3 and Wan2.1. Instead of predicting noise (DDPM), it predicts a <strong>velocity field</strong> that transports noise to data.
</div>

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

<div class="card text-sm mb-3">
<strong>Naïve bidirectional diffusion:</strong> Denoise the full video+action sequence at once. Every generation redoes all the compute. Slow, cannot stream.
</div>

<div class="blue-card text-sm mb-3">

**DreamZero's trick:** split the sequence into **chunks** of a few frames each. All frames in one chunk share a timestep $t_k$, but different chunks have **independent** timesteps.

</div>

<div class="teal-card text-sm mb-3">
<strong>Why it matters:</strong>

- Past chunks are clean → go in the KV cache
- Current chunk is being denoised
- Future chunks are noise
- One chunk can condition on all earlier clean chunks
</div>

</div>
<div>

<div class="accent-card text-sm mb-3">
<strong>Teacher forcing during training:</strong> Because timesteps are independent per chunk, the model is forced to handle "past clean, present noisy" contexts naturally. This is what makes autoregressive rollout work.
</div>

<div class="card text-sm mb-3">
<strong>KV cache reuse at inference:</strong> Once a chunk is fully denoised, its keys and values are cached. The next chunk only recomputes its own tokens.<br/><br/>
<strong>3–4× faster</strong> than bidirectional for long rollouts.
</div>

<div class="teal-card text-sm">
<strong>Variable-length training:</strong> The same architecture handles any sequence length at inference, even though training uses fixed chunk counts.
</div>

</div>
</div>

---

# Closed-Loop: Predicted → Real

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

<div class="card text-sm mb-3">
The big risk with video world models is <strong>drift</strong>: small prediction errors compound as you autoregress, and after a few seconds the dream diverges from reality.
</div>

<div class="accent-card text-sm mb-3">
<strong>DreamZero's fix — observation replacement:</strong><br/><br/>
After each action chunk executes on the real robot, the <strong>actually observed</strong> frame replaces the previously <em>predicted</em> frame in the KV cache.
</div>

<div class="blue-card text-sm mb-3">
<strong>Effect:</strong> the world model never has to commit to a long-horizon hallucination. At every step, the past KV cache is grounded in real observations.
</div>

</div>
<div>

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

</div>
</div>

---

# DreamZero-Flash: 7 Hz Real-Time

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

<div class="card text-sm mb-3">
A 14B DiT doing 50 denoising steps per chunk is <strong>way too slow</strong> for real-time robot control. DreamZero-Flash is the inference-time distillation that makes it work.
</div>

<div class="blue-card text-sm mb-3">

**Step 1 — Beta-distribution noise schedule**

Instead of uniform $t \sim U(0,1)$, sample from $\text{Beta}(\alpha, \beta)$ skewed toward low noise. Better denoisers on the timesteps that matter at inference.

</div>

<div class="teal-card text-sm mb-3">

**Step 2 — Few-step distillation**

Progressive distillation: train a student to match the teacher's trajectory in fewer steps. DreamZero-Flash runs in just a handful of denoising iterations per chunk.

</div>

<div class="accent-card text-sm">
<strong>Result:</strong> <strong>38× speedup</strong> → <strong>7 Hz closed-loop control</strong> on a single H100.
</div>

</div>
<div>

### Why this matters

<div class="card text-sm mb-3">
7 Hz is the magic number for manipulation: fast enough for visuomotor feedback, slow enough that the 14B model can run on a single H100.
</div>

<div class="teal-card text-sm mb-3">
Prior video-action models (UniPi, GR-1) had to cheat — run the video model open-loop and execute many actions between predictions. DreamZero doesn't.
</div>

<div class="blue-card text-sm">
<strong>Engineering punchline:</strong> you can have a huge world model AND real-time control — the two are no longer in tension.
</div>

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

<div class="blue-card text-sm mb-3">
<strong>DreamZero's result:</strong> Transfer from AgiBot G1 → YAM bimanual with just <strong>20 minutes of video-only play data</strong> (no demonstrations, no action labels, raw video).
</div>

<div class="accent-card text-sm mb-3">
Task progress on the new arm goes from <strong>38.3% → 55.4%</strong>. A +17 point absolute improvement from 20 minutes of unpaired video.
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
layout: center
---

# Part 3: Building Our Own

## Fine-tuning DreamZero for SO-101

<div class="mt-8 text-center opacity-70 text-sm">
From the arXiv paper → a LoRA checkpoint on real SO-101 data
</div>

---

# The Goal

<div class="grid grid-cols-2 gap-4">

<div class="accent-card">
<strong>Take DreamZero</strong><br/>
NVIDIA's open-source joint world-action model — 14B Wan2.1 backbone, video + action flow-matching head.
</div>

<div class="teal-card">
<strong>Adapt it to SO-101</strong><br/>
The low-cost 6-DOF community robot arm — different kinematics, different cameras, different embodiment than DreamZero was trained on.
</div>

</div>

<div class="mt-6 purple-card">
<strong>Why this is a meaningful build:</strong>
<ul class="text-sm mt-2">
<li>DreamZero was trained on AgiBot G1 (humanoid) + DROID-Franka. <strong>SO-101 is an unseen embodiment</strong>.</li>
<li>Tests the paper's claim: <em>cross-embodiment transfer from minutes of unpaired video</em>.</li>
<li>Gives the SO-101 community a foundation model tuned to their hardware.</li>
<li>Our pipeline is a <strong>template</strong> for porting DreamZero to any new robot.</li>
</ul>
</div>

---

# Hardware & Budget

<div class="grid grid-cols-2 gap-4">

<div class="blue-card text-sm">
<strong>Compute: RunPod 4×H100</strong>
<ul class="mt-2">
<li>4× NVIDIA H100 80GB</li>
<li>2 TB RAM, 1 TB /workspace</li>
<li>Python 3.11, PyTorch 2.11 + CUDA 13.0</li>
<li>DeepSpeed ZeRO-2 for multi-GPU</li>
</ul>
</div>

<div class="teal-card text-sm">
<strong>Weights: 77 GB download</strong>
<ul class="mt-2">
<li>Wan2.1-I2V-14B-480P (DiT backbone, 7 safetensors shards)</li>
<li>Wan2.1_VAE.pth (video compressor)</li>
<li>CLIP encoder (language)</li>
<li>UMT5-XXL encoder (long text)</li>
</ul>
</div>

</div>

<div class="mt-4 accent-card text-sm">
<strong>Cost estimates:</strong><br/>
<ul>
<li><strong>PoC run (1K steps):</strong> 2× H100 × 2.5 hr = ~$15</li>
<li><strong>Full LoRA (100K steps):</strong> 4× H100 × ~14 hr = ~$84</li>
<li><strong>Total project-to-date:</strong> under $150 of cloud compute</li>
</ul>
</div>

---

# Step 1 — Adding SO-101 Support to DreamZero

<div class="grid grid-cols-2 gap-4">

<div class="accent-card text-sm">
<strong>Files patched (5)</strong>
<ol class="mt-2">
<li><code>embodiment_tags.py</code><br/>Add <code>SO101 = "so101"</code> enum value</li>
<li><code>convert_lerobot_to_gear.py</code><br/>Add <code>"so101"</code> to <code>VALID_EMBODIMENT_TAGS</code></li>
<li><code>transform/base.yaml</code><br/>Add <code>so101: 22</code> to projector index map</li>
<li><code>base_48_wan_fine_aug_relative.yaml</code><br/>Add <code>modality_config_so101</code> + <code>transform_so101</code></li>
<li><code>so101_relative.yaml</code> (new)<br/>Data config: mixture dataset, decord backend</li>
</ol>
</div>

<div class="blue-card text-sm">
<strong>What each patch does</strong>

- **Embodiment tag** — tells the action projector "this is a 6-DOF arm, not a humanoid."
- **Validator** — lets the LeRobot→GEAR converter accept SO-101.
- **Projector index 22** — shares index with `xdof` (generic N-DOF), reusing an existing action head.
- **Modality config** — declares video keys: `front`, `gripper`, `top`.
- **Data config** — points to the dataset, sets relative action mode for joint positions.

</div>

</div>

<div class="mt-3 purple-card text-sm text-center">
<strong>Total diff:</strong> ~60 lines of YAML + 3 Python tokens. DreamZero's data abstraction is modular enough that adding an embodiment isn't a rewrite.
</div>

---

# Step 2 — Finding SO-101 Data

<div class="grid grid-cols-[2fr_3fr] gap-4">

<div>

<div class="accent-card text-sm">
<strong>Where the data lives</strong><br/>
HuggingFace LeRobot v3.0 datasets — open, community-contributed, varying quality.
</div>

<div class="mt-3 teal-card text-sm">
<strong>Search strategy</strong>
<ul class="mt-2">
<li>Filter by <code>robot_type = so101_follower</code></li>
<li>Filter for ≥25 episodes (too few = noisy)</li>
<li>Filter for published camera keys</li>
</ul>
</div>

<div class="mt-3 blue-card text-sm">
<strong>Result:</strong> 6 priority datasets<br/>
<strong>715 total episodes</strong>
</div>

</div>

<div>

<table class="text-xs">
<thead><tr><th>Dataset</th><th>Eps</th><th>Cameras</th><th>Tasks</th></tr></thead>
<tbody>
<tr><td>whosricky/so101-megamix-v1</td><td>400</td><td>front, gripper, top</td><td>8</td></tr>
<tr><td>lipsop/so101-block-in-bin</td><td>100</td><td>1</td><td>1</td></tr>
<tr><td>youliangtan/so101-table-cleanup</td><td>80</td><td>1</td><td>4</td></tr>
<tr><td>G3ND3K/so101-green-lego</td><td>60</td><td>2</td><td>0</td></tr>
<tr><td>lerobot/svla_so101_pickplace</td><td>50</td><td>2</td><td>0</td></tr>
<tr><td>observabot/so101_cloth_fold</td><td>25</td><td>1</td><td>1</td></tr>
</tbody>
</table>

<div class="mt-3 warn-card text-xs">
<strong>Megamix is the anchor</strong> — 400 episodes, 3 cameras, 8 tasks. The largest single-operator SO-101 dataset on HF. It's what our PoC trained on.
</div>

</div>

</div>

---

# Step 3 — Converting LeRobot v3.0 → DreamZero GEAR

<div class="flex justify-center mb-2">
  <img src="/figures/so101-data-pipeline.png" class="max-h-64 rounded-lg" />
</div>

<div class="grid grid-cols-3 gap-3">

<div class="accent-card text-xs">
<strong>Problem</strong><br/>
LeRobot v3.0 stores <em>all episodes</em> in one concatenated video file per camera + one parquet. DreamZero expects <em>per-episode</em> files.
</div>

<div class="blue-card text-xs">
<strong>Parquet splitting</strong><br/>
Use <code>episode_index</code> column → filter per episode → write 400 files. Finished in <strong>&lt;1 second</strong>.
</div>

<div class="teal-card text-xs">
<strong>Video splitting</strong><br/>
Decode all frames to RAM (162 GB), slice by episode boundaries, re-encode h264 MP4. <strong>2 hours total</strong> for 179K frames × 3 cams.
</div>

</div>

<div class="mt-3 purple-card text-xs">
<strong>GEAR metadata generated:</strong> <code>modality.json</code> (keys + indices), <code>embodiment.json</code> (tag: so101), <code>stats.json</code> (q01/q99/mean/std for normalization), <code>relative_stats_dreamzero.json</code>, <code>tasks.jsonl</code>, <code>episodes.jsonl</code>, <code>info.json</code>.
</div>

---

# Step 4 — The PoC Training Run

<div class="grid grid-cols-2 gap-4">

<div class="accent-card text-sm">
<strong>Config</strong>
<ul class="mt-2">
<li>2× H100 80GB</li>
<li>LoRA rank 4</li>
<li>Batch size 1</li>
<li>Learning rate 1e-4</li>
<li>DeepSpeed ZeRO-2</li>
<li>1,000 steps target</li>
</ul>
</div>

<div class="teal-card text-sm">
<strong>Loss trajectory (1K steps)</strong>

| Step | Total | Video | Action |
|---|---|---|---|
| 0 | 0.420 | 0.176 | 0.249 |
| 100 | 0.230 | 0.060 | 0.160 |
| 300 | 0.096 | 0.044 | 0.058 |
| 500 | 0.076 | 0.041 | 0.035 |
| 780 | 0.056 | 0.028 | 0.021 |
| 1000 | 0.068 | ~0.043 | ~0.030 |

</div>

</div>

<div class="mt-3 purple-card text-sm">
<strong>Total loss dropped 84% (0.42 → 0.068)</strong> in 1K steps — 2h 31min wall time, 8.75 s/step, 72.7 GB / 80 GB per GPU. Final LoRA checkpoint: <strong>217 MB safetensors</strong>.
</div>

---

# Step 5 — The Seven Bugs Before Training Worked

<div class="grid grid-cols-2 gap-3 text-sm">

<div class="warn-card">
<strong>1. cuDNN SDPA backend crash</strong><br/>
Wrap all SDPA calls with <code>sdpa_kernel([FLASH, EFFICIENT, MATH])</code> — cuDNN backend incompatible with PyTorch 2.11.
</div>

<div class="warn-card">
<strong>2. PyTorch 2.11 LR scheduler</strong><br/>
<code>zip(..., strict=True)</code> breaks on optimizer groups. Patched to remove <code>strict=True</code>.
</div>

<div class="warn-card">
<strong>3. DataLoader OOM</strong><br/>
<code>dataloader_num_workers=10</code> kills workers silently. Dropped to 4.
</div>

<div class="warn-card">
<strong>4. LoRA rank in wrong config key</strong><br/>
<code>lora_rank</code> is nested in <code>action_head_cfg</code>, not top-level. Removed from CLI override.
</div>

<div class="warn-card">
<strong>5. Missing <code>annotation.task</code></strong><br/>
<code>modality.json</code> needs <code>"task": {"original_key": "task_index"}</code> mapping.
</div>

<div class="warn-card">
<strong>6. Blinker distutils conflict</strong><br/>
<code>pip install --ignore-installed blinker</code> to avoid system package collision.
</div>

<div class="warn-card col-span-2">
<strong>7. torchvision / huggingface-hub version drift</strong><br/>
torchvision 0.19 incompatible with torch 2.11 → upgrade to 0.26. huggingface-hub 1.8 breaks transformers 4.51 → pin to <code>&lt;1.0</code>. deepspeed latest has broken <code>BaseMuonWithAuxAdam</code> → pin to <strong>0.16.4</strong>.
</div>

</div>

<div class="mt-3 purple-card text-xs">
<strong>Lesson:</strong> foundation model fine-tuning is 10% ML and 90% environment archaeology. Document every pin, every patch, every version — or repeat them.
</div>

---

# Step 6 — What's Next

<div class="grid grid-cols-2 gap-4">

<div class="teal-card text-sm">
<strong>Full LoRA training (100K steps)</strong>
<ul class="mt-2">
<li>4× H100, ~14 hours, ~$84</li>
<li>All 715 episodes mixed</li>
<li>Save checkpoint every 5K steps</li>
<li>LoRA rank 16 (up from 4)</li>
<li>Target: match DreamZero paper's AgiBot numbers on SO-101 tasks</li>
</ul>
</div>

<div class="blue-card text-sm">
<strong>Real-robot evaluation</strong>
<ul class="mt-2">
<li>Deploy LoRA on our SO-101 at Vizuara</li>
<li>Test: pick-and-place, sorting, cloth folding</li>
<li>Report success rates on seen + novel objects</li>
<li>Measure closed-loop Hz on single H100</li>
</ul>
</div>

</div>

<div class="mt-4 accent-card">
<strong>Release plan:</strong> open-source LoRA checkpoint + setup guide on HuggingFace. First SO-101-specific foundation model for the open community. <em>Repository:</em> <code>dreamzero-so101/</code>.
</div>

<div class="mt-4 purple-card">
<strong>The bigger bet:</strong> if the LoRA fine-tune matches DreamZero's cross-embodiment transfer numbers on a $300 robot, Paradigm B has a realistic path to the long tail of robot hardware — not just NVIDIA-scale labs.
</div>

---
layout: center
---

# Summary

<table class="text-sm">
<thead>
<tr><th>Axis</th><th>Paradigm A (Video → ID)</th><th>Paradigm B (Joint)</th></tr>
</thead>
<tbody>
<tr><td>Architecture</td><td>Two models (video + inverse dynamics)</td><td>One model, jointly denoised obs + action</td></tr>
<tr><td>Representation</td><td>Pixels are the plan</td><td>Latents span obs + action</td></tr>
<tr><td>Internet priors</td><td>Via video model pretraining</td><td>Via joint pretraining on Wan/Cosmos</td></tr>
<tr><td>Test-time compute</td><td>Generate full video, then decode</td><td>Conditional sampling, ~7 Hz closed-loop</td></tr>
<tr><td>Cross-embodiment</td><td>Requires per-robot action data</td><td>20 min of unpaired video → +17 pts</td></tr>
<tr><td>Best-in-class</td><td>GR-2, VPP</td><td>Cosmos + DreamZero</td></tr>
</tbody>
</table>

<div class="mt-6 text-center" style="font-family:'Caveat',cursive;font-size:1.6em;color:var(--claude-accent)">
Paradigm A erases the two-model boundary progressively.<br/>Paradigm B was never drawn.
</div>

---
layout: center
---

# Thank You

<div class="mt-6 accent-card">
<strong>Questions to sit with:</strong>
<ol class="text-sm mt-2">
<li>Which axis of the Paradigm A → B evolution feels <em>inevitable</em> and which feels like a choice?</li>
<li>DreamZero achieves the cross-embodiment transfer from 20 min of unpaired video. What makes this possible that a Paradigm-A system can't do?</li>
<li>For your own robot: which paradigm would you pick, and why?</li>
</ol>
</div>

<div class="pt-6 text-center opacity-70 text-sm">
Vizuara · Modern Robot Learning from Scratch V2<br/>
<code>dreamzero-so101/</code> · LoRA checkpoint coming soon
</div>
