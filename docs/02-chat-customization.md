# Specializing chat models without wasting training effort

## Three mechanisms

| Method | Changes weights? | Best for | Common failure |
|---|---|---|---|
| System prompt / Modelfile | No | Tone, role, response shape | Can't create missing skills reliably |
| RAG (retrieval augmented generation) | No | Current private documents, factual references | Poor retrieval yields wrong context |
| LoRA / QLoRA | Yes, adapter weights | Learned behavior, specialized format/style | Overfitting / poor eval / incompatibility |

Start with *one small base model*. A Modelfile gives it a role. This is a named configuration, not a new trained model. Ollama model variants can refer to the same underlying weight blobs. The template here uses `qwen3:4b`; verify tag availability when deploying. It is a starter, not a benchmark winner.

## Experiment: design three chat types
For each, write a goal, system prompt, sample dialogue, failure cases, and scoring criteria.

1. **Everyday assistant**: helpful answers, clear uncertainty.
2. **Fiction editor**: continuity, critique, editable suggestions.
3. **Coding reviewer**: Python/SQL correctness and tests.

Before fine-tuning: build a 15–30-prompt evaluation set and compare base vs configured model. Don't evaluate only on training examples. If information changes over time, use retrieval, not fine-tuning, as the primary storage mechanism.

## Privacy / data
If building personalities based on real individuals, use their consent and treat photos/messages as private. Keep datasets outside this Git repository.
