---
tags:
  - math
  - linalg
aliases:
  - Injective Surjective Invertable
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
- For this $T(w) = v$ to exist, it needs to be well defined. 
	- Note $T$ is defined for all $w \in W$ as every $w \in W$ is an output of $S$ ($T(w) = v$ for all $w \in W$) by [[Surjective Functions|Surjectivity]]
	- Note that $T$ is a function because every $w \in W$ is the output of a UNIQUE $v \in V$. If we had $S(v_{1}) = S(v_{2}) = w \implies v_{1} = v_{2}$ by [[Injective Functions|Injectivity]] of $S$
- Therefore, $T$ is well defined for all $w \in W$ and $T(w)$ is unique for each $w \in W$
Check that $T(w)$ is the inverse
- $T(S(v)) = T(w) = v$
- $S(T(w)) = S(v) = w$
Thus, $T(w)$ is the inverse of $S$ by defn of inverse