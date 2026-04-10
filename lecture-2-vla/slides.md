---
theme: default
title: "Vision-Language-Action Models: From Duct Tape to Transformers"
info: |
  Lecture 2 — Modern Robot Learning from Scratch V2 Bootcamp
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

# Vision-Language-Action Models

## From Duct Tape to Transformers

<div class="pt-8">
  <span class="px-4 py-2 rounded-lg text-lg" style="background:#c2785c;color:#fff;font-weight:700;">
    Modern Robot Learning from Scratch — V2
  </span>
</div>

<div class="pt-4 opacity-60">
  Lecture 2 — Vizuara Bootcamp
</div>

<div class="abs-br m-6 flex gap-2">
  <a href="https://vizuara.ai" target="_blank" class="text-sm opacity-50 hover:opacity-100">
    vizuara.ai
  </a>
</div>


---

<div style="height:1px;"></div>

---
layout: center
---

# What You'll Learn Today

<div class="grid grid-cols-3 gap-3 mt-4 text-left text-sm">

<div class="accent-card">

### Part 1: Encoding Language
We have vision (CNN) and actions (Diffusion). How do we **encode language** for a robot?
</div>

<div class="teal-card">

### Part 2: Build a VLA from Scratch
Combine all three modalities into a **mini-VLA** — and watch it fail spectacularly.
</div>

<div class="blue-card">

### Part 3: Transformers from Scratch
Why our approach failed — and the architecture that **fixes everything**.
</div>

</div>

<div class="grid grid-cols-2 gap-3 mt-3 text-left text-sm">

<div class="purple-card">

### Part 4: Vision & VLMs
Vision Transformers and models that **see and understand**.
</div>

<div class="card" style="border: 2px solid var(--claude-accent);">

### Part 5: Modern VLAs
From VLM to VLA — how **real robots** use pre-trained understanding to act.
</div>

</div>

---

<div style="height:1px;"></div>

---
layout: section
---

# Part 1
## We Have Two Pieces — Let's Add the Third

---

# Recap: What We Know from Lecture 1

In Lecture 1, we built **two** of the three pieces a robot needs:

<v-clicks>

<div class="grid grid-cols-2 gap-6 mt-4">

<div class="blue-card">

### Vision Encoding (CNN)

A camera image → ResNet-18 → **visual features** (512-d)

The robot can **see** — it extracts spatial features from pixels.

</div>

<div class="accent-card">

### Action Generation (Diffusion)

Pure noise → 1D U-Net denoiser → **smooth trajectory**

The robot can **act** — it generates multi-step motor commands.

</div>

</div>

</v-clicks>

<div v-click class="mt-4 teal-card text-center">

**But what happens when a human says "pick up the red cup"?** How does the robot understand language?

</div>

---

# The Missing Piece

<div class="flex justify-center items-start" style="padding-top:1rem;">
<img src="/figures/recap-cnn-diffusion.png" class="rounded-lg" style="max-height:68vh; max-width:85%;" />
</div>

---

<div style="height:1px;"></div>

---

# The Question

A human tells the robot: **"pick up the red cup"**

<v-clicks>

<div class="accent-card mt-4">

How do we convert this **sentence** — a sequence of words — into a **numerical vector** that our neural network can process?

</div>

<div class="mt-4 card">

This is exactly the same problem we faced with images:
- **Images** are pixels → CNN converts them to feature vectors
- **Sentences** are words → **???** converts them to feature vectors

</div>

<div class="mt-4 teal-card text-center">

Let's explore **three levels** of language encoding — from simplest to most sophisticated.

</div>

</v-clicks>

---

# Level 0: Bag of Words

The simplest possible idea: **count which words appear**.

<v-clicks>

<div class="mt-4 card">

Build a vocabulary of all known words, then represent each sentence as a **count vector**:

</div>

<div class="grid grid-cols-2 gap-4 mt-3">

<div class="accent-card text-sm">

**Sentence:** "pick up the red cup"

| pick | up | the | red | cup | grab | crimson | mug | ... |
|------|-----|------|------|------|--------|----------|------|------|
| 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | ... |

</div>

<div class="teal-card text-sm">

**Sentence:** "grab the crimson mug"

| pick | up | the | red | cup | grab | crimson | mug | ... |
|------|-----|------|------|------|--------|----------|------|------|
| 0 | 0 | 1 | 0 | 0 | 1 | 1 | 1 | ... |

</div>

</div>

</v-clicks>

<div v-click class="mt-3 accent-card text-center">

**These mean the same thing!** But the vectors share only 1 word ("the"). Cosine similarity ≈ 0.2.

</div>

---

# Bag of Words — Animated

<div class="text-sm opacity-60 -mt-2 mb-2">Watch how two synonymous sentences produce completely different sparse vectors.</div>

<div class="flex justify-center items-start" style="padding-top:0.5rem;">
<video controls class="rounded-lg" style="max-height:65vh; max-width:90%;">
  <source src="/viz/manim/Scene01_BagOfWords.mp4" type="video/mp4">
</video>
</div>

<div v-click class="mt-2 accent-card text-center text-sm">

The only overlap is "the" — a meaningless function word. Bag of Words is blind to meaning.

</div>

---

# Bag of Words: Why It Fails for Robots

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

<v-clicks>

<div class="card mb-3">

### Problem 1: No Synonyms
"pick" and "grab" are completely unrelated.
"cup" and "mug" are completely unrelated.
The vector space has **no concept of meaning**.

</div>

<div class="card mb-3">

### Problem 2: No Word Order
"put the cup ON the plate" and "put the plate ON the cup" produce **identical** vectors.
Word order is destroyed.

</div>

<div class="card">

### Problem 3: Sparse & High-Dimensional
With a vocabulary of 10,000 words, each sentence is a vector with ~99.95% zeros. Wasteful and uninformative.

</div>

</v-clicks>

</div>

<div v-click class="flex items-center justify-center">

<div class="accent-card text-center">

**Verdict:** Bag of Words is useless for robot instructions.

A robot that can't distinguish "pick up the cup" from "put down the cup" is dangerous!

</div>

</div>

</div>

---

<div style="height:1px;"></div>

---

# Level 1: Word Embeddings (Word2Vec)

**Key insight:** Words that appear in similar **contexts** should have similar **vectors**.

<v-clicks>

<div class="card mt-4">

Instead of sparse one-hot vectors, learn a **dense** vector (e.g., 300 dimensions) for each word by reading millions of sentences.

- "The cat sat on the ___" → "mat", "rug", "floor" → these words get similar vectors
- "Pick up the ___" → "cup", "mug", "glass" → similar vectors!

</div>

<div class="teal-card mt-3 text-center">

**Meaning is captured by geometry.** Similar words = nearby vectors in 300-d space.

</div>

</v-clicks>

---

# Word2Vec: The Famous Analogy

The most celebrated result in word embeddings:

<div class="flex justify-center items-start mt-3">
<img src="/figures/word2vec-embedding-space.png" class="rounded-lg" style="max-height:50vh; max-width:80%;" />
</div>

<div v-click class="mt-3 accent-card text-center">

**king − man + woman ≈ queen** — The model learned that "royalty" and "gender" are separate directions in vector space!

</div>

---

# Word Embeddings — Animated

<div class="text-sm opacity-60 -mt-2 mb-2">Watch synonyms cluster together and the king-queen analogy emerge from geometry.</div>

<div class="flex justify-center items-start" style="padding-top:0.5rem;">
<video controls class="rounded-lg" style="max-height:65vh; max-width:90%;">
  <source src="/viz/manim/Scene02_Word2VecSpace.mp4" type="video/mp4">
</video>
</div>

<div v-click class="mt-2 teal-card text-center text-sm">

Actions (pick/grab/grasp), objects (cup/mug/glass), and colors (red/crimson/scarlet) all cluster by meaning.

</div>

---

# Word2Vec: What It Means for Robots

Now "pick" and "grab" are **neighbors** in vector space:

<v-clicks>

<div class="grid grid-cols-3 gap-4 mt-4">

<div class="teal-card text-center">

### Actions Cluster
pick ≈ grab ≈ grasp ≈ lift

All nearby in embedding space

</div>

<div class="blue-card text-center">

### Objects Cluster
cup ≈ mug ≈ glass ≈ goblet

Semantically grouped

</div>

<div class="purple-card text-center">

### Colors Cluster
red ≈ crimson ≈ scarlet

The robot knows these are similar

</div>

</div>

</v-clicks>

<div v-click class="mt-4 card">

**But there's a catch:** Each word gets **one** fixed vector. "Bank" (river) = "bank" (money). And we get per-word vectors, not a **sentence** vector.

</div>

---

# Word2Vec: The Remaining Problem

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

### Per-Word vs Per-Sentence

Word2Vec gives us a vector for each word:
- "pick" → [0.3, -0.1, 0.8, ...]
- "up" → [0.1, 0.5, -0.2, ...]
- "the" → [0.0, 0.1, 0.0, ...]
- "red" → [0.7, 0.2, 0.4, ...]
- "cup" → [0.4, -0.3, 0.6, ...]

<div v-click class="accent-card mt-3">

**But our robot needs ONE vector for the whole sentence.** We could average them — but then "pick up the cup" and "the cup picks up" would be the same!

</div>

</div>

<div v-click>

### What We Need

A method that:

<div class="card mt-2 mb-2">

1. Uses **meaningful** word vectors (not sparse one-hot) ✓

</div>

<div class="card mb-2">

2. Respects **word order** ("on the table" ≠ "the table on") ✗

</div>

<div class="card">

3. Produces a **single vector** for the whole sentence ✗

</div>

<div class="teal-card mt-3 text-center">

We need something that **reads** the sentence in order...

</div>

</div>

</div>

---

<div style="height:1px;"></div>

---

# Level 2: GRU — Reading Word by Word

**GRU (Gated Recurrent Unit)**: A neural network that processes words **sequentially**, maintaining a running memory.

<v-clicks>

<div class="card mt-4 text-sm">

Think of it like reading a book:
- You read word 1 → update your understanding
- You read word 2 → update your understanding further
- ... continue through the whole sentence
- At the end, your "understanding" is the **sentence embedding**

</div>

<div class="mt-3 teal-card text-center">

**A GRU reads the sentence left-to-right, updating a hidden state at each word. The final hidden state IS the sentence vector.**

</div>

</v-clicks>


---

<div style="height:1px;"></div>

---

# GRU: How It Works

<div class="flex justify-center items-start" style="padding-top:0.5rem;">
<img src="/figures/gru-sequential-processing.png" class="rounded-lg" style="max-height:55vh; max-width:85%;" />
</div>

<div v-click class="mt-2 accent-card text-center text-sm">

Each GRU cell has **gates** that decide: what to remember, what to forget, and what to update. The hidden state accumulates meaning.

</div>

---

# GRU Processing — Animated

<div class="text-sm opacity-60 -mt-2 mb-2">Watch the GRU read "pick up the red cup" word by word, building up its hidden state.</div>

<div class="flex justify-center items-start" style="padding-top:0.5rem;">
<video controls class="rounded-lg" style="max-height:65vh; max-width:90%;">
  <source src="/viz/manim/Scene03_GRUProcessing.mp4" type="video/mp4">
</video>
</div>

<div v-click class="mt-2 accent-card text-center text-sm">

The entire sentence gets compressed into a single 128-d vector. This bottleneck is the GRU's fundamental limitation.

</div>

---

# GRU: A Concrete Example

Let's trace through "pick up the red cup":

<v-clicks>

<div class="card mt-3 text-sm">

| Step | Input Word | What the Hidden State "Knows" |
|------|-----------|-------------------------------|
| 1 | "pick" | An action is happening (grasping/lifting) |
| 2 | "up" | The action is upward (not "pick out" or "pick apart") |
| 3 | "the" | A specific object is coming next |
| 4 | "red" | The object has a color property: red |
| 5 | "cup" | **Full understanding:** lift a specific red cup upward |

</div>

<div class="grid grid-cols-2 gap-4 mt-3">

<div class="teal-card text-sm">

**Advantage over BoW:** Word order matters! "pick up the cup" ≠ "the cup picks up"

</div>

<div class="blue-card text-sm">

**Advantage over Word2Vec:** Produces ONE vector for the whole sentence, not separate word vectors

</div>

</div>

</v-clicks>

<div v-click class="mt-3 accent-card text-center text-sm">

**But there's a cost:** The entire sentence is squeezed into a **single fixed-size vector** (e.g., 128-d). This creates a bottleneck.

</div>

---

# GRU: The Bottleneck Problem

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

### Short Sentences — Fine

"pick up the red cup"

5 words → 128-d vector → plenty of room

<div v-click class="card mt-3">

### Long Sentences — Trouble

"pick up the cup that is next to the plate on the **left** side of the table"

16 words → same 128-d vector → information lost!

By the time the GRU reaches "left", it has partially forgotten "cup".

</div>

</div>

<div v-click>

### The Fundamental Issue

<div class="accent-card">

GRU processes **sequentially** — each word can only see what came before it.

Early words fade as the sentence gets longer. Information flows only **left → right**.

This is like reading a book and only being allowed to remember the last few pages.

</div>

<div class="teal-card mt-3 text-center text-sm">

We'll see how **Transformers** solve this in Part 3 — by letting every word look at every other word simultaneously.

</div>

</div>

</div>


---

<div style="height:1px;"></div>

---

<div style="height:1px;"></div>

---

# Summary: Three Levels of Language Encoding

<div class="flex justify-center items-start" style="padding-top:0.5rem;">
<img src="/figures/three-levels-language-encoding.png" class="rounded-lg" style="max-height:55vh; max-width:80%;" />
</div>

<div v-click class="mt-2 accent-card text-center text-sm">

For our mini-VLA, we'll use **Level 2 (GRU)** — the best we have so far. Let's see how far it gets us!

</div>

---

# The Code: GRU Text Encoder

<a href="/notebooks/Language_Encoding_Levels.ipynb" download class="text-xs px-2 py-1 rounded" style="background:rgba(90,127,165,0.08);color:#5a7fa5;text-decoration:none;border:1px solid rgba(90,127,165,0.2);position:absolute;right:2em;top:4.5em;">Notebook: Language_Encoding_Levels.ipynb</a>

This is the actual encoder we'll use — just **10 lines** of PyTorch:

```python {all|2-4|5|7-9|10-11|all}
class TextEncoderGRU(nn.Module):
    def __init__(self, vocab_size, d_word=64, d_model=128):
        super().__init__()
        self.embed = nn.Embedding(vocab_size, d_word)    # word → 64-d vector
        self.gru = nn.GRU(d_word, d_model, batch_first=True)  # 64-d → 128-d

    def forward(self, token_ids):       # token_ids: [batch, seq_len]
        x = self.embed(token_ids)       # → [batch, seq_len, 64]
        _, h_last = self.gru(x)         # h_last: [1, batch, 128]
        return h_last[0]                # → [batch, 128] — sentence embedding
```

<v-clicks>

<div class="grid grid-cols-3 gap-3 mt-3 text-sm">

<div class="card text-center">

**nn.Embedding**: Lookup table mapping each word ID to a 64-d vector (like Word2Vec, but learned)

</div>

<div class="card text-center">

**nn.GRU**: Reads the sequence, maintaining a 128-d hidden state that accumulates meaning

</div>

<div class="card text-center">

**h_last[0]**: The final hidden state — our sentence embedding for the whole instruction

</div>

</div>

</v-clicks>

---

<div style="height:1px;"></div>

---

# Quiz: Language Encoding (1/3)

<div class="quiz-card mt-2">

<div class="mb-3">

**Q1:** In Bag of Words, what is the cosine similarity between "pick up the cup" and "grab the mug"?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> Very low (~0.2). Only "the" overlaps. BoW treats "pick" and "grab" as completely unrelated.
</div>

<div class="mb-3">

