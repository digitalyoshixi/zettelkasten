---
tags:
  - programming
---
[[List Processor|LISP]]-inspired
```js
(module
	(import "math" "callback" (func $callback))
	(export "add" (func $add))
	(func $add (param $a i32) (param $b i32) (result i32)
		(local $sum i32
			(i32.add (local.get $a) (local.get $b)))
		(call $callback (local.get $sum))	
		(return (local.get $sum))
	)
)

```