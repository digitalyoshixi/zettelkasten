---
tags:
  - rust
---
This is an operator that allows for the value to be returned if no errors, or none if there is an error.

`let s = str::from_utf8([240,159,141,137])?;`

The operator is equivalent to this match statement
![[Rust ?-20241201061325158.webp]]