---
tags:
  - lisp
  - programming
---
These are variables that are defined for the entire file.
```lisp
(defparameter *myglobal* "this is my dynamic scoped variable")
(defvar *myglobal2*) ; when you dont want to assign an initial value
(print *myglobal* )
```