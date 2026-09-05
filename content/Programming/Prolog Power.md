---
tags:
  - programming
  - prolog
---
```prolog
% power(A,B,?R) iff R is A^B
power(A,0,1).
power(A,B,R) :- B > 0, BB is B-1, power(A,BB, RR) ,R is RR*A.
```