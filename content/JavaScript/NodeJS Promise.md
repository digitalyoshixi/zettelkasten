---
tags:
  - node
  - javascript
---
[[Asynchronous Programming|Asynchronous]] and [[Synchronous Programming|Non-Blocking]] method to write js.

# Example in [[NodeJS Read File]]
```node
const {readFile} = require('fs').promises;
const file = await readFile('hello.txt', 'utf8')
```
the promise will be fulfilled in the asynchronous await call