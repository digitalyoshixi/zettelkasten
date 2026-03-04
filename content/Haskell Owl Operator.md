---
tags:
  - programming
  - haskell
---
A method to write [[Pointfree]] code where you require multiple arguments.
```haskell
(.) . (.)
```
# Example
```haskell
dotProduct v1 v2 = sum $ zipWith (*) v1 v2
dotProduct = (sum .) . zipWith (*)
```