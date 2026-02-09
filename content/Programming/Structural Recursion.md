---
tags:
  - programming
---
If you have structure, and you use code to implement that recursion
```lisp
(define my-func
	(lambda (lst)
		(cond ((empty? lst) ... )
		(else ... (first lst) ...
					(my-func (rest lst)) ...
		)
		)	
	)
)
```