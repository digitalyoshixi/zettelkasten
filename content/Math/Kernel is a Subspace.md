---
tags:
  - math
  - linalg
---
For any linear map $T:V\to W$, the kernel $ker(T)$ is a subspace of $V$
# Proof
1. Apply [[Subspace Test]]
2. $ker(T)$ is non-empty as $\overrightarrow{0} \in ker(T)$
3. $T(c\overrightarrow{x} + \overrightarrow{y}) = cT(\overrightarrow{x}) + T(\overrightarrow{y})$
4. $= c(0w) + 0w$
5. $= 0w + 0w$
6. $= 0w$
7. Therefore, $cx+y \in ker(T)$, thus its closed under linear combinations
8. Thus, $ker(T)$ is a subspace