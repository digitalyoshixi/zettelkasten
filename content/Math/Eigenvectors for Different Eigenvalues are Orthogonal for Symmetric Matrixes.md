---
tags:
  - math
  - linalg
---
# Theorem
- If $A$ is a [[Symmetric Matrix]] (could be [[Unitary Operator|Unitary]], [[Normal Operator|Normal]], etc..)
- With eigenvalues $\lambda_{1},\lambda_{2}$ that are unique
- For eigenvector $x_{1}$ for $\lambda_{1}$, eigenvector $x_{2}$ for $\lambda_{2}$
- Then, $\langle x_{1}| x_{2} \rangle = 0$
# Proof
1. Given $Ax_{1} = \lambda_{1}x_{1}$
2. Given $Ax_{2} = \lambda_{2}x_{2}$
3. $\implies (Ax_{1})^{T} = (\lambda_{1}x_{1})^{T}$
4. $\implies x_{1}^TA^{T} = \lambda_{1}x_{1}^{T}$
5. $\implies x_{1}^TA^{T}x_{2} = \lambda_{1}x_{1}^{T}x_{2}$
6. $\implies x_{1}^T\lambda_{2}x_{2} = \lambda_{1}x_{1}^{T}x_{2}$
7. $\implies \lambda_{2}x_{1}^Tx_{2} = \lambda_{1}x_{1}^{T}x_{2}$
8. $\implies (\lambda_{2}- \lambda_{1})(x_{1}^Tx_{2}) = 0$
9. Note that since $\lambda_{2} \neq \lambda_{1}$, then it has to be that $x_{1}^{T}x_{2} = 0$, which means $\langle x_{1}, x_{2} \rangle = 0$ by definition of [[Standard Inner Product for Real Numbers|Dot Product]]