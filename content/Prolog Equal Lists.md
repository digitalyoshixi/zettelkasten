---
tags:
  - programming
---
```prolog
% equal_lists(X,Y) iff X and Y are the same list
equal_lists([],[]).
equal_lists([X|Xs], [Y|Ys]) :- X = Y, equal_lists(Xs,Ys).
```