---
tags:
  - programming
  - haskell
---
A [[Haskell Function]] to create a [[Haskell Type]].
Can be a [[Haskell Curried Value Constructor]]
# Example
```haskell
data Shape = Circle Float Float Float | Rectangle Float Float Float Float
> :t Circle
Circle :: Float -> Float -> Float -> Shape
```