---
tags:
  - javascript
---
Defining properties on [[JSON|Javascript Object]] that have specific access modifiers.
```js
Object.defineProperty(vulnerableObject, 'gadgetProperty', {
	configurable : false,
	writable : false,
	value : defaultvalue
})
```
- The descriptor object does not have any mandatory fields. You may be able to pollute ([[Prototype Pollution via Flawed Sanitiziation]])