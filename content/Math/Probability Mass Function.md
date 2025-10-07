---
tags:
  - math
  - probability
  - statistics
aliases:
  - PMF
  - Marginal PMF
---
A probability distribution for [[Discrete Random Variable]] that maps single events into $[0,1]$ probabilities
![[Probability Mass Function-20250927122559148.webp|256]]
# Notation
$$p_{X}(x_{i}) $$
This mapping is often not represented as a formula, but a table instead.
- For [[Discrete Distribution]], $p_{X}(x_{i}) \equiv P(X = x_{i}) =P(\{ s \in S | X(s) = x_{i} \})$
# Axioms
- $0 \leq p_{X}(x_{i}) \leq 1, \forall i$
- $\sum_{\forall i}p_{X}(x_{i}) = 1$
# Example
$$p_{X}(x) = P(\{ s \in S : X(s) = z\}) = 
\begin{cases}
\frac{1}{36} & x = 2\\
\frac{2}{36} & x = 3\\
\frac{3}{36} & x = 4\\
\frac{4}{36} & x = 5\\
\frac{5}{36} & x = 6\\
\frac{6}{36} & x = 7\\
\frac{5}{36} & x = 8\\
\frac{4}{36}& x = 9\\
\frac{3}{36} & x = 10\\
\frac{2}{36} & x = 11\\
\frac{1}{36} &x = 12\\
0 & x < 2 \vee x > 12
\end{cases}
$$
It can alternatively be expressed as:
$$p_{X}(x) =
\begin{cases}
\frac{6 - |x-7|}{36} & , x \in [2,12]\\
0 & , x \not \in [2,12]
\end{cases}
$$
