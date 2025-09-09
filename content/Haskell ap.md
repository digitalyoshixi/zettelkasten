---
tags:
  - haskell
  - programming
aliases:
  - Haskell Applicative Function
---
A function used to convert to a wrapped class into [[Haskell Applicative]] typeclass.
```
ap :: Monad m => m (a -> b) -> m a -> m b 
```
