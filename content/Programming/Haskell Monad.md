---
tags:
  - programming
  - haskell
---
A [[Haskell Typeclass]] used to return:
- data
- control data (Like success, fail, IO state, etc)
```haskell
class Monad m where
  (>>=)  :: m a -> (  a -> m b) -> m b
  (>>)   :: m a ->  m b         -> m b
  return ::   a                 -> m a
```