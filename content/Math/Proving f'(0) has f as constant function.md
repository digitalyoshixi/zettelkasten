---
tags:
  - math
  - proofs
---
WTS: $\forall x \in (a,b), f'(x)=0 \implies \forall x_{1},x_{2} \in (a,b), f(x_{1})=f(x_{2})$
# Proof
1. Let $a,b$ be arbitrary
2. Let $a < b$
3. Assume $\forall x \in (a,b), f'(x)=0$
4. This means $f$ is [[Differentiability|Differentiable]] on $(a,b)$
5. So $f$ is continuous on $(a,b)$
6. Let $x_{1},x_{2} \in (a,b)$ be arbitrary
7. Case 1: $x_{1}=x_{2}$
	1. Then $f(x_{1}) = f(x_{2})$
8. Case 2: $x_{1} < x_{2}$ or $x_{2}<x_{1}$
	1. Note that $f$ is [[Differentiability|Differentiable]] on $(x_{1},x_{2})$ as $(x_{1},x_{2}) \subset (a,b)$ 
	2. Note that $f$ is [[Continuity|Continuous]] on $[x_{1},x_{2}]$ as $(x_{1},x_{2}) \subset (a,b)$ 
	3. Thus by MVT, $f'(x) = \frac{f(x_{2})-f(x_{1})}{x_{2}-x_{1}}$ 
	4. $\implies 0 = \frac{f(x_{2}) - f(x_{1})}{x_{2}-x_{1}}$
	5. $\implies 0=f(x_{2})-f(x_{1})$
	6. $\implies f(x_{1})=f(x_{2})$
9. Hence $f(x_{2})=f(x_{1})$
10. As required $\square$