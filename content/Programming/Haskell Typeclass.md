---
tags:
  - programming
  - haskell
aliases:
  - Haskell Type Constructor
---
These are specific [[Interface]] used for determining what types are allowed for a function
- An instance of a typeclass is a [[Haskell Type]] (NOT the instance of a [[Haskell Type]])

```haskell
square Num => a -> a
```
Specifies that the [[Generics|Generic]] `a` is of `Num` type
# Definining
```Haskell
data Colour = Red | Green | Blue
```
The specific [[Haskell data|Haskell Data Constructor]] are defined independently.
# List
- [[Haskell Show]]
- [[Haskell Num]]
- [[Haskell Eq]]
- [[Haskell Ord]]
- [[Haskell Read]]
- [[Haskell Foldable]]
# Concepts
- [[Haskell Curried Type Constructor]]
- [[Haskell Class|Haskell Custom Typeclass]]