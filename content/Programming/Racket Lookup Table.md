---
tags:
  - programming
  - lisp
---
Alternative to [[Racket Hash Table]]
```lisp
(define simplifiers
  (list (cons 'and and-simplifier)
        (cons 'or or-simplifier)
        (cons 'not not-simplifier)
        (cons 'implies implies-simplifier)
        ))
```
- Associates `and` to `and-simplifier`