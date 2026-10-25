# ComfyUI workflows

## Planned first SDXL workflow
- Checkpoint Loader → sampler model input
- Positive / negative text encode → sampler conditioning inputs
- Empty Latent Image → sampler latent input
- KSampler → VAE Decode → Save Image
- Checkpoint VAE output → VAE Decode

Once ComfyUI runs, export the real workflow JSON here and annotate the model version and parameters. This file is a design sketch, **not** an importable ComfyUI workflow.
