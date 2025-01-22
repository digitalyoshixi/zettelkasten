---
tags:
  - calculus
aliases: []
---
# Definition (Riemann Sum Definition of Definite Integral)
- Let $a,b \in R$
- Let $a < b$
- Let $[a,b] \subset dom(f)$
- Let $P = \{x_{i}\}_{i=0}^n$ be $a$
- Create a [[Riemann Partition]] of $[a,b]$
**A function is integrable if:**
$$\int_{a}^b f(x) \, dx = \lim_{ n \to \infty } \sum_{i=1}^nf(x_{i}*)\triangle x, \forall x_{i}^* \in [x_{1}\dots x_{i}]$$
For Right-Riemann Sum:
$$\int_{a}^b f(x) \, dx = \lim_{ n \to \infty } \sum_{i=1}^nf\left( a+(i) \frac{b-a}{n} \right) \left( \frac{b-a}{n} \right), \forall x_{i}^* \in [x_{1}\dots x_{i}]$$
For Left-Riemann Sum:
$$\int_{a}^b f(x) \, dx = \lim_{ n \to \infty } \sum_{i=1}^nf\left( a+(i-1) (\frac{b-a}{n}) \right) \left( \frac{b-a}{n} \right), \forall x_{i}^* \in [x_{1}\dots x_{i}]$$
- You can create an infinite amount of integrals from a given function, different $a, b,x_{i}$ values and it will still work
# Example to convert Integral form to Riemann sum form
Convert: $\int _{0}^3 (x-5)\, dx$
- $a = 0$
- $b = 3$
- Note that $[a,b] \subset dom(f)$
- Given $[a,b] = [0,3]$
- $f(x) = x-5$
Then,
- we have $\triangle x \frac{(b-a)}{n}$
- $x_{i}^* = a+n \triangle x$