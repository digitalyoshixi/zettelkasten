---
tags:
  - web
  - security
---
A form of [[HTTP Parameter Pollution]] that involves APIs that take from paths.
```
GET /api/private/users/peter
```
- peter is the value of the parameter
Check for:
- [[Path Traversal]]
```
GET /api/private/users/peter/../admin
```