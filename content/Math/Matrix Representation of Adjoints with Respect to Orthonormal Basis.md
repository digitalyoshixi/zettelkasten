---
tags:
  - math
  - linalg
---
# Theorem
1. Let $V \in \mathcal{L}(v)$
2. With $\beta = \{ \alpha_{1},\dots,\alpha_{n} \}$ as an ordered [[Orthonormal Set|Orthonormal Basis]] of $V$
3. With $[T]_{\beta} = (A_{jk}$
4. The matrix representation $T^{*}$ with basis $\beta$ is the [[Conjugate Transpose]] of the matrix representation of $T$ using the same basis
# Proof
1. Let $A = [T]_\beta$
2. Let $B = [T^{*}]_{\beta}$
3. $\implies A_{jk} = \langle T \alpha_{k} | \alpha_{j} \rangle$ and $B_{kj} = \langle T^{*} \alpha_{j} | \alpha_{k} \rangle$
4. But, $B_{kj} = \langle T^{*} \alpha_{j} | \alpha_{k} \rangle = \overline{\langle \alpha_{k} | T^{*} \alpha_{j}\rangle} = \overline{\langle T\alpha_{k} | \alpha_{j}} = \overline A_{jk}$
