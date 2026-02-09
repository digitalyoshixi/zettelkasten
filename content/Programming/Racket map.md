---
tags:
  - programming
  - lisp
---
```lisp
(map proc '(l1 l2 ... ln))
```
- `proc` is a n-ary [[Racket Procedure]]
Applies the function proc against all the inputs `l1`, ..., `ln`
# Example
- `(map (lambda (x) (* x x) '(1 2 3))`