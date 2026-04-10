---
tags:
  - programming
  - prolog
---
```prolog
% sum_list(X,S) iff S is the sum of elements in X
sum_list([], 0).
sum_list([X|Xs], S) :- sum_list(Xs, SS), S is SS+X.
```