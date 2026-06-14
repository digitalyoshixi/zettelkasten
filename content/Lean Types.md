---
tags:
  - verification
  - programming
---
The type system is very robust.
- Every [[Lean Evaluation|Lean Expression]] must have a [[Type]]
# Primative
- `Nat` : Natural numbers, no upper limit, negatives round up to 0
- `Int` : Signed numbers
- `String` : Series of characters, unbounded length
- `Float` : [[Floating Point Numbers]]
# Type Aliasing
```lean
abbrev MyType : Type := OrigType
```
```lean
abbrev N : Type := Nat
```
