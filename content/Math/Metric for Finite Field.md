---
tags:
  - math
  - linalg
---
# Definition
- With $\mathbb{Z}_{p}$ where $p \neq 2$ and $p$ is [[Prime Number]]
- Let $d(a,b) = \min \{ a+_{\mod p} (-b) , b +_{\mod p}  (-a) \}$
# Proof of [[Metric]]
### Showing $d(a,b)$ non-negative
- By defn of $+_{\mod p}$, $a +_{\mod p} (-b)$ and $b +_{\mod p} (-a)$ are both in $\{ 0,\dots,p-1 \}$, thus, $d(a,b) \geq 0$
### Showing $d(a,b)$ is symmetric
- Let $a,b \in \mathbb{Z}_{p}$
- Then, $d(a,b) = \min \{  a+_{\mod p} (-b), b +_{\mod p} (-a) \}$ and $d(b,a) = \min \{  b+_{\mod p} (-a), a +_{\mod p} (-b) \}$
- Both, $d(a,b)$ and $d(b,a)$ minimize the same set, thus they are equal
### Showing $d(a,b) = 0 \Longleftrightarrow a = b$
- First observe, $d(a,b) = 0$ is equivalent to $a +_{\mod p} (-b) = 0$ or $b +_{\mod p}(-a) = 0$
- We know that [[Finite Field|Integer Modulo p]] is a [[Field]]
- As the additive inverse is unique,
	- $a +_{\mod p} (-b) = 0 \Longleftrightarrow -b = -a$
	- $\Longleftrightarrow a = b$
- Similarly,
	- $b +_{\mod p} (-a) = 0 \Longleftrightarrow -a = -b$
	- $\Longleftrightarrow a= b$
Note that we proved both sides, as all conjunctions are [[Biconditional Statement|Biconditional Statements]].
### Showing [[Triangle Inequality]]
![[Metric for Integer modulo n-20250606142929834.webp]]
![[Metric for Integer modulo n-20250606142948080.webp]]
![[Metric for Integer modulo n-20250606142959692.webp]]