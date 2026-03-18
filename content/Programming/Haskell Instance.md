---
tags:
  - haskell
---
A instance is like an [[Interface]] for a [[Haskell Typeclass]]. Inherits existing props from the [[Haskell Class]]
# Syntax
```haskell
instance TypeClass [Type] where
	function_defn_one
	function_defn_two
	...
```
# Example
```haskell
data Role = Crewmate | Impostor deriving (Show, Eq)

class Sus a where
	isSus :: a -> Bool
	isSafe :: a -> Bool
	
	isSus entity = not (isSafe entity)
	isSafe entity = not (isSus entity)

instance Sus Role where
	isSus Crewmate = False
	isSus Impostor = True

instance YesNo instance where
	yesno 0 = False
	yesno _ = True
```