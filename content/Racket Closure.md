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