---
tags:
  - verification
---
A [[Random Oracle|Oracle]] that checks if two [[Mealy Machine]] are equivalent. Often done by exhaustive testing (Like [[Model Checking]])
```
Hypothesis -> (equivalent | counterexample w)
```
# Definition
For machine $L$, hypothesis $H$,
Test if $L(H) = L$
# LearnLib
```
EquivalenceOracle<A,I,O>
```
- `A` is a automaton type
- `I` is input
- `O` is output