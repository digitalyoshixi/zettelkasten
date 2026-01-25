---
tags:
  - programming
  - lisp
aliases:
  - Racket let
  - Racket let*
---
```lisp
(let ([var1 expr1]
	...
	[varn exprn])
	body)
```
- Creates local variables and bind them to expression results
- [[Scope]] of these variables is in the body of the let statement
# Global Scope

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