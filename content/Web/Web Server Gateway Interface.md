---
tags:
  - web
aliases:
  - WSGI
  - ASGI
---
This is a web server interface for python apps. Inspired by [[Common Gateway Interface|CGI]]
It forwards requests to WSGI-compliant functions written in python.
# WSGI Compliant Function
```python
def app(env, start_response):
	start_response('200 OK', [('Content-Type', 'text/plain')])
	return [b'Hello, world!']
```
# ASGI Compliant Function
```python
async def app(scope, receive, send):
    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [(b'content-type', b'text/plain')],
    })
    await send({
        'type': 'http.response.body',
        'body': b'Hello, World!',
    })
```
# Synchronous WSGI
- [[Gunicorn]]
- [[uWSGI]]
- [[gevent]]
- [[Twisted Web]]
# Asynchronous WSGI
- [[Uvicorn]]
# Development WSGI
- [[Werkzeug]]