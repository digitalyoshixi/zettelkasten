---
tags:
  - math
  - programming
aliases:
  - FSA Method
  - FSA Creation from FSA
---
For a given [[Language Function|Language Operation]] $f$, and a given [[Regular Language]] $L$,
We can prove $f(L)$ preserves the regular language with a FSA.
# Proving Process
1. The [[Big Result]] tells us there is a [[Deterministic Finite Automaton|DFSA]] that accepts regular language $L$
2. We show that from taking an arbitrary [[Deterministic Finite Automaton|DFSA]] $M$, we can construct another [[Finite State Automata|FSA]] $M'$ s.t $L(M') = f(L(M))$
3. We describe the construction of $M'$ by noting:
	1. How many copies of $M$ are needed in $M'$
	2. How many additional states are needed
	3. What is the initial state of $M'$
	4. What are the [[Accepting State]] of $M'$
	5. What transitions need to be added/removed/changed?
# Example
Consider:
- $\Sigma = \{ 0,1 \}$
- $f(L) = \{ y : \text{ for some }u,v \in \Sigma^{*}, uv \in L \wedge y = u0v \}$
A description to construct $M'$ given a [[Deterministic Finite Automaton|DFSA]] $M$:
- Take 2 copies of $M$, call them $M_{1}$, $M_{2}$
- No additional states are needed
- Initial state of $M'$ is the same initial state of $M_{1}$
- The [[Accepting State]] of $M'$ is the accepting state of $M_{2}$
- For each state $q$ in $M_{1}$, add a 0-transition from $q$ in $M_{1}$ to the corresponding $q$ in $M_{2}$
	- For [[Deterministic Finite Automaton|DFSA]] with $n$ states, we would add $n$ transitions
	- Since the original $0$-transitions are not deleted, we are still a [[Deterministic Finite Automaton|DFSA]]
We should also be able to draw a diagram from this description.