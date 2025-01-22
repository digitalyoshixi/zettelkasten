---
tags:
  - math
  - calculus
---
# To Prove
If $f+g$ is integrable on $[a,b]$, then $\int _{a}^b [f(x) + g(x)] \, dx- \int _{a}^b f(x)\, dx = \int _{a}^b g(x)\, dx$
# Proof
Suppose $f$ and $g$ are integrable on $[a,b]$
- Let $P = {x_{i}^*}_{i=0}^n$ be a riemann partition
Then, by definition of $f(x)$ is integrable: $\int_{a}^b f(x) \, dx = \lim_{ n \to \infty } \sum_{i=1}^nf(x_{i}*)\triangle x, \forall x_{i}^* \in [x_{1}\dots x_{i}]$
Then, by definition of $g(x)$ is integrable: $\int_{a}^b g(x) \, dx = \lim_{ n \to \infty } \sum_{i=1}^ng(x_{i}*)\triangle x, \forall x_{i}^* \in [x_{1}\dots x_{i}]$
Then, $\int_{a}^{b} f(x) \, dx + \int_{a}^{b} g(x) \, dx$
... <proof here>
$\lim_{ n \to \infty } \sum_{i=1}^n(f+g)(x_{i}*)\triangle x, \forall x_{i}^* \in [x_{1}\dots x_{i}]$