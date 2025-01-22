---
tags:
  - javascript
  - node
aliases:
  - Blocking
---
![[Drawing 2024-09-16 20.32.50.excalidraw]]
A single thread runs the entire program.
No two tasks can run at the exact same time.
# Blocking
Code that blocks like nodeJS syncing functions will end up stalling and preventing the other code to run, while it performs its operations.
Blocking code should always be turned into [[NodeJS Events]], to make them [[Asynchronous Programming|Asynchronous]].
Example:
```node
readFile('hello.txt', 'utf8', (err, txt) -> {
	console.log(txt)
})

```
See more in [[NodeJS Read File]]
