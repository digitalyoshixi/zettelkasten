---
tags:
  - programming
  - lisp
---
Checks for elementhood in lists
```lisp
> (member "fall" (list "hop" "skip" "jump")) ; check for elem
#f
> (member "hop" (list "hop" "skip" "jump")) ; check for elem
#t
```