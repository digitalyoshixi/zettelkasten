---
tags:
  - web
  - security
---
A way to achieve [[Remote Code Execution|RCE]] in node servers with prototype pollution by overwriting the `env` property on an object
```
Object.prototype.env
Object.prototype.NODE_OPTIONS
```
Can be used with [[Prototype Pollution Child Process Spawning]] to cause DNS lookups.