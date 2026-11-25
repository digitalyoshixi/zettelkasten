---
tags:
  - security
aliases:
  - HTTP Request Smuggling
  - HTTP Response Splitting
  - HRS
  - CRLF Injection
cssclasses:
---
Abusing [[HTTP 1.1]] and [[HTTP 2.0]] issues to change the size of each request.

![[HTTP Smuggling-20260628202927834.webp]]
![[HTTP Smuggling-20260628202910913.webp]]
# Attacks
```
/?search=test%0d%0aSet-Cookie:%20csrfKey=YOUR-KEY%3b%20SameSite=None
```
- [[CRLF Injection CSRF Example]]
- [[HTTP Smuggling Content Length Transfer Encoding]]
- [[Content Length 0 Desync]]
- [[Expect Header Desync Attack]]