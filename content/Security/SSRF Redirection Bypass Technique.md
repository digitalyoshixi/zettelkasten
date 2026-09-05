---
tags:
  - security
  - web
---
A method to trigger [[Server Side Request Forgery|SSRF]] on fields that are usually redirect-focused.
# Example
```
https://vuln.com/logout?next=[open redirect]
```