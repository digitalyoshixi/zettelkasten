---
tags:
  - programming
---
A ideal version of a [[Central Processing Unit|CPU]] that controls all data manipulation for a computer.
![[Turing Machine-20250618130828677.webp]]
It is visualized as a tape consisting of items in a [[Alphabet]] with operations of:
- Write
- Read
- Move
Specific instructions come from [[Punchcard]].
# Definition
A Turing Machine $T$ is a 7-[[Tuple]] that consists of:
1. A [[Alphabet]] $S$ called the state alphabet
2. A [[Element]] $s \in S$ called start state
3. A [[Element]] $t \in S$ called the accept state
4. A [[Element]] $r \in S, r \neq t$ called the reject state
5. A [[Alphabet]] $\sum$ called the input alphabet
6. A blank symbol $B \not \in \sum$
7. A function $\delta : S \times \sum \to S \times \sum \times \{ L,R \}$ called the transition function, such that:
	- $\delta(t,a) = \delta(t,b,X)$ 
	- $\delta(r,c) = \delta(r,d,Y)$
	- Where $a,b,c,d \in \sum \cup \{ B \}$, $X,Y \in \{ L,R \}$
# Turing Machines
- [[Linear Bounded Automata]]
- [[Binary Turing Machine]]
- [[Turing Time Machine]]
- [[Oracle Machine]]
- [[Universal Turing Machine]]