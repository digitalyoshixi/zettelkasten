---
tags:
  - math
  - probability
  - statistics
---
For the integral
$$\int_{a}^{b} g(x)dx < \infty$$
For [[Independent and Identically Distributed Random Variables|IID]] [[Random Variable|RV]] $X_{i} \in (a,b)$ with [[Probability Density Function|PDF]] $f(x) > 0, \forall x \in (a,b)$
The integral can be approximated with $M_{n} = \frac{1}{n}\sum_{i=1}^{n}\frac{g(X_{i})}{f(X_{i})}$
Then, $E(M_{n}) = \int_{b}^{a} g(x)dx$ by [[Weak Law of Large Numbers|WLLN]]
# Proof
![[Monte Carlo Integration-20251218045739846.webp]]