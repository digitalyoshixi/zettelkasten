---
tags:
  - python
aliases:
  - Python Get Environment Variables
  - Python Get env
---
# Installation
`pip install python-dotenv`
# Loading Environmental Variables
```python
# app.py
from dotenv import load_dotenv
import os
load_dotenv()
secret_key = os.getenv('SECRET_KEY')
```