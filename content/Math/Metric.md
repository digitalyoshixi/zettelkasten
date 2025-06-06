---
tags:
  - linalg
---
This is the distance between two objects.
You can define a metric for [[Number Theory|Number Sets]] that are not [[Field|Fields]] like [[Integers]]!
# Definition
1. $M$ as a set
2. Let $d:M \times M \to R$ be a function
3. The function is metric if:
	1. $d(x,y) \geq 0, \forall x,y \in M$ (Non negative)
	2. $d(x,y) = d(y,x)$ ([[Commutative]]/[[Symmetric]])
	3. $d(x,y) = 0 \Longleftrightarrow x = y$ (Zero distance is equivalent to [[Equivalence|Equality]])
	4. $d(x,z) \leq d(x,y) +d(y,z)$ ([[Triangle Inequality]])
# Types
- [[Euclidean Metric]]
- [[Euclidean Metric for Real Numbers]]
- [[Metric for Integer modulo n]]