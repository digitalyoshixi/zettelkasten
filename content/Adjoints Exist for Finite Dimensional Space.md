---
tags:
  - math
  - linalg
---
# Definition
For [[Linear Operator]] $T$ on finite dimensional [[Inner Product Space]], there exists unique [[Linear Operator]] $T^{*}$ on $V$ such that $\forall \alpha, \beta \in V$, $\langle T\alpha | \beta \rangle = \langle \alpha | T^{*} \beta \rangle$
# Proof
1. Let $\beta$ be any vector $\in V$, $T \in \mathcal{L}(V)$
2. Let $f$ be the [[Linear Functional]] mapping $\alpha$ to $\langle T \alpha | \beta \rangle$
3. Now, $f( \alpha) = \langle T \alpha | \beta \rangle$
4. By construction, $f$ is a linear function
5. Thus, $\exists \beta' \in V$ such that $f(\alpha) = \langle \alpha | \beta' \rangle = \langle T \alpha | \beta \rangle, \forall \alpha \in V$
6. Let $T^{*}$ map $\beta$ to $\beta'$
7. Then, $T^{*}(\beta)= \beta'$
8. Thus, the inner product $\langle \alpha| \beta' \rangle = \langle \alpha | T^{*} (\beta) \rangle = \langle T \alpha | \beta \rangle, \forall \alpha \in V$
### Proving $T^{*}$ is linear and unique
1. $\langle \alpha | T_{1}^{*} \beta \rangle = \langle \alpha | T_{2}^{*} \beta \rangle, \forall \alpha,\beta \in V$
2. Now, we want to show $T_{1}^{*}\beta = T_{2}^{*}\beta, \forall \beta \in V$
3. Note $\implies \langle \alpha | T_{1}^{*} \beta \rangle - \langle \alpha | T_{2}^{*}\beta \rangle = 0, \forall \beta \in V$
4. $\implies \langle \alpha | T_{1}^{*} \beta \ -  T_{2}^{*}\beta \rangle = 0, \forall \beta \in V$
5. $\implies T_{1}^{*}\beta - T_{2}^{*} \beta = 0, \forall \beta \in V$
6. $\Longleftrightarrow T_{1}^{*}\beta = T_{2}^{*} \beta, \forall \beta \in V$