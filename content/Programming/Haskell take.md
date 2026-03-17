---
tags:
  - programming
  - haskell
---
```haskell
take n [...]
```
Takes the first `n` items from the list.
# Example
![[Haskell take-20250908151247544.webp]]
# [[Lazy Evaluation]] Example
```haskell
> ones = 1 : ones
> tenOnes = take 10 ones
[1,1,1,1,1,1,1,1,1,1]
```
# Formal Implementation
```haskell
take _ [] = []
take 0 _ = []
take n (x:xs) = x : take (n-1) xs
```