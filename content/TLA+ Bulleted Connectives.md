---
tags:
  - verification
---
A [[Syntactic Sugar]] for grouping multiple of the **same** logical connectives for expressions together without requiring brackets.
```
/\ pc = "start"
/\ i' \in 0..1000
/\ pc' = "middle"
```
Equivalent to:
```tla
( pc = "start"
/\ i' \in 0..1000
/\ pc' = "middle" )
```
Is terminated once a non-and symbol is a connective:
- `\/`
