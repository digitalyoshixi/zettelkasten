---
tags:
  - verification
---
A [[Set]] that includes objects that can be written as constant expressions of [[Temporal Logic of Actions|TLA+]].
# Example
```
CHOOSE v \in Real : (v > 0) /\ (v^2 = 3)
{z \in Real \X Real : z[1]^2 + z[2]^2 = 1}
```