**Q2:** What fundamental problem does Word2Vec solve that Bag of Words cannot?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> Semantic similarity. Words with similar meaning (pick/grab, cup/mug) get nearby vectors because they appear in similar contexts.
</div>

<div class="mb-3">

**Q3:** In Word2Vec, king − man + woman ≈ queen. What does this tell us about the embedding space?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> The embedding space has learned interpretable directions — "gender" and "royalty" are separate linear directions. Analogies are captured by vector arithmetic.
</div>

<div class="mb-3">

**Q4:** Why can't we simply average Word2Vec vectors to get a sentence embedding?

</div>

<div v-click class="px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> Averaging destroys word order. "The dog bit the man" and "the man bit the dog" would have identical average vectors, despite meaning opposite things.
</div>

</div>

---

# Quiz: Language Encoding (2/3)

<div class="quiz-card mt-2">

<div class="mb-3">

**Q5:** What does the GRU's hidden state represent after processing an entire sentence?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> A fixed-size vector (e.g., 128-d) encoding the meaning of the entire sentence, including word order and context. This IS the sentence embedding.
</div>

<div class="mb-3">

**Q6:** Why does the GRU struggle with long sentences like "pick up the cup that is next to the plate on the left"?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> The GRU compresses everything into one fixed-size vector — a bottleneck. Early words ("cup") partially fade by the time it reaches late words ("left"). Information flows only left-to-right.
</div>

<div class="mb-3">

**Q7:** In the code `nn.Embedding(vocab_size, d_word)`, what exactly is being stored?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> A lookup table of shape [vocab_size × d_word]. Each row is a learnable dense vector for one word. Word ID → row index → embedding vector.
</div>

<div class="mb-3">

**Q8:** A GRU with d_model=128 processes "pick up the red cup". What is the output shape?

</div>

<div v-click class="px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> [batch_size, 128]. The final hidden state h₅ is a 128-dimensional vector regardless of sentence length. 5 words or 50 words → always 128-d.
</div>

</div>

---

# Quiz: Language Encoding (3/3)

<div class="quiz-card mt-2">

<div class="mb-3">

**Q9:** If our robot vocabulary has 200 words and we use d_word=64, how many parameters does nn.Embedding have?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> 200 × 64 = 12,800 parameters. Each of the 200 words has a 64-dimensional learnable vector.
</div>

<div class="mb-3">

**Q10:** Why do we use a GRU instead of a simple RNN for our text encoder?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> GRUs have **gating mechanisms** (reset gate, update gate) that control information flow. This helps preserve important earlier information and mitigates the vanishing gradient problem that plagues simple RNNs on longer sequences.
</div>

</div>

---

<div style="height:1px;"></div>

---
layout: section
---

# Part 2
## Let's Build a VLA! — The Duct-Tape Pipeline

---

# We Have All Three Pieces!

From Lecture 1 and Part 1 today, we now have:

<v-clicks>

<div class="grid grid-cols-3 gap-4 mt-4">

<div class="blue-card text-center">

### Vision
CNN → 128-d features

**The robot can see**

</div>

<div class="accent-card text-center">

### Language
GRU → 128-d embedding

**The robot can read**

</div>

<div class="teal-card text-center">

### Actions
Diffusion → trajectories

**The robot can act**

</div>

</div>

</v-clicks>

<div v-click class="mt-4 purple-card text-center text-lg">

**The natural idea:** Encode each modality → combine them → generate actions. Let's build it!

</div>

---

# The mini-VLA Architecture

<div class="flex justify-center items-start" style="padding-top:0.5rem;">
<img src="/figures/mini-vla-architecture.png" class="rounded-lg" style="max-height:65vh; max-width:85%;" />
</div>

<div v-click class="mt-1 accent-card text-center text-sm">

Three parallel encoders → concatenate → MLP fusion → diffusion head. ~135K parameters total. Credit: <a href="https://github.com/keivalya/mini-vla">keivalya/mini-vla</a>

</div>

---

# mini-VLA Pipeline — Animated

<div class="text-sm opacity-60 -mt-2 mb-2">Watch data flow through the three encoders, get concatenated, and produce actions.</div>

<div class="flex justify-center items-start" style="padding-top:0.5rem;">
<video controls class="rounded-lg" style="max-height:65vh; max-width:90%;">
  <source src="/viz/manim/Scene04_MiniVLAPipeline.mp4" type="video/mp4">
</video>
</div>

<div v-click class="mt-2 teal-card text-center text-sm">

Notice the "duct tape" — three independent streams simply concatenated. Vision and language never interact during encoding.

</div>

---

# Component 1: Vision Encoder — TinyCNN

A minimal CNN that converts a camera image to a 128-d vector:

```python {all|2-5|7-10|11|all}
class ImageEncoderTinyCNN(nn.Module):
    def __init__(self, d_model=128):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=5, stride=2, padding=2)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=2, padding=1)
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, stride=2, padding=1)
        self.proj = nn.Linear(128, d_model)

    def forward(self, x):              # x: [batch, 3, H, W]
        x = F.relu(self.conv1(x))      # → [batch, 32, H/2, W/2]
        x = F.relu(self.conv2(x))      # → [batch, 64, H/4, W/4]
        x = F.relu(self.conv3(x))      # → [batch, 128, H/8, W/8]
        x = x.mean(dim=[2, 3])         # Global Average Pool → [batch, 128]
        return self.proj(x)            # → [batch, 128]
```

<v-clicks>

<div class="grid grid-cols-2 gap-4 mt-3 text-sm">

<div class="card">

**3 conv layers** progressively extract features: edges → textures → shapes. Much simpler than ResNet-18 from Lecture 1.

</div>

<div class="card">

**Global Average Pool** collapses the spatial dimensions — we lose WHERE things are, keeping only WHAT things are.

</div>

</div>

</v-clicks>

---

# Component 2: Language Encoder — GRU

The text encoder we just designed in Part 1:

```python
class TextEncoderTinyGRU(nn.Module):
    def __init__(self, vocab_size, d_word=64, d_model=128):
        super().__init__()
        self.embed = nn.Embedding(vocab_size, d_word)
        self.gru = nn.GRU(d_word, d_model, batch_first=True)

    def forward(self, token_ids):       # token_ids: [batch, seq_len]
        x = self.embed(token_ids)       # → [batch, seq_len, 64]
        _, h_last = self.gru(x)         # h_last: [1, batch, 128]
        return h_last[0]                # → [batch, 128]
```

<div v-click class="mt-3 accent-card text-sm">

**Vocabulary:** Only the words seen in our training data (maybe 30-50 words). **No pre-training** — embeddings are learned from scratch on our tiny robot dataset.

</div>

---

# Component 3: State Encoder — MLP

The robot also knows its own **joint positions** — encode those too:

```python
class StateEncoderMLP(nn.Module):
    def __init__(self, state_dim, d_model=128):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(state_dim, 64),
            nn.ReLU(),
            nn.Linear(64, d_model),
        )

    def forward(self, s):               # s: [batch, state_dim]
        return self.net(s)              # → [batch, 128]
```

<div v-click class="mt-3 teal-card text-sm">

**Proprioception:** The robot's sense of its own body. Joint angles, gripper open/close, end-effector position. A simple 2-layer MLP maps this to 128-d.

</div>

---

# The Fusion: Duct Tape (Concatenation + MLP)

Now the critical question: **how do we combine these three 128-d vectors?**

<v-clicks>

<div class="card mt-4">

The simplest possible approach — **concatenate** and pass through an MLP:

```python
class FusionMLP(nn.Module):
    def __init__(self, d_model=128):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(3 * d_model, d_model),   # 384 → 128
            nn.ReLU(),
            nn.Linear(d_model, d_model),       # 128 → 128
        )

    def forward(self, img_token, txt_token, state_token):
        x = torch.cat([img_token, txt_token, state_token], dim=-1)  # → [batch, 384]
        return self.net(x)                                           # → [batch, 128]
```

</div>

</v-clicks>

<div v-click class="mt-3 accent-card text-center">

**This is the "duct tape."** Three vectors stapled together. The MLP must figure out all cross-modal reasoning from these raw concatenated features. No interaction during encoding.

</div>

---

# The Complete Pipeline: VLADiffusionPolicy

<a href="/notebooks/Build_MiniVLA.ipynb" download class="text-xs px-2 py-1 rounded" style="background:rgba(90,127,165,0.08);color:#5a7fa5;text-decoration:none;border:1px solid rgba(90,127,165,0.2);position:absolute;right:2em;top:4.5em;">Notebook: Build_MiniVLA.ipynb</a>

Putting all four components together:

```python {all|3-7|9-13|15-17|19-21|all}
class VLADiffusionPolicy(nn.Module):
    def __init__(self, vocab_size, state_dim, action_dim, d_model=128):
        super().__init__()
        self.img_encoder = ImageEncoderTinyCNN(d_model)
        self.txt_encoder = TextEncoderTinyGRU(vocab_size, d_word=64, d_model=d_model)
        self.state_encoder = StateEncoderMLP(state_dim, d_model)
        self.fusion = FusionMLP(d_model)
        self.diffusion_head = DiffusionPolicyHead(action_dim, cond_dim=d_model)

    def encode_obs(self, image, text_tokens, state):
        img_tok = self.img_encoder(image)
        txt_tok = self.txt_encoder(text_tokens)
        state_tok = self.state_encoder(state)
        return self.fusion(img_tok, txt_tok, state_tok)

    def loss(self, image, text_tokens, state, actions):
        cond = self.encode_obs(image, text_tokens, state)
        return self.diffusion_head.loss(actions, cond)

    def act(self, image, text_tokens, state):
        cond = self.encode_obs(image, text_tokens, state)
        return self.diffusion_head.sample(cond)
```

<div v-click class="mt-2 teal-card text-center text-sm">

**~150 lines of code.** Every student in this room could write this. That's both its beauty and its limitation.

</div>

---

<div style="height:1px;"></div>

---

# Let's Train It!

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

### Training Setup

<v-clicks>

<div class="card mb-3 text-sm">

**Environment:** Meta-World `push-v2`
- Robot arm pushes a puck to a goal
- 4-d actions (dx, dy, dz, gripper)
- Camera image: 64×64 RGB

</div>

<div class="card mb-3 text-sm">

**Data:** 50 expert demonstrations
- Instruction: "push the cube to the goal"
- Same camera angle, same object
- ~200 timesteps per episode

</div>

<div class="card text-sm">

**Training:** 500 epochs, lr=1e-4, batch=32
- Loss: diffusion MSE (from Lecture 1)
- Everything trained jointly from scratch
- ~10 minutes on a laptop GPU

</div>

</v-clicks>

</div>

<div v-click>

### The Training Curve

<div class="accent-card text-center" style="min-height:200px; display:flex; flex-direction:column; align-items:center; justify-content:center;">

Loss goes down. The model is learning!

**Training loss: 0.85 → 0.12**

The diffusion head learns to denoise actions conditioned on the fused vision-language-state context.

</div>

<div class="mt-3 teal-card text-center text-sm">

So far so good. Let's test it...

</div>

</div>

</div>


---

<div style="height:1px;"></div>

---

# Test 1: Same Task, Same Words — It Works!

<div class="grid grid-cols-2 gap-6 mt-4">

<div class="teal-card text-center" style="min-height:280px; display:flex; flex-direction:column; align-items:center; justify-content:center;">

### Input
**Image:** Robot arm + cube (same view as training)

**Instruction:** "push the cube to the goal"

**State:** Current joint angles

</div>

<div class="card text-center" style="min-height:280px; display:flex; flex-direction:column; align-items:center; justify-content:center;">

### Result

**Success rate: 85%**

The robot pushes the cube to the goal. The diffusion head generates smooth trajectories.

Everything is within the training distribution — this is the easy case.

<div style="font-size:3em; margin-top:0.5em;">✅</div>

</div>

</div>

---

# Test 2: New Phrasing — It Breaks

<div class="grid grid-cols-2 gap-6 mt-4">

<div class="accent-card text-center" style="min-height:280px; display:flex; flex-direction:column; align-items:center; justify-content:center;">

### Input
**Image:** Same view as before

**Instruction:** "move the block to the target"

**State:** Same joint angles

</div>

<div class="card text-center" style="min-height:280px; display:flex; flex-direction:column; align-items:center; justify-content:center;">

### Result

**Success rate: 15%**

The robot barely moves or moves randomly.

**Why?** The GRU was trained from scratch on 50 demos. It has never seen "move", "block", or "target". These are **unknown words** — their embeddings are random.

<div style="font-size:3em; margin-top:0.5em;">❌</div>

</div>

</div>

---

# Test 3: Different Camera Angle — It Breaks

<div class="grid grid-cols-2 gap-6 mt-4">

<div class="accent-card text-center" style="min-height:280px; display:flex; flex-direction:column; align-items:center; justify-content:center;">

### Input
**Image:** Same scene, camera shifted 15° to the right

**Instruction:** "push the cube to the goal"

**State:** Same joint angles

</div>

<div class="card text-center" style="min-height:280px; display:flex; flex-direction:column; align-items:center; justify-content:center;">

### Result

**Success rate: 20%**

The robot generates actions that don't match the actual scene layout.

**Why?** TinyCNN learned pixel patterns, not object concepts. 15° shift = entirely new pixel distribution. It has no idea what a "cube" looks like from this angle.

<div style="font-size:3em; margin-top:0.5em;">❌</div>

</div>

</div>

---

# Test 4: New Task via Language — Complete Failure

<div class="grid grid-cols-2 gap-6 mt-4">

<div class="accent-card text-center" style="min-height:280px; display:flex; flex-direction:column; align-items:center; justify-content:center;">

### Input
**Image:** Robot arm + two cups on a table

**Instruction:** "stack the cups"

**State:** Current joint angles

</div>

<div class="card text-center" style="min-height:280px; display:flex; flex-direction:column; align-items:center; justify-content:center;">

### Result

**Success rate: 0%**

Random, meaningless motions.

**Why?** The model has never seen cups, never seen stacking, and the words "stack" and "cups" have random embeddings. There is **zero transfer** from pushing to stacking.

<div style="font-size:3em; margin-top:0.5em;">❌</div>

</div>

</div>

---

# The Failure Summary

<div class="flex justify-center items-start" style="padding-top:0.5rem;">
<img src="/figures/mini-vla-generalization-failure.png" class="rounded-lg" style="max-height:60vh; max-width:85%;" />
</div>

<div v-click class="mt-2 accent-card text-center text-sm">

**1 out of 4 tests passed** — and only the one that exactly matched training data. Our VLA is a one-trick pony.

</div>

---

<div style="height:1px;"></div>

---

# Why Does Our VLA Suck? — Three Root Causes

<v-clicks>

<div class="accent-card mt-4 mb-3">

### Failure 1: The GRU Has Never Read a Book
Trained from scratch on 50 demonstrations. Vocabulary: ~30 words. It doesn't know "move" = "push", "block" = "cube", "target" = "goal". A human has read millions of sentences before entering this room. Our GRU hasn't read anything.

</div>

<div class="blue-card mb-3">

### Failure 2: The CNN Has Never Seen the World
TinyCNN trained on 50 images from one camera angle. It learned pixel patterns that correlate with this specific setup. It doesn't know what a "cube" IS — just what this particular arrangement of pixels looks like. A human has seen millions of objects from every angle.

</div>

<div class="teal-card">

### Failure 3: The Duct-Tape Fusion Never Lets Modalities Talk
Vision and language are encoded **separately**, then stapled together. The word "red" never directly interacts with the red pixels during encoding. The MLP must learn ALL cross-modal reasoning from scratch with 50 examples.

</div>

</v-clicks>


---

<div style="height:1px;"></div>

---

# The Duct-Tape Fusion Problem (Visually)

<div class="flex justify-center items-start" style="padding-top:0.5rem;">
<img src="/figures/duct-tape-fusion-problem.png" class="rounded-lg" style="max-height:60vh; max-width:85%;" />
</div>

<div v-click class="mt-2 accent-card text-center text-sm">

