---
tags:
  - programming
  - javascript
aliases:
  - Object.freeze()
---
A way to combat [[Prototype Pollution]] by freezing properties on an object.
- Prevents all modifications to that object
```
Object.freeze(Object.prototype)
```
- Prevents changes to the object's prototype