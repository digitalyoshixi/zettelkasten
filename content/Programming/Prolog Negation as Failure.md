---
tags:
  - programming
  - prolog
---
A feature of prolog where:
```prolog
overlap(X, Y) :- member(Z,X),member(Z,Y).
disjoint(X,Y) :- \+(overlap(X,Y)).
? - disjoint([1,2], [X,4])
false.
```
- Overlap tries to become true first, since it becomes true, then disjoint will always be false
It is hard to say when things are false.