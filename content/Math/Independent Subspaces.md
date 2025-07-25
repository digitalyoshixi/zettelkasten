---
tags:
  - math
  - linalg
aliases:
  - Mutually Exclusive Subspaces
---
# Definition
Two [[Subspace]] $S_{1}, S_{2}$ are independent if:
$S_{1} \cap S_{2} = \{ 0 \}$
# Alternate Definitions
- Let $W_{1}, \dots, W_{k}$ be subspaces of $V$. $W_{1} ,\dots, W_{k}$ are said to be independent if $\sum_{i=1}^{k}\alpha_{i} = 0$, where $\alpha_{i} \in W_{i}$, implying that $\alpha_{j} = 0, \forall j$.
- $\forall j \in \{ 1,\dots, k \}, W_{j} \cap \{ W_{1}, \dots, W_{j-1} \} = 0$
- If $\beta_{1}, \dots, \beta_{k}$ are [[Ordered Basis]] for $W_{1} ,\dots, W_{k}$, Then $\beta = \{ \beta_{1},\dots,\beta_{k} \}$ is an ordered basis for $W = W_{1} + \dots + W_{k}$. The final sum is the [[Direct Sum]] $W = W_{1} \oplus \dots \oplus W_{k}$
# Intuition
The only shared factor between them is the trivial linear combination.
