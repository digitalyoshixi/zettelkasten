---
tags:
  - programming
  - compilers
---
An implementation of [[Higher Order Function|HOF]] in [[Monkey]]
```
let twice fn(f, x){
	return f(f(x));
};
```