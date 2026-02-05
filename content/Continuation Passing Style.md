---
tags:
  - programming
aliases:
  - CPS
---
A form of recursion that does not generate extra stack frames.
Functions do not return values, but instead pass control to a [[Continuation]].
![[Continuation Passing Style-20260204143939596.webp]]
# Example
For a given function
```lisp
(define (my-length-cps xs) ; return length[xs]
	(local
		[(define (len-cps xs k) ; return k[length[xs]]  - k is a function
		(if (empty? xs)
			; [k 0] = k [lenth[empty]] = k[length[xs]]
			(k 0)	 ; identity
			; [ (lambda (v) (k (+ 1 v))) [length [rest xs]]]
			(len-cps (rest xs) (lambda (v) (k (+ 1 v) )))
		)
		)]
	(len-cps xs (lambda (v) v)) ; identity function passed in
	)
)
```
The call trace could look like:
```lisp
; [len '[1 2] id]
; [len '[2] [ lambda [v] [id [+ 1 v]]]]
; [len '[] [lambda [v2] [ [lambda [v] [id [+ 1 v]]] [+ 1 v2]]]]
; [lambda [v2] [ [lambda [v] [id [+ 1 v]]] [+ 1 v2]]] 0]
; [ [ [lambda [v] [i]]]]
```