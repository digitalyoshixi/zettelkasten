---
tags:
  - programming
---
A revision of the [[Amortized Accounting Method]] that is stateless and uses a potential function.
# Definition
- Given a data structure, let $D$ be state of data structure
- Define a potential function $\phi(D_{i}) = \text{size of data structure after i operations}$
	- Tracks number of stored elements
	- Tracks distance from threshold
	- Tracks how unbalanced a structure is
- Let $t_{i} = time(\text{operation i})$
- Let total time $t = \sum_{i=1}^{n}t_{i}$
- Let the amortized cost $a_{i} = t_{i}+\phi(D_{i})-\phi(D_{i-1})$
- Then, the total amortized time is: $\sum_{i=1}^{n}a_{i} =t+\phi(D_{n})-\phi(D_{0})$
# Proving Process
1. Define $\phi(D_{i})$
2. Show $\phi(D) \geq 0, \forall D \in \Omega$ (greater than 0 for all states)
3. Prove $\phi(D_{n}) \geq \phi(D_{n_{0}})$ for all $n > n_{0}$ sequences of operations
4. Let $t_{i} = \text{actual time}(\text{operation i})$
5. Then, $a_{i}=t_{i}+phi(D_{i})-\phi(D_{i-1})$ (Note that this can be different for diff operations)
# Example
- Suppose data structure is [[Array List|Expandable Array]]
- Define invariant as $\text{capacity}\leq 2 * size$
- Define $\phi(D) = 2 * size - \text{capacity}$
- Then, $\phi(D_{i}) \geq 0, \forall i$
- Prove $\phi(D_{n}) - \phi (D_{0})\geq 0, \forall n \geq n_{0}=0$ operations
- `get()`, `size()`, `set(i,x)` do not change size or capacity, $O(1)$
- `add(x)`:
	- If no copying (no resizing): $a_{i} = t_{i}+\phi(D_{i}) - \phi (D_{i-1}) = 1 + (2*(s+1)-c) - (2*s-c) = 3$
	- If copying: $a_{i}=t_{i}+\phi(D_{i})-\phi(D_{i-1})=(c+1)+(2 * (s+1) - 2*c)-(2*s-c) = 3$