Left: our mini-VLA — three separate pipes tapled together. Right: what we **need** — modalities interacting at every layer. This requires **Transformers** (Part 3).

</div>

---

# The Core Insight

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

### The Problem Isn't the Idea

The concept of "encode vision + language + state → generate actions" is **correct**. That's exactly what modern VLAs do.

<v-click>

### The Problem Is Reinventing the Wheel

We tried to learn:
1. Language understanding (from 50 demos)
2. Visual understanding (from 50 images)
3. Cross-modal reasoning (from 50 examples)
4. Motor skills (from 50 trajectories)

**...all at the same time, from almost nothing.**

</v-click>

</div>

<div v-click>

<div class="teal-card">

### What If...

- Someone already trained a **really good** language model on trillions of words?
- Someone already trained a **really good** vision encoder on billions of images?
- Someone even trained a model that understands **both vision and language** together?

We wouldn't need to learn language or vision from scratch. We'd just teach the **last mile**: turning understanding into actions.

</div>

<div class="accent-card mt-3 text-center">

**This is the key insight behind modern VLAs.** But to understand how they work, we first need to learn about **Transformers**.

</div>

</div>

</div>

---

# What's Coming Next

<div class="grid grid-cols-2 gap-4 mt-6 text-left">

<div class="blue-card">

### Part 3: Transformers from Scratch
The attention mechanism — how every word can look at every other word. Why this fixes the GRU bottleneck and the fusion problem.
</div>

<div class="purple-card">

### Part 4: From VLMs to Modern VLAs
Next-token prediction, Vision Transformers, VLMs, and how real VLAs (RT-2, OpenVLA, pi0) are built.
</div>

</div>

<div v-click class="mt-6 accent-card text-center">

**The journey:** Duct tape (we are here) → Transformers → VLMs → Modern VLAs

</div>

---

<div style="height:1px;"></div>

---

# Quiz: mini-VLA Architecture (1/3)

<div class="quiz-card mt-2">

<div class="mb-3">

**Q1:** In the mini-VLA, what is the dimension of the fused context vector that enters the diffusion head?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> 128-d. Three 128-d vectors are concatenated (384-d), then the Fusion MLP projects back down to 128-d.
</div>

<div class="mb-3">

**Q2:** Why does the mini-VLA use Global Average Pooling in the vision encoder?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> To collapse the spatial dimensions (H, W) into a single vector. This makes the output size fixed regardless of input image resolution. Downside: spatial information (WHERE things are) is lost.
</div>

<div class="mb-3">

**Q3:** The mini-VLA fuses modalities by concatenation + MLP. What is the fundamental limitation of this approach?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> Vision, language, and state are encoded **independently** — they never interact during encoding. The word "red" never sees the red pixels. All cross-modal reasoning must be learned by a tiny 2-layer MLP.
</div>

<div class="mb-3">

**Q4:** How many total parameters does the mini-VLA have (approximately)?

</div>

<div v-click class="px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> ~135K parameters. TinyCNN ~50K, GRU ~25K, State MLP ~10K, Fusion ~50K. This is tiny compared to modern VLAs with billions of parameters.
</div>

</div>

---

# Quiz: mini-VLA Architecture (2/3)

<div class="quiz-card mt-2">

<div class="mb-3">

**Q5:** The mini-VLA fails when you say "move the block" instead of "push the cube". Why specifically?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> The GRU was trained from scratch on ~50 demos using a vocabulary of ~30 words. "Move" and "block" are out-of-vocabulary — their embeddings are random, untrained vectors. No pre-training = no synonym understanding.
</div>

<div class="mb-3">

**Q6:** If we gave the mini-VLA 10,000 demonstrations instead of 50, would it fix the language generalization problem?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> Partially — it would see more words and phrasings. But it still can't match the language understanding of a model trained on trillions of text tokens. Robot data is expensive; text data is essentially free at internet scale.
</div>

<div class="mb-3">

**Q7:** Why does the vision encoder fail with a 15° camera shift?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> TinyCNN learned pixel correlations from one viewpoint, not object understanding. A 15° shift changes the pixel distribution entirely. A model trained on billions of images (like CLIP/SigLIP) learns viewpoint-invariant object representations.
</div>

<div class="mb-3">

**Q8:** In the mini-VLA forward pass, what is the shape of `torch.cat([img_token, txt_token, state_token], dim=-1)`?

</div>

<div v-click class="px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> [batch_size, 384]. Three 128-d vectors concatenated along the feature dimension: 128 + 128 + 128 = 384.
</div>

</div>

---

# Quiz: mini-VLA Architecture (3/3)

<div class="quiz-card mt-2">

<div class="mb-3">

**Q9:** What is the analogy for why modern VLAs work better than our mini-VLA?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> Hiring someone who already speaks 50 languages and just teaching them to drive, versus teaching a baby both language AND driving simultaneously from scratch. Pre-trained foundation models provide the "50 languages" for free.
</div>

<div class="mb-3">

**Q10:** If you could only fix ONE component of the mini-VLA, which would give the biggest improvement and why?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> Replace fusion — use a Transformer that lets vision and language attend to each other, instead of concatenation + MLP. This is the biggest bottleneck: even with good encoders, late fusion with a tiny MLP can't learn rich cross-modal reasoning. Modern VLAs use cross-attention across all modalities.
</div>

</div>

---

# Brainstorm: Before We Move to Transformers

<div class="brainstorm-card mt-4">
<div class="text-center opacity-40 text-xl">
<p><em>Discussion space — draw and discuss</em></p>
<p>1. How would YOU fix the fusion problem? What if vision and language could "talk" during encoding?</p>
<p>2. Where could we get a language encoder that already knows millions of words?</p>
<p>3. What would it take for a vision encoder to recognize a "cup" from ANY angle?</p>
</div>
</div>

---

<div style="height:1px;"></div>

---
layout: section
---

# Part 3
## Transformers from Scratch — The Architecture That Fixes Everything

---

# The Problem We Need to Solve

Recall the three failures from Part 2:

<v-clicks>

<div class="grid grid-cols-3 gap-4 mt-4">

<div class="accent-card text-center">

### GRU Bottleneck
Entire sentence squeezed into one 128-d vector. Early words fade.

</div>

<div class="blue-card text-center">

### No Cross-Modal Talk
Vision and language encoded separately. "Red" never sees red pixels.

</div>

<div class="teal-card text-center">

### Sequential Processing
GRU reads left→right, one word at a time. Slow & forgetful.

</div>

</div>

</v-clicks>

<div v-click class="mt-4 purple-card text-center">

**What if every word could look at every other word — simultaneously?** That's attention.

</div>

---

<div style="height:1px;"></div>

---

# Intuition: Attention as a Lookup

Imagine you're reading the sentence: **"The robot picked up the red cup from the table."**

<v-clicks>

<div class="card mt-4">

When you read the word **"picked"**, your brain doesn't just see the previous word. You simultaneously check:
- **What** was picked? → "cup"
- **Which** cup? → "red"
- **Where** from? → "table"
- **Who** picked it? → "robot"

</div>

<div class="teal-card mt-3 text-center">

**Your brain is doing ATTENTION — each word "queries" every other word to find the relevant context. The GRU can't do this — it only sees what came before.**

</div>

</v-clicks>

---

# Attention: The Key Idea

<div class="flex justify-center items-start" style="padding-top:0.5rem;">
<img src="/figures/attention-key-idea.png" class="rounded-lg" style="max-height:60vh; max-width:85%;" />
</div>

<div v-click class="mt-2 accent-card text-center text-sm">

Every word broadcasts: "Here's what I am" (**Value**) and "Here's how to find me" (**Key**). Every word also asks: "What am I looking for?" (**Query**). Attention = matching queries to keys.

</div>


---

<div style="height:1px;"></div>

---

# Step 1: Create Q, K, V

Each word embedding gets projected into three separate vectors:

<v-clicks>

<div class="card mt-3 text-sm">

| Vector | Name | Purpose | Analogy |
|--------|------|---------|---------|
| **Q** | Query | "What am I looking for?" | A search query you type |
| **K** | Key | "What do I contain?" | A page title / tag |
| **V** | Value | "Here's my actual content" | The page content itself |

</div>

<div class="accent-card mt-3">

```python
# Each is a simple linear projection from the embedding
Q = W_q @ x    # [seq_len, d_model] @ [d_model, d_k] → [seq_len, d_k]
K = W_k @ x    # same shape
V = W_v @ x    # same shape
```

</div>

<div class="teal-card mt-3 text-center text-sm">

**Three different "views" of the same word.** The word "red" has a Query (looking for the noun it modifies), a Key (saying "I'm a color"), and a Value (its actual meaning content).

</div>

</v-clicks>

---

# Step 2: Compute Attention Scores

**How much should each word attend to every other word?**

<v-clicks>

<div class="card mt-4">

Take the **dot product** of each Query with every Key:

$$\text{score}(i, j) = Q_i \cdot K_j$$

High dot product = Q and K are aligned = word $i$ should pay attention to word $j$.

</div>

<div class="grid grid-cols-2 gap-4 mt-3">

<div class="accent-card text-sm">

**Example:** "picked" as query

| Word | Score | Why? |
|------|-------|------|
| robot | 0.3 | Who did it — moderate |
| picked | 0.1 | Self — low |
| up | 0.8 | Part of verb phrase — high |
| the | 0.0 | Filler — near zero |
| red | 0.2 | Modifier — low |
| cup | 0.9 | The object — highest! |

</div>

<div class="teal-card text-sm">

**After softmax** (normalize to sum to 1):

| Word | Weight |
|------|--------|
| robot | 0.07 |
| picked | 0.06 |
| up | 0.22 |
| the | 0.05 |
| red | 0.06 |
| cup | 0.54 |

"picked" pays 54% attention to "cup".

</div>

</div>

</v-clicks>

---

# Attention Scores — Animated

<div class="text-sm opacity-60 -mt-2 mb-2">Watch how each word computes attention scores against all other words, then reads a weighted mix.</div>

<div class="flex justify-center items-start" style="padding-top:0.5rem;">
<video controls class="rounded-lg" style="max-height:65vh; max-width:90%;">
  <source src="/viz/manim/Scene05_AttentionScores.mp4" type="video/mp4">
</video>
</div>

<div v-click class="mt-2 accent-card text-center text-sm">

Every word simultaneously queries every other word — no sequential bottleneck. This is the core of Transformers.

</div>

---

# Step 3: The Output — Weighted Sum of Values

Each word's new representation = **weighted average of all Values**:

<v-clicks>

<div class="card mt-4">

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right) V$$

</div>

<div class="grid grid-cols-2 gap-4 mt-3">

<div class="accent-card">

### What's the $\sqrt{d_k}$?

Without it, dot products grow large when $d_k$ is big, making softmax extremely peaky (one word gets ~100% weight). Dividing by $\sqrt{d_k}$ keeps gradients healthy.

</div>

<div class="teal-card">

### What this means

The output for "picked" is:
- 54% of cup's Value
- 22% of up's Value
- 7% of robot's Value
- ...and a little of everything else

**"Picked" now KNOWS about "cup".**

</div>

</div>

</v-clicks>

<div v-click class="mt-3 blue-card text-center text-sm">

**The GRU had to remember "cup" through a chain of hidden states. Attention connects "picked" directly to "cup" — no matter how far apart they are.**

</div>


---

<div style="height:1px;"></div>


---

<div style="height:1px;"></div>

---

<div style="height:1px;"></div>

---

# Why Scale? — The Temperature Problem

<v-clicks>

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

### Without scaling ($\sqrt{d_k}$)

If $d_k = 128$, dot products can reach values like 40-60.

```
softmax([42, 38, 5, 3, 1, 0])
→ [0.98, 0.02, 0.00, 0.00, 0.00, 0.00]
```

Almost **one-hot** — the model only looks at one word. Gradients vanish for all other positions.

</div>

<div>

### With scaling ($\div \sqrt{128} \approx 11.3$)

```
softmax([3.7, 3.4, 0.4, 0.3, 0.1, 0.0])
→ [0.38, 0.28, 0.14, 0.12, 0.05, 0.03]
```

**Smooth distribution** — the model can attend to multiple words. Gradients flow to all positions.

</div>

</div>

</v-clicks>

<div v-click class="mt-4 accent-card text-center text-sm">

Scaling is a simple trick, but without it, attention degenerates into hard lookup. With it, attention is a soft, differentiable retrieval.

</div>

---

# Self-Attention in Code

The entire mechanism in **8 lines** of PyTorch:

```python {all|2-4|6-8|all}
def self_attention(x, W_q, W_k, W_v):
    Q = x @ W_q             # [seq_len, d_k]   — what am I looking for?
    K = x @ W_k             # [seq_len, d_k]   — what do I contain?
    V = x @ W_v             # [seq_len, d_v]   — here's my content

    scores = Q @ K.T         # [seq_len, seq_len] — pairwise similarity
    scores = scores / (d_k ** 0.5)       # scale
    weights = softmax(scores, dim=-1)    # normalize each row
    return weights @ V       # [seq_len, d_v]   — weighted mix of values
```

<v-clicks>

<div class="grid grid-cols-3 gap-3 mt-3 text-sm">

<div class="card text-center">

**Input:** 5 words × 128-d
`[5, 128]`

</div>

<div class="card text-center">

**Attention map:** 5×5 matrix
Each row sums to 1

</div>

<div class="card text-center">

**Output:** 5 words × 128-d
Each word now "knows" about all others

</div>

</div>

</v-clicks>

---

<div style="height:1px;"></div>

---

# Multi-Head Attention: Different Perspectives

One attention head learns **one** pattern (e.g., "what object?"). We need many:

<v-clicks>

<div class="card mt-4 text-sm">

| Head | What it might learn | Example |
|------|-------------------|---------|
| Head 1 | Subject-verb | "robot" ↔ "picked" |
| Head 2 | Adjective-noun | "red" ↔ "cup" |
| Head 3 | Verb-object | "picked" ↔ "cup" |
| Head 4 | Spatial relations | "from" ↔ "table" |

</div>

<div class="accent-card mt-3">

```python
class MultiHeadAttention(nn.Module):
    def __init__(self, d_model=128, n_heads=4):
        super().__init__()
        self.heads = nn.ModuleList([
            AttentionHead(d_model, d_model // n_heads) for _ in range(n_heads)
        ])
        self.proj = nn.Linear(d_model, d_model)

    def forward(self, x):
        head_outputs = [h(x) for h in self.heads]          # 4 × [seq, 32]
        return self.proj(torch.cat(head_outputs, dim=-1))   # → [seq, 128]
```

</div>

</v-clicks>

<div v-click class="mt-2 teal-card text-center text-sm">

**4 heads × 32-d each = 128-d total.** Each head specializes in a different relationship. The projection combines their findings.

</div>

---

# Multi-Head Attention — Animated

<div class="text-sm opacity-60 -mt-2 mb-2">Watch four attention heads independently discover different word relationships, then merge their outputs.</div>

<div class="flex justify-center items-start" style="padding-top:0.5rem;">
<video controls class="rounded-lg" style="max-height:65vh; max-width:90%;">
  <source src="/viz/manim/Scene06_MultiHeadAttention.mp4" type="video/mp4">
</video>
</div>

<div v-click class="mt-2 teal-card text-center text-sm">

Each head sees the same sentence but attends to different patterns. Together, they capture the full richness of language.

</div>

---

# But Wait — Where's the Word Order?

Attention treats input as a **set**, not a sequence. It doesn't know that "picked" comes before "up":

<v-clicks>

<div class="card mt-4">

**"The robot picked up the cup"** and **"cup the picked up robot the"** would produce identical attention outputs! We need to inject position information.

</div>

<div class="accent-card mt-3">

### Positional Encoding

Add a **position-dependent signal** to each word embedding before attention:

