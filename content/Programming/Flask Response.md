---
tags:
  - python
  - web
---
```python
from flask import Flask, request, make_response
app = Flask(__name__)

def hello():
	response = make_response()
	response.status_code = 202
	response.headers['content-type'] = 'application/octet-stream'
    return response
```
![[Flask Reponse-20241004035015016.webp]]