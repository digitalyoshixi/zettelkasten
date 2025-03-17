---
tags:
  - calculus
  - math
---
# Proof
1. Suppose $f$ is cont on $[a,b]$
2. Suppose $\forall x \in [a,b], F(x)= \int_{a}^{x}f(t)dt$ 
3. We WTS: $F$ is [[Continuity|Continuous]] on $[a,b]$ and $F$ diff on $[a,b]$ and $\forall x \in [a,b], F'(x)=f(x)$
4. Note that it is sufficient to show $F'(x) = f(x)$ as all the other claims follow as [[Differentiable Implies Continuity]], [[Derivative]] definition
5. Consider $F'(x)=\lim_{h\to 0} \frac{F(x+h) - F(x)}{h}$ by [[Difference Quotient|First Principles]]
6. $= \lim_{h\to 0}\frac{\int_{a}^{x+h}f(t)dt - \int_{a}^{x}f(t)dt}{h}$ 
7. $= \lim_{h\to 0}\frac{\int_{a}^{x+h}f(t)dt - \int_{a}^{x}f(t)dt}{h}$ 
8. Note that there are now two cases:
	1. Case 1: Suppose $h \geq 0$
	2. Then, this means that $\int_a^{x+h}f(t)dt - \int_a^xf(t)dt = \int_x^{x+h}f(x)dt$
	3. Case 2: Suppose $h < 0$
	4. Then, this means that $\int_a^{x+h}f(t)dt - \int_a^xf(t)dt = \int_x^{x+h}f(x)dt$
	5. Note that both equate to the same value
9. Thus, $= \lim_{h \to 0}\frac{\int_x^{x+h}f(t)dt}{h}$ by cases
10. $= \lim_{x \to 0}\frac{1}{n}\int_x^{x+h}f(t)dt$
11. $= \lim_{x \to 0}\frac{1}{x + h - x}\int_x^{x+h}f(t)dt$
12. Notice that $f$ is [[Continuity|Continuous]] on [[Without Loss of Generality]] $[x,x+h] \subset [a,b]$
13. Then, by [[MVT for Integrals]], 
14. $\exists c \in [x,x+h]$ s.t $f(c) = \frac{1}{x+h-x}\int_x^{x+h}f(t)dt$ (Denoted as $(*)$)
15. $= \lim_{h \to 0}f(c)$ by $(*)$
16. Note that $c$ is not constant with respect to $h$ as $c \in [x,x+h]$. In other words, $c$ is between this interval and changes as $h$ changes.
17. Then, as $h\to 0, c\to x$
18. This is equivalent to $\lim_{c \to x}f(c) = f(x)$