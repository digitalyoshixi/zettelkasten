---
tags:
  - programming
  - lisp
---
```lisp
(define counter
	(let ([count 0])
		(lambda ()
			(set! count (+ count 1))
			count)
		)
	)
	
(counter) ; value is 1
(counter) ; value is 2
(counter) ; value is 3
```
# Fucked Up Example
```lisp
(define make-counter
	(let ([global-count 0])
		(lambda ()
		(let ([local-count 0])
			(lambda ()
				(set! global-count (+ global-count 1))
				(set! local-count (+ local-count 1))
				(cons global-count local-count)
			)
		)
		)
	)
)
```