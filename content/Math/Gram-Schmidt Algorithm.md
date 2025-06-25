---
tags:
  - math
  - linalg
---
A process to make two vectors [[Orthogonal]].

# Procedure
- Let $\{ \beta_{1}  ,\dots, \beta_{j}\}$ be a [[Linear Independence|Linearly Independent]] set of vectors
- Consider set of vectors $\{  \alpha_{1},\dots, \alpha_{n} \}$
1. $\alpha_{1} = \beta_{1}$
2. $\alpha_{2} = \beta_{2} = \frac{\langle \beta_{1} | \alpha _{1} \rangle}{ \langle \alpha _{ 1} | \alpha _{1} \rangle} \alpha _1$
3. ...
4. $\alpha_{j} = \beta_{k} - \sum_{i=1}^{j-1} \frac{\langle \beta _{j} | \alpha_{i}}{\langle \alpha _{i} | \alpha_{1} \rangle} \alpha_{i}$