# How text-to-image works in ComfyUI

Typical SDXL pipeline:

1. **Checkpoint loader** selects the neural network components/conditioning encoders and VAE.
2. **Text encoders** convert positive/negative prompts into embeddings.
3. **Empty latent** chooses dimensions and initial latent shape.
4. **Sampler** iteratively denoises a seeded latent using model and conditioning.
5. **VAE decoder** translates latent into pixels.
6. **Save Image** writes an output and may include recoverable workflow metadata.

Start with a known working official example workflow; do not assume a specific newer architecture uses exactly these SDXL nodes. Advanced image control (ControlNet, image-to-image, inpainting, LoRA, tiled upscale) comes after a reproducible base run.

## First notebook entry
Track date, GPU, checkpoint name/version/license, prompt, seed, resolution, sampler, scheduler, steps, CFG, time, peak VRAM, and observations. Test one changed variable at a time.

## Download hygiene
Use official model sources or well-understood trusted repositories. Review model licenses and file formats. Prefer `safetensors` for weights where supported. Avoid executing unfamiliar custom nodes without review. Never commit model downloads or output media by default.

## Next exercise
Sketch the following graph in `workflows/README.md`: checkpoint → text encoding → sampler → decode → save, plus a latent input. After deployment, replace the sketch with an actual exported ComfyUI workflow JSON.
