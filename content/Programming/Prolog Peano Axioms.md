---
tags:
  - programming
  - prolog
---
```verilog
% nat(?X) iff X is a natural number represented as above.
nat(zero).
nat(s(X)) :- nat(X).

% sum(+X, +Y, ?Z) iff Z is the sum of X and Y
sum(X,zero,X).
sum(X,s(Y),s(Z)) :- sum(X, Y, Z).

% prod(+X, +Y, ?Z) iff Z is the product of X and Y.
prod(X,zero,zero).
prod(X,s(zero),X).
prod(X,s(Y),Z) :- prod(X, Y, W), sum(X, W, Z).
```