---
tags:
  - programming
  - haskell
---
A function that takes:
- Binary function
- Identity value
- List of other values
- Applies the binary function right associative
# Type
```haskell
>>> :t foldr 
foldr :: (a -> b -> b) -> b -> [a] -> b
```