---
tags:
  - lisp
---
LISP is very expressive when it comes to documentation
# Program Comment
```lisp
;;;; Describe Program
```
# Stand-Alone Line Comment
```lisp
(atom 2.22)
;;; Comment that takes its own line
(atom 2.23)
```
# Indented Comment
```lisp
(defun hello-world ()
  ;; My indented comment
  (print "hello world!"))
```
# After-Line Comment
```lisp
(atom 2.15) ; my after-line comment
```
# Multiline Comment
```lisp
#!!
Multiline
comment
!!#
```