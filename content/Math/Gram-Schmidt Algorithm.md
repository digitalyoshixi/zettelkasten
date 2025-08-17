---
tags:
  - math
  - linalg
---
A process to make convert a set into an [[Orthogonal Set]]
# Procedure
- Let $\{ \beta_{1}  ,\dots, \beta_{j}\}$ be a [[Linear Independence|Linearly Independent]] set of vectors
- Consider set of vectors $\{  \alpha_{1},\dots, \alpha_{n} \}$
1. $\alpha_{1} = \beta_{1}$
2. $\alpha_{2} = \beta_{2} - \frac{\langle \beta_{2} | \alpha _{1} \rangle}{ \langle \alpha _{ 1} | \alpha _{1} \rangle} \alpha _1$
3. ...
4. $\alpha_{j} = \beta_{k} - \sum_{i=1}^{k-1} \frac{\langle \beta _{k} | \alpha_{i}\rangle}{\langle \alpha _{i} | \alpha_{1} \rangle} \alpha_{i}$
# Intuition
1. Pick a first vector to base everything off. This first vector is now a fundamental basis vector.
2. The second vector is projected down with the first vector, and that component is subtracted from the second vector. This second vector is now a fundamental basis vector
3. The third vector is projected down with second, that component is subtracted, projected down with first vector, that component is subtracted. Now the third vector is a fundamental basis vector
4. Repeat for all other vectors
