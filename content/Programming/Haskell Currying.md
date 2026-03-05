---
tags:
  - programming
  - haskell
aliases:
  - Currying
  - Uncurring
  - curry
  - uncurry
---
The ability for [[Haskell Function]] to take portions of arguments, to define the rest of the function to work with an already supplied expression.
# Example
![[Haskell Currying-20250908194445398.webp]]
# Underlying Logic
```haskell
t (\x -> \y -> x + y)
```
Functions that can be curried will have the form where each function with multiple inputs returns a new function based of the next input.
# Built-in Methods
- We can curry to convert [[Tuple]] argument into seperate arguments
- We can uncurry to convert all arguments into a tuple argument
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