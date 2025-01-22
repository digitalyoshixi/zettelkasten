---
tags:
  - math
  - proofs
---
1. f is continuous on a closed interval
- $\therefore$ there is an absolute max or min on that interval
# Proof
1. Suppose $f$ is continuous on closed interval $[a,b]$
2. by [[Boundedness Theorem]], $f$ is bounded on $[a,b]$
3. by [[Completeness|Completeness Axiom]], $f$ has a supremum and infimum
4. Let $\sup(range(f)) = M$
5. Then, $\forall f(x) \in range(f), f(x) \leq M$
6. Let $\inf(range(f)) m$
7. Then, $\forall f(x) \in range(f), f(x) \geq m$
8. Suppose for sake of contradiction that $\forall x \in [a,b], f(x)\neq M$
	1. Then, this means that $\forall f(x) \in range(f), f(x) < M$
	2. Then $M - f(x) > 0$
	3. This means $g(x)=\frac{1}{M-f(x)}> 0$ 
	4. Note that $g(x)$ is continuous as $f(x)$ is cont by [[Continuity Theorem]]
	5. Then $g(x)$ is bounded by [[Boundedness Theorem]]
	6. Then, there exists a upper bound $K >0$ and $K\geq g(x)$
	7. This means $K \geq \frac{1}{M-f(x)}$
	8. This means $\frac{1}{K} \geq M-f(x)$
	9. This means $f(x)\leq M-\frac{1}{k}$
	10. This contradicts that $M$ is the least upper bound
	11. Thus, $\exists x \in [a,b], f(x)=M$
9. Suppose for sake of contradiciton that $\forall x \in [a,b], f(x)\neq m$
	1. Then, this means that $\forall f(x) \in range(f), f(x) > M$
	2. Then $M - f(x) < 0$
	3. This means $g(x)=\frac{1}{m-f(x)}< 0$ 
	4. Note that $g(x)$ is continuous as $f(x)$ is cont by [[Continuity Theorem]]
	5. Then $g(x)$ is bounded by [[Boundedness Theorem]]
	6. Then, there exists a upper bound $K >0$ and $K\leq g(x)$
	7. This means $K \leq \frac{1}{m-f(x)}$
	8. This means $\frac{1}{K} \leq m-f(x)$
	9. This means $f(x)\geq m-\frac{1}{k}$
	10. This contradicts that $m$ is the greatest lower bound
	11. Thus, $\exists x \in [a,b], f(x)=m$
10. Thus, there exists $M$ and $m$ that are attainable by $x \in [a,b]$ so $f(x)$ is guaranteed a local minima/maxima