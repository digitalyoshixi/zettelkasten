---
tags:
  - programming
---
A programming convention.
- Try and reduce the number of arguments you define in custom functions
If you have a function, you can just replace the function definition with another function.
# Example
```haskell
vectorAdd :: Num a => [a] -> [a] -> [a]
vectorAdd v1 v2 = zipWith (+) v1 v2
vectorAdd = zipWith (+) -- eta reduce
```
that just calls another function, then ,
The programming standard to [[Haskell Currying|Curry]] a function if it works with constants.
