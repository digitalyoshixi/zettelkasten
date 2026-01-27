---
tags:
  - programming
  - lisp
---
```lisp
<expr> ::= (cond {<expr> <expr>} [(else <expr>)])
```
Can be interpreted as:
```lisp
(cond [(cond0 expr0)
	   (cond1 expr1)
	   ...
	   (else exprN)
	  ])
```
- Evaluate `cond0`, if result is not `#f` ,evaluate `expr0`
- Otherwise, evaluate `cond1`, if result is not `#f`, ...