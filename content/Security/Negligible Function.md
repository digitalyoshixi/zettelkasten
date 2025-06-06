---
tags:
  - math
  - cryptography
  - security
aliases:
  - Negligible
---
# Definition
A function $f:\mathbb{N}\to \mathbb{R}$, $f \in negl(\lambda)$ if:
- $\forall c \in \mathbb{Z}_{>0}$,
- $\lim_{ \lambda \to \infty }f(\lambda) * \lambda^c = 0$
### Alternate Definition
The function $\mu : \mathbb{N}\to \mathbb{R}$ defined such that $\forall c \in \mathbb{Z}^{>0}$ s.t $\exists N_{c} \in \mathbb{Z}$ s.t $\forall x > N_{c}$, $|\mu(x)| < \frac{1}{x^{c}}$
