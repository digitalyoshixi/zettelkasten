---
tags:
  - web
---
A [[Web Server Gateway Interface]] for running [[Flask]] applications.
# Installation
- `pip install gunicorn`
# Running Gateway
`gunicorn -b 0.0.0.0:8000 app:app`