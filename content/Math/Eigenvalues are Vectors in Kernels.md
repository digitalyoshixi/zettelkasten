---
tags:
  - math
  - linalg
---
# Theorem
$T(v) = \lambda v \Longleftrightarrow v \in ker(T - \lambda I)$
# Proof
### Proving $\implies$
1. Suppose $T(v) = \lambda v$
2. $\implies T(v) = \lambda I(v)$ by identity transform
3. $\implies T(v) - \lambda I(v) = 0$
4. $\implies (T- \lambda I)(v)$ as $T, \lambda I$ are both linear
5. Thus, $v \in ker(T- \lambda I)$
### Proving $\Longleftarrow$
1. Suppose $v \in ker(T - \lambda I)$
2. $\implies (T - \lambda I)(v) = 0$ by defn of kernel
3. $\implies T(v) - \lambda I (v) = 0$ as $T, \lambda I$ are both linear
4. $\implies T(v) = \lambda I (v)$ 
5. $\implies T(v) = \lambda v$ by identity transform