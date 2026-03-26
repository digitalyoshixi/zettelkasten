---
tags:
  - programming
  - prolog
aliases:
  - Prolog Relation
  - Prolog Rule
---
A [[Conditional Statement|Implication]] rule that specifies when a rule is true
# Rules
### Conjoined Antecedents
$$
a_{1} \wedge \dots \wedge a_{n} \to c
$$
```verilog
sibling(X,Y) :- parent(P,X),parent(P,Y).
```
### Disjoint Antecedents
$$
a_{1} \vee \dots \vee a_{n} \to c
$$
```verilog
% or case
person(X) :- male(X);female(X).
% equivalent to:
% person(X) :- male(X).
% person(X) :- female(X).
```
# Functor Notation
```
isaParent(+X, ?Y)
```
- `X` is always given
- `Y` is an optional variable