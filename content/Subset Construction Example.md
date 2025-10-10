---
tags:
  - programming
  - math
---
```mermaid
stateDiagram
[*] --> q0
q0 --> q1 : 0
q0 --> q0 : 0
q1 --> q2 : 1
q2 --> q0 : 1, eps
q2 --> [*]
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
3. Then, for $q_{0}$, point to the set of all transitionable states and all [[Dead State]] 
```mermaid
stateDiagram-v2
emptyset
M --> q0
q0 --> q0,q1 : 0
q0 --> emptyset : 1
q1
q2
q1,q2
q0,q2
q0,q1,q2
```
4. Define the transitions for the dead state
```mermaid
stateDiagram-v2
emptyset --> emptyset : 0,1
M --> q0
q0 --> q0,q1 : 0
q0 --> emptyset : 1
q1
q2
q1,q2
q0,q2
q0,q1,q2
```
5. Continue for subsequent states
```mermaid
stateDiagram-v2
emptyset --> emptyset : 0,1
M --> q0
q0 --> q0,q1 : 0
q0 --> emptyset : 1
q0,q1 --> q0,q1 : 0
q0,q1 --> q0,q2 : 1
q0,q2 --> q0,q1 : 0
q0,q2 --> q0 : 1
q1
q2
q1,q2
q0,q2
q0,q1,q2
```
Now, we can draw [[Deterministic Finite Automaton|DFSA]] like:
```mermaid
stateDiagram
[*] --> A
A --> B : 0
B --> B : 0
B --> C : 1
C --> B : 0
C --> A : 1
C --> [*]
```
