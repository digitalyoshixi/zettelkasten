---
tags:
  - programming
  - haskell
---
```haskell
mylast :: [a] -> a
mylast [x] = x
mylast (x:xs) = mylast xs
```