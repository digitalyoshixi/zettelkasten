---
tags:
  - linalg
  - math
---
Let $a \in \mathbb{R}^{2}$ be a non-zero vector.
It determines a line $L = span(a) \subset \mathbb{R}^{2}$
Consider the linear map $P_{n} : \mathbb{R}^{2} \to \mathbb{R}^{2}$ given by:
$P_{a}$ where $v \in \mathbb{R}^{2}$ constructing a perpendicular line to $L$ through $v$, this line intersects $L$ at $P_{a}(v)$

Give a formula for $P_{a}(v)$ using the inner product $\langle ., . \rangle$
![[Drawing 2025-02-07 11.38.32.excalidraw]]
This will be $P_{a} = \frac{\langle a, v \rangle}{\langle a, a \rangle} * a$
# Example
Project $(4,3)$ onto $span\{ \langle 1, 1 \rangle \}$

$P_{\langle 1, 1 \rangle}(4,3) = \frac{\langle (1,1), (4,3) \rangle}{\langle (1,1), (1,1) \rangle} * (1,1)$
$= \frac{4+3}{1+1}(1,1) = \frac{7}{2}(1,1)$