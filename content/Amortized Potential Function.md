---
tags:
  - programming
---
# Definition
- Given a data structure, let $D$ be size of data structure (size of stack, size of list, etc..)
- Define a potential function $\phi(D_{i}) = \text{size of data structure after i operations}$
- Let $t_{i} = time(\text{operation i})$
- Let total time $t = \sum_{i=1}^{n}t_{i}$
- Let the amortized cost $a_{i} = t_{i}+\phi(D_{i})-\phi(D_{i-1})$
- Then, the total amortized time is: $\sum_{i=1}^{n}a_{i} =t+\phi(D_{n})-\phi(D_{0})$
# Proving Process
1. Define $\phi(D_{i})$
2. Prove $\phi(D_{n}) \geq \phi(D_{0})$ for all $n > n_{0}$ sequences of operations
3. Let $t_{i} = time(\text{operation i})$
4. Then, $a_{i}=t_{i}+phi(D_{i})-\phi(D_{i-1})$ (Note that this can be different for diff operations)
