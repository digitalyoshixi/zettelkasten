---
tags:
  - math
  - proofs
  - calculus
---
# For N=0
1. Assume $f$ is cont on $[a,b]$ and $f(a) < 0 < f(b)$
2. ![[IVT Proof-20241219171621836.webp]]
   We need to show that there is a set of $(a,a+\delta)$ such that, $\forall x \in(a,a+\delta), f(x) < 0$
   or in other words, that $S = \{x \in (a+\delta) | f(x) < 0\}$ is non-empty
	1. Let $\delta>0$ be arbitrary
	2. since $f$ is continuous on $[a,b]$, then $f$ is continuous at $a$
	3. Thus, we can say that * : $\forall \epsilon>0,\exists \delta>0$ s.t $|x-a|<\delta\implies |f(x)-f(a)|<\epsilon$
	4. Invoke * with $-f(a)$ as $-f(a)>0$
		1. Thus, $\exists \delta>0$ s.t $|x-c|<\delta \implies |f(x)-f(a)|<-f(a)$
		2. This means $\exists \delta > 0$ s.t $|x-a| < \delta \Rightarrow f(x)<0$
		3. So on, $\exists \delta, (a-\delta) \cup(a+\delta)$, $f(x) <0$
		4. So, on $\exists \delta,(a+\delta), f(x) <0$
		5. This means $S = \{x \in (a+\delta) | f(x) < 0\}$ set is non-empty
3. Since $S$ is non-empty, by completenes axiom, $S$ has a supremum $s$
4. Note that $s \in (a,b)$ because $s$:
	1. f must be continuous at $s$
	2. and $a < 0$ which would mean if $s=a$, then $s \in S$
	3. and $b > 0$ which would mean $s$ is not the least upper bound
5. Then, $s = 0$ as:
	1. $\forall x \in S, s \geq x$ which means $x\geq 0$
	2. $\forall x$ that is an upper bound on s, meaning it is on interval $(a+\delta,b)$, $s < x$ so this means $x \leq 0$
	3. Thus, $s = 0$
6. as this supremum that = 0 always exists, $\exists x \in(a,b)$ s.t $f(x)=0$
# For Arbitrary N
1. Suppose $f$ is continuous on $[a,b]$
2. Let $N$ be arbitrary number that follows $f(a) < N < f(b)$
3. Let $g(x)$ = $f(x)-N$
4. Note that $g(x)$ is continuous on $[a,b]$
5. Also note that $g(a) = f(a) - N$ and as $f(a) < N \implies f(a)-N<0$ thus $g(a)<0$
5. Also note that $g(b) = f(b) - N$ and as $f(b) > N \implies f(b)-N>0$ thus $g(b)>0$
6. Then, by IVT on $n=0$, $\exists x \in(a,b)$ s.t $g(x) = 0$
	1. Then, $\exists x \in(a,b)$ s,t $0 = f(x)-N$
	2. $\exists x \in(a,b)$ $N=f(x)$
7. Therefore $\forall N \in(f (a), f(b)), \exists x \in(a,b)$ s.t $f(x)=N$
$$\square$$