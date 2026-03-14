---
tags:
  - programming
  - haskell
---
# Single Generator
```haskell
>>> [x | x <- [1..5] ]
[1,2,3,4,5]
>>> [x^2 | x <- [1..5] ]
[1,4,9,16,25]
```
# Multiple Generator
```haskell
>>> cartesian_product = [(x,y) | x <- [1,2,3], y <- [4,5] ]
[(1,4), (1,5), (2,4), (2,5), (3,4), (3,5)]
```
# Dependent Generator
```haskell
>>> [(x,y) | x <- [1..3], y <- [x..3]]
[(1,1), (1,2), (1,3), (2,2), (2,3), (3,3)]
```
# Generator with [[Haskell Guards]]
```haskell
>>> evens_squared xs = [x^2 | x <- xs, even xs]
>>> evens_squared [1,2,3,4]
[4,16]
```