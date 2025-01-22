---
tags:
  - llvm
---
Typecasting non-aggregate type (integers, vectors) into any other type of the same bit-width.
```llvm
%bits = bitcast double %fp to i64
```