---
tags:
  - programming
  - lisp
aliases:
  - Racket Function
  - Racket Variable Length Argument Procedure
  - Racket Parameter Lists
---
A function.
Applying a procedure has the form:
```lisp
(procedure arg1 arg2 ...)
```
# Infinite Argument Procedure
```lisp
(define (function-name arg1 arg2 . rest-args-list)
	; body stuff
)
```