---
tags:
  - security
  - web
aliases:
  - SSRF Open Redirect Technique
---
A method to trigger [[Server Side Request Forgery|SSRF]] on fields that are usually redirect-focused (`300`).
# Example
```
https://vuln.com/logout?next=[open redirect]
```