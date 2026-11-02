---
tags:
  - web
  - security
---
Logic errors where websites fail to validate password reset tokens.
Often from urls like:
```
http://vulnerable-website.com/reset-password?token=a0ba0d1cb3b63d13822572fcff1a241895d893f659164d4cc550b421ebdd48a8
```
- Token doesn't matter, it can be removed from the URL
- Token doesn't matter, it can be any arbitrary value
- Once token is used, it is removed from database, attempting to use it again defaults to acceptance