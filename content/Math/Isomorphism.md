---
tags:
  - math
  - linalg
aliases:
  - Same Shape Matrix
  - Isomorphic
---
A function $T : V \to W$ is an isomorphism if:
- [[Injective Functions|Injective]]
- [[Surjective Functions|Surjective]]
# Isomorphism
If $V,W$ are isomorphic, then there exists an isomorphism $T :V \to W$
### Formal Definition
A linear transformation $T : V\to W$ is an isomorphism $\Longleftrightarrow$
$T$ is [[Injective Functions|Injective]] and $T$ is [[Surjective Functions|Surjective]].
### Formal Definition for $T : \mathbb{R}^{2} \to \mathbb{R}^{2}$
A function $T :\mathbb{R}^{2} \to \mathbb{R}^2$ is isomorphic if it sends the unit square to a paralellogram with non-zero signed area.
$[0,1] \times [0, 1] = \{ ae_{1} +be_{2} : a, b \in[0,1] \}$
![[Isomorphism-20250314211141205.webp]]
# Proving Isomorphism
### Example
Prove $M_{2 \times 2}(\mathbb{R}) \to \mathbb{R}^{4}$ is isomorphic
1. Consider $T : M_{2 \times 2}(\mathbb{R}) \to \mathbb{R}^{4}$  as $T([a b c d]) = (a,b,c,d)$
2. Note that $T$ is a linear map
3. Moreover, it is surjective and injective
4. Therefore, it is an isomorphism by definition
### Example 2
Prove $P_3(\mathbb{R}) \to \mathbb{R}^{4}$ is isomorphic
1. Consider $S(ax^{3} + bx^{2} + cx + d) = (a,b,c,d)$
2. Note $S$ is linear, injective and surjective
3. Therefore $T$ is an isomorphism by definition