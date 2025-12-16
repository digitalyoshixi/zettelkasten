---
tags:
  - math
  - probability
  - statistics
---
A [[Discrete Distribution]] for an [[Countable Infinity|Countably Infinite]] series of [[Independent Events|Independent]] [[Bernoulli Trials]] with:
- The same probability of success $p$
- The same probability of failure $q = 1-p$
Used for waiting for multiple occurrences of an event.
![[Negative Binomial Distribution-20251006184134082.webp]]
# Random Variable
The [[Random Variable|RV]] $X/Y$ counts $\text{\# of failures/trials until } r-th \text{ success}$
# [[Protected Management Frames|PMF]]
$P_{X}(x)= \binom{x+r+1}{r-1}p^{r}q^{x}, \forall x \in \mathbb{R}$
# CDF
There is no CDF
# [[Expectation]]
$E(X) = \frac{r}{p}$
# [[Variance]]
$\sigma^{2} = \frac{rq}{p^{2}}$
# [[Moment Generating Function|MGF]]
$$
(\frac{pe^{t}}{1-(1-p)e^{t}})^{r}
$$
With $t < -\ln (1-p)$