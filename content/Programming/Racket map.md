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
```
>>> (map (lambda (x) (* x x) '(1 2 3))
'(1 4 9)
>>> (map + '(1 2 3) '(1 2 3))
'(2 4 6)
```
# Tail Call Implementation
```lisp
(define (custom-map f l)
	(define (map-iter l accum)
		(cond   
        [(empty? l) (accum l)]
				[else (map-iter (rest l) (lambda (x) (accum (cons (f (first l)) x))) )]
		)
	)
	(map-iter l (lambda (x) x))
)
```