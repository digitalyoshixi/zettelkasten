---
tags:
  - programming
  - web
  - security
  - javascript
---
A way to prevent [[Prototype Pollution]] by setting the prototype of an object to null during object creation.
```js
let myObject = Object.create(null);
Object.getPrototypeOf(myObject); // null
```