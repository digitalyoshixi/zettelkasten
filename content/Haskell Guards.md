---
tags:
  - programming
  - haskell
---
A [[Syntactic Sugar]] for checking against a series of conditions
```haskell
sign x | x > 0 = 1 -- if
	   | x < 0 = -1 -- else-if
	   | otherwise = 0 -- else
```