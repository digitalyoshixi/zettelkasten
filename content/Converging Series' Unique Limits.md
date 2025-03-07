---
tags:
  - math
  - calculus
  - proofs
---
# Theorem
- If $\{  a_{n} \}$ converges
- Then, $\{ a_{n} \}$'s limit is unique
# Proof
1. Suppose $\{ a_{n} \}$ converges
2. Choose arbitrary $l_{1}, l_{2}$ s.t $\{ a_{n} \} = l_{1}$ and $\{ a_{n} \} = l_{2}$
3. We want to show that $l_{1}=l_{2}$ 
	1. $\implies l_{1} - l_{2} = 0$
	2. $\implies \forall \epsilon >0, |l_{1} - l_{2}| < \epsilon$
4. Let $\epsilon > 0$ be arbitrary
5. Invoke 1 with $\epsilon_{1} = \frac{\epsilon}{2}$
6. Note that $\exists N > 0$ s.t if $n > N$ then $|a_{n} - l_{1}| < \epsilon_{1}$
7. Invoke 1 with $\epsilon_{2} = \frac{\epsilon}{2}$
8. Note that $\exists N > 0$ s.t if $n > N$ then $|a_{n} - l_{2}| < \epsilon_{2}$
9. Then, consider $|l_{1} - l_{2}|=|-a_{n} - l_{1} + a_{n} - l_{n}| \leq |a_{n}-l_{1}| + |a_{n} - l_{2}| = \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon$
10. $\square$