---
tags:
  - web
---
A conditional [[HTTP Request Header]] used for request optimization.
- Expects an [[Entity Tag]] value, if the server would return an [[Entity Tag]] header that equal to it, then it would instead return a simple `304 Not Changed
# Example
### Request
```
...
If-None-Match: W/"3683-IwLoHx9rejeu5pzfs+mllFidepk"
...
```
### Response
```
HTTP/2 304 Not Changed
...
```
