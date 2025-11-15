---
tags:
  - math
  - distributions
---
A [[Discrete Distribution]] with [[Dependent Events|Dependent]] [[Bernoulli Trials]].
Commonly used when items are removed from the set.
![[Hypergeometric Distribution-20251006184544895.webp|425]]
$$\text{Hypergeometric}(N,M,n)$$
- $N$ is Total items in set
- $M$ is number of successes in trial
- $n$ is number of trials
# [[Probability Mass Function|PMF]]
$$P(X=x) = \frac{\binom{M}{x} \binom{N-M}{n-x}}{\binom{N}{n}}, \forall \begin{cases}
x \geq max \{ 0, n-(N-M) \}\\
x \leq min \{ n, M\}\\
\end{cases}$$
# Formula
The probability of outcomes *x* successful outcomes in *r* trials is:
$$\frac{_{a}C_{x} * _{n-a}C_{r-x}}{_{n}C_{r}}$$
r : # of selections
a : what random variable x will take from. the success set. number of possible successes
n : population total set(universal set fit within the selection space)
### Memorizing the formula
![[Hypergeometric Distribution-20240122210727030.webp]]
![[Pasted image 20240122210828.png]]
# Expectations
$$E(x) = \frac{ra}{n}$$
# Example
Probability distribution of the number of hearts in a 5 card hand from a standard deck of cards

| Number of hearts, x | P(x)                                                    | x P(x) |
| ------------------- | ------------------------------------------------------- | ------ |
| 0                   | ($\frac{_{13}C_{0} * _{39}C_{5}}{_{52}C_{5}}$) = 0.2215 | 0      |
| 1                   | ($\frac{_{13}C_{1} * _{39}C_{4}}{_{52}C_{5}}$) = 0.4114 | 0.4114 |
| 2                   | ($\frac{_{13}C_{2} * _{39}C_{3}}{_{52}C_{5}}$) = 0.2743 | 0.5486 |
| 3                   | = 0.815                                                 | 0.2445 |
| 4                   | = 0.0143                                                | 0.0572 |
| 5                   | = 0.0005                                                | 0.0025       |
The expected value is the sum of column x P(x). that is 1.26
**What this means is that we are expected to get 1.26 hearts for every 5 card hand**

# Example 2. Find population
in 2002, 300 tagged bass released. in 2003, 200 bass caught and 20 found were tagged. what is the estimate size of bass population in 2003?

n = ?
a = 300
r = 200

E(x) = ra/n
n = ra
n = 3000
