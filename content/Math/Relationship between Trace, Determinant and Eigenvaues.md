---
tags:
  - math
---
# THeorem
- With $A$ as a $n \times n$ matrix in $M_{n,n}(\mathbb{C})$
- With $\lambda_{1},\dots,\lambda_{n}$ as [[Eigenvector|Eigenvalues]] for $A$ repeating the terms if there is algebraic multiplicity
Then,
1. $trace(A) = \sum_{i=1}^{n}\lambda_{i}$
2. $\det(A) = \Pi^{n}_{i=1} \lambda_{i}$
# Proof
- By [[Schur's Decomposition]], $A$ is similar to a diagonal matrix $B$.
- Then, $\det(B - \lambda I)$ is the product of the diagonal entries.
- Thus, $\forall j, \exists i$ s.t $\lambda i = b_{ij}$ and $\forall i, \exists j$ s.t $b_{ii} = \lambda_{j}$
	- Reordering the labeling allows us to say that $\lambda_{i} = b_{ii}$
- Now, we can say $trace(A) = trace(B) = \sum_{i=1}^{n}b_{ii} = \sum_{i=1}^{n}\lambda_{i}$
- Now we can say $\det(A) = \det(B) = \Pi_{i=1}^{n}b_{ii} = \Pi_{i=1}^{n}\lambda_{i}$