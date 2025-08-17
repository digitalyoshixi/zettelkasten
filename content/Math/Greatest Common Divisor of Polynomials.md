---
tags:
  - math
  - linalg
aliases:
  - GCD
---
# Definition
- Let $p_{1},\dots,p_{n} \in \mathbb{F}[x]$
- The $gcd(p_{1},\dots,p_{n}) = d$, A [[Monic Polynomial]] $d \in \mathbb{F}[x]$ such that:
	1. $d \in \mathbb{F}[x] \{ p_{1},\dots,p_{n} \}$ ( $= \mathbb{F}[x]p_{1} + \dots + \mathbb{F}[x]p_{n}$)
	2. $d$ divides $p_{i}, \forall i$
	3. $d$ divides every polynomial that divides $p_{i}, \forall i$ (this divisor is the greatest)

We can say that $p_{1},\dots,p_{n}$ is [[Coprime|Relatively Prime]] if $gcd(p_{1},\dots,p_{n}) = 1$