```python
# Sinusoidal positional encoding (original Transformer)
pos_enc = torch.zeros(max_len, d_model)
position = torch.arange(max_len).unsqueeze(1).float()
div_term = torch.exp(torch.arange(0, d_model, 2).float() * -(math.log(10000.0) / d_model))
pos_enc[:, 0::2] = torch.sin(position * div_term)   # even dimensions
pos_enc[:, 1::2] = torch.cos(position * div_term)   # odd dimensions

x = x + pos_enc[:seq_len]  # add position info to word embeddings
```

</div>

<div class="teal-card mt-3 text-center text-sm">

Each position gets a unique sinusoidal fingerprint. Now "cup" at position 6 is different from "cup" at position 1. Word order is preserved.

</div>

</v-clicks>


---

<div style="height:1px;"></div>

---

<div style="height:1px;"></div>

---

# The Transformer Block

Self-attention is the core — but one block has more:

<div class="flex justify-center items-start" style="padding-top:0.5rem;">
<img src="/figures/transformer-block.png" class="rounded-lg" style="max-height:55vh; max-width:80%;" />
</div>

<div v-click class="mt-2 accent-card text-center text-sm">

**Attention** (who should I listen to?) → **FFN** (what should I think about what I heard?) → Repeated L times. LayerNorm + residual connections keep training stable.

</div>

---

# The Transformer Block in Code

<a href="/notebooks/Transformer_From_Scratch.ipynb" download class="text-xs px-2 py-1 rounded" style="background:rgba(90,127,165,0.08);color:#5a7fa5;text-decoration:none;border:1px solid rgba(90,127,165,0.2);position:absolute;right:2em;top:4.5em;">Notebook: Transformer_From_Scratch.ipynb</a>

```python {all|3-5|7-9|11-16|all}
class TransformerBlock(nn.Module):
    def __init__(self, d_model=128, n_heads=4, d_ff=512):
        super().__init__()
        self.attn = MultiHeadAttention(d_model, n_heads)
        self.norm1 = nn.LayerNorm(d_model)

        self.ffn = nn.Sequential(
            nn.Linear(d_model, d_ff), nn.GELU(), nn.Linear(d_ff, d_model)
        )
        self.norm2 = nn.LayerNorm(d_model)

    def forward(self, x):
        # Attention sub-layer with residual
        x = x + self.attn(self.norm1(x))     # "Who should I listen to?"
        # FFN sub-layer with residual
        x = x + self.ffn(self.norm2(x))      # "What should I make of it?"
        return x
```

<v-clicks>

<div class="grid grid-cols-3 gap-3 mt-2 text-sm">

<div class="card text-center">

**Residual connections** (`x + ...`) let gradients flow through. Without them, deep networks can't train.

</div>

<div class="card text-center">

**LayerNorm** stabilizes activations. Applied *before* each sub-layer (Pre-LN — used by GPT, PaLM, Gemma).

</div>

<div class="card text-center">

**FFN** expands to 4× width then compresses back. This is where individual token "thinking" happens.

</div>

</div>

</v-clicks>

---

# Stacking Transformer Blocks

A full Transformer = **many blocks stacked**:

<v-clicks>

<div class="card mt-4">

```python
class Transformer(nn.Module):
    def __init__(self, vocab_size, d_model=128, n_heads=4, n_layers=6):
        super().__init__()
        self.embed = nn.Embedding(vocab_size, d_model)
        self.pos_enc = PositionalEncoding(d_model)
        self.blocks = nn.ModuleList([
            TransformerBlock(d_model, n_heads) for _ in range(n_layers)
        ])

    def forward(self, token_ids):
        x = self.embed(token_ids) + self.pos_enc(token_ids.shape[1])
        for block in self.blocks:
            x = block(x)           # each block refines every token
        return x                   # [batch, seq_len, d_model]
```

</div>

<div class="grid grid-cols-2 gap-4 mt-3">

<div class="accent-card text-sm text-center">

**Early layers:** Low-level patterns (syntax, word grouping)

**Later layers:** High-level semantics (who did what to whom, intent)

</div>

<div class="teal-card text-sm text-center">

**Key difference from GRU:** Output is a **sequence** of vectors — one per token — not a single bottleneck vector!

</div>

</div>

</v-clicks>

---

<div style="height:1px;"></div>

---

# How Transformers Fix Our Three Failures

<v-clicks>

<div class="teal-card mt-4 mb-3">

### Fix 1: No More Bottleneck
The GRU compressed everything into 1 vector. A Transformer outputs **N vectors for N tokens** — each enriched by attention. "Cup" at position 6 carries the full context of "the red cup that was picked up from the table."

</div>

<div class="blue-card mb-3">

### Fix 2: Cross-Modal Attention (The Fusion Fix)
Put vision tokens AND language tokens into the **same sequence**. Self-attention lets "red" (text) directly attend to red pixels (vision). No more duct tape — modalities talk at every layer.

</div>

<div class="accent-card">

### Fix 3: Parallel Processing
The GRU processes words one at a time (sequential). Self-attention computes **all pairwise scores simultaneously** — the entire $N \times N$ matrix in one matrix multiply. GPU-friendly and fast.

</div>

</v-clicks>

---

# GRU vs Transformer — Side by Side

<div class="flex justify-center items-start" style="padding-top:0.5rem;">
<img src="/figures/gru-vs-transformer.png" class="rounded-lg" style="max-height:55vh; max-width:85%;" />
</div>

<div v-click class="mt-2 accent-card text-center text-sm">

**Left:** GRU — sequential, bottleneck, no cross-modal. **Right:** Transformer — parallel, per-token outputs, cross-attention. Same inputs, radically different architecture.

</div>

---

# The Computational Cost

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

### Attention is $O(N^2)$

<div class="card mt-2 text-sm">

The attention matrix is $N \times N$ (every token vs every token). For a sequence of 1000 tokens, that's **1,000,000** scores.

| Sequence Length | Attention Scores |
|----------------|-----------------|
| 10 tokens | 100 |
| 100 tokens | 10,000 |
| 1,000 tokens | 1,000,000 |
| 10,000 tokens | 100,000,000 |

</div>

<div v-click class="accent-card mt-2 text-sm">

This is why GPT-4 has a **context window** limit. Long sequences are expensive.

</div>

</div>

<div v-click>

### But It's Worth It

<div class="teal-card mt-2 text-sm">

The $O(N^2)$ cost buys us:
- **Direct** connections between any two tokens
- **Parallel** computation on GPUs
- **No information loss** over long distances
- Ability to **scale** with more layers and heads

</div>

<div class="blue-card mt-2 text-sm">

For robot instructions (5-20 words), $N^2$ is tiny. Even for VLAs with ~300 tokens (image patches + text + state), it's only ~90K scores — trivial for modern GPUs.

</div>

</div>

</div>

---

<div style="height:1px;"></div>

---

# Quiz: Transformers (1/3)

<div class="quiz-card mt-2">

<div class="mb-3">

**Q1:** In self-attention, what do Query, Key, and Value represent intuitively?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> Query = "What am I looking for?" Key = "What do I contain?" Value = "Here's my actual content." Attention matches queries to keys, then returns a weighted sum of values.
</div>

<div class="mb-3">

**Q2:** Why do we divide attention scores by $\sqrt{d_k}$?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> Without scaling, dot products grow with dimension, making softmax extremely peaky (near one-hot). Dividing by $\sqrt{d_k}$ keeps the distribution smooth and gradients healthy.
</div>

<div class="mb-3">

**Q3:** What is the shape of the attention weight matrix for a 5-word sentence?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> [5, 5]. Each of the 5 words has a weight for every other word (including itself). Each row sums to 1.0 after softmax.
</div>

<div class="mb-3">

**Q4:** Why does multi-head attention use multiple heads instead of one big attention?

</div>

<div v-click class="px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> Different heads can learn different relationship types (subject-verb, adjective-noun, spatial). One head can only learn one attention pattern per position. Multiple heads capture richer interactions.
</div>

</div>

---

# Quiz: Transformers (2/3)

<div class="quiz-card mt-2">

<div class="mb-3">

**Q5:** Without positional encoding, "the robot picked the cup" and "cup the picked robot the" produce identical outputs. Why?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> Self-attention treats its input as a **set** — it computes all pairwise dot products regardless of position. QKᵀ gives the same scores regardless of word order. Positional encoding breaks this symmetry.
</div>

<div class="mb-3">

**Q6:** What is the purpose of the FFN (feed-forward network) in a Transformer block?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> Attention mixes information across tokens (inter-token reasoning). The FFN processes each token independently — it's where per-token "thinking" and non-linear transformation happen (intra-token reasoning). It expands to 4× width for richer computation.
</div>

<div class="mb-3">

**Q7:** Why are residual connections (`x = x + sublayer(x)`) critical in deep Transformers?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> They provide a direct gradient path from the loss back to early layers, preventing vanishing gradients. They also let each layer learn a **refinement** rather than a complete transformation — easier to optimize.
</div>

<div class="mb-3">

**Q8:** A Transformer with d_model=128, 4 heads produces outputs of shape [batch, seq_len, 128]. How is this different from a GRU with d_model=128?

</div>

<div v-click class="px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> The GRU outputs [batch, 128] — one vector for the whole sentence (bottleneck). The Transformer outputs [batch, seq_len, 128] — a rich 128-d vector **per token**. Each token encodes its meaning contextualized by all other tokens.
</div>

</div>

---

# Quiz: Transformers (3/3)

<div class="quiz-card mt-2">

<div class="mb-3">

**Q9:** How does putting vision and language tokens in the same sequence enable cross-modal attention?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> Self-attention computes scores between ALL token pairs. If image patch tokens and text word tokens are in the same sequence, "red" (text) can directly attend to red pixel patches (vision). Cross-modal reasoning happens automatically — no duct tape needed.
</div>

<div class="mb-3">

**Q10:** The attention matrix for N tokens costs $O(N^2)$ memory. For a VLA with 256 image patches + 20 text tokens + 6 state tokens = 282 tokens, how many attention scores are computed per head?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> 282 × 282 = 79,524 scores per head. With 4 heads, that's ~318K scores. Trivial for a modern GPU — this is why the $O(N^2)$ cost is fine for robot-scale sequences.
</div>

</div>

---

# Brainstorm: Now You Know Attention

<div class="brainstorm-card mt-4">
<div class="text-center opacity-40 text-xl">
<p><em>Discussion space — draw and discuss</em></p>
<p>1. If you put image patches AND text tokens in the same sequence, what kind of cross-modal patterns would each attention head learn?</p>
<p>2. Why might a 6-layer Transformer understand language better than a 1-layer one, even though both use attention?</p>
<p>3. What happens if we make the Transformer REALLY deep (100+ layers) and train it on the entire internet?</p>
</div>
</div>

---

<div style="height:1px;"></div>

---
layout: section
---

# Part 4
## Vision & Vision-Language Models — Seeing with Transformers

---

# The Key Insight (Again)

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

### What we tried (Part 2)

<v-clicks>

<div class="accent-card mb-3 text-sm">

Learn **everything** from scratch:
- Language understanding → 50 demos
- Visual understanding → 50 images
- Cross-modal reasoning → 50 examples
- Motor skills → 50 trajectories

**Result:** Catastrophic failure on anything new.

</div>

</v-clicks>

</div>

<div v-click>

### What the field discovered

<div class="teal-card mb-3 text-sm">

**Don't reinvent the wheel.** Someone already trained:
- A language model on **trillions** of words
- A vision encoder on **billions** of images
- A VLM that fuses both with **cross-attention**

Just teach the **last mile**: turning understanding into robot actions.

</div>

<div class="blue-card text-sm text-center">

**Modern VLA = Pre-trained VLM + Action Fine-tuning**

This is the recipe. Let's understand each ingredient.

</div>

</div>

</div>

---

<div style="height:1px;"></div>

---

# Ingredient 1: Language Models (Next-Token Prediction)

How do you train a Transformer to understand language? **Predict the next word.**

<v-clicks>

<div class="card mt-4">

Given: "The robot picked up the red"

Predict: → **"cup"** (not "sky", not "elephant", not "seven")

To predict correctly, the model must understand:
- Grammar ("the red ___" → noun)
- Semantics ("picked up" → physical object)
- Context ("robot" → manipulation scenario)

</div>

<div class="accent-card mt-3">

### The Training Scale

| Model | Training Data | Parameters |
|-------|-------------|-----------|
| GPT-2 (2019) | 40 GB text | 1.5B |
| GPT-3 (2020) | 570 GB text | 175B |
| PaLM (2022) | 780 GB text | 540B |
| Gemma 2B (2024) | Trillions of tokens | 2B |

</div>

</v-clicks>

<div v-click class="mt-2 teal-card text-center text-sm">

After reading the internet, these models know that "pick" ≈ "grab" ≈ "grasp", "cup" ≈ "mug", and "on the table" describes a spatial relation. Exactly what our GRU was missing.

</div>

---

# Next-Token Prediction — Animated

<div class="text-sm opacity-60 -mt-2 mb-2">Watch a language model predict the next token, shifting context one word at a time using causal (left-to-right) attention.</div>

<div class="flex justify-center items-start" style="padding-top:0.5rem;">
<video controls class="rounded-lg" style="max-height:65vh; max-width:90%;">
  <source src="/viz/manim/Scene07_NextTokenPrediction.mp4" type="video/mp4">
</video>
</div>

<div v-click class="mt-2 accent-card text-center text-sm">

**Causal attention mask:** each token can only attend to tokens before it (no peeking!). This is how GPT, Gemma, and LLaMA work.

</div>

---

# But Wait — Images Aren't Sequences

We have powerful language models. But a robot doesn't just read — **it sees**.

<v-clicks>

<div class="card mt-4">

### The Problem

Transformers process **sequences of tokens** (words, subwords).

But a camera produces a **2D grid of pixels** — 224 × 224 = 50,176 pixels per frame.

How do we turn an image into something a Transformer can understand?

</div>

<div class="grid grid-cols-2 gap-4 mt-3">

<div class="accent-card text-sm">

**Approach 1: Ignore vision entirely**

Just use language. But "pick up the red cup" is ambiguous without seeing which cup is red, where it is, or where the gripper is.

</div>

<div class="teal-card text-sm">

**Approach 2: Treat image patches as tokens**

Split the image into patches. Each patch becomes a "visual word." Now we can use the same Transformer architecture!

</div>

</div>

</v-clicks>

---

# The CNN Limitation: Local Vision

Our TinyCNN from Part 2 used 3×3 convolution kernels. What does that mean for understanding a scene?

<v-clicks>

<div class="flex justify-center items-start" style="padding-top:0.5rem;">
<img src="/figures/cnn-vs-vit-attention.png" class="rounded-lg" style="max-height:42vh; max-width:85%;" />
</div>

<div class="grid grid-cols-2 gap-4 mt-3">

<div class="accent-card text-sm">

**CNN:** Each neuron sees only a tiny 3×3 local neighborhood. Even with 3 layers, the effective receptive field is just 7×7 — the model **cannot** relate a cup in one corner to a gripper in another.

</div>

<div class="teal-card text-sm">

**ViT:** Self-attention connects **every** patch to **every** other patch in a single layer. The cup's handle can attend to the gripper across the entire image. Global reasoning from layer 1.

</div>

</div>

</v-clicks>

---

# Ingredient 2: Vision Transformers (ViT)

<a href="/notebooks/Vision_Transformer_From_Scratch.ipynb" download class="text-xs px-2 py-1 rounded" style="background:rgba(90,127,165,0.08);color:#5a7fa5;text-decoration:none;border:1px solid rgba(90,127,165,0.2);position:absolute;right:2em;top:4.5em;">Notebook: Vision_Transformer_From_Scratch.ipynb</a>

**The breakthrough (2020):** Treat an image as a sequence of patches — then use a Transformer!

<v-clicks>

<div class="grid grid-cols-2 gap-4 mt-3">

<div class="card">

### How ViT Works

