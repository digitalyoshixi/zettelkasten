---
tags:
  - math
  - programming
---
# Example
```mermaid
stateDiagram
[*] --> q0
q0 --> q1 : 1
q0 --> q0 : 0,1
q1 --> q2 : 0
q2 --> [*]
```
# Table
We lay out the node and the transitions

|                             | 0             | 1                   |
| --------------------------- | ------------- | ------------------- |
| $\emptyset$                 | $\emptyset$   | $\emptyset$         |
| $\{ q_{0} \}$               | $\{ q_{0} \}$ | $\{ q_{0},q_{1} \}$ |
| $\{ q_{1} \}$               | $\{ q_{2} \}$ | $\emptyset$         |
| $\{ q_{2} \}$               | $\emptyset$   | $\emptyset$         |
| $\{ q_{0}, q_{1} \}$        |               |                     |
| $\{ q_{1}, q_{2} \}$<br>    |               |                     |
| $\{ q_{0}, q_{2} \}$        |               |                     |
| $\{ q_{1}, q_{2}, q_{3} \}$ |               |                     |

