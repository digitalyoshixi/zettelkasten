---
tags:
  - math
  - linalg
---
# Theorem
1. With $V$ as a vector space, and $d$ a [[Nice Metric]]
	1. This means $\lambda \in \mathbb{F} \implies d(\lambda x, \lambda y) = |\lambda|d(x,y)$
	2. This means $x \in V \implies d(x+z,y+z)\leq d(x,y)$
2. Then, $||x|| = d(x,0)$ is a [[Norm]] for $V$
# Proof
### Showing $||x|| \geq 0$
1. Let $x \in V$
2. Then, $||x||=d(x,0) \geq0$
### Showing $||x|| = 0 \Longleftrightarrow x = 0$
1. Let $x \in V$
2. Then, $||x|| = 0 \Longleftrightarrow d(x,0) = 0 \Longleftrightarrow \lambda = 0$
### Showing $||\lambda x|| + ||\lambda|| * ||x||$
1. Let $\lambda \in \mathbb{F}$
2. Let $x \in V$
3. Then, $|| \lambda x || = d(\lambda x, 0)$
4. $= d(\lambda x, \lambda 0) = |\lambda| d(x,0)$ by nice metric property
5. $=|\lambda| * ||x||$
### Showing $||x+y|| \leq ||x||+||y||$
1. Let $x,y \in V$
2. $||x + y|| = d(x+y, 0)$
3. $=d(x+y-y, -y)$ by adding $-y$ to both terms, assuming this is allowed
4. $\leq d(x,0) + d(0,-y)$
5. $\leq d(x,0) + d(y,y-y)$
6. $\leq d(x,0) + d(y,0)$ (Note we could also use $|\lambda| |y|$ symmetry)
7. $\leq d(x,0) + d(y,0)$
8. $\leq ||x|| + ||y||$