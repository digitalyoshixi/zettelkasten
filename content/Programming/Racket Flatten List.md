---
tags:
  - programming
  - lisp
---
```racket
(define (my-flatten xs) 
  (cond
    [(empty? xs) '()]
    [(list? (first xs)) (append (my-flatten (first xs)) (my-flatten (rest xs)))]
    [else (append (list (first xs)) (my-flatten (rest xs)))]
    )
  )
```