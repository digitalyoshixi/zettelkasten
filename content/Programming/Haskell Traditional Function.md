---
tags:
  - programming
  - haskell
---
This is a Haskell function that takes in an input as a [[Haskell Tuple]].
```haskell
f :: Num => (a,a,a) -> a
```
Cannot be [[Haskell Currying|Curried]] unless you use the built-in [[Haskell Currying|curry]] method.
