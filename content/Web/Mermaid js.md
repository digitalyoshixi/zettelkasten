---
tags:
  - obsidian
  - javascript
---
Mermaid js is a javascript library that allows markdown generation of diagrams like flowcharts and trees.
Obsidian natively supports mermaid.js, so we can generate diagrams very easily using code blocks.
# Tree diagrams

```mermaid
graph TD;
Start-->Y
Start-->N
Y-->YY
Y-->YN
N-->NY
N-->NN
```

# Flow charts
```mermaid
graph TD;
A(Make Bed)
B(Spend 17 hours trying to tuck the corner of the sheet in)
C(End)
D(Well what else are you going to do?)

A-->|Yes|B
B-->C
A-->|Leave|C
A-->|No|D
D-->B
```
# [[Finite State Automata|FSA]]
```mermaid
stateDiagram-v2
M --> q0
q0 --> q1 : 0
q0 --> q0 : 0
q1 --> q2 : 1
q2 --> q0 : 1, eps
```