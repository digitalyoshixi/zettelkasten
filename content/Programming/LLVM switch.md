---
tags:
  - llvm
---
### `switch <datatype> %value, label %default`
```c
switch i32 %value, label %default [
	i32 0, label %if_zero,
	i32 1, label %if_one,
	;etc
]
```