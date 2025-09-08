---
tags:
  - programming
  - haskell
aliases:
  - Haskell Type Constructor
---
These are specific [[Interface]] used for determining what types are allowed for a function

```haskell
square Num => a -> a
```
Specifies that the [[Generics|Generic]] `a` is of `Num` type
# Definining
```Haskell
data Colour = Red | Green | Blue
```
The specific [[Haskell data|Haskell Data Constructor]] are defined independently.