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

`uv init --lib` creates `pyproject.toml`, `.python-version` and a `src/` layout. `uv sync` creates the virtual environment (`.venv`) and the lockfile (`uv.lock`).
## 4. PostgreSQL (Docker)

      cp .env.example .env   # then set a real password in .env
      docker compose up -d
      docker compose ps

Requires Docker and Compose. Postgres listens on `127.0.0.1:5432~ only. Data persists in the `pgdata` volume.
