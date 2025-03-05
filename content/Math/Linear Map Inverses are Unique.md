---
tags:
  - math
  - proofs
---
# Theorem
If function $S : V \to W$ has an inverse $T : W \to V$ then, $T$ is unique
# Proof
- Suppose $T_{1} : W\to V$ and $T_{2} : W\to V$ are both inverses of $S \to V \to W$
- Pick any $w \in W$
- We know that $S : V \to W$ is surjective and so $S(v) = w$
- $T_{1}(W) = T_{1}(S(v)) = V$
- $T_{2}(W) = T_{2}(S(v)) = V$
- Therefore, $T_{1}(W) = T_{2}(W) = V$  thus the two maps are the same