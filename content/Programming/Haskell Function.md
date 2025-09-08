---
tags:
  - programming
  - haskell
---
These are operations on haskell data.
![[Haskell Function-20250908193827515.webp|495]]
You can view function signatures using [[Haskell Type|Haskell :type]]
# Types
- [[Haskell Infix Function]]
- [[Haskell Prefix Function]]
- [[Haskell Postfix Function]]
# Defined Functions
```haskell
myfunction :: Int -> Int -> Int
myfunction x y = x+x + y*2
```
# Generic Type Functions
```haskell
head :: [a] -> a
```
Allows this function to work with any datatype and return that same datatype generic
# Generic with [[Haskell Typeclass]]
```haskell
square Num => a -> a
```