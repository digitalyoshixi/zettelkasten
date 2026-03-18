---
tags:
  - programming
  - haskell
aliases:
  - "Haskell :"
  - Haskell Prepend
---
```haskell
> "a" : ["b", "c"]
["a", "b", "c"]
```
# Haskell Function With Colons
```haskell
composeAll :: [(a -> a)] -> (a->a)
composeAll [] = \x -> x
composeAll (f:fs) = f . composeAll $ fs
```