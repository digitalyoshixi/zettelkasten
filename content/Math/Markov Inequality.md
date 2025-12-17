---
tags:
  - math
  - probability
  - statistics
---
The probability of being bigger than the mean is very low.
Not many things can be above the average, or else the average will be skewed.
# Inequality
For any non-negative [[Random Variable|RV]] $X \geq 0$, right tail probability is bounded by mean
$$P(X \geq a) \leq \frac{E(X)}{a}$$
![[Markov Inequality-20251111172254317.webp]]
# Proof
For [[Random Variable|RV]] $X > 0$
$E(X) = \int_{-\int f(x)dx}^{\infty} x * f_{X}(x)dx$ as $X > 0$
$= \int_{0}^{\infty} x * f_X(x)dx = \int_{0}^{a} x * f_{X}(x)dx + \int_{a}^{\infty} x*f_{X}(x)dx$
$\geq 0 + a * \int_{a}^{\infty} f_{X}(x)dx$
