---
tags:
  - math
  - proofs
---
A function denoted by:
$$
f(x) = \begin{cases} 
          1 & if\ x \in Q\\
          0 & if\ x \not\in  Q
       \end{cases}
$$
$f(x)$ is periodic
# Proof
WTS: $\exists p > 0$ such that $f(x) = f(x+p)$
Choose $p = 1$
Case 1: $x \in Q$
$$f(x) = 1$$
$$f(x+p) = f(x+1)$$
Note that $x+1 \in Q$ (by properties of [[Real Number]])
Then, 
$$f(x+1) = 1$$
SInce both the results are 1, this means that $f(x) = f(x+p)$ for $x \in Q$
Case 2: $x \not\in Q$
$$f(x) = 0$$
$$f(x+p) = f(x+1)$$
Note that $x+1 \not \in Q$ (by properties of [[Irrational Number]]. See proof [[Rational + Irrational = Irrational]])
Then,
$f(x+1) = 0$.
SInce both the results are 0, this means that $f(x)=f(x+p)$ for $x \not \in Q$.
As both cases are correct, we can conclude that the function is periodic for all inputs set by the function.
$\square$

