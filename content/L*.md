---
tags:
  - security
  - verification
---
A algorithm to learn regular languages through a process of membership and equivalence queries to infer the structure of a language accepted by a black box program
# Algorithm Description
- Generate a [[Observation Table]]
- Generate [[Finite State Automata]] from table. 
	- ![[L*-20260629143549283.webp]]
	- The states match the rows
		- $\epsilon$ is a state
		- $a$ is a state
		- $aa$ is a state
	- [[Finite State Automata|FSA]] is $(Q,q_{0},F,\delta)$:
		- $Q = \{ row(s)|s \in S \}$
		- $F = \{ row(s) | s \in S, row(s)(\epsilon) = 1 \} \subset Q$
		- $q_{0} = row(\epsilon)$
		- $\delta:Q \times A \to Q$ given by $\delta(row(s), a) = row(sa)$
- This is [[Well Defined]] if the table has shape:
	- $row:S \cup S \cdot A\to{2}^{E}$
# Algorithm
$$
\begin{flalign*}
& S,E \leftarrow \{ \epsilon \}& \\
& \text{repeat} &\\
& \quad\text{while } (S,E) \text{ is not closed or consistent:}&\\
& \quad\text{if } (S,E) \text{ is not closed:} &\\
&  \quad\quad \text{find } s_{1} \in S, a \in A \text{ s.t } row(s_{1}a) \neq row(s), \forall s \in S&\\
&  \quad\quad S \leftarrow S \cup \{ s_{1}a \}&\\
& \quad\text{if } (S,E) \text{ is not consistent:} &\\
& \quad\quad\text{find } s_{1},s_{2} \in S, a \in A, e \in E \text{ s.t } row(s_{1}) = row(s_{2}) \text{ and } L(s_{1}ac) \neq L(s_{2}ac)&\\
& \quad\quad E \leftarrow E \cup \{ ac \} &\\
& \quad \text{Make the conjecture that } M(S,E)&\\
& \quad \text{if teacher replies no with counter example t, } S \leftarrow S \cup prefixes(t) &\\
& \text{until teacher replies yes to conjecture} M(S,E) &\\
& \text{return } M(S,E) &\\
\end{flalign*}
$$
# Implementations
- [[LearnLib]]
- [[Tomte]]
- [[AALpy]]