#!/usr/bin/env python3
"""Offline Phase 0 template sanity checker. Does not require Docker or a GPU."""
from pathlib import Path
root = Path(__file__).resolve().parents[1]
required = ["README.md", "docs/00-roadmap.md", "docs/01-architecture.md", "docs/02-chat-customization.md", "infra/chat/compose.yaml", "models/chat/fiction-assistant.Modelfile", "configs/.env.example"]
missing = [p for p in required if not (root / p).is_file()]
if missing:
    raise SystemExit(f"Missing files: {missing}")
compose = (root / "infra/chat/compose.yaml").read_text()
assert "127.0.0.1:" in compose, "Ports should default to localhost"
assert "capabilities: [gpu]" in compose, "Compose template is missing GPU request"
assert "OLLAMA_BASE_URL: http://ollama:11434" in compose
modelfile = (root / "models/chat/fiction-assistant.Modelfile").read_text()
assert modelfile.startswith("FROM ")
try:
    import yaml
except ImportError:
    print("PyYAML not installed; skipped YAML parse. Structural checks passed.")
else:
    parsed = yaml.safe_load(compose)
    assert set(parsed['services']) == {'ollama', 'open-webui'}
    print("Structure and YAML parse passed.")
print("Phase 0 static validation complete; deployment not tested.")
