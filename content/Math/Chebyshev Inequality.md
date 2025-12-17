---
tags:
  - math
  - calculus
---
The probability of being far from the mean is very low.
# Inequality
For any [[Random Variable|RV]] $X$, probability of both tails is bounded by [[Variance]].
$$P(|X-\mu| \geq a) \leq \frac{V(X)}{a^{2}}$$
![[Chebyshev Inequality-20251111172407853.webp]]
# Proof
1. Apply [[Markov Inequality]] to $g(x) = (x - \mu)^{2} > 0$
2. Then, $P(g(X) \geq a^{2}) \leq \frac{E(g(x))}{a^{2}}$
3. $\Longleftrightarrow P( (x-\mu)^{2} \geq a^{2}) \leq \frac{E((X-\mu)^{2}}{a}$
4. $\Longleftrightarrow P(|X-\mu)| \geq a) \leq \frac{V(X)}{a^{2}}$