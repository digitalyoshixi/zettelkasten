---
tags:
  - programming
  - haskell
---
A clause to specify local implementations of functions.
# Example
### Original
```haskell
magnitude x y = sqrt (square x + square y)
```
### Localized Version
```haskell
magnitude = sqrt sqMag where sqMag = square x + square y
```