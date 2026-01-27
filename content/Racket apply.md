---
tags:
  - programming
  - lisp
---
```lisp
(apply op lst)
```
- `op` : a n-ary procedure
- `lst` : list of `n` arguments
- It will apply `op` to elements of `lst` and return result of evaluation
# Example
- `(apply + '(1 2 3 4)) => 10`