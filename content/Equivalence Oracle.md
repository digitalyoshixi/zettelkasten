---
tags:
  - verification
---
A [[Random Oracle|Oracle]] that checks if two [[Mealy Machine]] are equivalent
```
Hypothesis -> (equivalent | counterexample w)
```
# LearnLib
```
EquivalenceOracle<A,I,O>
```
- `A` is a automaton type
- `I` is input
- `O` is output