---
tags:
  - math
  - proofs
---
If $f'(x) > 0$ then $f(x)$ is [[Strictly Increasing]].
# Theorem
Let $f$ be a diff function on an open interval $I$.
1. if $x \in I, f'(x)>0$ then $f(x)$ is increasing on $I$
2. If $x \in I, f'(x) < 0$ then $f(x)$ is decreasing on $I$
# Proof (1)
1. Assume $f'(x) > 0$
2. Then $f(x)$ is diff on $I$
3. Then $f(x)$ is cont on $I$ as [[Differentiable Implies Continuity]]
4. Let $x_{1},x_{2} \in I$ be arbitrary
5. Assume $x_{1} < x_{2}$
6. Note that $f$ is cont on $[x_{1},x_{2}]$
7. Note that $f$ is diff on $(x_{1},x_{2})$
8. Then consider $f'(x) = \frac{f(x_{2})-f(x_{1})}{x_{2}-x_{1}}$
	1. $\implies0 < \frac{f(x_{2})-f(x_{1})}{x_{2}-x_{1}}$
	2. $\implies 0 < f(x_{2})-f(x_{1})$
	3. $\implies f(x_{1}) < f(x_{2})$
As required $\square$