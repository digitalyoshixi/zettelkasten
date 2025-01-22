---
tags:
  - llvm
---
Brought to scope with [[LLVM declare]].
These are functions that are llvm-exclusive to deal with error-handing and compiler optimization.
They are added to the IR by default when they are needed.

Most start with `@llvm.` and can be appended an attribute representing the datatype like `i32`
An example intrinsic is:
`declare i1 @llvm.expect.i1(i1, i1)`
# List
- [[LLVM smul.with.overflow]]
- [[LLVM expect]]