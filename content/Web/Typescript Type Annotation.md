---
tags:
  - javascript
---
# Variables
```ts

let lucky : number;
lucky = 24;
// or
let lucky : number = 24;
let a : int | string;

```

# Functions
```ts
function pow(x : number, y : number) : string {
	return Math.pow(x,y).toString();
}
```
# Any Type
If you want to opt-out of the default type-checking, then do:
```js
let myvar : any;
```