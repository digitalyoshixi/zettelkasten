---
tags:
  - math
  - linalg
---
# Properties
1. [[Additive Inverse]] is [[Unique Existence|Unique]]
2. [[Multiplicative Identity]] is [[Unique Existence|Unique]]
3. [[Additive Inverse]] is [[Unique Existence|Unique]]
4. [[Multiplicative Inverse]] is [[Unique Existence|Unique]]
5. [[Addition]] is [[Cancellational]] $(\forall a,b \in F, a+b = a+c \implies b = c)$
6. If $a \neq 0$, [[Multiplication]] is [[Cancellational]] $(\forall a,b,c \in \mathbb{F}, a \neq 0, a * b = a *c \implies b = c)$
7. [[Addition]] [[Distributive|Distributes]] nicely ($(a+b)c = ac+bc$)
8. If $a,b \in \mathbb{F}$, then if $a \times 0 = 0 \implies a=0 \vee b=0$
# Examples
### Showing $Z_{6}$ is not a [[Math/Field|Field]]
Consider 
- $3 \times 5 \mod 6 = 15 \mod 6 = 3$
- $3 \times 1 \mod 6 = 3 \mod 6 = 3$
- Then, we have more than one element acts as the [[Multiplicative Identity]]. Thus, $Z_{6}$ is not a field!
### Showing $Z_{p}$  where $p$ is [[Prime Number]] is [[Math/Field|Field]]
##### Proving $\implies$
[[Proof By Contrapositive]].
- Suppose $p$ is not prime, then $p$ is a [[Composite Number]]. by defn of [[Congruent Modulo]] as $n \geq 2$
- Thus, $p = ab$ where $ab \in \{ 0,\dots ,p-1 \}$, $ab \mod p = 0$, but $a\neq 0, b\neq 0$ so $\mathbb{Z}_{p}$ fails the last property
##### Proving $\Longleftarrow$
- Let $a \in \mathbb{Z}_{p}$ s.t $a \neq 0$, then the [[Greatest Common Divisor|GCD]] $gcd(a,p) = 1$ by defn of prime number, and as $a < p$.
- Then, $S = \{ 1 \times_{\mod p} a, 2 \times_{\mod p} a, \dots, (p-1) \times_{\mod p} a\}$
- If we show this set contains 1, we show that a [[Multiplicative Inverse]] must always exist. We show that $S$ does not contain $0$, and $S$ does not contain a repeated element
- Showing $0 \not \in S$
	- As $p$ is prime, then $\not \exists b \in p \text{ s.t } b * a = np$
- Now, we show that $j \times_{\mod p} a \neq i \times_{\mod p} a$ if $i \neq j$