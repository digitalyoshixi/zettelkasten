---
tags:
  - math
  - calculus
---
# Theorem
$Df(x) v= \nabla f \cdot v$
# Proof
1. With $f : \mathbb{R}^{k} \to \mathbb{R}$
2. With $v \in \mathbb{R}^{k}$
3. The function $h(t) = f(x+tv) = h(t)=f(c(t))$ where $c(t) = x+tv$
4. Then, $Df(x)v = \frac{d}{dx}f(x+tv) |_{t=0}$
5. $= D(f \circ c)$
6. $= \nabla f(c(t)) c'(t)$
7. $=\nabla f(c(t)) \cdot v$
8. $=\nabla f \cdot v$