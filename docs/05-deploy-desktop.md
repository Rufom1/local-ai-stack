# Phase 1 deployment guide (not executed yet)

Requirements: Windows 11; WSL2 Ubuntu; recent supported NVIDIA Windows driver; Docker Desktop with WSL2 integration and GPU support. Confirm each before proceeding.

```powershell
wsl --install -d Ubuntu-24.04
wsl --update
wsl -l -v
```

From Ubuntu, verify GPU visibility with `nvidia-smi` and container GPU access using a current NVIDIA CUDA image with `docker run --rm --gpus all ... nvidia-smi`. The latter placeholder requires selection of a published image tag at deployment time.

Then:

```bash
cd ~/projects/local-ai-stack/infra/chat
cp ../../configs/.env.example .env
docker compose config
docker compose up -d
docker compose exec ollama ollama pull qwen3:4b
```

Connect to `http://localhost:3000` from the Windows host, set up WebUI admin authentication, and verify chat responses. Check `docker compose logs --tail=100` and `nvidia-smi` if something fails. `docker compose down` stops services; **do not use `down -v` unless intentionally deleting data**.

## Create persona

```bash
cd ~/projects/local-ai-stack
docker cp models/chat/fiction-assistant.Modelfile "$(docker compose -f infra/chat/compose.yaml ps -q ollama)":/tmp/fiction-assistant.Modelfile
docker compose -f infra/chat/compose.yaml exec ollama ollama create fiction-assistant -f /tmp/fiction-assistant.Modelfile
```

The base model must have been pulled. Open WebUI may require refreshing its model list.

## ComfyUI
Use native WSL2 Python virtual environment in a **separate folder**, following ComfyUI's current manual install steps and PyTorch's current compatible NVIDIA build. Avoid hardcoding a CUDA wheel index until you verify compatibility. Bind the UI to localhost first. Save exported workflow JSON in `workflows/` after testing.

## Acceptance criteria
- GPU visible to both WSL and the Ollama container.
- Open WebUI local access works; no public port exposure.
- One small model works and telemetry recorded.
- Persona loads and is tested against same prompts as base.
- First ComfyUI image exported with exact reproducibility settings.
