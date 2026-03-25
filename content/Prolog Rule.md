---
tags:
  - programming
  - prolog
---
A [[Conditional Statement|Implication]] rule that specifies when a rule is true
```verilog
sibling(X,Y) :- parent(P,X),parent(P,Y).
```
```verilog
% or case
person(X) :- male(X).
person(X) :- female(X).
```
# Optional Variables
```
isaParent(?X)
```
- `X` is an optional variable