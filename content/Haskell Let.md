---
tags:
  - programming
  - haskell
---
A clause to specify local implementations of functions.
# Example
### Original
```
magnitude x y = sqrt (square x + square y)
```
### Localized Version
```haskell
magnitude = let sqMag = square x + square y in sqrt sqMag
```