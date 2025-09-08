---
tags:
  - programming
  - haskell
---
A standard programing interface to data or control structures.
```haskell
class Monad m where
  (>>=)  :: m a -> (  a -> m b) -> m b
  (>>)   :: m a ->  m b         -> m b
  return ::   a                 -> m a
```