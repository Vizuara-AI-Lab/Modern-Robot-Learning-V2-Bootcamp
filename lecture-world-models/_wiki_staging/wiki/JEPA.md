---
created: 2026-04-15
updated: 2026-04-15
source_chat: vjepa2-lecture-slides
status: active
tags: [architecture, self-supervised-learning, representation-learning, yann-lecun]
---

# JEPA

**Joint Embedding Predictive Architecture (JEPA)** is a framework proposed by Yann LeCun for [[Self-Supervised Learning]] that learns representations by predicting in latent space rather than in pixel/token space. It is a cornerstone of LeCun's vision for building world models and achieving machine intelligence.

## Core Principle

JEPA is **non-generative**: instead of predicting exact pixels or tokens (like GPT or diffusion models), it predicts abstract representations of targets. This forces the model to learn high-level causal and semantic structure rather than low-level texture details.

## Three Components

1. **Context Encoder** -- Encodes the observed (unmasked) portion of the input into a latent representation
2. **Predictor** -- Takes the context encoding and predicts the latent representation of the masked/target region
3. **Target Encoder** -- Encodes the target (masked) portion into the latent space; updated via **EMA (Exponential Moving Average)** of the context encoder weights with **stop-gradient** (no backpropagation through the target encoder)

## Key Insight

By predicting in latent space with an EMA target encoder:
- The model cannot "cheat" by memorizing pixel patterns
- It must learn the **causal structure** and **semantic content** of the data
- Irrelevant details (exact textures, lighting variations) are naturally discarded
- The representation collapse problem is avoided via the EMA + stop-gradient mechanism

## Variants

- **I-JEPA** -- Image JEPA: self-supervised learning on images
- **V-JEPA** -- Video JEPA: extends to video, masking spatiotemporal regions
- **[[V-JEPA 2]]** -- Scaled-up V-JEPA with 1B parameters, achieving SOTA results and enabling robot planning

## Relation to World Models

LeCun argues that JEPA-style architectures are the right foundation for [[World Models]] because:
- Generative models waste capacity on irrelevant details
- Latent prediction naturally captures causal/physical structure
- The learned representations are reusable for downstream planning and control
- [[V-JEPA 2]]-AC validates this by achieving 80% pick-and-place success with a frozen JEPA encoder

## Related Pages
- [[V-JEPA 2]]
- [[Self-Supervised Learning]]
- [[World Models]]
- [[Meta AI]]
