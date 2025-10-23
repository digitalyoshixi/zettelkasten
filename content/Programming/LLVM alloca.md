---
tags:
  - llvm
---
Used to allocate memory onto the stack, similar to [[C alloca]].
```
%variable = alloca i32
```
LLVM by default only uses the [[OS Stack]], it does not have the [[OS Heap]]