---
tags:
  - programming
  - haskell
---
A [[Haskell Typeclass]] used for numbers.
Inherits from [[Haskell Eq]]
```haskell
data Num = Int | Integer | Float
```
Requires implementing of:
- [[Haskell +]]
- [[Haskell -]]
- [[Haskell *]]
- [[Haskell negate]]
- [[Haskell abs]]
- [[Haskell signum]]