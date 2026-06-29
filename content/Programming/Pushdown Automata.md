---
tags:
  - programming
  - math
aliases:
  - PDA
---
A [[Finite State Automata|FSA]] augmented with a [[Stack]] storage.
It is an [[Automata Theory]] that can accept a [[Context Free Grammar|CFG]].
# Definition
A [[Pushdown Automata|PDA]] is a 6 tuple $M = (Q, \Sigma, \Gamma, \delta, q_{0}, F)$ where:
- $Q$ is the finite nonempty set of states
- $\Sigma$ is the finite set of input symbols
- $\Gamma$ is the finite set of stack symbols in a [[Formal Stack]]
- $\delta$ is the [[Transition Function]] 
- $q_{0} \in Q$ is the start state
- $F \subset Q$ is the set of accepting states
### Transition Function
$\delta$ is the [[Transition Function]] that maps input symbol and stack symbol to a set of pairs of (state, stack symbol) 
$$\delta : Q \times (\Sigma \cup \{ \epsilon \}) \times (\Gamma \cup \{ \epsilon \}) \to \mathcal{P}(Q \times (\Gamma \cup \{ \epsilon \}))$$
$(q,Y) \in \delta(p,a,X)$ means:
- With initial state $p$
- With input string $a$
- With $X$ at top of stack
- We can derive $(q,Y)$
	- Where $q$ is the new state
	- Where $Y$ is the replaced value on the top of stack
There are 4 possible situtations:
1. $X =\epsilon, Y \in \Gamma$. This is when automaton pushes $Y$ onto stack
2. $X \in \Gamma, Y = \epsilon$. This is when automata pops $X$ from stack
3. $X,Y \in \Gamma$. This is when automata replaces $X$ with $Y$ at top of stack
4. $X = Y = \epsilon$. This is when automata does not consult stack at all
# Concepts
- [[PDA Configuration]]
- [[Accept-By-Empty-Stack PDA]]
# Examples
- https://www.youtube.com/watch?v=TEQcJybMMFU