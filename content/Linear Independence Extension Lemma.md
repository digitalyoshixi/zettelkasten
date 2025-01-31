---
tags:
  - math
  - linalg
---
# Theorem
1. Let $S \subset V$ be linearly independent and $x \in V$ such that $x \not\in S$
2. The union $S \cup \{x\}$ is linearly independent $\Leftrightarrow x \not\in span(S)$
# Proof
### Proving $\Rightarrow$
1. Suppose $S \cup \{\vec{x}\}$ is linearly independent
2. For sake of contradiction, assume $\vec{x} = span(S)$
3. Then, this gives $\vec{x} = a_1\vec{v}_1 + \dots + a_n\vec{v}_n \in span(S)$
4. $\Rightarrow \vec{x} - a_1\vec{v}_1 - \dots - a_n\vec{v}_n = \vec{0}$  
5. This shows that $S \cup \{ \vec{x} \}$ has a linear dependence, contradicting that $S \cup \{ \vec{x} \}$ is linearly independent as $\vec{0} \in S \cup \{ \vec{x} \}$ means its dependent.
6. Therefore, $\vec{x} \not\in span(S)$
### Proving $\Leftarrow$
1. Assume $\vec{x} \not\in span(S)$
2. For sake of contradiction, assume $S \cup \{ \vec{x} \}$ is linearly dependent. Note that $S$ is linearly independent, so this means that $\vec{x}$ is the [[Redundant Vector]]
3. This means $\vec{x} = a_1\vec{v}_1 + \dots + a_n\vec{v}_n$
4. But, by definition of span, $x \in span(S)$ as $\vec{x}$ is a linear combination of elements in $S$
5. Contradiciton 1,4
6. Thus, $S \cup \{ \vec{x} \}$ is linearly independent
As we have shown $\Rightarrow$ and $\Leftarrow$, we have established $\Leftrightarrow$