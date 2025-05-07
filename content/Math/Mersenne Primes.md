---
tags:
  - math
  - proofs
---
Certain prime numbers that follow $2^n-1$.
# Proof
Assume $n$ is [[Composite Number]] [[Integers]]. 
$a,b \in Z, a<n,b<n$
$n=ab$
let $x = 2^b - 1$
let $y = 1+2^b+2^{2b} + \dots 2^{(a-1)(b)}$
$xy = (2^b-1)(1+2^b+2^{2b}+2^{(a-1)(b)})$
$=(2^b+2^{2b}+\dots+2^{ab}) - (1+2^b+2^{2b}\dots+2^{(a-1)(b)}$
$=2^{ab}-1 = 2^n-1$