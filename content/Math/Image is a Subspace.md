---
tags:
  - math
  - linalg
---
# Theorem
For any linear map $T:V \to W$, the $Image(T)$ is a subspace of $W$.
# Proof
1. Apply [[Subspace Test]]
2. Notice $Image(T)$ is non-empty. This is because $T(0 \overrightarrow{v}) = \overrightarrow{0}w \in Image(T)$
3. Then notice that any two vectors $w_{1}, w_{2} \in Image(T)$ and for any scalar $c \in \mathbb{F}$. $w_{1} = T(v_{1})$ , $w_{2} =T(v_{2})$
4. Thus, we have: $c(w_{1}) + w_{2} = cT(v_{1}) + T(v_{2})$
5. $= T(cv_{1} + v_{2})$ by [[Linearity]]
6. Note that this is also in the image. $T(cv_{1} + v_{2}) \in Image(T)$
7. Therefore, $Image(T)$ is a [[Subspace]] of $W$