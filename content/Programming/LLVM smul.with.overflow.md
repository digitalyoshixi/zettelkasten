---
tags:
  - llvm
---
```llvm
@llvm.smul.with.overflow.i32(i32 %x, i32 %y)
```
This function checks if a multiplication between `%x` and `%y` results in an overflow error and returns an [[Aggregates|Aggregate]] of `(i32, bool)`
# Example Utilization
```llvm
start:
  %0 = call { i32, i1 } @llvm.smul.with.overflow.i32(i32 %x, i32 %x)
  %_2.0 = extractvalue { i32, i1 } %0, 0
  %_2.1 = extractvalue { i32, i1 } %0, 1
  %1 = call i1 @llvm.expect.i1(i1 %_2.1, i1 false) ; expects false in %2.1
  br i1 %1, label %panic, label %bb1

panic:
  ; some panic function here
  unreachable
bb1:
  ; some code here
```