---
tags:
  - verification
  - programming
---
Implementing [[Parametric Polymorphism]] for a function

# Example
```lean
structure PPoint (a : Type) where
	x : a
	y : a
	
def natOrigin : PPoint Nat := {x := Nat.zero, y := Nat.zero}
```
# Example Implicit Type Parameterization
- Compiler automatically figures out the type for you
```lean
def replaceX {a : Type} (point : PPoint a) (newX : a) : PPoint a := {point with x  := newX}
```
# Automatic Implicit Type Parameterization
```lean
def replaceX (point : PPoint a) (newX : a) : PPoint a := {point with x  := newX}
```
- You don't need to write down implicit types if it has never been defined before