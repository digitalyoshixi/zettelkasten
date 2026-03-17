---
tags:
  - programming
  - haskell
aliases:
  - Haskell Data Constructor
  - Haskell User Defined Datatype
  - Haskell Type Cosntructor
---
A keyword used to define a new [[Haskell Type|Haskell Datatype]].
Involves a:
- [[Haskell Typeclass]] constructor `Typectr` for defining the type
- Specific [[Haskell Value Constructor]] `Valctr` which is a [[Haskell Function]] to create a value of the type
- A collection of components/fields with varying datatypes
```haskell
data Typectr = Valctr Datatype1 Datatype2 ...
```
# Example
```haskell
data BookInfo = Book Int String [String]
				deriving (Show)
```
- [[Haskell Show]] allows us to use the [[Haskell Show|Haskell show]] function to get a string representation