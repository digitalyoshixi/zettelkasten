---
tags:
  - security
  - web
---
A vulnerability against [[Javascript Prototype]] that allows you to add arbitrary properties to `Object` to be automatically be inherited by children [[Javascript Object]]. 
If a child uses this property somewhere dangerously, it can execute any code.

```javascript
`{ existingProperty1: 'foo', existingProperty2: 'bar', __proto__: { evilProperty: 'payload' } }`
```
# Requirement
- Source to insert new fields (URL, Json input, Web messages)
- Sink to abuse new properties (document.write, innerHTML, eval, outerHTML)
- Gadget that allows unsage usage
# Tools
- [[DOM Invader]]