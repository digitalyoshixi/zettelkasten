---
tags:
  - math
  - linalg
---
# Theorem
- If $T : U \to V$ is linear
- If $S : V \to W$ is linear
- Then $ST : U \to W$ is also linear
# Proof
1. Suppose $T$ and $S$ are both linear
2. Suppose the composition $ST : U \to W$ is defined
3. Pick $x,y \in U$ and $a,b, \in \mathbb{F}$
4. We calculate:
	1. $ST(ax + by)$
	2. $= S(aT(x) + bT(y))$
	3. $= aS(T(x)) + bS(T(x))$a
	4. ...