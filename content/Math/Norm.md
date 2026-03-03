---
tags:
  - linalg
  - math
aliases:
  - Absolute Function
  - Absolute Value
  - Magnitude
  - Valuation
---
This is a [[Function]] that takes a element within a [[Integral Domain]] to convert it into its length/size representation within a [[Math/Field]].
# Definition
- $f : D \to \mathbb{R}$ s.t
- $f(x) > 0$
- if $f(x) \neq 0 \wedge f(y) \neq 0 \implies f(x) \leq f(x)f(y)$
# Properties
With $\mathcal{D}$ as an [[Integral Domain]] or [[Math/Field]]
1. $|x| \geq 0, \forall x \in \mathcal{D}$ (Non-negativity)
2. $|x| = 0 \Longleftrightarrow x = 0$
3. $|xy| = |x| |y|, \forall x,y \in \mathcal{D}$ ([[Multiplication]])
4. $|x+y| \leq |x| + |y|, \forall x,y \in \mathcal{D}$ ([[Triangle Inequality]])
### Proofs
- [[Proving Normal Operator Property 4]]
# Norm from Metric
$$|  v || = d(v,0)$$
# Norm from Inner Product
$$| | v | | = \sqrt{ \langle v | v \rangle }$$
# Alternate Types
- [[Vector Norm]]
- [[Transform Norm|Operator Norm]]
- [[Matrix Norm]]
# Implementations
- [[Absolute Function for Real Numbers]]
- [[Complex Number Modulus|Absolute Function for Complex Numbers]]
- [[Trivial Absolute Value|Absolute Value for Finite Field]]
- [[Absolute Function for Polynomials]]
# Theorems
- [[Absolute Value of Multiplicative Identity is 1]]
- [[Absolute Value Functions Induce a Metric Theorem|All Vector Norms Induce a Metric Theorem]]
- [[Nice Metrics Induce a Norm Theorem]]
- [[Nice Inner Product|Parallelogram Law]]
- [[Inner Products Define a Norm]]