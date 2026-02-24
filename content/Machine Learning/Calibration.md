---
tags:
  - ai_safety
  - statistics
---
When classifications mean the same thing for members of different groups.
- A's given classification and B's classification scores look the same in terms of actual outcomes
# Formal Definition
A [[Score Function]] $S$ is calibrated if:
$$
\forall \text{scores }s,P(Y=1 | S=s) = s
$$
# Calibration Methods
- [[Platt Scaling]]