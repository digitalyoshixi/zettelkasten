---
tags:
  - math
  - security
  - cryptography
aliases:
  - LWE
---
Solving noisy systems of linear equations modulo a number.
Can be reduced to a [[Short Vector Problem]]
# LWE Problem
- For positive integers $n \in \mathbb{Z}$ and $q \geq 2$
- For secret vector $s \in \mathbb{Z}_{q}^{n}$
- For [[Probability Distribution]] $\mathcal{X}$ on $\mathbb{Z}$
Define distribution $A_{s, \mathcal{X}}$ as follows:
- Choose a vector $a$ from $\mathbb{Z}_{q}^{n}$ uniformly at random and sample a noise term $e$ from $\mathcal{X}$
- Output the pair $(a, [\langle a,s \rangle + e]_{q})$ where:
	- $\langle , \rangle$ is the [[Standard Inner Product for Vector Spaces|Inner Product]]
	- $q$ is the reduction [[Modulus|Modulo]]
# Intuition
- Messages are repesented as vectors or polynomials
- Noise is added during encryption to hide plaintext
- Difficulty in solving encrypted form depends on complexity of lattice problem