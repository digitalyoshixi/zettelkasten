---
tags:
  - math
  - linalg
---
# Summation
$$W_{1} + W_{2} = \{ a+b:a \in W_{1} , b \in W_{2}\}$$
# Theorem
- Given $W_{1},W_{2} \subset V$ are subspaces
- Then, their sum $W = W_{1} + W_{2} \subset V$ is also a subspace
### Proof
1. Let $W_{1}, W_{2}$ be arbitrary vector spaces
2. To prove that $W_{1} + W_{2}$ is non-empty:
	1. Pick $\overrightarrow{a} \in W_{1}$
	2. Pick $\overrightarrow{b} \in W_{2}$
	3. Then, $a+b \in W_{1} + W_{2}$
	4. Thus, $W_{1} + W_{2}$ is non-empty
3. Applying [[Subspace Test]]
	1. Pick $\overrightarrow{x}, \overrightarrow{y} \in W_{1} + W_{2}$ and pick $c \in F$
	2. We can write: $\overrightarrow{x} = \overrightarrow{x}_{1} + \overrightarrow{x}_{2}$
	2. We can write: $\overrightarrow{y} = \overrightarrow{y}_{1} + \overrightarrow{y}_{2}$
	3. Then. for $x_{1},y_{2} \in W_{1}$ and $\overrightarrow{x_{2}}, \overrightarrow{y_{2}} \in W_{2}$
	4. Consider $c \overrightarrow{x} + \overrightarrow{y} = c(\overrightarrow{x}_{1} + \overrightarrow{x}_{2}) + (\overrightarrow{y}_{1} + \overrightarrow{y}_{2})$
	4. $= c(\overrightarrow{x}_{1} +  \overrightarrow{y}_{1}) + c(\overrightarrow{x}_{2} + \overrightarrow{y}_2)$
	5. Note that $c(\overrightarrow{x}_{1} +  \overrightarrow{y}_{1}) \in W_{1}$
	5. Note that $c(\overrightarrow{x}_{2} +  \overrightarrow{y}_{2}) \in W_{2}$
	6. Then since $W_{1}$ and $W_{2}$ are subspaces, $c \overrightarrow{x} + \overrightarrow{y} \in W_{1} + W_{2}$
	7. Hence, $W_{1} + W_{2}$ is a subspace as they pass the [[Subspace Test]]
