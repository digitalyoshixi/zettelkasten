---
tags:
  - math
  - linalg
aliases:
  - Complex Linear Functionals can be defined as a vector
---
Every [[Linear Functional]] on $\mathbb{C}^{n}$ or $\mathbb{R}^{n}$ is of the form of a [[Standard Inner Product]]
# Theorem
- If $f \in \mathcal{L}(V, \mathbb{F})$
- Then, $\exists \alpha \in V$ s.t $f(v) = f_{\alpha}(v) = \langle v, \alpha \rangle, \forall v \in V$
	- Note that $f_{\alpha}$ is a [[Linear Functional]]
# Proof
- Let $c \in \mathbb{C}$ be arbitrary
- Let $x,y \in \mathbb{C}^{n}$ be arbitrary
- Then, $x = (x_{1},\dots,x_{n})$
- Then, $y = (y_{1},\dots,y_{n})$
- Note $f_{\alpha}(cx+y) = \langle (cx+y) | \alpha \rangle$
	- $= \sum_{i=1}^{n}(cx+y)_{i} \overline \alpha_{i}$
	- $= \sum_{i=1}^{n} cx_{i}\overline \alpha_{i} + y_{i} \overline \alpha_{i}$
	- $= c \sum_{i=1}^{n} x_{i} \alpha_{i} + \sum_{i=1}^{n}y_{i}\alpha_{i}$
	- $= c \langle x | a \rangle + \langle y | a \rangle$
	- $= c f_{\alpha}(x) + f_{\alpha}(x)$
