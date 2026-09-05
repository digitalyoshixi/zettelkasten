---
tags:
  - windows
  - verification
  - networking
  - security
---
A [[Network Fuzzer]] written as a [[Python]] library.
# Installation
```
pip install boofuzz
```
# Usage
```python
from boofuzz import *

session = Session(
	target=Target(
		connection=SocketConnection("127.0.0.1",80,proto='tcp')
		),
	)
	
	s_initialize(name="Request")
	with s_block("Request-Line"):
		s_group("Method", ['GET', 'HEAD', 'POST', 'PUT', 'DELETE'])
		s_delim(" ", name='space-1')
		s_string("/index.html", name='Request-URI')
		s_delim(" ", name='space-2')
		s_string("HTTP/1.1", name='HTTP-Version')
		s_static("\r\n", "Request-CRLF")
	session.connect(s_get("Request"))
	session.fuzz()
```