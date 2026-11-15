---
tags:
  - security
  - web
  - javascript
---
A way to get around WAF rules that block `__proto__`.
- `object.constructor.prototype` is equivalent to `object.__proto__`
```js
var myObject = {};
myObject.constructor // function Object(){...}
myObject.constructor.prototype // Object.Prototype
```
