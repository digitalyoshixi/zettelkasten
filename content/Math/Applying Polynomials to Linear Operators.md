---
tags:
  - math
  - linalg
---
# Definition
1. Let $f = c_{0} + \dots + c_{k}x^{k}$
2. Let $T \in \mathcal{L}(V)$
3. Let $A \in M_{n \times n}(\mathbb{F})$
Then,
4. $f(T) = c_{0}I + c_{1}T + \dots + c_{k}T^{k} = \sum_{i=1}^{n}c_{i}T^{i}$ (For operators)
5. $f(A) = c_{0}T + c_{1}A + \dots + c_{k}A^{k} = \sum_{i=1}^{n}c_{i}A^{i}$ (For matrixes)
# Example
With $T : \mathbb{R}^{2} \to \mathbb{R}^{2}$ as $T(x_{1},x_{2}) = (x_{2},3x_{1}-x_{2})$
Find $f(T)$ where $f(x) = x^{2}-1$
### Soln
1. $f(T) =T^{2} - I$
2. $= f(T)(x_{1},x_{2}) = (T^{2}-1)(x_1,x_{2})$
3. $=T^{2}(x_{1},x_{2}) - I(x_{1},x_{2})$
4. $=T(T(x_{1},x_{2})) - I(x_{1},x_{2})$
5. $=T(x_{2},3x_{1}-x_{2}) - (x_{1},x_{2})$
6. $= (3x_{1}-x_{2}, 3x_{2} - (3x_{1}-x_{2})) - (x_{1},x_{2})$
7. $= (2x_{1}-x_{2}, 3x_{2}-3x_{1})$