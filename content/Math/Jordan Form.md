---
tags:
  - math
  - linalg
aliases:
  - Jordan Canonical Form
---
A jordan canonical form is a [[Upper Triangular Matrices|Upper Triangular Matrix]] that is of the structure of a [[Jordan Matrix]].
# Definition
- Suppose $T \in \mathcal{L}(V)$ 
- A jordan basis $\beta$ allows for jordan matrix:
  $$[T]_{\beta} = \left[\begin{array}{cc} 
A_{1} &  & 0\\
 & \ddots & \\
0 &  & A_{p} \\
\end{array}\right]
$$
- Where, $$A_{i} = \left[\begin{array}{cc} 
\lambda_{k} & 1 & \dots & 0\\
& \ddots & \ddots & \\
&  & \ddots & 1\\
0 &  &  & \lambda_{k}\\
\end{array}\right]$$
### Alternate Definition
A jordan form of $A$ exists $\Longleftrightarrow$ the [[Characteristic Polynomial]] of $A$ splits into [[Linear Factor|Linear Factors]]
# Guides
- [[Finding Jordan Form of Matrix]]
# Theorems
- [[Jordan Basis Exists for Triangularizable Linear Transformations]]
- [[All Operators on A Vector Space Defined Over an Algebraically Closed Field Have A Jordan Form]]