---
tags:
  - machine_learning
aliases:
  - KL Divergence
  - Relative Entropy
---
A general number describing the divergence between two distributions.
Often used as a [[Loss Function]]
![[Kullback-Leibler Divergence-20251010215534843.webp|307]]
# Formula
$$D_{KL} (P||Q) = \sum_{x \in X} P(x)\log(\frac{P(x)}{Q(x)})$$