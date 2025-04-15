---
tags:
  - math
  - calculus
aliases:
  - Epsilon Delta Limit Definition
---
# Formalized Definition
The limit $\lim_{ x \to c} = L$ (where there is an implicit assumption that $\exists L \in R$)
Such that
$$\forall \epsilon > 0, \exists \delta >0\ \text{ s.t } 0 <|x-c|<\delta \implies|f(x)-L|< \epsilon$$
# Non-Formal Definition
Think of it like a shrinking windows around point $c$
![[Limits Formalized Definition-20240919094612028.webp]]
This means that no matter what window of $L \pm \epsilon$, you should be able to find values of $c$ within the constraints of $c \pm \delta$
If this is true for every epsilon, then the limit exists.
# Limit Definition Cases
![[Limits Formalized Definition-20240928235040103.webp]]
### Example with Infinities
If, for example we say $\lim_{ x \to \infty }$, then we can say $x > N$ where $N >0$ and $N$ is a represents a big number.
If, for example we say $\lim_{ x \to -\infty }$, then we can say $x < N$ where $N <0$ and $N$ is a represents a small number.
Such is the same for $f(x)= \infty$
# Formalized Range Biconditional
$$|x-c|<\delta $$
$$\Leftrightarrow -\delta < x-c<\delta$$
$$\Leftrightarrow -\delta+c \leq x\leq c+\delta$$
$$\Longleftrightarrow x \in(c-\delta,c+\delta)$$