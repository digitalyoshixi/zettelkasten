---
tags:
  - security
  - web
---
A vulnerability against [[Javascript Prototype]] that allows you to add arbitrary properties to be automatically typecasted into other javascript objects.
```javascript
`{ existingProperty1: 'foo', existingProperty2: 'bar', __proto__: { evilProperty: 'payload' } }`
```