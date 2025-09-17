---
tags:
  - proofs
  - math
---
# Example
Prove that any amount $n \in \mathbb{N}$  can be created from $k, l \in \mathbb{N}$.
# Proof
- Let [[Logical Predicate]] $P (n) : \exists k,l \in \mathbb{N}$ s.t $4k+7l = n$
Base step:
Consider 4 cases: $n = 18, 19, 20, 21$
- For $n = 18$, $k=1, l=2$ then, $4k+7l = n$ as wanted
- For $n = 19$, $k=3, l=1$ then, $4k+7l = n$ as wanted
- For $n = 20$, $k=5, l=0$ then, $4k+7l = n$ as wanted
- For $n = 21$, $k=0, l=3$ then, $4k+7l = n$ as wanted
Induction step:
- Let $n \geq 22$
- Suppose $P(k)$ holds for whatever $18 \leq k \leq n$ ([[Induction Hypothesis]])
- WTP: $P(n)$ holds
- Since $n \geq 22 \implies 18 \leq n-4 < n$
- Then, $P(n-4)$ holds
- In other words, $\exists k, l \in \mathbb{N}$ s.t $4k+7l = n-4$
- Then, $k' = k+1, l' = l$, note that $k', l' \in \mathbb{N}$
- Then, $4k' + 7l' = 4(k+1)+7l = 4k+7l+4 = n-4+4 = n$ ([[Induction Hypothesis]])
- By [[Induction Hypothesis|IH]], $p$