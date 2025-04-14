---
banner: "[[Definite Integral-20250113182157683.webp]]"
tags:
  - calculus
aliases:
  - Integrable
---
# Notation
![[Definite Integral-20250113182157683.webp]]
$\int ^b_{a} f(x)\, dx$
- $f(x)$ is referred to as the integrand
- $dx$ is the differential
The process to evaluate this integral is called integration
# Definitions (Integrable)
- [[Definite Integral Riemann Sum Definition]]
- [[Definite Integral Darboux Sum Definition]]
- [[Definite Integral Darboux Sum Epsilon Reformed Definition]]
- [[Definite Integral Lebesgue Sum Definition]]
# Not Integrable
- When there is a [[Essential Discontinuity|Infinite Discontinuity]] within the interval
- When there are too-many [[Jump Discontinuities]] (Like [[Dirichlet Function]])
# Properties of Definite Integral
Given $a,b \in R, a < b$, $f(x)$ and $g(x)$ are integrable on $[a,b]$
1. $\forall x \in [a,b], f(x) \geq 0 \implies \int _{b}^a f(x)\, dx \geq 0$
1. $\forall x \in [a,b], f(x) \leq 0 \implies \int _{b}^a f(x)\, dx \leq 0$
2. If $f+g$ is integrable on $[a,b]$, then $\int _{a}^b [f(x) + g(x)] \, dx- \int _{a}^b f(x)\, dx = \int _{a}^b g(x)\, dx$
3. $\forall c \in R, \int _{a}^b cf(x)\, dx = c \int _{a}^b f(x) \, dx \implies$ $cf(x)$ is integrable on $[a,b]$
4. $\int _{a}^a f(x)\, dx = 0$
5. $\int_{a}^{b} f(x) \, dx = -\int_{b}^{a} f(x) \, dx$
6. $\forall c \in (a,b), \int_{a}^{b} f(x) \, dx = \int_{a}^{c} f(x) \, dx+ \int_{c}^{b} f(x) \, dx$ [[Union Interval Property]]
### Proofs
- [[Proving Definite Integral Property 2]]
# Helpful Formulas
- [[Integral of x]]