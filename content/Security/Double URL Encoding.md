---
tags:
  - security
---
The practice of [[Percent Encoding|URL Encoding]] your payload twice to exploit servers that only URL decode once, and send to a different web server that decodes itself.
- Bypasses XSS filters
- Bypasses SSRF filters