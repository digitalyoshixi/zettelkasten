---
tags:
  - llvm
---
Creates a copy of the aggregate with a field changed.
```llvm
; In Rust-like syntax, this is
;   let s2 = { let mut s = s; s2.1.1 = 42; s };
%s2 = insertvalue %MyStruct %s, i64 42, 1, 1
```