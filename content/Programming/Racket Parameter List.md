---
tags:
  - programming
  - lisp
---
```lisp
(define list-args (lambda varparam varparam))
```
Binding a formal parameter to a list of actual parameters for unbounded parametered functions
# Example
```
(define sum-non1-args (lambda (p . ps) (apply + ps) ))

(sum-non1-args ) ==> Error, requires atleast one argument (we are not using it)
(sum-non1-args 1) ==> 0
(sum-non1-args 1 2) ==> 2
(sum-non1-args 1 2 3) ==> 5
```