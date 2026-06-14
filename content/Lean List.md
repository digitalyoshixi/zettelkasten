---
tags:
  - programming
  - verification
aliases:
  - Lean cons
  - "Lean ::"
---
# Definition
```lean
inductive List (a : Type) where
| nil : List a
| cons : a -> List a -> List a
```

# Example
```lean
def primesUnder10 : List Nat := [2, 3, 5, 7]
```
# Cons
```lean
List.cons
```
Will return the prepending of list 1 and list 2
Has a shorthand:
```lean
::
```