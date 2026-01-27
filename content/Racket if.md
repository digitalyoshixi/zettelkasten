---
tags:
  - programming
  - lisp
---
```lisp
<expr> ::= (if <expr> <expr> <expr>)
```
Can be thought of as:
```
(if condition expr0 expr1)
```
- If condition is true, then evaluate `expr0`
- If condition is false, then evaluate `expr1`