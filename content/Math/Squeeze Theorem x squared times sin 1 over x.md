---
tags:
  - math
---
$\lim_{ x \to 0}x^2\sin(\frac{1}{x})$
# Solution
Solving with squeeze theorem
1. Note that $\forall x \in R$, $-1 \leq \sin(x) \leq 1$                                   defn of sine
1. Then $\forall x \in R$, $-1 \leq \sin(\frac{1}{x}) \leq 1$                                          choice of x
2. Then $\lim_{ x \to 0 }-x^2 \leq \lim_{ x \to 0} x^2\sin(\frac{1}{x}) \leq \lim_{ x \to 0}x^2$                As $x^2$ is positive
2. Then $0 \leq \lim_{ x \to 0} x^2\sin(\frac{1}{x}) \leq 0$                                            limit properties
3. Thus $\lim_{ x \to 0}x^2\sin(\frac{1}{x}) = 0$                                                     by squeeze theorem
