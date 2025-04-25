---
tags:
  - programming
---
An [[Expression]] that is outside of any [[Function Closures|Closures]].
```js
var myself = 20; // top-level expression. not inside any closure

function myfunction(){
	console.log("rat");
}
```
Certain languages (like [[C]]) do not allow for top-level expressions.