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

hello(goodbye);

function hello(callback){
	console.log("Hello");
	callback();
}

function goodbyte(){
	console.log("Goodbye");
}
```