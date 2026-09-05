---
tags:
  - programming
  - lisp
---
Uses [[Racket set!]]
```racket
(define n 0)
(define nn 1)
(define (ff)
    (set! nn (+ n nn))
    (set! n (- nn n))
	nn
)

(printf "~v\n" (ff)) ; 1
(printf "~v\n" (ff)) ; 2
(printf "~v\n" (ff)) ; 3
(printf "~v\n" (ff)) ; 5
```