---
tags:
  - compiling
---
A undefined behavior value that takes on every value at once.
These are usually garbage values that are returned at undefined behavior.

Doing operations with poison values like dereferencing it, [[LLVM br]], [[LLVM select]], [[LLVM phi]] will also result in [[Undefined Behaviors]]

# Examples that lead the poison values
- [[C]] signed overflow
- [[Low Level Virtual Machine|LLVM]] `add nsw` (adding no signed wrap)
- floating point operations marked with `nnan` and `ninf`
- [[LLVM getelementptr|LLVM GEP]] with out-of-bounds
- [[LLVM udiv]] without zero remainder like 5 / 2

