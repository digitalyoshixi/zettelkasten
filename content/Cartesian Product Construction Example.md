---
tags:
  - math
  - calculus
---
# Example
We have languages:
$L_{1} = \{ w \in \{ 0,1 \}^{*} : w \text{ starts with } 0 \}$
$L_{2} = \{ w \in \{ 0,1 \}^{*} : w \text{ contains } 1 \}$
We can construct [[Finite State Automata|FSA]] for both languages:
For $L_{1}$:
```mermaid
stateDiagram
[*] --> q0
q0 --> q0 : 0
q0 --> q1 : 1
q1 --> q1 : 0,1
q1 --> [*]
```
For $L_{2}$
```mermaid
stateDiagram
[*] --> r0
r0 --> r1 : 0
r1 --> r1 : 0,1
r1 --> [*]
```
We now construct the cartesian product consturction, create the sets of tuples of things

```mermaid
stateDiagram
[*] --> (q0,r0)
(q0,r0)
(q0,r1)
(q0,r2)
(q1,r0)
(q1,r1)
(q1,r2)
```
For each tuple, every item of the tuple points to the same item, for example if $q_{0} \to q_{1}$, then $(q_{0},*) \to (q_{1},*)$
So, lets construct the new FSA
```mermaid
stateDiagram
[*] --> (q0,r0)
(q0,r0) --> (q0,r1) : 0
(q0,r0) --> (q1,r2) : 1
(q0,r1) --> (q0,r1) : 0
(q0,r1) --> (q1,r1) : 1
(q0,r2) --> (q0,r2) : 0
(q0,r2) --> (q1,r2) : 1
(q1,r0) --> (q1,r1) : 0
(q1,r0) --> (q1,r2) : 1
(q1,r1) --> (q1,r1) : 0,1
(q1,r2) --> (q1,r2) : 0,1
```
Now, we make all the states that contain a terminal state, its own terminal state
```mermaid
stateDiagram
[*] --> (q0,r0)
(q0,r0) --> (q0,r1) : 0
(q0,r0) --> (q1,r2) : 1
(q0,r1) --> (q0,r1) : 0
(q0,r1) --> (q1,r1) : 1
(q0,r2) --> (q0,r2) : 0
(q0,r2) --> (q1,r2) : 1
(q1,r0) --> (q1,r1) : 0
(q1,r0) --> (q1,r2) : 1
(q1,r1) --> (q1,r1) : 0,1
(q1,r2) --> (q1,r2) : 0,1
(q0,r1) --> [*]
(q1,r0) --> [*]
(q1,r1) --> [*]
(q1,r2) --> [*]
```
