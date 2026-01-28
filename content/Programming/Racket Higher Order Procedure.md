---
tags:
  - programming
  - lisp
---
These are [[Racket Procedure]] that can take procedures as input values.
# Example 1
```
(all-ok? ok? lst) -> boolean
```
- `ok?` : procedure applicable to every element of lst
- `lst` : list?
# Example 2
A procedure that returns a procedure
```lisp
(make-proc f g) -> procedure?
; return a composition f(g(x))
```