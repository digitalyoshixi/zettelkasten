---
tags:
  - math
  - linalg
---
Every finite dimensional vector space can be written as a direct sum of cyclic invariant subspaces.
# Theorem
- Let $T \in \mathcal{L}(V)$
- Let $f(x) = p_{1}(x)^{d_{1}} \dots p_{k}(T)^{d_{k}}$ be the characteristic polynomial
- Let $p(x) = p_{1}(x)^{r_{1}} \dots p_{k}(x)^{r_{k}}$ be the minimal polynomial
Then, there exists $\alpha_{1},\dots,\alpha_{j}$ such that:
1. $V = Z(\alpha_{1} T) \oplus \dots \oplus Z(\alpha_{j}T)$
2. $p = p_{1}$
3. $p_{i}$ divides $p_{i-1}$ for all $i \in \{ 2,\dots,j \}$
Where $p_{j}$ is the minimal polynomial of $Z(\alpha_{j}T)$
Note that by construction, $f = p_{1}p_{2} \dots p_{j}$
# Theorems
- [[Cyclic Decomposition Theorem Lemma]]
# Concepts
- [[Permutation Orbit]]