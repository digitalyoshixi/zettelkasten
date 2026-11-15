---
tags:
  - web
  - security
  - javascript
  - programming
---
A way to prevent [[Prototype Pollution]] by sealing an object which:
- Allows modification of existing properties
- Prevents creation of new properties
```
Object.seal(Object.prototype)
```