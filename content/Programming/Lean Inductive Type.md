---
tags:
  - programming
  - verification
---
# Example
```lean
inductive Bool where
	| false : Bool
	| true : Bool
```
- Defines two constructors `false` and `true`
# Example 2
```lean
inductive Nat where
	| zero : Nat
	| succ (n : Nat) : Nat
```