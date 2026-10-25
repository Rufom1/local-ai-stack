# Architecture decision log

| Decision | Baseline | Why | Revisit when |
|---|---|---|---|
| OS | Windows desktop + WSL2 Ubuntu | Preserve gaming and Linux AI tooling | Deployment or CUDA limitations |
| Chat | Ollama + Open WebUI in Docker | Simple, reversible services | Need throughput or advanced serving |
| Image | ComfyUI native in WSL2 | Custom nodes and Python environment control | Need container deployment |
| First chat customization | System instructions + evaluations | Cheapest experiment | Measured limits |
| Future GPUs | Dedicated Linux rack server | Avoid Windows V100 compatibility concerns | After benchmarking and budget review |

## Open questions
- Which specialized chat types matter most?
- Which SDXL checkpoint and license best fit intended images?
- Where are model weights stored and backed up?
- What latency/token-throughput is acceptable?
- Will remote access use SSH port forwarding or Tailscale?
