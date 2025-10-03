---
tags:
  - math
  - proofs
  - programming
---
The property for [[Regular Language]] to create new languages under functions.
# Theorem
- For a given function $f : \Sigma^{*} \to \Sigma^{*}$
- For a given [[Regular Language]] $L$
- $f(L)$ is a new [[Regular Language]]
# Proof
- Define a regex $\mathcal{R}$
- The predicate $P(\mathcal{R})$ : There exists a regex $R'$ s.t $\mathcal{L}(\mathcal{R}) = f(\mathcal{L}(\mathcal{R}))$
- Then, we proves that $P(\mathcal{R})$holds for every regex $\mathcal{R}$ using [[Proof by Structural Induction]]
- Suppose $A$ is an arbitrary [[Regular Language]]
- Then, $A = \mathcal{L}(\mathcal{R}) = f(A)$
- So, $f(A)$ is denoted by some regex, thus it is regular
# Example
- [[Insertion Language Function]]