---
tags:
  - haskell
---
A instance is like an [[Interface]] for a [[Haskell Typeclass]]. Inherits existing props from the [[Haskell Class]]
```haskell
instance YesNo instance where
	yesno 0 = False
	yesno _ = True
```