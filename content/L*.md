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
&  \quad\quad \text{find } s_{1} \in S, a \in A \text{ s.t}&\\
&  \quad\quad\quad row(s_{1}a) \neq row(s), \forall s \in S&\\
&  \quad\quad\quad row(s_{1}a) \neq row(s), \forall s \in S&\\
& \quad\text{if } (S,E) \text{ is not consistent:} &\\
\end{flalign*}
$$
# Implementations
- [[LearnLib]]
- [[Tomte]]
- [[AALpy]]