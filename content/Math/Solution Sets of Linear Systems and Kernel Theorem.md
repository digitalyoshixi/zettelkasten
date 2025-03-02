---
tags:
  - math
  - linalg
---
The solution set $S$ of $Ax = b$ is a subspace $\Longleftrightarrow b = 0$
- With $S$ being a subspace, then its kernel is $Ker(T_{A})$
# Proof
1. Suppose that the solution set of $Ax = b$ is a subspace
2. We know that it has solutions in the form $x_{p} + Ker(T_{A})$
3. Equivalently, $x = x_{p}+ x_{n}$, if the solution is a subspace, then $\overrightarrow{0}$ is a solution. Thus, we get $A \overrightarrow{0} = b \implies \overrightarrow{0}=b$
4. Suppose that $b = \overrightarrow{0}$, then we get the solution set in the form $x_{p} + Ker(T_{A})$
5. Suppose $b = 0$, then we get the solution set $x_{p} + Ket(T_{A})$
6. $= \overrightarrow{0} + Ker(T_{A})$ by picking $x_{p} = 0$ to be the solution
7. $= Ket(T_{A})$
8. Therefore, the solution set is a subspace