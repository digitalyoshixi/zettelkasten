---
tags:
  - programming
  - lisp
---
```lisp
'()
'(a b)
'(1 2 foo 3.14)
```
- Each list can be represented by a [[Racket Pair]] ([[Pair List Equivalence]])
# Create a List
```lisp
(list 2)
```
# Selectors
- `first`
- `rest`
# Value
List `(f . (arg0 ... argN))` has value `f(arg0, ... , argN)`
# Functions
- [[Racket length]]
- [[Racket list-ref]]
- [[Racket member]]