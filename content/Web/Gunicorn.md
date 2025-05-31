---
tags:
  - web
---
A [[Web Server Gateway Interface]] for running [[Flask]] applications.
# Installation
- `pip install gunicorn gevent`
# Running Gateway
For [[Flask]] app written in file: `server.py`
`gunicorn -b 0.0.0.0:8000 --worker-class gevent server:app`