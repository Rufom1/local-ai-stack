# Architecture explained

## Hosts, environments, and services

**Windows host**: controls display and the NVIDIA Windows driver. **WSL2 Ubuntu**: Linux environment for Python, ComfyUI, and repository work. **Docker Desktop (WSL integration)**: container engine for isolated services. **Container**: running application instance. **Image**: immutable application package. **Volume**: persistent data separate from a container's lifecycle.

```text
MacBook (editing, git, eventual browser/SSH)
               |
           private LAN
               |
Windows gaming desktop — NVIDIA RTX 5080
  | WSL2 Ubuntu                 | Docker Desktop GPU containers
  | ComfyUI / Python venv       | Ollama <-- Open WebUI
  | model paths on Linux FS     | model and app named volumes
```

### Why split ComfyUI and Ollama?
ComfyUI custom node dependencies change frequently; a Python venv makes debugging easier. Docker Compose makes chat services reproducible and independently restartable. Both share the RTX 5080 VRAM: expect contention while both are loaded. Do not assume 16GB + system RAM behaves like unified GPU memory.

### Configuration vs persistent data
Git tracks `compose.yaml`, Modelfiles, instructions, and exported workflow JSON. Git **does not** track downloaded weights, Docker volumes, virtual environments, images, or secrets. Plan backup/restore for each. A `docker compose down` normally retains named volumes; `down -v` destroys them.

### Intended network
For initial deployment, localhost-only port bindings: Open WebUI `127.0.0.1:3000`; Ollama `127.0.0.1:11434`. To reach the service from a Mac, use a secure SSH tunnel or managed private overlay later. Never expose an unauthenticated Ollama endpoint to the public internet.

### Learning check
Why does pushing this repository **not** back up your pulled models or chat history? Where would you look if a service updated and a model disappeared?
