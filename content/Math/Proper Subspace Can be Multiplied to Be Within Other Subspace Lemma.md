---
tags:
  - math
  - linalg
---
# Lemma
1. With $V$ as a finite dimensional [[Vector Space]]
2. With $T \in \mathcal{L}(V)$ such that the minimal polynomial for $T$ is a product of linear factors:
	1. $P(x) = (x-c_{1})^{d_{1}} \dots (x-c_{k})^{d_{k}}$
3. With $W$ as a [[Proper Subspace]] of $V$ invariant under $T$
4. Then, there exists a vector $\alpha \in V$ such that: 
	1. $\alpha \in W$
	2. $(T - qI) \alpha \in W$ for some $c_{i} \in \{  c_{1},\dots,c_{k} \}$
# Intuition
There is a vector in $W$, that allows it to be multiplied by a $\lambda$ so that it is within the other subspace
# Proof
1. Let $g$ be the $T$-Conductor of $S_{T}(\beta, W)$
2. As $g$ divides the minimal polynomial of $T$, there exists $T_{1},\dots,T_{k}$ where $t_{i} \in \{ d_{1},\dots,d_{i} \}, \forall i$ such that: $g = (x-c_{1})^{r_{1}}\dots(x-c_k)^{r_{k}}$ With at least one $r_{i} \neq 0$
3. We redefine $g = \Pi_{i=1}^{n}(x- \lambda_{i})$ where $n = \sum_{i=1}^{k}r_{i}$, and consider $\beta$
4. Then, consider the sequence $\{ g_{1},\dots,g_{n} \}$ where $g_{j} = \Pi_{i=1}^{j}(x - \lambda)$
5. As $\beta \not\in W$, there must exist a $m \in \{ 1,\dots,m \}$ such that:
	1. $g_{m-1}(T) \beta \not \in W$
	2. $g_{m}(T) \beta \in W$
6. Letting $\alpha = g_{m-1}(T) v$ gives our result as $\alpha \not \in W$, but $(T - \lambda_{m}I) \alpha \in W$

