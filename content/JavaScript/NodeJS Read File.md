---
tags:
  - javascript
  - node
---
# Blocking Version
```node
const = {readFile, readFileSync} = require('fs');
const txt = readFileSync('hello.txt', 'utf8');
console.log(txt) // fires first
console.log('do this ASAP') // fires second (must wait for the blocking function)
```
# [[NodeJS Events]] Version
```node
const = {readFile, readFileSync} = require('fs');
const txt = readFileSync('hello.txt', 'utf8');

readFile('hello.txt', 'utf8', (err, txt) -> {
	console.log(txt)
}) // fires second after the 'do this ASAP'
console.log('do this ASAP') // fires first
```
# [[NodeJS Promise]] Version
```node
const {readFile} = require('fs').promises;
const file = await readFile('hello.txt', 'utf8')
```
the promise will be fulfilled in the asynchronous await call