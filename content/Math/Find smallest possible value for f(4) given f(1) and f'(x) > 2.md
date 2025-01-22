---
tags:
  - math
  - calculus
---
Suppose $f(1) = 10$ and $f'(x) \geq 2$ for all $x \in R$. Determine the smallest possible value for $f(4)$.
# Proof
1. Note that $f$ is differentiable as $f'(x) \geq 2$
2. Note that $f$ is continuous as $f$ is differentiable
3. Then by [[Mean Value Theorem|MVT]], there exists a $c \in (1,4)$ such that $f'(c) = \frac{f(4) - f(1)}{4 - 1}$
4. $\frac{1}{3}(f(4) - 10) = f'(c) \geq 2$                           as $f'(x) \geq 2$ for all $x \in R$
5. $f(4) \geq 16$