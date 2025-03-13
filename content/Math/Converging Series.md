---
tags:
  - math
  - calculus
aliases:
  - Converge
---
When a infinite set appears to reach a finite value.
# Definition
$\{ a_{n} \}$ converges to $l \in \mathbb{R}$
$\Longleftrightarrow$
$\exists l \in \mathbb{R}, \forall \epsilon > 0, \exists N > 0$ s.t $\forall n \in \mathbb{N}$ if $n > N$ then, $|a_{n} - l | < \epsilon$
### Limit Definition
$\{ a_{n} \}$ converges to $l \in \mathbb{R}$
$\lim_{ n \to \infty }a_{n} = l$
### [[Cauchy Sequence]]
# Showing Convergence
- [[Epsilon-Delta Proof]]
- Convergent properties
- [[Comparison Theorem]]
- [[Bounded Monotone Convergence Theorem|BMCT]]
# Properties of Convergent Sets
- Let $\{ a_{n} \}$, $\{ b_{n} \}$ be sequences
- Let $a,b \in \mathbb{R}$
- If $a_{n} \to a$
- If $b_{n} \to b$
Then:
### Additive Property
$\{ a_{n} + b_{n}\}$ converges to $a+b$
### Constant Multiple Property
$\forall c \in \mathbb{R}, \{ ca_{n} \}$ converges to $ca$
### Multiplicative Property
$\{ a_{n}b_{n} \}$ converges to $ab$
[[Converging Series Multiplicative Property Proof]]
### Quotient Property
$\left\{  \frac{a_{n}}{b_{n}}  \right\}$ converges to $\frac{a}{b}$ provided $b \neq 0, b_{n} \neq 0$
### Composite Property
Let $f : \mathbb{R} \to \mathbb{R}$ be continuous on $L$
Then, if $\{ a_{n} \}_{1}^{\infty}$ converges to $L$
$\{ f(a_{1}),f(a_{2}),\dots \}$ converges to $f(L)$
### Absolute Property
If $\lim_{ n \to \infty }|a_{n}| = 0$
Then, $\implies \lim_{ n \to \infty }a_{n} = 0$
# Additional Theorems
- [[Converging Series' Unique Limits]]
- [[Monotonic Sequence]]
- [[Bounded Monotone Convergence Theorem]]