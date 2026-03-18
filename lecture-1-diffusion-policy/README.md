# Lecture 1: Diffusion Policy

**Visuo-Motor Policy Learning via Action Diffusion**

A 4-part lecture covering:
1. **Diffusion from Scratch** -- How to generate anything from pure noise (using Batman as our example)
2. **From Images to Robot Actions** -- Instead of generating images, generate robot actions
3. **The Full Architecture** -- Every component: ResNet18, SpatialSoftmax, U-Net, FiLM, receding horizon
4. **Build It Yourself** -- Hands-on Colab notebooks to implement and train a Diffusion Policy

## Structure

```
slides.md              # Main Slidev presentation (~120 slides)
public/
  figures/             # PaperBanana + matplotlib diagrams
  notebooks/           # Colab notebooks (downloadable from slides)
  vizuara-logo.png
notebooks/             # Source Colab notebooks
narration/             # Audio narration assets
  audio/               # Per-slide audio files
  slides/              # Slide screenshots
  script.json          # Narration script
global-bottom.vue      # Slide footer component
```

## Component Notebooks

| Notebook | Topic |
|----------|-------|
| Component_ResNet18 | Vision encoder backbone |
| Component_SpatialSoftmax | Spatial keypoint extraction |
| Component_Timestep_Embedding | Sinusoidal position encoding |
| Component_1D_UNet | 1D U-Net denoiser architecture |
| Component_FiLM | Feature-wise Linear Modulation |
| Component_Conditioning_Vector | Full conditioning pipeline |
| Component_Receding_Horizon | Predict-16, execute-8 control loop |

## Running

```bash
npm install
npx slidev
```
