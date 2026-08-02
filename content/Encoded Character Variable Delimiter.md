---
tags:
  - web
  - security
---
The delimiter for url parameters in:
- [[OpenLiteSpeed]] Server
- [[Akamai]] Cache
- [[Fastly]] Cache
```
/profile%00foo.js
```
- `%00` is the delimiter
# Dont Use Characters
These are parsed by browser, do not register these as API delimiters:
- `{`
- `}`
- `<`
- `>`
- `#`