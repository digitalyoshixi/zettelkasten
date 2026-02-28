---
tags:
  - security
---
A attack using [[Server Side Request Forgery|SSRF]] to obtain [[Cross Site Request Forgery|CSRF]]
# Process
1. Some subdomain `b.site.com` allows [[Server Side Request Forgery|SSRF]]
2. Some subdomain `a.site.com` allows [[Cross Origin Resource Sharing|CORS]] to enable localhost, protected against CSRF
3. Launch [[Server Side Request Forgery|SSRF]] against `b.site.com` from `a.site.com`