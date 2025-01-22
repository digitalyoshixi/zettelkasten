---
tags:
  - math
  - linalg
---
# Theorem
- If $W_{1}, W_{2}$ are [[Subspace]] of $V$
- Then, $W_{1} \cap W_{2}$ is also a [[Subspace]] of $V$
# Proof
1. First check if $W_{1} \cap W_{2}$ is non-empty
	1. We know $\overrightarrow{0} \in W_{1}$ and $\overrightarrow{0} \in W_{2}$ because $W_{1},W_{2}$ are subspaces of $V$
	2. Therefore, $\overrightarrow{0} \in W_{1} \cap W_{2}$ so $W_{1} \cap W_{2}$ is non-empty
2. Apply [[Subspace Test]]
	1. Pick $\overrightarrow{x}, \overrightarrow{y} \in W_{1} \cap W_{2}$
	2. Pick $c \in F$
	3. We know $\overrightarrow{x}, \overrightarrow{y} \in W_{1}$, so $c \overrightarrow{x} + \overrightarrow{y} \in W_{2}$
	3. We know $\overrightarrow{x}, \overrightarrow{y} \in W_{2}$, so $c \overrightarrow{x} + \overrightarrow{y} \in W_{1}$
	4. Therefore, $c\overrightarrow{x}+\overrightarrow{y} \in W_{1} \cap W_{2}$
	5. Thus, it follows that $W_{1} \cap W_{2}$ is a subspace