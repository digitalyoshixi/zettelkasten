---
tags:
  - programming
  - python
---
# Installation
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```
# Creation
```
uv init --python 3.12 .
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
uv sync
```
# Add Packages
```
uv add requests
```