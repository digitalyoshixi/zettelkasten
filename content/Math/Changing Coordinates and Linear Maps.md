---
tags:
  - math
  - linalg
---
# Theorem
- If $T : V \to W$ is a linear map
- With $[T]_{\alpha}^{\beta}$ as the matrix representation for $T$
- If $V$ has bases $\alpha, \alpha'$
- If $W$ has bases $\beta, \beta '$
- Then, $[T]_{\alpha'}^{\beta'} = [I_{W}]_{\beta}^{\beta'}[T]_{\alpha}^{\beta}[I]_{\alpha'}^{\alpha}$
Notice the composition $T \xrightarrow{I_{V}} V \xrightarrow{I_{W}} W$
# Proof
- For every vector $v \in V$, we have $T(v) = I_{W}(T(I_{V}(v)))$
- Note that $[T]_{\alpha'}^{\beta'} = [I_{W}TI_{V}]_{\alpha'}^{\beta'}$
- $= [I_{W}]^{\beta'}_{\beta}[T]_{\alpha}^{\beta}[I_{V}]_{\alpha'}^{\alpha}$ by [[Matrix Vector Multiplication|Matrix Vector Product]] and [[Matrix Multiplication of Composite Maps]]

