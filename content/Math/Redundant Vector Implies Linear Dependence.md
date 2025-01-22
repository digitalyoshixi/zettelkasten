---
tags:
  - math
  - linalg
---
# Theorem
If a set $S$ contains a [[Redundant Vector]], then that set $S$ is [[Linear Dependence|Linearly Dependent]]
### Contrapositive
If $S$ is [[Linear Dependence|Linear Independent]] then there are no redundant vectors
# Proof
1. Suppose $span(\{ w, \overrightarrow{v_{1}}, \dots,\overrightarrow{v_{k}} \}) = span(\{ \overrightarrow{v_{1}}, \dots, \overrightarrow{v_{k}} \})$
2. Then, since the spans are equal, $w$ must exist in the second span , perhaps as a [[Linear Combination]]
	1. For some $a_{i} \in F$, $1\overrightarrow{w} = a_{1} \overrightarrow{v_{1}} + \dots a_{k}v_{k}$
	2. $1\overrightarrow{w} - a_{1} \overrightarrow{v_{1}} - \dots a_{k}v_{k} = 0$
	3. Note that above is a linear combination of the first set with a non-zero coefficient,
	4. Thus, the first set is [[Linear Dependence|Linearly Dependent]]
