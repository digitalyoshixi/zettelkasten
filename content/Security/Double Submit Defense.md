---
tags:
  - security
---
A solution to [[Cross Site Request Forgery|CSRF]] that doesn't require keeping track of CSRF on the server.

Involves duplicating the token within a cookie and request parameter.
```
POST /email/change HTTP/1.1
Host: vulnerable-website.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 68
Cookie: session=1DQGdzYbOJQzLP7460tfyiv3do7MjyPw; csrf=R8ov2YBfTYmzFyjit8o2hKBuoIjXXVpa

csrf=R8ov2YBfTYmzFyjit8o2hKBuoIjXXVpa&email=wiener@normal-user.com
```
- Can be abused if the server allows setting arbitrary cookies