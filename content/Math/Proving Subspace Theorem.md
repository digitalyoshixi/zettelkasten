---
tags:
  - proofs
  - math
  - linalg
---
# Theorem
1. $W$ is a non-empty [[Subset]] of vector space $V$
2. $W$ is a subspace of $V \Longleftrightarrow \forall x,y\in W$  and $\forall c \in R, cx+y\in W$
# Proof
Assume W is a non-empty subset of vector space V
### $\implies$
1. Assume W is a subspace of V
2. Then, $\forall x \in W, \forall c \in R, cx \in W$
3. Then, $\forall y \in W,cx+y \in W$ as well
4. By definition of subspace, $W$ of $V$ is [[Closed Under Addition]] and [[Closed Under Scalar Multiplication]].
### $\Longleftarrow$
1. Suppose $W$ is a subset of $V$ that satisfies $\forall c \in R, cx+y \in W$
2. Take $c=1$
	1. $x+y \in W$ thus, $W$ is [[Closed Under Addition]]
3. Take $x = y$ and $c = -1$
	1. Then, $-y + y = 0 \in W$
4. Take $y=0$
	1. Then $cx \in W$, thus $W$ is [[Closed Under Scalar Multiplication]]
5. Thus, $W$ is a subspace
$$\square$$