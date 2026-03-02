---
tags:
  - programming
  - haskell
aliases:
  - Haskell GADT
  - First Class Phantom Type
  - Generalized Algebraic Datatype
  - GADT
  - Equality Unified Type
  - Guarded Recursive Type
---
This is a combination of multiple types you can choose in [[Haskell]].
```haskell
data Expr a where
    EBool  :: Bool     -> Expr Bool
    EInt   :: Int      -> Expr Int
    EEqual :: Expr Int -> Expr Int  -> Expr Bool
```