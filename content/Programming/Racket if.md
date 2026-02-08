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
- If condition not `#f`, then evaluate `expr0`
- If condition is `#f`, then evaluate `expr1`