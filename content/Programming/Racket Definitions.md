---
tags:
  - programming
  - lisp
aliases:
  - Racket Variable
  - Racket defn
---
Binding a name to  a constant or function in racket.
# Constants
```lisp
(define x 3)
(define y (+ x 1))
```
# Functions
```lisp
(define (square x) (* x x))

(define (sum-of-squares x y)
	(+ (square x)
	   (square y)
	)
)
```