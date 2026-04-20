---
tags:
  - math
  - distributions
aliases:
  - Waiting-time_Distribution
---
A [[Discrete Distribution]] that can lead to [[Countable Infinity|Countably Infinite]] sequence of [[Independent Events|Independent]] [[Bernoulli Trials]].
![[Geometric Distribution-20251006183144830.webp]]
[[Random Variable|RV]] $X/Y$ defined as $\text{\# of failures/trials before 1st success}$
- $Y = X+1$

Commonly used when:
- Finding the waiting time of something to occur
It is [[Memorylessness|Memoryless]]
# [[Probability Mass Function|PMF]]
- $p$ = probability of success.
- $q$ = probability of failure
- $x =$ random variable for number of failures before success occurs. usually its success - 1.
- $y =$ number of trials
$$P(X=x) = q^x p, \forall x \in \mathbb{N}_{0}$$
$$P(Y=y)=q^{y-1}p, \forall y \in \mathbb{N}$$
# [[Cumulative Distribution Function|CDF]]
$$F_{X}(x) = P(X < x) = \sum_{k=0}^{x } p_{x}(k) = 1-q^{x+1}, \forall x \in \mathbb{N}$$
# Expectation formula
$E(Y)= \frac{q}{p}$
$E(X)= \frac{1}{p}$
# Variance
$\sigma^{2} = \frac{q}{p^{2}}$
# [[Moment Generating Function]]
$$
\frac{pe^{t}}{1 - (1-p)e^{t}}
$$
### Example
Calculate the probability distribution for getting out of jail in MONOPOLY in x rolls of dice.
- $p  = 6/36 = 1/6$
- $q = 5/6$
- $E(x) = (5/6)/(1/6) = 5$
- Thus, we have 5 tries before getting a success
# Geometric Distribution Table
With
p = 0.1
q = 0.9

| x   | P(x)                  |
| --- | --------------------- |
| 0   | 0.9^0 \* 0.1          |
| 1   | 0.9^1 \* 0.1 = 0.09   |
| 2   | 0.9^2 \* 0.1 = 0.081  |
| 3   | 0.9^3 \* 0.1 = 0.0729 |