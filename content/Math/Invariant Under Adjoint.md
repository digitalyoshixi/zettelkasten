---
tags:
  - math
  - linalg
---
# Definition
- Let $V$ be a finite dimensional [[Inner Product Space]]
- Let $T \in \mathcal{L}(V)$
- Suppose $W$ is a subspace of $V$
- Suppose $W$ [[Invariant]] under $T$
- Then, $W^{\perp}$ is [[Invariant]] under $T^{*}$
# Proof
1. Let $\alpha \in W$
2. Let $\beta \in W^{\perp}$
3. Since $\alpha \in W, T \alpha \in W \implies \langle T \alpha | \beta \rangle = 0$
4. Thus, $\langle \alpha | T^{*} \beta \rangle = 0$
5. Since $\langle T \alpha | \beta \rangle = \langle \alpha | T \beta \rangle$
6. Thus, if $\beta \in W^{\perp}$, Then, $T^{*} \beta \in W^{\perp}$
