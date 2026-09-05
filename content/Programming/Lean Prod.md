---
tags:
  - verification
  - programming
---
A way of joining multiple values together like a [[Tuple]].
```lean
structure Prod (a : Type) (b : Type) : Type where
	fst : a
	snd : b
```
# Example
```lean
def fives : String × Int := {fst : "five", snd := 5}
// equivalently
def fives : String × Int := {"five", 5}
```