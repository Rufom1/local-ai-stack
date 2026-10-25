# Local AI Stack — Phase 0

A Git-first learning repository for an **RTX 5080 / Windows + WSL2 + Docker** workstation, with a possible later **Linux V100 inference server**. Work on the documentation and templates from a Mac; deploy only after validating the desktop environment.

## First goals
1. Text-to-image using **ComfyUI** (planned to run natively in WSL2).
2. Lightweight chat using **Ollama + Open WebUI** (planned via Docker Compose).
3. Specialized chat profiles, first through system instructions, next with knowledge retrieval, and eventually through fine-tuned adapters.

## Learn / edit on your Mac now
1. Read `docs/00-roadmap.md` and `docs/01-architecture.md`.
2. Edit `configs/decisions.md` to log choices.
3. Read `docs/02-chat-customization.md`; edit `models/chat/fiction-assistant.Modelfile` as a first exercise.
4. Read `docs/03-image-pipeline.md`; sketch your first ComfyUI workflow in `workflows/README.md`.
5. Run `python3 scripts/validate.py` to check repository structure and parse the sample YAML (PyYAML optional).
6. Create your own Git repository, commit, and push to a private remote (instructions in `docs/04-git-workflow.md`).

**Do not deploy on your Mac**: the `infra/chat/compose.yaml` is intended for Docker Desktop on your Windows machine using the WSL2 backend and an NVIDIA GPU. It is a starting template, **not a tested deployment**.

## Repository map
- `docs/`: explanations, learning goals, deployment notes
- `infra/chat/`: Docker Compose for Ollama/Open WebUI
- `models/chat/`: Ollama Modelfiles for chat specialties
- `configs/`: decisions, hardware assumptions, `.env` example
- `workflows/`: ComfyUI workflow notes (real exported workflows later)
- `experiments/`: evaluation rubric and experiment logs
- `scripts/`: lightweight static validator

## Security
Keep ports on `127.0.0.1`, keep WebUI authentication enabled, do not commit `.env`, personal images, datasets, private documents, model weights, API keys, or secrets. For access from the Mac later, prefer SSH tunnels or Tailscale with access controls rather than opening services on the internet.

## Documentation sources
- [Docker Compose GPU reservations](https://docs.docker.com/compose/how-tos/gpu-support/)
- [Open WebUI quick start](https://docs.openwebui.com/getting-started/quick-start/)
- [Ollama Docker](https://ollama.com/blog/ollama-is-now-available-as-an-official-docker-image)
- [ComfyUI repository](https://github.com/Comfy-Org/ComfyUI)

# local-ai-stack