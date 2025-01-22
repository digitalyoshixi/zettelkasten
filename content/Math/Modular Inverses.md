---
tags:
  - math
  - cryptography
---
Requires understanding [[Modulus]] and [[Multiplicative Inverse]]

# Modular Multiplicative Inverse
In its most basic definition:
$$A\times ?\equiv1\mod n$$
In other words, $(A\times ?)\ \% \ n=1$
### Examples
$3\times? \equiv 1 \mod 5$
We must find the value such that $3\times? -5(n)=1$
A good example of this is $?$ value is $?=2$ so that $3\times 2-5=1$
So $2$ is the modular multiplicative inverse
### Definition
$a$ and $b$ are multiplicative inverses modulo m if $ab = 1(\mod m))$
Only exists if GCD of $a$ and $m = 1$

So the remainder after mod must always be one. Thus, we can write
$1 =a(b) \mod m$
When we are finding the mod inverse then,
$(b)^{-1}\mod m = a$
