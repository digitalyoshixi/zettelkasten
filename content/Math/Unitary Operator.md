---
tags:
  - math
  - linalg
aliases:
  - Unitary
  - Unitary Matrix
---
# Definition
A unitary operator is a [[Linear Operator]] on an [[Inner Product Space]] that has a vector isomorphism of the space to itself.
# Formal Definition
$T \in \mathcal{L}(V)$ s.t $\langle T \alpha | T \beta \rangle = \langle \alpha | \beta\rangle, \forall \alpha, \beta \in V$
Its a isomorphism that [[Preserving Inner Products and Vector Isomorphism|Preserves Inner Products]]
# Equivalent Definitions
1. $UU^{*} = I = U^{*}U$ 
2. $U$ is [[Preserving Inner Products and Vector Isomorphism]] ($\langle U \alpha, U \beta \rangle = \langle \alpha | \beta\rangle$)
3. $U$ is [[Norm]] preserving. ($|| U \alpha || = || \alpha ||, \alpha \in V$)
4. if $\{  \alpha_{1},\dots,\alpha _n\}$ is an [[Orthonormal Set|Orthnormal Basis]] for $V$, then $\{ U(\alpha_{1}),\dots,U(\alpha_{n}) \}$ is also a [[Orthonormal Set|Orthonormal Basis]] for $V$
5. If $B$ is any [[Orthonormal Set|Orthonormal Basis]] for$V$ ,then the columns of $[U]_{\beta}$ are orthonormal in $\mathbb{F}^{n}$ with the standard inner product
6. If $\beta$ is any ordered [[Orthonormal Set|Orthonormal Basis]] for $V$, then the rows $[U]_{\beta}$ are orthonormal in $\mathbb{F}^{n}$ with the standard inner product
### Proofs
1. [[Proving Unitary Operators Property 1]]