---
tags:
  - programming
  - lisp
---
A function to extend two [[Racket List]] together
```lisp
> (append '(1 2 3) '(4 5))
'(1 2 3 4 5)
```
# Implementation via [[Racket fold]]
```lisp
(append '(1 2 3 4) '(5 6 7))
=> (foldr cons '(5 6 7) '(1 2 3 4))
```