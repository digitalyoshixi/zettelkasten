---
tags:
  - programming
  - prolog
---
```prolog
% second_largest(L, S) if S is the second largest element of L
second_largest(L,S) :- sort(L,Ls), reverse(Ls,Lss), n_index(1,Lss, S).

n_index(0,[X|Xs], X).
n_index(N,[X|Xs], R) :-  Ns is N-1, n_index(Ns, Xs, R).
```