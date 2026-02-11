---
tags:
  - programming
  - lisp
---
Uses [[Racket call|call/cc]]
```lisp
(let (
	(my-val (call/cc
		(lambda (the-continuation)
			(display "this will be executed\n")
			(the-continuation 5)
			(display "this will not be executed\n")
		)
		
	
	))
))
```