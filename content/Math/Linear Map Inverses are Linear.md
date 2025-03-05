---
tags:
  - math
  - proofs
---
# Theorem
If a linear transformation $S : V \to W$ has an inverse $T : W \to V$, then $T$ is linear
# Proof
- Assume that $S$ is linear and $T$ is its inverse
- Then, apply the linearity test for $T$
- Pick arbitrary $x, y \in W$
- Pick arbitrary $c \in \mathbb{F}$
- Then, consider $T(cx + y)$
- Note that since $S$ is [[Surjective Functions|Surjective]], and since $x,y \in W$, $x,y$ can be rewritten in terms of $S$
- $x = S(v_{1})$
- $y = S(v_{2})$
- Then, we get $T(cS(v_{1}) + S(v_{2}))$
- Note that $S$ is linear, so we can apply linearity properties
- $= T(S(cv_{1}+v_{2}))$
- Note that the two are inverses, so they undo eachother
- $= cv_{1} + v_{2}$
- $= cT(x) + T(y)$ by definition of $T$
- Therefore, $T$ is a linear map by linearity test