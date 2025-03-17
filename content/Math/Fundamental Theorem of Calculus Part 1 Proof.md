---
tags:
  - calculus
  - proofs
---
# Proof
1. Suppose $f$ is cont on $[a,b]$
2. Consider $\int_{a}^{b} f(x) \, dx$
3. $= \lim_{ n \to \infty }\sum_{i=1}^{n}f(x_{i}^{*})\triangle x$
4. Suppose $F$ is any anti-derivative on $[a,b]$
	1. Then, $\forall x \in [a,b], F'(x) = f(x)$ by defn of [[Antiderivative]]
	2. Since $F'(x) = f(x)$, $F(x)$ is [[Differentiability|Differentiable]] on $[a,b]$
	3. Thus. $F(x)$ is continuous on $[a,b]$ as [[Differentiable Implies Continuity|Differentiability Implies Continuous]]
	4. It follows that $F(x)$ is also diffferentiable on $(a,b)$
	5. By [[Mean Value Theorem|MVT]], $\exists c \in (x_{i-1},x_{i})$ s.t $f'(c_{i}) = \frac{f(x_{i})-f(x_{i-1})}{x_{i}-x_{i-1}}$
	6. $\implies f'(c_{i}) = f(x_{i})-f(x_{i-1}) (\triangle x)$ by defn of $\triangle x$
	7. Note that $f'(c_{i}) = F(c) = F(x)|_{b}^{a}$
	8. Thus, $f(x_{i})-f(x_{i-1}) = F(c_{i})(\triangle x)$
	9. By [[Mean Value Theorem|MVT]], $c_{i} \in [a,b]$. Choose $x_{i}^{*} = c_{i}$
	10. Now, $\lim_{ n \to \infty }\sum_{i=1}^{n}f(c_{i}) \triangle x$
	11. $= \lim_{ n \to \infty }\sum_{i=1}^{n}(F(x_{i})-F(x_{i-1}))$
	12. This is a [[Telescoping Series]], then, you should get after computation: $\lim_{ n \to \infty }F(x_{0}) - F(x_{n}) = \lim_{ n \to \infty } F(a) - F(B)$
	13. Thus, $\int_{a}^{b} f(x) \, dx = F(a)-F(b)$