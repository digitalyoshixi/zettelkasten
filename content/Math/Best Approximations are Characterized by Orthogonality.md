---
tags:
  - math
  - linalg
---
# Theorem
With $W$ as a subspace of an inner product space $V$. Let $\beta \in V$. Then,
Best approximations are characterized by an orthogonality relation
# Explanation
The vector $\alpha$ is a best approximation to $\beta \in W \Longleftrightarrow \beta - \alpha$  is [[Orthogonal]] to every vector in $W$
# Proof
1. We first prove an equality that is useful. Let $\gamma \in V$, then $\beta - \gamma = (\beta - \alpha) + (\alpha - \gamma)$ and $|| \beta - \gamma || ^2 = || \beta - \alpha || ^2 + 2 Re( \langle \beta - \alpha | \alpha - \gamma \rangle ) + || \alpha - \gamma || ^2$ ($*$)
### Proving $\Longleftarrow$
Suppose $\beta - \alpha$ is orthogonal to every vector
### Proving $\implies$
- Suppose that $|| \beta - \alpha || ^2 \leq || \beta - \gamma || ^2$ for every $\gamma \in W$
- It  follows that $|| \beta - \gamma || ^2 - || \beta - \alpha || ^2 \geq 0 \implies 2Re( \langle \beta - \alpha | \alpha - \gamma \rangle + || \alpha- \gamma ||^{2} > 0$, from previous equality $(*)$
- Now, $\forall \gamma \in W$, as $\alpha \in W$, and this is true for all $\gamma \in W$, we see that every $r \in W$, $2 Re( \langle \beta - \alpha | r \rangle) + || r || ^2 \geq 0$
- If $\gamma \in W, \gamma \neq \alpha$, we may take $r = -\frac{ \langle \beta - \alpha | \alpha - \gamma \rangle}{ || \alpha - \gamma ||} \cdot \langle \alpha - \gamma \rangle$. We are subtracting the projection onto $\alpha - \gamma$
- Then, the inequality reduces to the statement $- 2 \cdot \frac{ | \langle \beta - \alpha | \alpha - \gamma \rangle | ^{2}}{ \langle \alpha - \gamma | \alpha - \gamma \rangle} ( \alpha - \gamma) + \frac{| \langle \beta - \alpha | \alpha - \gamma \rangle | ^{2}}{ \langle \alpha - \gamma | \alpha - \gamma \rangle} \geq 0$
- Then, this is equivalent to $- \frac{| \langle \beta - \alpha | \alpha - \gamma \rangle| ^{2}}{|| \alpha - \gamma || ^{2}} \geq 0$. Now, this only holds if $\langle \beta - \alpha | \alpha - \beta \rangle = 0$, so its perpendicular to every vector in $W$

