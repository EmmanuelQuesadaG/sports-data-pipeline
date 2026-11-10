# Setup

Environment: CachyOS (Arch-based Linux), bash.

## 1. Repository

    mkdir -p ~/projects/sports-data-pipeline
    cd ~/projects/sports-data-pipeline
    git init -b main

## 2. Git identity

    git config --global user.name "Your Name"
    git config --global user.email "you@example.com"
    git config --global init.defaultBranch main

Verify with `git config --global --list`.

## 3. Python project (uv)

      uv init --lib --python 3.13
      uv sync
'uv init --lib`
cat >> docs/SETUP.md << 'EOF'

## 3. Python project (uv)

    uv init --lib --python 3.13
    uv sync

`uv init --lib` creates `pyproject.toml`, `.python-version` and a `src/` layout. `uv sync` creates the virtual environment (`.venv`) and the lockfile (`uv.lock`).
