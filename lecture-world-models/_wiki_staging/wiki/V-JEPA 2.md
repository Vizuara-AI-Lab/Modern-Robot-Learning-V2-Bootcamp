---
created: 2026-04-15
updated: 2026-04-15
source_chat: vjepa2-lecture-slides
status: active
tags: [world-models, self-supervised-learning, video-understanding, robotics, meta]
---

# V-JEPA 2

**V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning** is a paper by [[Meta AI]] FAIR, published June 2025 (ArXiv: 2506.09985). It extends the [[JEPA]] framework to large-scale video representation learning and demonstrates that a single self-supervised video encoder can power both video understanding and robot planning.

## Architecture

- **Backbone:** ViT-g/16 with ~1B parameters
- **Positional encoding:** 3D RoPE (rotary position embeddings across space and time)
- **Tubelets:** 2x16x16 (2 frames temporally, 16x16 spatially)
- **Training paradigm:** [[Self-Supervised Learning]] via masked prediction in latent space (non-generative, following [[JEPA]] principles)

## Training

- **Dataset:** VideoMix22M -- 22 million videos, over 1 million hours of video
- **Iterations:** 252K training iterations
- **Progressive resolution:** Starts at 256px, increases to 384px during training
- **Scale:** Large-scale distributed training at Meta FAIR

## Key Results

- **+4.0 points** over V-JEPA 1 on video benchmarks
- **44% improvement** on Epic-Kitchens action anticipation task
- **State-of-the-art** video QA performance at the 8B parameter scale
- Demonstrates that self-supervised (non-generative) video models can match or exceed generative approaches

## V-JEPA 2-AC (Action-Conditioned Predictor)

V-JEPA 2-AC extends the frozen V-JEPA 2 encoder with an action-conditioned world model for robot planning:

- **Architecture:** Frozen V-JEPA 2 encoder + 300M parameter action-conditioned predictor
- **Robot training data:** Only 62 hours of robot manipulation data
- **Evaluation:** Zero-shot manipulation tasks (no task-specific fine-tuning)
- **Pick-and-place:** 80% success rate (vs 10% for the Octo baseline -- 8x improvement)
- **Key insight:** A strong general video encoder, trained purely self-supervised on internet video, provides representations rich enough for robot planning with minimal robot-specific data

## Significance

V-JEPA 2 validates Yann LeCun's vision that non-generative, latent-space prediction ([[JEPA]]) can produce world models useful for both understanding and planning. The robot results are particularly striking: a frozen encoder trained on internet video transfers directly to manipulation, suggesting that video prediction in latent space captures causal structure relevant to physical interaction.

## Related Pages
- [[JEPA]]
- [[World Models]]
- [[Meta AI]]
- [[Self-Supervised Learning]]
