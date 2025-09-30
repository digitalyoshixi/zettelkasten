---
tags:
  - programming
  - haskell
---
A [[Higher Order Function]] that takes two [[Haskell List]] and a binary [[Haskell Function]] and returns a new list with that applys the binary function to every pair of elements in the two lists.
```
zipWith :: (a->b->c) -> [a] -> [b] -> [c]
```
# Example
```haskell
-- return the pair-wise sums of xs and ys
zipWith (+) xs ys 
```