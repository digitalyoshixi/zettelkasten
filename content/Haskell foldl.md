---
tags:
  - programming
  - haskell
---
A function that takes:
- Binary function
- Identity value
- List of other values
- Applies the binary function left associative
# Type
```haskell
>>> :t foldl 
foldl :: (b -> a -> b) -> b -> [b] -> b
```