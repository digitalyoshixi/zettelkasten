---
tags:
  - llvm
---
Used for accessing fields.
For example:
```llvm
%MyStruct = type {i32, {[5 x i8], i64}}

; In Rust-like syntax, this is `let v = s.1.0[4];`
%v = extractvalue %MyStruct %s, 1, 0, 4
```