---
tags:
  - programming
  - haskell
---
A keyword used to define a new [[Haskell Type|Haskell Datatype]].
```haskell
data Typectr = Valctr Datatype1 Datatype2 ...
```
# Example
```haskell
data BookInfo = Book Int String [String]
				deriving (Show)
```