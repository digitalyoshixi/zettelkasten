---
tags:
  - web
  - security
---
Abusing uses of [[defineProperty()]] by polluting [[JSON|Javascript Object]] to overwrite one of the descriptor fields if not set:
- `configurable`
- `writable`
- `value` (default value, very good to overwrite)
```js
Object.defineProperty(vulnerableObject, 'gadgetProperty', {
	configurable : false,
	writable : false
	value : ""
})
```
