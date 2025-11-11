---
tags:
  - math
  - calculus
  - linalg
---
$$| \langle \alpha | \beta \rangle| \leq || \alpha || ||\beta ||$$
# Specific Domains
- [[Cauchy Schwarz Inequality Integrals]]
- [[Cauchy Schwarz Inequality Dot Product]]
- [[Cauchy Schwarz Inequality Trace]]
- [[Cauchy Schwarz Inequality Expectation]]
# Proof
### Case 1: $\alpha = a \beta$ (They are scalars of eachother)
- Then, $| \langle \alpha | \beta \rangle | = | \langle a \beta | \beta \rangle |$
- $= | a |\langle B | B\rangle$
- $= \sqrt{ |a|^{2} \langle \beta | \beta \rangle ^{2}}$
- $= || \alpha || \cdot ||\beta ||$
### Case 2: $\alpha \neq a \beta$
- Consider $\langle\alpha = a \beta | \alpha - a \beta \rangle$
- By the fourth property of [[Standard Inner Product for Vector Spaces|Inner Products]], we know $\langle\alpha - a \beta | \alpha - a \beta \rangle > 0$
- $\implies \langle \alpha | \alpha \rangle - \langle   \beta | \alpha \rangle - \langle   \alpha | \beta \rangle - \langle \beta | \beta \rangle$
- We choose $a = \frac{\langle \alpha | \beta \rangle}{\langle \beta | \beta \rangle}$
- Then, $\implies \langle \alpha \ \alpha \rangle \langle \beta | \beta \rangle - \langle\alpha | \beta \rangle \langle \beta | \alpha \rangle > 0$
- $\implies | \langle \alpha | \beta \rangle | < || \alpha || || \beta ||$