---
tags:
  - python
---
Alternative to [[pip]].
Automatically sets up virtual environments.
# Installation
`sudo pacman -S poetry`
# Setup Poetry Project
1. `poetry init`
2. `poetry add ...`
3. `poetry env info --path`
# Usage
### `poetry init`
Setup pyproject.toml file in local directory
### `poetry add`
Add a new dependency to pyproject.toml
### `poetry install`
Add all dependencies from pyproject.toml
### `poetry run python`
Runs python with poetry dependencies