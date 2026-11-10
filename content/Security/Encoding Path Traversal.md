---
tags:
  - web
  - security
---
A way to bypass path traversal filters by using encodings
# URL Encoding
- `%2e%2e%2f`
- `%252e%252e%252f`
# UTF-8 Encoding
- `..%c0%af` (`../`)
- `..%ef%bc%8f` (`..\`)