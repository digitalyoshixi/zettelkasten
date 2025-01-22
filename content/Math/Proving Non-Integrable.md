---
tags:
  - math
  - calculus
  - proofs
---
You use the [[Definite Integral Darboux Sum Definition]] or [[Definite Integral Darboux Sum Epsilon Reformed Definition]] to prove non-integrability.
# Example
Consider the [[Dirichlet Function]]:
$f = \{ 0 \text{ if } x \in Q, 1 \text{ if } x \not\in Q \}$
Then, to show non-integrability, we want to show that the upper darboux sum is not equa lower darboux sum.
1. Let $a,b \in \mathbb{R}$ be arbitrary and suppose $a<b$
2. Let $P=\{ x_{i} \}^n_{i=0}$ be an arbitrary partition
3. Then, the lower Darboux sum = $L(f,p) = \sum_{k=1}^{n} m_{i}(x_{i} - x_{i-1})$
	1. $L(f,p) = \sum_{k=1}^{n}(0)(x_{i} - x_{i-1})$ as the minimum is always 0, as there is always an irrational in a set by [[Density]]
	2. $L(f,p) = (0)(-x_{0} + x_{n})$ by [[Linearity]] dist prop and since $\sum_{k=1}^{n}(x_{i} - x_{i-1})$ is a [[Telescoping Series]]
	2. $L(f,p) = 0$ 
4. Then, the upper Darboux sum = $U(f,p) = \sum_{k=1}^{n} M_{i}(x_{i} - x_{i+1})$
	1. $U(f,p) = \sum_{k=1}^{n}(1)(x_{i} - x_{i-1})$ as the maximum is always 1, as there is always a rational in a real set by [[Density]]
	2. $U(f,p) = (1)(-x_{0} + x_{n})$ by [[Linearity]] dist prop and since $\sum_{k=1}^{n}(x_{i} - x_{i-1})$ is a [[Telescoping Series]]
	2. $U(f,p) = (-x_{0} + x_{n})$ 
	2. $U(f,p) = (-a + b)$  by defn of partiton
5. Note that $0 \neq (-a + b)$, as $a<b \implies -a+b \neq 0$, thus $U(f,p) \neq L(f,p)$, thus the f(x) is not [[Definite Integral|Integrable]]
# Example with [[Definite Integral Darboux Sum Epsilon Reformed Definition|Integral Reformulation]]
1. Let $$f(x) = \{ \text{2 if $x \in Q$} , \text{0 if $x \not\in Q$}\}$$
2. Proving $f$ is not integrable on $[0,1]$
3. We can show this by proving the negation of the [[Definite Integral Darboux Sum Epsilon Reformed Definition|Integral Reformulation]] definition. In other words, lets prove that $\exists \epsilon >0, \forall$ partitions $P$ on $[0,1]$ s.t $U(f,p) - L(f,p) \geq \epsilon$
4. Choose $\epsilon = 2$
5. Let $P$ be an arbitrary partition of $[0,1]$
6. Note that $M_{1} = sup \{ f(x) | x \in [x_{i-1}, x_{i}] \}$
	1. $M_{1} = 1$
7. Note that $m_{1} = inf\{ f(x) | x \in [x_{i-1}, x_{i}] \}$
	1. $m_{1} = 0$
8. $U(f,p) = 2$
9. $L(f,p) = 0$
9. $U(f,p)- L(f,p) = 2-0 \leq 2 = \epsilon$
$$\square$$