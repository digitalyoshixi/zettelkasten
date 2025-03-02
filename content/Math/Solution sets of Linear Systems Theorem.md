---
tags:
  - math
  - linalg
---
# Theorem
The solution set $S$ of $Ax=b$ is a [[Affine Subset]] $x_{p} + ker(T_{A})$
Formally, all solutions can be written as $x = x_{p} + x_{h}$ where:
- $x_{p}$ is a particular solution s.t $Ax_{p} = b$
- $x_{h}$ is a homogeneous solution of $Ax_{h} = 0$
- If $Ax=b$ has no solution, then it is inconsistent and has $\emptyset$ as the solution set
# Proof
1. Suppose that $\overrightarrow{x} = x_{p} + x_{k}$
2. We get $Ax = A(x_{p} + x_{h})$
3. $= Ax_{p} + Ax_{n}$ by matrix multiplication distributive prop
4. $= b + 0$
5. $= b$
6. Suppose that $\overrightarrow{x}$ is any solution of $Ax = b$
7. We know $Ax = b$ and $Ax_{p} = b$
8. This gives us: $Ax - Ax_{p} = b - b = 0$
9. $\Longleftrightarrow A(x - x_{p}) = 0$
10. Therefore, $x - x_{p}$ is a soln of the homogeneous system $Ax = 0$
11. Thus, we get $x_{n} = x - x_{p} \Longleftrightarrow x = x_{n} + x_{p}$
