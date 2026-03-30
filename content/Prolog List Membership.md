---
tags:
  - programming
  - prolog
---
```verilog
% member(?X,?List) iff X is an element of List
member(X,[X|_]).
member(X,[_|Tail]) :- member(X,Tail).
```
- We implement only the true things
- Prolog will automatically mark non-defined things as false