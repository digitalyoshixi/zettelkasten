---
tags:
  - math
  - linalg
---
# Proof
1. We define $trace(A) = \sum_{n=1}^{\infty}A_{ii}$
2. By definition, $trace : \mathbb{F}^{n \times n} \to \mathbb{F}$
3. Thus, if we show trace is a linear linear transformation, $trace \in L(\mathbb{F}^{n \times n}, \mathbb{F})$
### Proving Linear Transformation
1. Let $c \in \mathbb{F}, A,B \in \mathbb{F}^{n \times n}$
2. We denote $A$ by $A_{ij}$ and $B$ with $B_{ij}$
3. Then, $trace(cA + B) = \sum_{n=1}^{\infty}(cA+B)_{ii}$
4. $= \sum_{n=1}^{\infty} (cA)_{ii} + B_{ii}$ by defn of matrix addition
5. $= \sum_{n=1}^{\infty}c(A_{ii}) + B_{ii}$ by defn of scaling matrixes
6. $= c(\sum_{n=1}^{\infty}A_{ii}) + \sum_{n=1}^{\infty}(B_{ii})$ by field properties, asocciative
7. $= c *trace(A) +trace(B)$
8. Thus, it follows that $trace$ is a [[Linear Transform|Linear Function]]
9. Thus, it follows that $trace$ is a [[Linear Functional]]