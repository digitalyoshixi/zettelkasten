---
tags:
  - javascript
---
# General Datatypes
```ts
type MyList = [number, string, boolean]

const arr : MyList = [1,'two',false]
```
# Optional Data

```ts
type MyList = [number?, string?, boolean?]

const arr : MyList = []
arr.push(1)
arr.push("hello")
arr.push(false)
```