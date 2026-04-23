---
tags:
  - programming
  - haskell
---
```haskell
x = 1 : map (+2) x
x = [x | x <- [0..], odd x]
```