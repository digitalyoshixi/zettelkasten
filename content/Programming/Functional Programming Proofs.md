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
1. Define axioms and stuff we know
	1. `lst = ()`
	2. `lst = (cons lst1 lst2)`
	3. `(len '()) = 0` by lines 2-3 of code
	4. `(len (cons X Y)) = (+ 1 (len Y))` by lines 2-4
	5. `(append '() 12) = 12`
	6. `(append (cons X Y) 12) = (cons X (append Y 12))`
	7. Assume all built-ins perform correctly
2. Want to prove `(len (append l1 l2)) = (+ (len l1) (len l2))` ([[Induction Hypothesis|IH]])
3. We want to prove this structural induction on `l1`
4. Case 1: `l1` is `'()`
	1. Then, we establish left side is equal to right side
	2. `(len (append l1 l2))`
	3. `= (len (append () l2))`
	4. `= (len l2)`
	5. `= (+ 0 (len l2))`
	6. `= (+ (len ()) (len l2))`
	7. `= (+ (len l1) (len l2))`
	8. Thus, we have shown our WTP
5. Case 2: `l1` is `(cons X Y)`
	1. Assume IH 
	2. Then, start with `(len (append l1 l2))`
	3. `= (len (append (cons X Y) 12))` by case
	4. `= (len (cons X (append Y 12)))` by 4
	5. `= (+ 1 (len (append Y 12)))` by 2
	6. `= (+ (+ (len Y) (len l2)))` by [[Induction Hypothesis|IH]]
	7. `= (+ (+ 1 (len Y) (len l2))` by arithmetic
	8. `= (+ (len (cons X Y) (len l2))`  by 2
	9. `= (+ (len l1) (len l2))` by case