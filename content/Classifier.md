---
tags:
  - math
  - statistics
---
A function that takes a [[Score Function]] and reduces it down into a discrete set of cases.
$$
C_{t}(x) = \begin{cases}
0 & \text{ if } S(x) < t\\
1 & \text{ if } S(x) \geq t
\end{cases}
$$
Where:
- $x$ is the given [[Event]] from [[Random Variable|RV]] $X$
- $S(\cdot)$ is the [[Score Function]]
- $t$ is the threshold, often determined by a [[Receiver Operating Characteristic]]
![[Classifier-20260224143744441.webp]]