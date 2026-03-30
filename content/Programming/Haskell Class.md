---
tags:
  - programming
  - haskell
aliases:
  - Haskell Custom Typeclass
---
A method to assign [[Haskell Typeclass]] to a collection of virtual methods.
```haskell
class myClass a where
	myclass :: a -> Bool
```
# Defining Own Typeclass
```haskell
class YesNo a where
	yesno :: a -> Bool
	negate :: a -> Bool
	negate x = not (yesno x)

-- all children (instances)	inherit the methods from class
instance YesNo Integer where
	yesno 0 = False
	yesno _ = True

instance (Show a) => YesNo [a] where -- a has a type restriction example
	yesno [] = False
	yesno _ = True
```
# Examples
- [[Haskell Eq]]
- [[Haskell Show]]