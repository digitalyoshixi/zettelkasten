---
tags:
  - math
  - linalg
---
# Theorem
1. Let $T \in \mathcal{L}(V)$, $dim(V) < \infty$
2. Suppose $T$ is diagonalizable and $c_{1},\dots,c_{k}$ are distinct [[Eigenvector|Eigenvalues]] of $T$
3. There $\exists E_{1}, \dots, E_{k} \in \mathcal{L}(V)$ such that:
	1. $T = c_{1} E_{1} + \dots + c_{k}E_{k}$
	2. $I = E_{1} + \dots + E_{k}$ 
	3. $E_{i}E_{j} = 0, \forall i \neq j$
	4. $Ej^{2} = E_{j}, \forall j$
	5. $range(E_{i}) = ker(T -e_{i}I)$
# Proof
1. Suppose $T$ is diagonalizable with distinct [[Eigenvector|Eigenvalues]] $e_{1},\dots,e_{k}$.
2. let $W_{i}$ be the space of characteristic vectors associated with characteristic values $c_{i}$
3. As we have that $\forall e, W_{1} \oplus \dots \oplus W_{k}$
4. Let $E_{i}$ be the projections associated with the decomposion as with property 1, Then, the last 4 conditions are satisfied
### Proof of Property 1
1. We have shown that $\alpha = E \alpha_{1} + \dots +E\alpha_{k}$
2. Then, $T \alpha = T E \alpha_{1} + \dots + TE \alpha_{k}$
3. That is to say, $T = c_{1}E_{1} + \dots + c_{k}E_{k}$