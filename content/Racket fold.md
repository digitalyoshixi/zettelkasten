---
tags:
  - programming
  - lisp
---
```lisp
(foldr op id lst)
```
- `op` : a binary [[Racket Procedure]]
- `lst` : list of arguments
- Apply `op` right associatively to elements of a `lst`
- the identity element id is always used at the end
- Return result of evaluation
```lisp
(foldl op id lst)
```
- `op` : a binary [[Racket Procedure]]
- `lst` : list of arguments
- Apply `op` left associatively to elements of a `lst`
- the identity element id is always used at the end
- Return result of evaluation
# Example
- `(foldr op id '()) => id`
- `(foldr op id '(e1 e2 ... em)) => (op e1 (op e2 (op ... (op en id))))`