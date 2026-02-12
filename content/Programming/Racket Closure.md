---
tags:
  - programming
  - lisp
---
A closure is a record containing:
- [[Subroutine|Function]]
- A environment
```lisp
(define (make-inc x)
	(lambda (y) (+ x y))
)
```
# Free Variables
In expression `(lambda (y) (+ x y))`, `x` is a free variable
# Examples
- [[Racket Closure Counter Example]]