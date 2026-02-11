---
tags:
  - programming
  - haskell
---
A clause to specify local [[Haskell Variable]].
# Example
### Original
```haskell
magnitude x y = sqrt (square x + square y)
```
### Localized Version
```haskell
magnitude = let sqMag = square x + square y in sqrt sqMag
```