1. **Split** image into 16×16 pixel patches
2. **Flatten** each patch → vector (768-d)
3. **Add** positional encoding
4. **Feed** through Transformer blocks
5. **Output:** one token per patch, enriched by attention

For a 224×224 image with 16×16 patches:
→ 14 × 14 = **196 patch tokens**

</div>

<div class="flex items-center justify-center">
<img src="/figures/vit-patch-sequence.png" class="rounded-lg" style="max-height:40vh; max-width:100%;" />
</div>

</div>

</v-clicks>

<div v-click class="mt-3 teal-card text-center text-sm">

**The same architecture for both vision and language!** Patches are "visual words." Self-attention lets every patch see every other patch — the model learns that the cup's handle relates to its body.

</div>

---

# What ViT Attention Actually Sees

Different attention heads in the same ViT layer learn **different visual patterns** — automatically, from data:

<div class="flex justify-center items-start" style="padding-top:0.5rem;">
<img src="/figures/vit-attention-heads.png" class="rounded-lg" style="max-height:45vh; max-width:90%;" />
</div>

<v-clicks>

<div class="grid grid-cols-3 gap-3 mt-3 text-sm">

<div class="accent-card text-center">

**Spatial heads** learn local neighbors — edges, textures, shapes

</div>

<div class="purple-card text-center">

**Part-whole heads** link handle → cup body → rim — object structure

</div>

<div class="teal-card text-center">

**Semantic heads** group by color, material, or category — "all red things"

</div>

</div>

</v-clicks>

<div v-click class="mt-2 card text-center text-sm">

No one programmed these patterns. They **emerge** from training on millions of images. This is why ViT outperforms hand-designed CNNs.

</div>


---

<div style="height:1px;"></div>

---

# ViT Sees Shapes — But Does It Understand "Cup"?

A ViT trained on ImageNet can recognize edges, textures, and object parts. But for a robot, that's not enough.

<v-clicks>

<div class="grid grid-cols-2 gap-4 mt-4">

<div class="accent-card">

### What ViT gives us
- Detects shapes, edges, spatial structure
- Groups similar-looking patches
- Classifies: "this is category #473"

But it has **no connection to language**. The word "cup" and the image of a cup live in completely different worlds.

</div>

<div class="teal-card">

### What a robot needs
- "Pick up the **red cup**" → which patches are "red"? Which are "cup"?
- Vision features that **align with language** — so "cup" in text and cup in an image produce similar embeddings
- A vision encoder trained with **language supervision**

</div>

</div>

</v-clicks>

<div v-click class="mt-3 card text-center text-sm">

We'll solve this in Part 5 — for now, let's see how far we get with a raw ViT + an LLM.

</div>


---

<div style="height:1px;"></div>

---

<div style="height:1px;"></div>

---

# Ingredient 3: Vision-Language Models (VLMs)

**Combine a ViT + an LLM** into one model that can see AND talk:

<v-clicks>

<div class="flex justify-center items-start" style="padding-top:0.5rem;">
<img src="/figures/vlm-architecture.png" class="rounded-lg" style="max-height:45vh; max-width:85%;" />
</div>

<div class="card mt-2 text-sm">

### The VLM Recipe

| Component | Role | Example |
|-----------|------|---------|
| Vision encoder | ViT — converts image to patch tokens | ViT-Base (~86M params) |
| Language model | LLM — understands text + generates output | Gemma 2B |
| Projection layer | Aligns vision dim → LLM dim | Linear (~2M params) |

**Idea:** The ViT "sees." The LLM "thinks." The projection layer connects them.

</div>

</v-clicks>

<div v-click class="mt-2 accent-card text-center text-sm">

A VLM can answer "What color is the cup?" by attending between the word "color" and the red pixels. **Cross-modal attention** — the duct tape fix we needed!

</div>


---

<div style="height:1px;"></div>

---

# The Projection Bridge

But wait — the ViT outputs **d_v-dimensional** vectors and the LLM expects **d_model-dimensional** vectors. They speak different "languages." How do we connect them?

<v-clicks>

<div class="card mt-4">

### A Simple Linear Projection

$$\text{visual\_token}_{d_{model}} = W \cdot \text{ViT\_token}_{d_v} + b$$

A single matrix multiplication. That's it.

</div>

<div class="grid grid-cols-3 gap-3 mt-3 text-sm">

<div class="blue-card text-center">

**ViT output**

196 tokens × **d_v** (e.g. 768-d)

Rich visual features from the ViT

</div>

<div class="accent-card text-center">

**Linear projection**

$W$: d_v × d_model

Learned during VLM training

</div>

<div class="teal-card text-center">

**LLM-compatible**

196 tokens × **d_model** (e.g. 2048-d)

Now "visual words" in the LLM's language

</div>

</div>

</v-clicks>

<div v-click class="mt-3 purple-card text-center text-sm">

**Why not a deep MLP?** Because the ViT's features are already rich. A linear map just "translates" them into the LLM's coordinate system. More layers would risk overfitting.

</div>

---

# How a VLM Processes Input

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

<v-clicks>

<div class="card mb-3 text-sm">

### Step 1: Encode the Image
The ViT splits the 224×224 image into 14×14 patches → 196 visual tokens → project to the LLM's dimension

</div>

<div class="card mb-3 text-sm">

### Step 2: Tokenize the Text
"pick up the red cup" → tokenizer → [token IDs] → embedding → text tokens × 2048-d

</div>

<div class="card mb-3 text-sm">

### Step 3: Concatenate
[196 visual tokens | text tokens] → one long sequence

</div>

<div class="card text-sm">

### Step 4: Self-Attention
The Transformer attends across **both** modalities. The word "red" directly attends to red patches. The word "cup" directly attends to cup-shaped patches.

</div>

</v-clicks>

</div>

<div v-click class="flex items-center">

<div class="teal-card text-center">

**This is exactly what our mini-VLA couldn't do.**

Instead of three separate pipes stapled with duct tape, we have one unified Transformer processing everything together.

Every layer deepens the cross-modal understanding.

</div>

</div>

</div>

---

# Cross-Modal Attention: The Core Magic

When visual and text tokens share the same Transformer, something remarkable happens:

<v-clicks>

<div class="flex justify-center items-start" style="padding-top:0.5rem;">
<img src="/figures/cross-modal-attention-viz.png" class="rounded-lg" style="max-height:42vh; max-width:85%;" />
</div>

<div class="grid grid-cols-2 gap-4 mt-3 text-sm">

<div class="accent-card">

**Text → Image attention:** The word "red" attends to red-colored patches. "Cup" attends to cup-shaped patches. "Pick" attends to the gripper. The model **learns** what each word refers to visually.

</div>

<div class="teal-card">

**Image → Text attention:** A patch showing the gripper attends to "pick" and "up" — understanding that these words relate to its role. Context flows in **both directions**.

</div>

</div>

</v-clicks>

<div v-click class="mt-2 card text-center text-sm">

**No one labels which patches correspond to which words.** Cross-modal attention emerges automatically from next-token prediction training on millions of image-text pairs.

</div>

---

# VLM Processing — Animated

<div class="text-sm opacity-60 -mt-2 mb-2">Watch image patches and text tokens enter the same transformer, with cross-modal attention connecting "red" to red patches.</div>

<div class="flex justify-center items-start" style="padding-top:0.5rem;">
<video controls class="rounded-lg" style="max-height:65vh; max-width:90%;">
  <source src="/viz/manim/Scene08_VLMProcessing.mp4" type="video/mp4">
</video>
</div>

<div v-click class="mt-2 accent-card text-center text-sm">

Vision and language tokens in the same sequence — cross-modal attention happens automatically. No duct tape required.

</div>

---

# What VLMs Give Us — Before Any Robot Data

A pre-trained VLM like PaliGemma brings **four capabilities** that our mini-VLA completely lacked:

<v-clicks>

<div class="grid grid-cols-2 gap-4 mt-3">

<div class="blue-card text-sm">

### 1. Scene Understanding
"There is a red cup on a brown table next to a blue plate." The model can **describe** what it sees — from any camera angle, any lighting condition.

</div>

<div class="teal-card text-sm">

### 2. Spatial Reasoning
"The cup is to the **left** of the plate and **behind** the gripper." Relationships between objects come for free from internet pre-training.

</div>

<div class="accent-card text-sm">

### 3. Object Recognition
"That's a **cup**, even though I've never seen this exact cup before." A ViT pre-trained on large-scale data gives robust, angle-invariant recognition.

</div>

<div class="purple-card text-sm">

### 4. Instruction Grounding
"Pick up the **red** cup" → the model knows which patches are "red" and which are "cup." Language **refers** to specific visual regions.

</div>

</div>

</v-clicks>

<div v-click class="mt-3 card text-center text-sm">

All of this is **free** — no robot demos needed. The only missing piece: how to turn this understanding into **motor commands**. That's Part 5.

</div>

---

<div style="height:1px;"></div>

---

# Quiz: Vision & VLMs (1/3)

<div class="quiz-card mt-2">

<div class="mb-3">

**Q1:** What is the training objective of GPT-style language models?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> Next-token prediction. Given a sequence of tokens, predict the next token. To do this well, the model must learn grammar, semantics, facts, and reasoning — all emerge from this simple objective.
</div>

<div class="mb-3">

**Q2:** Why is ViT's global attention better than CNN's local kernels for understanding spatial relationships?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> A CNN's 3×3 kernel only sees immediate neighbors — it takes many layers to build a wide receptive field, and information degrades through layers. ViT's self-attention connects every patch to every other patch in a single layer, enabling instant global reasoning about spatial relationships across the entire image.
</div>

<div class="mb-3">

**Q3:** How does a ViT convert a 224×224 image into tokens?

</div>

<div v-click class="px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> Split the image into 16×16 pixel patches → 14×14 = 196 patches. Flatten each patch into a vector (768-d), apply a linear projection, add positional encoding, then process through Transformer blocks. Each patch becomes a "visual word" token.
</div>

</div>

---

# Quiz: Vision & VLMs (2/3)

<div class="quiz-card mt-2">

<div class="mb-3">

**Q4:** In a VLM, why are the visual tokens projected from the ViT's dimension to the LLM's dimension?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> The ViT outputs d_v-dimensional tokens (e.g. 768-d), but the LLM's embedding dimension is different (e.g. 2048-d). A linear projection aligns them to the same dimension so they can be concatenated into one sequence for the Transformer. It's a simple "translation" between two embedding spaces.
</div>

<div class="mb-3">

**Q5:** Is cross-modal attention (text attending to image patches) explicitly programmed or does it emerge?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> It **emerges** automatically. No one labels which patches correspond to which words. By placing visual and text tokens in the same sequence and training with next-token prediction, the attention mechanism learns to connect "red" to red-colored patches, "cup" to cup-shaped regions, etc.
</div>

<div class="mb-3">

**Q6:** Name four capabilities a pre-trained VLM gives a robot — before any robot data.

</div>

<div v-click class="px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> (1) Scene understanding — describe what's visible. (2) Spatial reasoning — relative positions of objects. (3) Object recognition — identify objects from any angle. (4) Instruction grounding — map language to specific image regions. All from internet pre-training, zero robot data.
</div>

</div>

---

# Quiz: Vision & VLMs (3/3)

<div class="quiz-card mt-2">

<div class="mb-3">

**Q7:** If you had a pure text LLM (like GPT) and wanted to add vision, what are the minimum components you'd need?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> (1) A **vision encoder** (like ViT) to convert images into token-like embeddings. (2) A **projection layer** to align the vision encoder's dimension to the LLM's embedding dimension. (3) A way to **concatenate** visual tokens with text tokens. That's exactly the VLM recipe: ViT + linear projection + LLM.
</div>

</div>

---

# Brainstorm: Vision & VLMs

<div class="brainstorm-card mt-4">
<div class="text-center opacity-40 text-xl">
<p><em>Discussion space — draw and discuss</em></p>
<p>1. A ViT with 14×14 = 196 patches processes a robot workspace. Which patches do you think get the MOST attention from other patches? Why?</p>
<p>2. If the ViT was only trained on ImageNet classification, what kinds of visual understanding would it have vs miss? (Hint: think about language.)</p>
<p>3. Could a VLM alone control a robot? It understands "pick up the red cup" and sees the cup. What's still missing?</p>
</div>
</div>

---

<div style="height:1px;"></div>

---
layout: section
---

# Part 5
## Moving Well — Turning Understanding into Action

---

# The VLM Can Think — But Can It Move?

In Part 4, we built a VLM that can **see** an image and **understand** text. It knows "red cup" when it sees one.

<v-clicks>

<div class="card mt-4">

### What the VLM gives us

"I see a **red cup** on the table, to the left of the blue plate. The robot gripper is above and to the right."

</div>

<div class="accent-card mt-3">

### What the robot actually needs

"Move joint 1 to **1.42 rad**, joint 2 to **-0.38 rad**, joint 3 to **2.15 rad**, joint 4 to **0.67 rad**, joint 5 to **-1.23 rad**, joint 6 to **0.91 rad**, open gripper to **0.3**"

</div>

<div class="teal-card mt-3 text-center">

**Understanding ≠ Acting.** The gap between "I see a red cup" and "move these 7 joints to these exact angles" is what Part 5 is all about.

</div>

</v-clicks>

---

# The Gap Between Thinking and Acting

<div class="flex justify-center items-start" style="padding-top:0.5rem;">
<img src="/figures/vlm-to-vla-gap.png" class="rounded-lg" style="max-height:55vh; max-width:85%;" />
</div>

<div v-click class="mt-2 card text-center text-sm">

The VLM lives in the world of **language and images**. The robot lives in the world of **joint angles and motor commands**. We need to build a bridge.

</div>

---

# What Are Robot Actions, Exactly?

Let's start from the very basics. When we say a "robot action," what do we actually mean?

<v-clicks>

<div class="card mt-4">

### A robot action = a set of numbers

Each number controls one **joint** (motor) on the robot. For our SO-101 arm:

- **Joint 1** (base rotation): how much to rotate left/right → e.g., **1.42 radians**
- **Joint 2** (shoulder): how much to lift up/down → e.g., **-0.38 radians**
- **Joint 3** (elbow): how much to bend → e.g., **2.15 radians**
- **Joint 4** (wrist pitch): tilt the wrist → e.g., **0.67 radians**
- **Joint 5** (wrist roll): rotate the wrist → e.g., **-1.23 radians**
- **Joint 6** (gripper): how open/closed → e.g., **0.30**

</div>

<div class="teal-card mt-3 text-center">

**One "action" = 6 numbers.** Each number is called an **action dimension**. Our robot has **6 action dimensions**.

</div>

</v-clicks>

---

# Robot Action Dimensions — Visualized

<div class="flex justify-center items-start" style="padding-top:0.5rem;">
<img src="/figures/robot-action-dimensions.png" class="rounded-lg" style="max-height:55vh; max-width:85%;" />
</div>

<div v-click class="mt-2 accent-card text-center text-sm">

Each joint has a **range** of possible angles (typically -π to +π radians). The action for one timestep is just **one number per joint** — telling it exactly where to go.

</div>

---

# The Action Space: Infinite Possibilities

Each joint angle is a **continuous** number — it can be 1.42, or 1.421, or 1.4217, or 1.42173...

<v-clicks>

<div class="card mt-4">

### Continuous vs Discrete

- **Discrete:** Like choosing from a menu — a fixed set of options, you pick one
- **Continuous:** Like a dimmer switch — any value in a smooth range, with infinite precision between any two points

</div>

<div class="grid grid-cols-2 gap-4 mt-3">

<div class="blue-card text-sm">

### Discrete examples
A light switch: ON or OFF. Two options.

A dice roll: 1, 2, 3, 4, 5, or 6. Six options.

Text vocabulary: ~32,000 tokens. Pick one.

</div>

<div class="accent-card text-sm">

### Continuous examples
A dimmer: any brightness from 0% to 100%.

A steering wheel: any angle in a smooth range.

A joint angle: any value from -3.14 to +3.14 radians.

