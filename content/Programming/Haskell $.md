---
tags:
  - programming
  - haskell
aliases:
  - Haskell Application Operator
---
```haskell
($) :: (a->b) -> a -> b
```
Applies a function to an argument, but evaluated right-to-left
- Right associative
- Low precedence
Think about the `$` as putting brackets around everything to the right
# Example
```haskell
-- Instead of:
print (show (1 + 2))

-- You can write:
print $ show $ 1 + 2
```