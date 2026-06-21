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
Program $Q$ is refined $P$ if:
- $dom(\sigma_{P}) \subset dom(\sigma_{Q})$ ($Q$ has same starting states and more than $P$)
- 