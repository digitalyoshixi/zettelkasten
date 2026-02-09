---
tags:
  - programming
  - lisp
---
# Usage
```lisp
(require test-engine/racket-tests)

(define (my-fold f id xs)
  (if (empty? xs)
      id
      (f (first xs) (my-fold f id (rest xs)))
      ) 
  )

(check-expect (my-fold * 1 '(1 2 3)) 6) ; test case

(test) ; test all above
```