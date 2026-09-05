---
tags:
  - programming
  - prolog
---
# Rule Mode
For rules, if a variable is defined newly in the rule, then those variables are bound existentially.
```verilog
sibling(X,Y) :- parent(P, X), parent(P,Y).
```
Expressed as:
$$
\forall X,Y, \text{sibling}(X,Y) \leftarrow \exists P, \text{parent}(P,X) \wedge \text{parent}(P,Y)
$$