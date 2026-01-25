---
tags:
  - programming
  - lisp
aliases:
  - Racket let
  - Racket let*
---
# Non-reference Scope `let`
```lisp
(let ([var1 expr1]
	...
	[varn exprn])
	body)
```
- Creates local variables and bind them to expression results
- [[Scope]] of these variables is in the body of the let statement
# Back Reference Scope `let*`
```lisp
(define (sq-cube x)
	(let* ([sqr (* x x)]
		   [cube (* x sqr)]
		   (list sqr cube)
	))
)
```
- Creates local variables and bind them to expression results
- [[Scope]] of these variables is in the body of the let statement
- The variable `sqr` can be referenced
# Forward-Backward-Self Reference Scope `letrec`
```lisp
(letrec ([my-even?
			(lambda (x)
				(if (= x 0))
				#t
				(my-odd? (-x 1))
			)
		]
		[my-odd?
			(lambda (x)
				(if (= x 0))
				#f
				(my-even? (-x 1))
			)	
		]
		)
		
		(if (and (my-even? 4) (not (my-odd? 4))
			(my-odd? 5) (not (my-even? 5))
		)
		
		42
		0
		)
		)
```
- Creates local variables and bind them to expression results
- [[Scope]] of these variables is in the body of the let statement
- The variable `sqr` can be referenced before it is referenced, after it is referenced, and referenced by itself (lazily)