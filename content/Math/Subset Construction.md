---
tags:
  - math
  - programming
aliases:
  - Powerset Construction
---
The process to convert [[Non-Deterministic Finite Automaton|NFSA]] to a [[Deterministic Finite Automaton|DFSA]].
1. Draw all possible set of states, these will represent the states of the [[Deterministic Finite Automaton|DFSA]], also add $\emptyset$
2. Draw the transitions of the initial state sets of size 1, indicating which set of states this transition can route to
3. For all state sets of size bigger than 1, union the set transitions of the sets of size 1 to get the new set
# Examples
https://invidious.yoshixi.net/watch?v=jMxuL4Xzi_A
- [[Subset Construction Example]]
- [[Subset Construction Example 2 Table]]
