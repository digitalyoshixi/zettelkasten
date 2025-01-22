---
tags:
  - llvm
---
You can bring external functions into scope using the declare keyword.
```llvm
declare void @llvm.memcpy.p0.p0.i64(ptr, ptr, i64, i1)
```

# LLVM intrinsic functions
These are functions that start with `llvm.`