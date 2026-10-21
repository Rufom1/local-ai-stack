# Git workflow: Mac to remote to desktop

## On Mac (after extracting this starter)

```bash
cd local-ai-stack-starter
git init
git add .
git commit -m "Phase 0: document local AI architecture"
git branch -M main
```

Create a **private empty** repository on GitHub/GitLab, then follow its provided instructions, for example:

```bash
git remote add origin git@github.com:YOUR_USERNAME/local-ai-stack.git
git push -u origin main
```

SSH authentication must already be configured, or use an HTTPS remote. Never paste tokens into tracked config files.

## On Windows desktop (from Ubuntu WSL, not `/mnt/c`)

```bash
mkdir -p ~/projects
cd ~/projects
git clone git@github.com:YOUR_USERNAME/local-ai-stack.git
cd local-ai-stack
cp configs/.env.example infra/chat/.env
```

Edit `infra/chat/.env` locally. It is ignored by Git. `configs/.env.example` documents the schema, but contains no private values.

## Everyday cycle

```bash
git status
git add docs/ models/ workflows/ infra/ configs/ scripts/
git commit -m "Document chat profile and evaluation"
git push
# On the other machine, before editing:
git pull --ff-only
```

Avoid tracking generated models and datasets. Use Git LFS only if you intentionally decide to version large files and understand the storage costs.

## Practice
Make a one-line edit on the Mac, push, then clone in a second Mac directory as a dry run for desktop migration.
