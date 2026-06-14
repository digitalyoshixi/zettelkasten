---
tags:
  - programming
  - verification
---
A function to calculate the length of a [[Lean List]]
# Definition
```lean
def length (a : Type) (xs : List a) : Nat :=
	match xs with
	| List.nil => Nat.zero
	| List.cons y ys => Nat.succ (length a ys)
```
# Example
```lean
length String ["Sourdough", "bread"]
// 2
```