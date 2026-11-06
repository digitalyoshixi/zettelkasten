---
tags:
  - web
  - security
---
A blind [[SQL Injection|SQLI]] exploit that involves returning verbose error messages that include useful data. 
# Typecasting Verbose errors
```
CAST((SELECT password FROM users) AS int)
```
