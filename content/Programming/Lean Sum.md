---
tags:
  - verification
  - programming
---
A way to allow choice between values of two different data types
- Left injection and right injection
- uses cartesian product symbol `⊕`
# Example
```lean
inductive Sum (a : Type) (b : Type) : Type where
| inl : a -> Sum a b
| inr : b -> Sum a b
```
# Example
```lean
def PetName : Type := String ⊕ String
```