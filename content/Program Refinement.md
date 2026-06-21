---
tags:
  - programming
  - math
---
A program $P, Q$ with shared:
- [[Set]] $X$ as initial states
- [[Set]] $Y$ as final states
With program [[Function|Mapping]] represented as:
- $\sigma_{P}$ for $P$
- $\sigma_{Q}$ for $Q$
Program $Q$ is refined $P$ ($Q \sqsubset P$) if:
- $dom(\sigma_{P}) \subset dom(\sigma_{Q})$ ($Q$ has same starting states and more than $P$)
- $\forall x \in dom(\sigma_{P}), \sigma_{P}(x) = \sigma_{Q}(x)$ ($Q$ has same initial transitions as $P$)
- $\sigma_{P} \leq \sigma_{Q}$ ([[Order]] implies $Q$ terminates from at least one state from which $P$ fails to terminate)