</div>

</div>

<div class="teal-card mt-3 text-center">

Robot joints are **continuous** — they can be at *any* angle, not just a few predetermined ones. This will matter enormously for how we represent actions.

</div>

</v-clicks>

---

# Continuous Action Space — Visualized

<div class="flex justify-center items-start" style="padding-top:0.5rem;">
<img src="/figures/continuous-vs-discrete-actions.png" class="rounded-lg" style="max-height:55vh; max-width:85%;" />
</div>

<div v-click class="mt-2 card text-center text-sm">

With 6 joints, the action space is **6-dimensional** — every single point in this space is a unique robot pose. The model must pick the **exact** right point from an infinity of possibilities.

</div>

---

# The Big Idea: What If Actions Were "Words"?

Here's where things get clever. Remember how VLMs work?

<v-clicks>

<div class="card mt-3">

### How VLMs generate text

1. VLM has a **vocabulary** of ~32,000 tokens (words/subwords)
2. Given an image + prompt, it predicts the **next token**
3. "pick" → "up" → "the" → "red" → "cup"

Each word is just a **number** (its position in the vocabulary). "pick" = token #4,521.

</div>

<div class="accent-card mt-3">

### The RT-2 insight (Google, 2023)

What if we add **action numbers** to the vocabulary?

- "pick" = token #4,521
- "up" = token #892
- **Joint 1 angle** = token #32,147 ← NEW!
- **Joint 2 angle** = token #32,052 ← NEW!

Now the VLM can "speak" in both **words** and **motor commands**!

</div>

</v-clicks>

---

# Actions as Tokens — The Analogy

<div class="flex justify-center items-start" style="padding-top:0.5rem;">
<img src="/figures/actions-as-tokens.png" class="rounded-lg" style="max-height:55vh; max-width:85%;" />
</div>

<div v-click class="mt-2 teal-card text-center text-sm">

