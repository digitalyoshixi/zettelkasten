---
tags:
  - programming
  - prolog
---
```prolog
% factorial(X,R?) iff R is X!
factorial(0,1).
factorial(X,R) :- X>0, XX is X-1, factorial(XX, RR), R is RR*X.
```