---
tags:
  - programming
  - lisp
aliases:
  - cc
  - call-with-current-continuation
  - call/cc
---
A function that can be used to [[Reify]] a [[Racket Continuation]].
```
call f
```
- Takes unary function `f`
- Applies `f` to current continuation
When the continuation is called, it will:
- Get rid of current stack
- Replace it with the stack contained in the continuation
- Perform the return of the function using the argument to the continuation
Can be used to implement:
- [[Exception Handling]]
- non-determinism
- [[Generator]]