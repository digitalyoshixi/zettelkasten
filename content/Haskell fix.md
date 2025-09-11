---
tags:
  - programming
  - haskell
---
An implementation of a [[Y Combinator]].
```
fix :: (a -> a) -> a
```
Returns the least [[Fixed Point]] of a given function, assuming the give function takes `Number`.
This function is recursive by nature.
```
fix f = f (fix f)
```