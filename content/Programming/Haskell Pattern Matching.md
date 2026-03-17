---
tags:
  - programming
  - haskell
---
The ability for the compiler to check the implementation of a function by checking against its [[Function Signature]].
Functions are checked from top to bottom.
```haskell
zeroToOne 0 = 1
zeroToOne x = x
```
# Throwaway Pattern
```haskell
(_,x,y) = (1,2,3)
```