---
tags:
  - programming
  - javascript
---
A function passed as an argument to another function that is called after the function finishes executing.
Similar to [[Continuation]]. *When you're done, call this next*
- Reading files
- Network requests
- Interacting with databases
# Example
```javascript

sum(2,3,displayConsole);

function sum(x, y, callback){
	let result = x+y;
	callback(result);
}

function displayConsole(result){
	console.log(result);
}

```