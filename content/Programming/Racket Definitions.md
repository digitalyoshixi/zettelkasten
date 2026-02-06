---
tags:
  - programming
  - lisp
aliases:
  - Racket Variable
  - Racket defn
  - Racket local
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
# Local Definitions
Defining in a local space like [[Racket Scope|Racket let]]
```lisp
(define (multiples-of n ilist)
    (local
        [;; (is-mult? m) produces true if m is a multiple of n,
         ;; and false otherwise
         ;; is-mult?: Int -> Bool
         (define (is-mult? m)
            (zero? (remainder m n)))]
        (filter is-mult? ilist)))
```