---
tags:
  - programming
  - compilers
---
A [[Compiler Optimization]] that directly moves memory to register, removing all the useless [[LLVM alloca]] and [[LLVM store]] with direct register manipulations instead.

```
define i32 @f(i32, i32) #0 {
	%3 = add nsw i32 %1, %0
	ret i32 %3
}
```