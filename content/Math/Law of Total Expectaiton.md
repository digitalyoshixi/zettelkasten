---
tags:
  - math
  - statistics
  - probability
aliases:
  - LoTE
  - Tower Law
  - Law of Iterated Expectations
---
The expectation of a distribution can be seen as the weighted sum
# Theorem
$$
E(Y) = E[E(Y|X)] = \begin{cases}
\Sigma_{x}E(Y|X = x)p_{X}(x)\\
\int_{\mathbb{R}} E(Y|X=x)f_{X}(x)dx
\end{cases}
$$
