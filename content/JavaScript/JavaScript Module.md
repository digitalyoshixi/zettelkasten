---
tags:
  - node
  - javascript
---
A 'library' of predefined methods and classes.
Can be imported with `require()`, `import` and created with `export`
![[JavaScript Module-20240917125222000.webp]]
# Making Own Module
1. Make a file `my-module.js` and write:
```js
module.exports = {
	science : "COOL"
}
```
3. In `index.js`, write:
```js
const myModule = require('./my-module.js')

```
# Module Package Manager
- [[npm]]