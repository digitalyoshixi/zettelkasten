---
tags:
  - programming
  - haskell
aliases:
  - Currying
  - Uncurring
---
The ability for [[Haskell Function]] to take portions of arguments, to define the rest of the function to work with an already supplied expression.
# Example
![[Haskell Currying-20250908194445398.webp]]
# Built-in Methods
```haskell
curry :: ((a,b) -> c) -> a -> b -> c
member :: Eq t => (t, [t]) -> Bool
>>> curry member
curry member :: Eq t => t -> [t] -> Bool
```
```haskell
uncurry :: (a->b->c) -> (a,b) -> c
sum' :: Num a => a -> a -> a
>>> uncurry sum'
uncurry sum' :: Num c => (c, c) -> c
```