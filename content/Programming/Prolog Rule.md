---
tags:
  - programming
  - prolog
aliases:
  - Prolog Relation
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
# Function Notation
```
isaParent(+X, ?Y)
```
- `X` is always given
- `Y` is an optional variable
