# Learning roadmap

## Phase 0: Architecture and repository (Mac; no GPU needed)
- [ ] Understand Windows host vs WSL2 Linux filesystem vs Docker daemon vs containers.
- [ ] Explain how model files, Docker volumes, config files and generated outputs differ.
- [ ] Edit one chat persona and one image-generation workflow plan.
- [ ] Explain prompt customization vs RAG vs LoRA fine-tuning.
- [ ] Push a private Git remote, clone it into a second directory, and rehearse an update.
- [ ] Record the first deployment acceptance tests.

## Phase 1A: Chat on desktop
- [ ] Verify `nvidia-smi` in WSL2 and GPU pass-through to Docker.
- [ ] Start Ollama and Open WebUI with Compose.
- [ ] Pull an appropriately small baseline model and log RAM/VRAM and response latency.
- [ ] Create a named model from `models/chat/fiction-assistant.Modelfile`.

## Phase 1B: Images on desktop
- [ ] Install ComfyUI in a distinct WSL2 Python virtual environment.
- [ ] Install a compatible PyTorch GPU build.
- [ ] Obtain a legally usable SDXL checkpoint and run a simple workflow.
- [ ] Save exported ComfyUI JSON, seed, sampler, steps, CFG, model identifier, and license notes.

## Phase 2: Specialization
- [ ] Compare custom system instructions against base-model behavior on a fixed test set.
- [ ] Build knowledge retrieval separately if documents are needed.
- [ ] Prepare a *small* licensed/consensual training dataset and a held-out evaluation set before attempting LoRA.

## Later: rack-mounted V100 server
- Host LLM inference on native Linux, leave RTX 5080 on gaming desktop. Determine runtime support, driver/CUDA version, and cooling before hardware purchase.
