---
tags:
  - probability
  - statistics
aliases:
  - CDF
  - Marginal CDF
---
A function that determine the probability that a [[Random Variable|RV]] $X$ will take a value less than or equal to $x$.
Oftentimes messy to compute.
![[Cumulative Distribution Function-20250927122611447.webp|257]]
# Notations
- $F_{X}(x) \equiv P(X \leq x)  = P(\{ s \in S | X(s) \leq x \}), \forall x$ represents probability of random variable being less or equal to value $x$
- $F_{X}(x) \equiv P(a < X \leq b)=P(X \leq b) - P(X \leq a) = F_{X}(b) -F_{X}(a)$ represents probability of random $X$ being in any interval $(a,b]$
# Axioms
- $F_{X}(\infty) = \lim_{ x \to -\infty } F_{X}(x)=  1$
- $F_{X}(-\infty) = \lim_{ x \to \infty }F_{X}(x) = 0$
- $\forall x_{1} < x_{2} \in \mathbb{R} \implies F_{X}(x_{1}) \leq F_{X}(x_{2})$
- $F_{X}(\cdot)$ is right-continuous