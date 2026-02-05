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
(define (my-length-cps xs)
	(local
		[(define (len-cps xs k)
		42)]
	(len-cps xs )
	
	)

)
```