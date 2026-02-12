---
tags:
  - programming
  - math
---
# Example
Given
```lisp
(define (len lst)
	(if (empty? lst)
		0
		(+ 1 (len (rest lst)))
	)
)
(define (append lst1 lst2)
	(if (empty? lst1)
		lst2
		(cons (first lst1)
				(append (rest lst1) lst2)	
		)
	)
)
```
We prove via [[Proof by Structural Induction]]
### Proof
1. Define axioms
	1. `lst = ()` or a cons of a list
2. Note that `(len '()) = 0` by lines 2-3 of code
3. `(len`