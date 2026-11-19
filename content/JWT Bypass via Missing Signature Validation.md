---
tags:
  - web
  - security
---
A way to forge JWT cookies by directly modifying the JWT body. If the web server does not verify the signature, then the cookie is read directly and used.