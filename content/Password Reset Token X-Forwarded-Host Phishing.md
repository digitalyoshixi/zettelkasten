---
tags:
  - security
  - web
---
An attack wherein the `X-Forwarded-Host` header is used in the request, the server uses it as the original domain to issue the request for.
```
X-Forwarded-Host: exploit-0ad100bb038e8346806b2598011500e7.exploit-server.
```
- This is a phishing attack, the other user must click the reset link pointing to your domain
- You must own the domain and read the access logs to find their reset token