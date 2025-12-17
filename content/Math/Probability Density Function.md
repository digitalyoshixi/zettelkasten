---
tags:
  - math
  - probability
  - statistics
aliases:
  - PDF
  - Marginal PDF
---
A function used to specify the probability of a [[Random Variable|RV]] falling within a particular range of values. Maps a [[Random Variable|RV]] into a probability from $[0,1]$
It measures the rate at which a given probability accumulates around $x$ of [[Random Variable|RV]] $X$
![[Probability Density Function-20250927122848977.webp|206]]
# Definition
The [[Probability Density Function|PDF]] is the function $f_{X}(x)$ such that:
$$P(X \in [a,b]) = \int_{a}^{b}f_{X}(x)dx$$
# Properties
- $0 \leq f_{X}(x), \forall x \in \mathbb{R}$ (Can have $f(x) > 1!$)
- $\int_{-\infty}^{+\infty}f_{X}(x)dx = 1 = P(-\infty < X < +\infty)=P(S)$
- $F_{X}(x) = \int_{-\infty}^{x}f_{X}(u)du \implies f_{X}(x)=\frac{d}{dx}F_{X}(x)=F'_{X}(x)$ ([[Probability Density Function|PDF]] $\leftrightarrow$ [[Cumulative Distribution Function|CDF]])