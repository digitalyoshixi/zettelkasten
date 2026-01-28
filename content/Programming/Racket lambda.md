---
tags:
  - programming
  - lisp
---
```lisp
<lambda> ::= (lambda (<arg> ...) <expr> ...)
```
A function with zero or more arguments and a body expr
# Example Definitions
```lisp
> (lambda (x y) (+ x y))
#<procedure>
> ((lambda (x y) (+ x y)) 1 2)
3
```