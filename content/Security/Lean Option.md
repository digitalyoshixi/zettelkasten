---
tags:
  - programming
  - verification
---
A type used to create a type that could error and become null.
Two constructors:
- `none` : representing null value
- `some` : representing non-null value
# Example
```lean
inductive Option (a : Type) : Type where
| none : Option a
| some (val : a) : Option a
```
# Example 2
```lean
def List.head? {a : Type} (xs : List a) : Option a :=
match xs with
| [] => none
| y :: _ => some y
```
- Operations that might fail have suffixes `?`
- Operations that might crash have suffixes `!`
