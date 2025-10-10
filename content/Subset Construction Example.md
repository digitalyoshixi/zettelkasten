---
tags:
  - programming
  - math
---
```mermaid
stateDiagram-v2
M --> q0
q0 --> q1 : 0
q0 --> q0 : 0
q1 --> q2 : 1
q2 --> q0 : 1, eps
```
# Conversion to [[Deterministic Finite Automaton|DFSA]] with [[Subset Construction]]

1. Write out all the possible sets of states
```mermaid
stateDiagram-v2
emptyset
q0
q1
q2
q1,q2
q0,q2
q0,q1
q0,q1,q2
```
2. 
Then, denote the starting state
```mermaid
stateDiagram-v2
emptyset
M --> q0
q1
q2
q1,q2
q0,q2
q0,q1
q0,q1,q2
```
3. Then, for $q_{0}$, point to t