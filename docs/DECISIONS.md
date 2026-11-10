# Decisions

Short log of technical decisions and the reasoning behind them.

## 001. Repository name

`sports-data-pipeline`: descriptive, lowercase, hyphenated. It names the domain and the kind of project, and does not tie the name to a single architecture pattern.

## 002. Default branch

`main`, set globally so every new repository starts the same way.

## 003. Project and dependency management with uv

uv handles the Python version, virtual environment, dependencies and lockfile in a single tool, replacing pip, venv and requirements.txt.

## 004. src layout

Package code lives in `src/sports_data_pipeline/`, so tests always run against the installed package and not against whatever is in the working directory.
