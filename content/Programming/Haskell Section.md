---
tags:
  - programming
  - haskell
---
Special syntax for applying a infix operator to a single argument. Uses [[Haskell Currying]] under the hood.
```haskell
(#y)
(y#)
```
# Example
```haskell
>>> map (+2) [1,2,3]
[3,4,5]
>>> map (/2) [1,2,3]
[0.5,1,1.5]
```
