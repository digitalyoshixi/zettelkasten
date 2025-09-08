---
tags:
  - programming
  - haskell
---
A [[Haskell Function]] that returns a comparrison enum:
- `LT`
- `EQ`
- `GT`
between two numbers `x,y` to see if `x > y`
```
compare x y
```
# Checking Equal
```haskell
(compare 2 2) == EQ
```