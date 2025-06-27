---
tags:
  - math
  - linalg
aliases: []
---
# Definition
1. With $W$ as a [[Subspace]] of a [[Inner Product Space]] $V$
2. With [[Vector]] $\beta \in V$
3. The best approximation to $\beta$ by vectors $V$ is the vector $\alpha \in W$ such that $|| \beta - \alpha || <+ || \beta - \gamma ||, \forall \gamma \in W$ 
### Alternate Definitions
- $|| \beta - \alpha || = min_{\forall \gamma \in W} ||\beta - \gamma ||$
- $d(\beta, \alpha) = min_{\forall \gamma \in W}d(\beta, \gamma)$
- The [[Orthogonal Projection]] of vector $\beta$ onto the [[Subspace]] $W$, is the same as the best approximation
# Formula
If $W$ is in finite dimension, and $\{ \alpha_{1}, \dots, \alpha_{n} \}$ is any [[Orthogonal Set|Orthogonal Basis]] for $W$. Then,
$\alpha = \sum_{i=1}^{n} \frac{ \langle \alpha | \alpha_{k} \rangle}{ || \alpha_{k} || ^{2}} \cdot \alpha_{k}$
# Theorems
- [[Best Approximations are Characterized by Orthogonality]]
- [[Best Approximations Computed from Formula]]
- [[Best Approximations are Unique]]