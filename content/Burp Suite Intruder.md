---
tags:
  - security
  - web
---
A tool used to automatically [[Fuzzing|Fuzz]] requests with [[Burp Suite]].
# Example Fuzz Template
```
GET /api/v1/books?show=$file$ HTTP/1.1
...
```
- `$file$` will be fuzzed with targets