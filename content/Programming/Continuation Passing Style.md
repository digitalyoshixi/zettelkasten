---
tags:
  - programming
aliases:
  - CPS
---
A form of recursion that does not generate extra stack frames.
Functions do not return values, but instead direct control to a new [[Continuation|Continuation Function]], wherein the final call has the return value.

![[Continuation Passing Style-20260204143939596.webp]]
# Example 1
For factorial $n!$
```lisp
(define (fact-cps n)
	(local [(define (fcps n k)
			(if (= n 0)
				(k 1) ; k is a continuation
				(fcps (- n 1) (lambda (v) (k (* n v))))
			)
	)]
	(fcps n (lambda (x) x))
	)
)
```
# Example 2
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
; [ [ [lambda [v] [id [+ 1 v] [+ 1 0]]]]]
; [ [lambda [v] [id [+ 1 v]]] 1]
; [id [+ 1 1]]
; [id 2]
; 2
```
# Usages
- [[Function and Value Return with CPS]]
- [[Multithreading with CPS]]
- [[Exception Handling with CPS]]
- [[Logic Programming with CPS]]