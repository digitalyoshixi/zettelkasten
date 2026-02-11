---
tags:
  - programming
  - lisp
---
Uses [[Racket call|call/cc]] which restores previous stack and returns early.
![[Racket Early Exit-20260211044653793.webp]]
```lisp
(let (
	(my-val (call/cc
		(lambda (the-continuation)
			(display "this will be executed\n")
			(the-continuation 5)
			(display "this will not be executed\n")
		)
	))
	)
	(display my-val)
)
```