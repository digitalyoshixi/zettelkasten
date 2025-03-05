---
tags:
  - math
  - linalg
---
# Theorem
A function $S : V \to W$ has an inverse $T : W \to V$ if and only if $S$ is [[Injective Functions|Injective]] and [[Surjective Functions|Surjective]]
# Proof
### Proving $\implies$
Suppose $S : V \to W$ has an inverse $T : W \to V$
We want to show that $S$ is injective.
Suppose $S(x) = S(y)$
Apply $T$ to get
$T(S(x)) =T(S(y)) \implies x = y$ as $T$ is the inverse of $S$
We want to show that $S$ is surjective
Pick $w \in W$, we have $S(T(w)) = w$ and so $w$ is a output of $S$
Thus, we have proved $S$ is both injective and surjective
### Proving $\Longleftarrow$
Suppose  $S$ is injective and surjective
If $S(v) = w$, then we define $T(w) = v$.
Note that $T(w)$ exists and is well-defined as $$