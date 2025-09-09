---
tags:
  - haskell
  - programming
---
```
flip :: (a -> b -> c) -> (b -> a -> c)
```
Flips arguments of a two argument function
# Example
```haskell
revdiv = flip div
revdiv 4 2 -- is 0
div 4 2 -- is 2
```