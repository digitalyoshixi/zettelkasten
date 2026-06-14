---
tags:
  - verification
  - programming
---
The ability for a function to have different behavior depending on the pattern of the type.
# Example
```lean
def isZero (n : Nat) : Bool :=
	match n with
	| Nat.zero => true
	| Nat.succ k => false
```
# Example 2
```lean
def pred (n : Nat) : Nat :=
	match n with
	| Nat.zero => Nat.zero
	| Nat.succ k => k
```