**Text tokens** are discrete (word #4,521 or word #892). But joint angles are **continuous** (1.4237 radians). To make actions into tokens, we need to make them discrete too. This process is called **discretization**.

</div>

---

# What Is Discretization?

Discretization means taking a **continuous** range and chopping it into **bins** (buckets).

<v-clicks>

<div class="card mt-4">

### Simple example: Temperature

Imagine temperature ranges from 0°C to 100°C. We create **10 bins**:

| Bin | Range | Label |
|-----|-------|-------|
| 0 | 0–10°C | "freezing" |
| 1 | 10–20°C | "cold" |
| 2 | 20–30°C | "mild" |
| 3 | 30–40°C | "warm" |
| ... | ... | ... |
| 9 | 90–100°C | "boiling" |

A temperature of **23.7°C** falls into Bin 2 (20–30°C). We represent it as just the number **2**.

</div>

<div class="accent-card mt-3 text-center">

**We lose precision:** 23.7°C becomes "somewhere in the 20–30 range." But we gain something — now temperature is a single **bin number**, just like a word token!

</div>

</v-clicks>

---

# Discretization — Visualized

<div class="flex justify-center items-start" style="padding-top:0.5rem;">
<img src="/figures/discretization-explained.png" class="rounded-lg" style="max-height:55vh; max-width:85%;" />
</div>

<div v-click class="mt-2 card text-center text-sm">

The more bins you use, the finer the precision — but also the larger the vocabulary. **256 bins** is the standard choice: enough precision for most tasks, small enough for the VLM to handle.

</div>

---

# Discretizing Robot Joint Angles

Now let's apply this to real robot joints.

<v-clicks>

<div class="card mt-4">

### One joint: base rotation

- Range: **-π to +π** radians (-3.14 to +3.14)
- Total range: **2π ≈ 6.28** radians
- Divide into **256 bins**
- Each bin width: 6.28 / 256 ≈ **0.0245 radians** (about **1.4°**)

</div>

<div class="grid grid-cols-2 gap-4 mt-3">

<div class="blue-card text-sm">

### Example mapping

Robot wants joint at **1.4237 rad**:
1. Which bin? → bin **#147**
2. Bin 147 center = **1.4125 rad**
3. Error = |1.4237 - 1.4125| = **0.011 rad** (~0.6°)

The exact angle is *rounded* to the nearest bin center.

</div>

<div class="teal-card text-sm">

### For all 7 joints

Each joint gets its own 256 bins. One complete action becomes **7 tokens**:

**[147, 52, 230, 89, 12, 201, 155]**

These 7 bin numbers are 7 "action words" that get added to the VLM's vocabulary.

</div>

</div>

</v-clicks>

---

# Robot Action Discretization — Visualized

<div class="flex justify-center items-start" style="padding-top:0.5rem;">
<img src="/figures/rt2-action-tokenization.png" class="rounded-lg" style="max-height:55vh; max-width:85%;" />
</div>

<div v-click class="mt-2 accent-card text-center text-sm">

Each joint's continuous range gets sliced into 256 bins. The desired angle maps to the nearest bin. **7 joints × 1 bin each = 7 action tokens** appended to the VLM's vocabulary.

</div>


---

<div style="height:1px;"></div>

---

# Explore: From Conditioning Vectors to Token Attention

Before RT-2, let's understand the key shift: how actions go from receiving a **single conditioning vector** (mini-VLA) to **attending to individual tokens** (modern VLAs).

<iframe src="https://pi0-token-attention-viz.vercel.app/" style="width:100%; height:58vh; border:1px solid var(--claude-border); border-radius:12px;" allowfullscreen></iframe>

<div v-click class="mt-2 teal-card text-center text-sm">

**Scroll through all 7 sections inside the frame**, or <a href="https://pi0-token-attention-viz.vercel.app/" target="_blank">open full-screen in a new tab</a>. This is the bridge from our mini-VLA's concat+MLP to pi0's token attention.

</div>


---

<div style="height:1px;"></div>

---
layout: center
---

# Now Let Us Talk About Some VLA Architectures

---

# RT-2: The First Real VLA (Google, 2023)

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

<v-clicks>

<div class="card mb-3 text-sm">

### Architecture

1. Start with **PaLI-X** (55B parameter VLM — already understands images + text)
2. Add **256 new tokens** to its vocabulary (one per action bin)
3. Fine-tune the VLM on **robot demonstration data**

**Input:** Camera image + "pick up the red cup"
**Output:** "147 52 230 89 12 201 155" (7 action tokens)

</div>

<div class="accent-card text-sm">

### Why does this work?

The VLM already understands "red cup" from pre-training on the internet. Fine-tuning just teaches it: *"when you see a red cup and hear 'pick up', output action tokens that move the arm toward it."*

</div>

</v-clicks>

</div>

<div v-click>

<img src="/figures/rt2-architecture-diagram.png" class="rounded-lg" style="max-height:45vh; max-width:100%;" />

</div>

</div>

---

# RT-2: The Results Are Dramatic

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

<div class="teal-card text-sm">

| Test | mini-VLA | RT-2 |
|------|----------|------|
| Same task, same words | 85% | 95% |
| New phrasing | 15% | **76%** |
| New camera angle | 20% | **72%** |
| Unseen object | 0% | **62%** |

</div>

<div v-click class="blue-card mt-3 text-sm text-center">

**From 15% → 76% on new phrasing** — because the VLM already knows "grab" ≈ "pick up" from its internet pre-training.

</div>

</div>

<div v-click>

<div class="card text-sm">

### Why the massive jump?

Our mini-VLA's GRU saw only **50 demos**. It had never encountered "grab" or "move" — only "pick up."

RT-2's PaLI-X was pre-trained on **billions** of internet text-image pairs. It already knows:
- "grab" ≈ "pick up" ≈ "take" ≈ "grasp"
- "cup" ≈ "mug" ≈ "glass"
- A red cup looks the same from any angle

</div>

<div class="accent-card mt-3 text-sm text-center">

**Pre-training is the cheat code.** Instead of learning language from 50 demos, inherit it from the entire internet.

</div>

</div>

</div>

---

# But RT-2 Has Two Serious Problems

Despite the impressive results, action tokenization has fundamental limitations.

<v-clicks>

<div class="accent-card mt-4 mb-3">

### Problem 1: Discretization Is Lossy

We're rounding continuous joint angles to the nearest bin:
- Desired angle: **1.4237 rad**
- Closest bin center: **1.4125 rad**
- Error: **0.011 rad** (~0.6°)

For reaching toward a cup, 0.6° is fine. But for **threading a needle** or **inserting a USB plug**, this error **adds up** across all 7 joints, and the task fails.

</div>

<div class="card mb-3">

### Problem 2: Autoregressive Prediction Is Slow

RT-2 predicts action tokens **one at a time**, like typing words:

Joint 1 → wait → Joint 2 → wait → ... → Joint 7

Each token takes ~15ms on a 55B model. Total: **7 × 15ms = 105ms**. Real-time control needs 10 Hz = one action every **100ms**. We're already **over budget**.

</div>

</v-clicks>

---

# Problem 1: Precision Loss — Up Close

<div class="flex justify-center items-start" style="padding-top:0.5rem;">
<img src="/figures/discretization-precision-loss.png" class="rounded-lg" style="max-height:50vh; max-width:85%;" />
</div>

<v-click>

<div class="grid grid-cols-2 gap-4 mt-2">

<div class="card text-sm text-center">

**More bins = more precision.** 1,024 bins → ~0.006 rad error. But more bins = larger vocabulary = even slower decoding.

</div>

<div class="accent-card text-sm text-center">

**The fundamental problem:** you can never fully eliminate rounding error. Continuous problems deserve **continuous** solutions.

</div>

</div>

</v-click>

---

# Problem 2: Sequential Slowness — The Timeline

<div class="flex justify-center items-start" style="padding-top:0.5rem;">
<img src="/figures/autoregressive-speed-problem.png" class="rounded-lg" style="max-height:50vh; max-width:85%;" />
</div>

<v-click>

<div class="teal-card mt-2 text-center text-sm">

**Each joint must wait for the previous one.** Joint 7 can't be predicted until joints 1–6 are done. This is the same "autoregressive bottleneck" that makes LLMs slow at generating long text.

</div>

</v-click>

---

# Can We Do Better?

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

<div class="accent-card mb-3">

### What we want

- **Continuous** actions (no binning → no precision loss)
- **Simultaneous** prediction (all joints at once → fast)
- Keep the **pre-trained VLM** understanding

</div>

<div v-click class="card text-sm">

### The two problems, summarized

| Problem | Cause | Impact |
|---------|-------|--------|
| Precision loss | 256 bins per joint | ~0.6° error per joint |
| Slow decoding | Sequential (1 token at a time) | 105ms for 7 joints |

</div>

</div>

<div v-click>

<div class="teal-card" style="min-height:200px; display:flex; align-items:center; justify-content:center;">

<div class="text-center">

### Yes — meet pi0

pi0 solves **both problems** with a completely different architecture. Let's walk through it step by step.

</div>

</div>

</div>

</div>

---

<div style="height:1px;"></div>

---

# pi0: What a VLA Can Actually Do

Before we look at the architecture — watch what pi0 made possible. **One model**, trained across multiple robots and tasks, doing things no robot has done before:

<div class="grid grid-cols-3 gap-3 mt-3">

<div class="card" style="padding:8px;">
<video src="https://website.pi-asset.com/v2/upload/lowres_processed2xspeed_arx4_website_batch4.mp4" autoplay muted loop playsinline style="width:100%; border-radius:8px;"></video>
<div class="text-center text-sm mt-1" style="color:var(--claude-muted);">Folding laundry</div>
</div>

<div class="card" style="padding:8px;">
<video src="https://website.pi-asset.com/v2/upload/lowres_processed2xspeed_bussing_2.mp4" autoplay muted loop playsinline style="width:100%; border-radius:8px;"></video>
<div class="text-center text-sm mt-1" style="color:var(--claude-muted);">Bussing a table</div>
</div>

<div class="card" style="padding:8px;">
<video src="https://website.pi-asset.com/v2/upload/lowres_processed1xspeed_eggs_2.mp4" autoplay muted loop playsinline style="width:100%; border-radius:8px;"></video>
<div class="text-center text-sm mt-1" style="color:var(--claude-muted);">Placing eggs in carton</div>
</div>

</div>

<div v-click class="mt-3 accent-card text-center text-sm">

Laundry folding, table bussing, egg handling — tasks that require **dexterity, contact-rich manipulation, and long-horizon planning**. All from a single VLA architecture. Let's understand how.

</div>

---

# pi0: More Tasks, One Model

<div class="grid grid-cols-3 gap-3 mt-3">

<div class="card" style="padding:8px;">
<video src="https://website.pi-asset.com/v2/upload/lowres_processed2xspeed_unload_dryer_3.mp4" autoplay muted loop playsinline style="width:100%; border-radius:8px;"></video>
<div class="text-center text-sm mt-1" style="color:var(--claude-muted);">Unloading a dryer</div>
</div>

<div class="card" style="padding:8px;">
<video src="https://website.pi-asset.com/v2/upload/lowres_processed1xspeed_togo_box4.mp4" autoplay muted loop playsinline style="width:100%; border-radius:8px;"></video>
<div class="text-center text-sm mt-1" style="color:var(--claude-muted);">Packing food to-go</div>
</div>

<div class="card" style="padding:8px;">
<video src="https://website.pi-asset.com/v2/upload/lowres_processed1xspeed_build_box_3.mp4" autoplay muted loop playsinline style="width:100%; border-radius:8px;"></video>
<div class="text-center text-sm mt-1" style="color:var(--claude-muted);">Constructing a box</div>
</div>

</div>

<div v-click class="mt-3 teal-card text-center text-sm">

**None of these were possible before 2024.** The key? A pre-trained VLM that understands the world + a diffusion-based Action Expert that generates precise continuous motor commands. Let's break it down.

</div>

---

# pi0: See It Before We Build It

Before we break down pi0's architecture, **play with the real thing**. This visualizer shows how image tokens, text tokens, and action tokens flow through pi0's transformer — with the attention patterns you can click and explore.

<iframe src="https://pi05-attention-visualizer.vercel.app/" style="width:100%; height:55vh; border:1px solid var(--claude-border); border-radius:12px;" allowfullscreen></iframe>

<div v-click class="mt-2 accent-card text-center text-sm">

Explore the attention patterns — notice how action tokens **attend to** visual and text tokens. Now let's understand **why** it works this way, piece by piece. <a href="https://pi05-attention-visualizer.vercel.app/" target="_blank">Open full-screen ↗</a>

</div>

---

# pi0: The State of the Art

Let's walk through pi0 — the most capable VLA architecture to date — **one component at a time**.

<div class="flex justify-center items-start" style="padding-top:0.5rem;">
<img src="/figures/pi0-full-architecture.png" class="rounded-lg" style="max-height:50vh; max-width:85%;" />
</div>

<div v-click class="mt-2 accent-card text-center text-sm">

**PaliGemma VLM (2.4B frozen) + Action Expert (300M trainable) + DDPM.** Continuous actions, no discretization, pre-trained understanding retained.

</div>

---

# First Ingredient: Vision-Language Alignment

pi0's vision encoder isn't a regular ViT — it's **SigLIP**. Why? In Part 4 we saw the gap:

<v-clicks>

<div class="grid grid-cols-2 gap-4 mt-4">

<div class="accent-card">

### What a raw ViT knows
- Edges, textures, shapes
- Object categories (if trained on ImageNet)

But "cup" in text and cup in an image live in **completely different embedding spaces**. The ViT has no connection to language.

</div>

<div class="teal-card">

### What a robot needs
- "Pick up the **red cup**" → which patches are "red"? Which are "cup"?
- Vision features that **align with language** — so "cup" in text and cup in an image produce **similar embeddings**

</div>

</div>

</v-clicks>

<div v-click class="mt-3 card text-center text-sm">

**SigLIP** solves this with **contrastive learning** — training a ViT on 400M image-text pairs so vision and language share the same embedding space.

</div>

---

# SigLIP: How Contrastive Learning Works

<div class="grid grid-cols-2 gap-4 mt-3">

<div class="card text-sm">

### The Contrastive Objective

<v-clicks>

1. Take a batch of (image, caption) pairs
2. Compute similarity between **every** image and **every** caption
3. **Maximize** diagonal (matching pairs)
4. **Minimize** off-diagonal (non-matching pairs)

After training on **400M image-text pairs**, the vision encoder doesn't just see pixels — it understands **concepts**.

</v-clicks>

</div>

<div class="flex items-center justify-center">
<img src="/figures/contrastive-similarity-matrix.png" class="rounded-lg" style="max-height:35vh; max-width:100%;" />
</div>

</div>

<div v-click class="grid grid-cols-2 gap-4 mt-3">

<div class="accent-card text-sm text-center">

**Result:** "Red cup" from any angle → similar embedding. "Blue plate" → different embedding. The model learns **what things are**, not just how they look.

</div>

<div class="teal-card text-sm text-center">

**This is what our TinyCNN was missing.** SigLIP has seen 400M image-text pairs. Camera angle shifts? New objects? No problem.

</div>

</div>

---

# pi0 Step 1: Visual Encoding (SigLIP)

<div class="grid grid-cols-2 gap-6 mt-3">

<div>

<v-clicks>

<div class="card mb-3 text-sm">

### What happens

1. Camera captures a **224×224 image** of the robot's workspace
2. Image is split into **14×14 = 196 patches** (each 16×16 pixels)
3. Each patch goes through the **SigLIP encoder** (ViT-So400M)
4. Output: **196 visual tokens**, each a 1,152-dimensional vector

</div>

<div class="blue-card text-sm">

### Why SigLIP, not a regular ViT?

Because SigLIP was pre-trained on **400M image-text pairs** using contrastive learning. It doesn't just see edges — it understands that certain patches correspond to "cup", "table", "gripper."

**Frozen** ❄ — already knows everything it needs. No fine-tuning required.

</div>

</v-clicks>

</div>

<div v-click>
<img src="/figures/pi0-visual-encoding-detail.png" class="rounded-lg" style="max-height:50vh; max-width:100%;" />
</div>

</div>

---

# pi0 Step 2: VLM Backbone (PaliGemma)

<div class="grid grid-cols-2 gap-6 mt-3">

<div>

<v-clicks>

<div class="card mb-3 text-sm">

### What happens

1. **196 visual tokens** from SigLIP are projected from 1,152-d to **2,048-d**
2. Text instruction is tokenized → **N text tokens** (each 2,048-d)
3. Both streams **concatenated** into one sequence: [visual | text]
4. Fed through **Gemma 2B** (26 transformer layers with self-attention)
5. Output: **fused embeddings** where vision and text have cross-attended

</div>

<div class="teal-card text-sm">

### The magic of cross-attention

Inside the transformer, the text token "red" **attends to** image patches containing red pixels. The token "cup" attends to cup-shaped patches. Language gets **grounded** in vision — automatically, from the pre-training.

**Frozen** ❄ — 2.4B params of understanding, untouched during robot training.

</div>

</v-clicks>

</div>

<div v-click>
<img src="/figures/pi0-vlm-backbone-detail.png" class="rounded-lg" style="max-height:50vh; max-width:100%;" />
</div>

</div>

---

# From Understanding to Action

The VLM has given us **fused embeddings** — rich representations where vision and language are deeply cross-attended. But embeddings aren't joint angles.

<div class="grid grid-cols-2 gap-6 mt-3">

<div>

<v-clicks>

<div class="card mb-3 text-sm">

### What we have

The fused embeddings from PaliGemma encode:
- **Where** objects are in the scene (spatial information)
- **What** they are (semantic understanding)
- **What to do** with them (instruction grounding)

All encoded in 196+N tokens × 2048 dimensions.

</div>

<div class="accent-card text-sm">

### What we need

Actual **joint angles**: 7 precise numbers that tell the robot exactly where to move.

These live in a completely different world — the world of continuous motor commands.

How do we get from understanding to movement?

</div>

</v-clicks>

</div>

<div v-click>
<img src="/figures/action-expert-transition.png" class="rounded-lg" style="max-height:50vh; max-width:100%;" />
</div>

</div>

---

# The Bridge: DDPM — You Already Know This!

From Lecture 1, you learned **Denoising Diffusion Probabilistic Models** (DDPM). The same idea powers the Action Expert.

<v-clicks>

<div class="card mt-3 text-sm">

### Recall: How DDPM works

1. **Start** with pure noise (random numbers)
2. A neural network **predicts the noise** in the input
3. **Subtract** the predicted noise → slightly cleaner
4. **Repeat** for T steps → clean output

</div>

<div class="teal-card mt-3 text-sm">

### Apply it to robot actions

1. Start with **noisy actions** (7 random joint angles)
2. A neural network predicts the noise, **conditioned on fused embeddings**
3. Subtract noise → slightly better actions
4. Repeat → **clean, precise joint angles**

The only new ingredient: the denoiser is **conditioned** on what the robot sees and hears.

</div>

</v-clicks>

---

# The Action Expert Pipeline

<div v-click>
<img src="/figures/action-expert-ddpm-pipeline.png" class="rounded-lg mx-auto" style="max-height:55vh; max-width:90%;" />
</div>

<div v-click class="mt-2 card text-center text-sm">

Same DDPM you know from Lecture 1 — but now the denoiser can "see" the scene through fused embeddings. The key question: **what neural network architecture should the denoiser use?**

</div>

---

# The Denoiser: A Black Box (For Now)

<div class="grid grid-cols-2 gap-6 mt-3">

<div>

<v-clicks>

<div class="card mb-3 text-sm">

### What goes IN

1. **Noisy actions** — the joint angles we want to clean up
2. **Timestep t** — how noisy are we? (early = very noisy, late = almost clean)
3. **Fused embeddings** — the VLM's rich understanding of the scene + instruction

</div>

<div class="blue-card mb-3 text-sm">

### What comes OUT

**Predicted noise** — the neural network's best estimate of what noise was added.

Subtract this from the noisy actions → one step closer to clean actions.

</div>

<div class="accent-card text-sm">

### The question

What **architecture** should this neural network have? It can't just be any network — it has to satisfy a crucial property...

</div>

</v-clicks>

</div>

<div v-click>
<img src="/figures/action-expert-black-box.png" class="rounded-lg" style="max-height:50vh; max-width:100%;" />
</div>

</div>

---

# Key Requirement: Deep Conditioning

The denoiser must **deeply interact** with the fused embeddings — not just glance at them.

<v-clicks>

<div class="grid grid-cols-2 gap-4 mt-3">

<div class="card text-sm" style="border-left: 3px solid #D4543A;">

### Shallow conditioning

Concatenate fused embeddings with noisy actions, feed into an MLP.

**Problem:** The MLP sees a single averaged context. It can't ask "which patch has the cup?" or "what verb did the instruction use?"

This is the duct-tape approach from Part 2 — it doesn't scale.

</div>

<div class="teal-card text-sm">

### Deep conditioning

The denoiser can **attend to individual tokens** in the fused embeddings.

- "The instruction says 'pick up' — attend to the grasping tokens"
- "The red cup is at position (x,y) — attend to those visual patches"

This requires an **attention mechanism**.

</div>

</div>

<div v-click class="mt-3 accent-card text-center text-sm">

**Insight:** We need the denoiser to have attention over the fused embeddings. What architecture is built entirely on attention? **A Transformer.**

</div>

</v-clicks>

---

# The Insight: Build Another Transformer

<div class="grid grid-cols-2 gap-6 mt-3">

<div>

<v-clicks>

<div class="card mb-3 text-sm">

### We already have one Transformer

The VLM backbone (PaliGemma) is a Transformer:
- Input: visual + text tokens (2048-d each)
- Output: fused embeddings (2048-d each)

</div>

<div class="blue-card mb-3 text-sm">

### Build a second Transformer

The Action Expert will be another Transformer:
- Input: noisy action tokens (2048-d each)
- Output: denoised action tokens (2048-d each)

</div>

<div class="teal-card text-sm">

### Why this works

Both Transformers operate on **sequences of 2048-d vectors**. They speak the same "language." The action tokens can be the same shape as VLM tokens.

But there's a problem: they're still **separate**. How does the Action Transformer read the VLM's understanding?

</div>

</v-clicks>

</div>

<div v-click>
<img src="/figures/action-expert-two-transformers.png" class="rounded-lg" style="max-height:50vh; max-width:100%;" />
</div>

</div>

---

# Two Transformers — But How Do They Talk?

<div class="grid grid-cols-2 gap-6 mt-3">

<div>

<v-clicks>

<div class="card mb-3 text-sm">

### The problem

We have:
1. **VLM Transformer** (frozen, 2.4B params) — holds scene understanding
2. **Action Transformer** (trainable) — needs to generate actions

But they're **isolated**. The Action Transformer can't see any of the VLM's rich visual-language features.

</div>

<div class="accent-card text-sm">

### The key question

How do we let the Action Transformer **read** the VLM's fused embeddings while keeping the VLM **frozen**?

We need a connection. Let's think about this step by step...

</div>

</v-clicks>

</div>

<div v-click>
<img src="/figures/action-expert-connection-question.png" class="rounded-lg" style="max-height:50vh; max-width:100%;" />
</div>

</div>

---

# The Connection: Shared Self-Attention

The elegant solution: **put all tokens in the same attention mechanism**.

<v-clicks>

<div class="grid grid-cols-2 gap-4 mt-3">

<div class="card text-sm">

### Separate attention (complex)

Two separate transformers. The Action Transformer uses **cross-attention** to peek at VLM tokens.

Like two separate meeting rooms with a window between them.

More complex, more parameters, harder to implement.

</div>

<div class="teal-card text-sm">

### Shared attention (elegant)

**One** self-attention mechanism. All tokens — visual, text, AND action — attend to each other.

Like putting everyone in the **same conference room**.

Simpler, leverages existing Transformer, natural interaction.

</div>

</div>

<div v-click class="mt-3">
<img src="/figures/action-expert-shared-attention.png" class="rounded-lg mx-auto" style="max-height:38vh; max-width:85%;" />
</div>

</v-clicks>

---

# Building the Layer: Step 1 — Assemble the Sequence

<div class="grid grid-cols-2 gap-6 mt-3">

<div>

<v-clicks>

<div class="blue-card mb-2 text-sm">

### Visual tokens (196)

From SigLIP, projected to 2048-d. Each token "knows" what's in its image patch, grounded in language from PaliGemma.

</div>

<div class="teal-card mb-2 text-sm">

### Text tokens (N)

Tokenized instruction, embedded at 2048-d. Cross-attended with visual tokens in PaliGemma — "red" is grounded to red patches.

</div>

<div class="accent-card mb-2 text-sm">

### Action tokens

Noisy actions embedded at 2048-d. These start out meaningless (random noise) but will be refined through attention.

</div>

<div class="card text-sm">

### The combined sequence

**[visual₁ ... visual₁₉₆ | text₁ ... textₙ | action₁ ... actionₖ]**

All tokens are 2048-d. The Transformer treats them as one big sequence.

</div>

</v-clicks>

</div>

<div v-click>
<img src="/figures/action-expert-input-sequence.png" class="rounded-lg" style="max-height:50vh; max-width:100%;" />
</div>

</div>

---

# Building the Layer: Step 2 — Shared Self-Attention

Every token attends to every other token. This is where the magic happens.

<div v-click>
<img src="/figures/action-expert-attention-matrix.png" class="rounded-lg mx-auto" style="max-height:38vh; max-width:85%;" />
</div>

<v-clicks>

<div class="grid grid-cols-3 gap-3 mt-2 text-sm">

<div class="accent-card">

### Action → Visual

"Where is the cup?" Action tokens learn to attend to the specific image patches that matter for the current task.

</div>

<div class="teal-card">

### Action → Text

"What's the goal?" Action tokens attend to the instruction tokens — "pick up" activates grasping-related features.

</div>

<div class="blue-card">

### Visual ↔ Text

Maintains PaliGemma's grounding. "Red" still attends to red patches. This happens for free in shared attention.

</div>

</div>

</v-clicks>

---

# Building the Layer: Step 3 — The FFN Dilemma

After attention, every token passes through a **Feed-Forward Network** (FFN). But there's a problem.

<div class="grid grid-cols-2 gap-6 mt-3">

<div>

<v-clicks>

<div class="card mb-3 text-sm">

### Recall: Transformer = Attention + FFN

Each Transformer layer has two parts:
1. **Self-Attention** — tokens interact with each other
2. **FFN** — each token is processed independently (2 linear layers + activation)

</div>

<div class="card mb-3 text-sm" style="border-left: 3px solid #D4543A;">

### The problem with one FFN

If we use **one shared FFN** for all tokens:
- During training, gradients flow through the FFN
- This **updates the FFN weights**
- But VLM tokens pass through this same FFN
- We'd be modifying the **frozen VLM's weights**!

The whole point of freezing is to protect the VLM from catastrophic forgetting.

</div>

<div class="accent-card text-sm">

### We need a different approach...

</div>

</v-clicks>

</div>

<div v-click>
<img src="/figures/action-expert-ffn-dilemma.png" class="rounded-lg" style="max-height:50vh; max-width:100%;" />
</div>

</div>

---

# The Solution: Two Separate FFNs (Mixture of Experts)

<div class="grid grid-cols-2 gap-6 mt-3">

<div>

<v-clicks>

<div class="blue-card mb-3 text-sm">

### VLM Expert FFN (Frozen ❄)

Processes visual + text tokens. These weights come from PaliGemma's pre-training and are **never updated**.

2.4B parameters of internet-scale knowledge, safely preserved.

</div>

<div class="accent-card mb-3 text-sm">

### Action Expert FFN (Trainable 🔥)

Processes action tokens only. These weights are **trained from scratch** on robot data.

300M parameters that learn: *"given this scene understanding, which motor commands achieve the goal?"*

</div>

<div class="teal-card text-sm">

### Why "Mixture of Experts"?

Each token is routed to its **specialist FFN** based on what type it is. Visual/text tokens → VLM expert. Action tokens → Action expert. Two experts, one Transformer.

</div>

</v-clicks>

</div>

<div v-click>
<img src="/figures/action-expert-moe-ffn.png" class="rounded-lg" style="max-height:50vh; max-width:100%;" />
</div>

</div>

---

# The Complete Action Expert Layer

<div v-click>
<img src="/figures/action-expert-complete-layer.png" class="rounded-lg mx-auto" style="max-height:48vh; max-width:85%;" />
</div>

<v-clicks>

<div class="grid grid-cols-4 gap-2 mt-2 text-sm">

<div class="card text-center">

**Step 1**

Assemble sequence: [visual | text | action]

</div>

<div class="card text-center">

**Step 2**

Shared self-attention: all tokens interact

</div>

<div class="card text-center">

**Step 3**

Split FFN: frozen for VLM, trainable for actions

</div>

<div class="card text-center">

**Step 4**

Merge & repeat × 26 layers

</div>

</div>

</v-clicks>


---

<div style="height:1px;"></div>

---

# pi0 Step 3: The Action Expert — Summary

<div class="grid grid-cols-2 gap-6 mt-3">

<div>

<v-clicks>

<div class="card mb-3 text-sm">

### What happens

1. Start with **random noise** (7 random numbers — one per joint)
2. Embed noise as **action tokens** (2048-d, same as VLM tokens)
3. Concatenate with VLM's fused embeddings into one sequence
4. Pass through **26 connected layers** (shared attention + split FFN)
5. DDPM denoising: **predict noise → subtract → repeat**
6. After several steps → **clean, precise, continuous actions**

</div>

<div class="accent-card text-sm">

### Why this architecture is brilliant

- **Shared attention** = action tokens deeply read VLM features (no shallow conditioning)
- **Separate FFNs** = training never touches VLM weights (protection)
- **Same token format** = seamlessly extends the existing Transformer
- **DDPM** = generates continuous actions (no discretization into bins)

**Trainable** 🔥 — 300M params, the *only* part trained on robot data.

</div>

</v-clicks>

</div>

<div v-click>
<img src="/figures/action-expert-summary.png" class="rounded-lg" style="max-height:50vh; max-width:100%;" />
</div>

</div>

---

# pi0 vs mini-VLA: The Full Picture

<div class="card mt-3 text-sm">

| Aspect | mini-VLA (Part 2) | pi0 |
|--------|-------------------|-----|
| **Vision** | TinyCNN trained on 50 images | SigLIP trained on 400M image-text pairs |
| **Language** | GRU trained on 50 demos | Gemma 2B trained on trillions of tokens |
| **Fusion** | Concatenation + 2-layer MLP | Self-attention across all modalities |
| **Action generation** | Diffusion conditioned on 128-d | DDPM with shared attention to VLM |
| **Parameters** | ~135K (all from scratch) | ~2.7B (2.4B pre-trained + 300M trainable) |
| **Training data** | 50 demos | 10K+ hours of robot data (fine-tuning only) |
| **New phrasing** | 15% | 90%+ |
| **New objects** | 0% | 75%+ |

</div>

<div v-click class="mt-3 accent-card text-center">

**Same concept, vastly different scale.** Both are "encode vision + language → generate actions." pi0 just uses 2.4 billion parameters of pre-trained understanding instead of learning from scratch.

</div>

---

# Why pi0 Works: The Four-Part Recipe

<div class="grid grid-cols-2 gap-4 mt-4">

<v-clicks>

<div class="blue-card">

### 1. Freeze the VLM
The PaliGemma backbone (2.4B params) stays **frozen**. It already understands vision + language from internet pre-training. Fine-tuning on 10K robot demos would cause **catastrophic forgetting** — it would lose everything it learned about cups, language, and the visual world.

</div>

<div class="teal-card">

### 2. Train Only the Action Expert
A small (300M param) Action Expert learns to translate VLM understanding into motor commands. It has its own FFN but **shares attention** with the VLM — so it can "read" the VLM's rich visual-language features without modifying them.

</div>

<div class="accent-card">

### 3. Diffusion, Not Tokenization
Instead of discretizing actions into 256 bins (losing precision), DDPM generates **continuous** actions. All 7 joint dimensions predicted simultaneously — no slow autoregressive decoding. Fast, precise, and elegant.

</div>

<div class="purple-card">

### 4. Multi-Task, Multi-Robot
Trained on 10K+ hours across **7 different robot embodiments** and dozens of tasks. The shared VLM backbone enables transfer: understanding "pick up cup" is the same concept regardless of which robot arm executes it.

</div>

</v-clicks>

</div>

---

# The Evolution: From Duct Tape to Transformers

<div class="flex justify-center items-start" style="padding-top:0.5rem;">
<img src="/figures/vla-evolution-timeline.png" class="rounded-lg" style="max-height:55vh; max-width:85%;" />
</div>

<div v-click class="mt-2 teal-card text-center text-sm">

**2023:** Duct-tape VLA (separate encoders, MLP fusion). **2024:** VLM + tokenized actions (RT-2, OpenVLA). **2025:** VLM + diffusion-based action generation (pi0). Same core idea, dramatically better ingredients.

</div>

---

# The Frontier: Where VLAs Are Heading

<v-clicks>

<div class="grid grid-cols-2 gap-4 mt-4">

<div class="blue-card text-sm">

### Scaling Up
pi0 uses a 2.7B model. What happens with 70B? 700B? Larger VLM backbones bring richer understanding — "make me a sandwich" might become feasible with enough world knowledge.

</div>

<div class="teal-card text-sm">

### Learning from Video
YouTube has millions of hours of humans cooking, cleaning, building. VLAs could learn manipulation skills from **passive video observation** — no robot demos needed.

</div>

<div class="accent-card text-sm">

### Closed-Loop Reasoning
Current VLAs predict short action chunks. Future VLAs will **re-plan continuously** — detecting mistakes, adapting to unexpected objects, recovering from drops. Real-time visual feedback loops.

</div>

<div class="purple-card text-sm">

### Your Turn
The field is **3 years old**. The tools are open-source (LeRobot, OpenVLA). The robots are affordable (SO-101: ~$100). **You** can build the next breakthrough.

</div>

</div>

</v-clicks>

---

<div style="height:1px;"></div>

---

# Quiz: Action Foundations

<div class="quiz-card mt-2">

<div class="mb-3">

**Q1:** A robot arm has 6 joints. How many "action dimensions" does it have, and what does each dimension represent?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> 6 action dimensions — one per joint. Each dimension is a single number representing the target angle (in radians) for that joint. Together, the 6 numbers define a complete robot pose for one timestep.
</div>

<div class="mb-3">

**Q2:** What is "discretization" and why does RT-2 need it?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> Discretization divides a continuous range into a finite number of bins. RT-2 needs it because VLMs predict tokens from a fixed vocabulary — they can't output continuous numbers directly. By mapping each joint angle to one of 256 bins, each action dimension becomes a "word" the VLM can predict as the next token.
</div>

<div class="mb-3">

**Q3:** Why does diffusion (DDPM) solve *both* problems of action tokenization (precision loss AND slow decoding)?

</div>

<div v-click class="px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> DDPM outputs **continuous** values (no binning → no rounding error) and predicts noise for **all action dimensions simultaneously** (no sequential token-by-token decoding → much faster). It transforms random noise into precise actions through iterative denoising.
</div>

</div>

---

# Quiz: Modern VLAs (1/3)

<div class="quiz-card mt-2">

<div class="mb-3">

**Q1:** RT-2 tokenizes actions into 256 bins. What is the precision for a joint with range [-π, π]?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> Range = 2π ≈ 6.28 radians. 256 bins → each bin covers 6.28/256 ≈ 0.0245 radians ≈ 1.4°. Adequate for coarse tasks but lossy for precision manipulation.
</div>

<div class="mb-3">

**Q2:** Why does pi0 use diffusion (DDPM) instead of action tokenization?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> DDPM generates **continuous** actions (no discretization loss) and predicts all action dimensions simultaneously (not autoregressively). This gives higher precision and faster inference than tokenized approaches.
</div>

<div class="mb-3">

**Q3:** Why is the VLM backbone frozen during pi0 fine-tuning?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> The VLM (PaliGemma, 2.4B params) was pre-trained on internet-scale data. Fine-tuning it on ~10K robot demos would cause catastrophic forgetting — it would lose its general vision-language understanding. Only the 300M Action Expert is trained.
</div>

<div class="mb-3">

**Q4:** What is the "Mixture of Experts" trick in pi0?

</div>

<div v-click class="px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> Each transformer layer has **shared** attention (all tokens interact) but **separate** FFN experts: a frozen VLM expert for visual/text tokens and a trainable Action expert for action tokens. This lets modalities interact via attention while keeping the VLM weights safe.
</div>

</div>

---

# Quiz: Modern VLAs (2/3)

<div class="quiz-card mt-2">

<div class="mb-3">

**Q5:** Our mini-VLA had ~135K parameters. pi0 has ~2.7B. Where does the difference come from?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> ~2.4B from the pre-trained VLM (SigLIP 400M + Gemma 2B), ~300M from the Action Expert. The mini-VLA learned vision (50K params), language (25K), and fusion (50K) from scratch — pi0 inherits 2.4B params of pre-trained understanding for free.
</div>

<div class="mb-3">

**Q6:** RT-2 predicts 7 joint actions autoregressively. At ~15ms per token on a 55B model, what's the total time vs the 10Hz (100ms) control budget?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> 7 tokens × 15ms = 105ms — already **over** the 100ms budget for 10Hz control, and that's with an optimized setup. This is why autoregressive action generation is too slow for real-time manipulation. pi0's DDPM predicts all dimensions simultaneously.
</div>

<div class="mb-3">

**Q7:** pi0 was trained across 7 different robot embodiments. Why does this work?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> The VLM backbone understands **tasks** (language + vision), not specific robots. "Pick up the red cup" means the same thing regardless of which arm does it. The Action Expert adapts to each robot's specific kinematics. Shared understanding + specialized execution.
</div>

<div class="mb-3">

**Q8:** When would training a VLA from scratch beat using a pre-trained VLM backbone?

</div>

<div v-click class="px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> Almost never with current data budgets. You'd need millions of robot demos to match what a VLM learned from internet-scale data. Only if your robot domain is completely unlike anything on the internet (e.g., underwater, microscopic) and you have massive data. For most tasks, pre-trained wins.
</div>

</div>

---

# Quiz: Modern VLAs (3/3)

<div class="quiz-card mt-2">

<div class="mb-3">

**Q9:** If you could only take ONE lesson from this lecture to apply to your own robot project, what would it be?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> **Don't learn from scratch what can be inherited.** Use pre-trained models for vision and language — they've seen billions of examples. Focus your precious robot data budget on the last mile: teaching the model to translate understanding into actions.
</div>

<div class="mb-3">

**Q10:** You're building a kitchen robot with 500 demonstrations. Which approach do you choose and why?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> Pre-trained VLM + action fine-tuning (the pi0 recipe). 500 demos is far too few to learn vision and language from scratch, but plenty for the "last mile" — teaching the Action Expert which motor commands correspond to the VLM's rich scene understanding. The VLM already knows what a cup, plate, and stove look like.
</div>

</div>

---

# Quiz: SigLIP & Vision-Language Alignment

<div class="quiz-card mt-2">

<div class="mb-3">

**Q11:** What does SigLIP's contrastive training achieve that ImageNet classification doesn't?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> SigLIP aligns vision and language in a shared embedding space. It doesn't just classify "cup" vs "plate" — it understands that "a red cup on a table" matches a specific image. This gives rich, language-grounded visual features rather than simple category labels.
</div>

<div class="mb-3">

**Q12:** In SigLIP's similarity matrix, what do the diagonal vs off-diagonal cells represent?

</div>

<div v-click class="mb-4 px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> Diagonal cells = matching image-text pairs (should be high similarity). Off-diagonal = mismatched pairs (should be low similarity). The contrastive objective maximizes the diagonal and minimizes everything else, forcing the model to learn precise image-text alignment.
</div>

<div class="mb-3">

**Q13:** SigLIP was trained on 400M image-text pairs. Our TinyCNN was trained on ~50 images. What's the ratio, and what does it explain?

</div>

<div v-click class="px-3 py-2 rounded-lg" style="background:rgba(194,120,92,0.12); border-left:3px solid var(--claude-accent);">
<strong>A:</strong> 400,000,000 / 50 = **8 million times** more data. This explains the generalization gap: SigLIP has seen cups from every angle, in every color, in every context. TinyCNN has seen 50 specific images — of course it fails on anything new.
</div>

</div>

---

# Brainstorm: Looking Ahead

<div class="brainstorm-card mt-4">
<div class="text-center opacity-40 text-xl">
<p><em>Discussion space — draw and discuss</em></p>
<p>1. If a VLA can understand "pick up the red cup" — could it understand "make me a sandwich"? What's the gap?</p>
<p>2. pi0 uses 2.4B pre-trained params. What would change with 70B? 700B?</p>
<p>3. These models learn from demonstrations. What if the robot could learn from YouTube videos of humans cooking, cleaning, building?</p>
</div>
</div>

---

<div style="height:1px;"></div>

---

# What We've Learned Today

<div class="grid grid-cols-3 gap-3 mt-4 text-sm">

<div class="accent-card">

### Part 1: Language Encoding
Three levels: Bag of Words (no meaning) → Word2Vec (meaning, no order) → GRU (meaning + order, but bottleneck)

</div>

<div class="teal-card">

### Part 2: Build a VLA from Scratch
Combine CNN + GRU + Diffusion → mini-VLA. Works on training data, **fails everywhere else**.

</div>

<div class="blue-card">

### Part 3: Transformers
Self-attention lets every token see every other. Q/K/V, multi-head, positional encoding. Fixes the bottleneck.

</div>

</div>

<div class="grid grid-cols-2 gap-3 mt-3 text-sm">

<div class="purple-card">

### Part 4: Vision & VLMs
ViT: global attention > local CNNs. ViT + projection + LLM = VLM that sees AND understands. **Cross-modal attention** is the magic.

</div>

<div class="card" style="border: 2px solid var(--claude-accent);">

### Part 5: Moving Well
VLM + Action Expert = VLA. Action dimensions → bins (RT-2) → diffusion (pi0). Same concept, **standing on the shoulders of giants**.

</div>

</div>

---

# The Journey We Took

<v-clicks>

<div class="card mt-4 mb-2 text-center text-sm">

**Bag of Words** → "pick" ≠ "grab" — useless

</div>

<div class="card mb-2 text-center text-sm">

**Word2Vec** → "pick" ≈ "grab" — but per-word, not per-sentence

</div>

<div class="card mb-2 text-center text-sm">

**GRU** → Full sentence embedding — but bottleneck for long sentences

</div>

<div class="card mb-2 text-center text-sm">

**Transformer** → Every word sees every word — parallel, no bottleneck

</div>

<div class="card mb-2 text-center text-sm">

**ViT** → Images as patch sequences — global attention replaces local CNNs

</div>

<div class="card mb-2 text-center text-sm">

**ViT + VLM** → Vision and language understood together at internet scale

</div>

<div class="accent-card text-center text-lg">

**VLM + Action Expert = VLA** → A robot that understands the world and acts in it

</div>

</v-clicks>

---

# Resources & Further Reading

<div class="grid grid-cols-2 gap-4 mt-4 text-sm">

<div class="card">

### Papers
- **Attention Is All You Need** (Vaswani et al., 2017) — The Transformer
- **An Image is Worth 16x16 Words** (Dosovitskiy et al., 2020) — ViT
- **SigLIP** (Zhai et al., 2023) — Contrastive vision-language
- **PaliGemma** (Beyer et al., 2024) — Vision-Language Model
- **RT-2** (Brohan et al., 2023) — First VLA at scale
- **pi0** (Black et al., 2024) — Diffusion-based VLA

</div>

<div class="card">

### Interactive Explorations
- [pi0 Visual Guide](https://pi0-visualizer.vercel.app) — 5-step interactive walkthrough
- [pi0 3D Hub](https://pi0-viz-hub.vercel.app) — Three.js architecture animations
- [pi0 Training Walkthrough](https://pi0-training.vercel.app) — Real data end-to-end

</div>

</div>

<div class="accent-card mt-4 text-center">

### Notebooks from Today

**Language_Encoding_Levels.ipynb** — BoW, Word2Vec, GRU side-by-side | **Build_MiniVLA.ipynb** — The full mini-VLA | **Transformer_From_Scratch.ipynb** — Self-attention, multi-head, full block | **Vision_Transformer_From_Scratch.ipynb** — ViT, projection, VLM assembly

</div>

---

# Thank You!

<div class="mt-8 text-center">
  <span class="px-4 py-2 rounded-lg text-lg" style="background:#c2785c;color:#fff;font-weight:700;">
    Modern Robot Learning from Scratch — V2
  </span>
</div>

<div class="mt-6 text-center opacity-60">

**Lecture 2: Vision-Language-Action Models — From Duct Tape to Transformers**

</div>

<div class="grid grid-cols-3 gap-4 mt-8 text-center text-sm">

<div class="card">

### Next Lecture
Hands-on: Train a VLA on your own robot data using LeRobot + SmolVLA

</div>

<div class="card">

### Practice
Run the four notebooks. Break things. Ask questions.

</div>

<div class="card">

### Explore
Visit the interactive visualizations and trace pi0 step by step.

</div>

</div>

<div class="abs-br m-6 flex gap-2">
  <a href="https://vizuara.ai" target="_blank" class="text-sm opacity-50 hover:opacity-100">
    vizuara.ai
  </a>
</div>
