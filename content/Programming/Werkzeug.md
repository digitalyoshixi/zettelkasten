---
tags:
  - programming
  - python
  - web
---
A [[Web Server Gateway Interface]] for python
# Installation
```
pip install werkzeug redis jinja2
```
# Boilerplate
```python
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

def app(environ, start_response):
	request = Request(environ)
	text = f"Hello {request.args.get('name', 'World')}!"
	response = Response(text, mimetype='text/plain')
	return response(environ, start_response)
	
run_simple("localhost", 5000, app)
```