---
tags:
  - programming
  - haskell
aliases:
  - Haskell Throwaway Argument
  - Haskell Optional Argument
  - Haskell Variable Arguments
  - Haskell Infinite Argument
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
# Haskell Throwaway Arguments
```haskell
implies :: Bool -> Bool -> Bool
-- throwaway second arg
implies False _ = True 
implies True False = False 
implies True True = True 
```
# Haskell Rest of Arguments
```haskell
-- call it repeatTwice'
repeatTwice' [] = []
-- first list element and then the rest of the list
repeatTwice' (x:xs) = x : x : repeatTwice' xs
```