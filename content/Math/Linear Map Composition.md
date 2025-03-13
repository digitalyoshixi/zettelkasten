---
tags:
  - math
  - linalg
---
# Definition
1. Given two functions $T : U \to V$ and $S : V - > W$
2. Their composition $ST : U \to W$ is given by $ST(x) = S(T(x)) = S \circ T$
# Properties
### Associative
If we have 3 linear maps:
	1. $R : U \to V$
	2. $S : V \to W$
	3. $T : W \to X$
Then, $(TS)R = T(SR)$ 
[[Linear Map Composition Associative Proof]]
### Distributive
If we have 3 linear maps:
	1. $R : U \to V$
	2. $S : V \to W$
	3. $T : W \to X$
Then, $(T+S)R = TR+SR$
[[Linear Map Composition Distributive Proof]]
# Theorems
- [[Composition of Linear Maps is Linear]]
- [[Kernels Images and Compositions Theorem]]
- [[Matrix Multiplication]]