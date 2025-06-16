---
tags:
  - go
  - reverse_engineering
---
Golang's compiler will blindly reuse the stack if its not used by another compiler.

Makes decompilers storing variables quite challenging.
Its better to not follow the decompiler's variable names, and revert back to simply offsets.
