---
tags:
  - programming
  - haskell
aliases:
  - Haskell show
---
A [[Haskell Typeclass]] used to convert values to [[Haskell String]].
# Typeclass
This typeclass allows any [[Haskell Typeclass]] that derives from `Show` to be used in `show` function.
# Function
```haskell
show :: (Show a) => a -> String
```