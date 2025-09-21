---
tags:
  - programming
  - haskell
---
A [[Haskell]] [[Higher Order Function]] that takes a verifying function and a list of elements, and returns all elements that return true in the verifying function.
```haskell
filter :: (a -> Bool) -> [a] -> [a]
```
# Example
```haskell
-- return all even numbers in xs
filter even xs
```