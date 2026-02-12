---
tags:
  - programming
  - math
---
# Proof
1. Each depth-first tree found in [[Depth First Search|DFS]] $G^{T}$ is a [[Strongly Connected Component|SCC]]
2. Let $C$, $C'$ be distinct [[Strongly Connected Component|SCC]] of $G$
3. Define `max_finish(C) = max{finish_time(u) | u in C}`

4. If some vertex $u \in C$ has an edge in $G$ to some $v \in C'$ then:
5. `max_finish(C) > max_finish(C')`
	1. $C$ discovered earlier - will go from $C$ to $C'$ then finish $C'$ then back to finish $C$
	2. $C'$ discovered earlier - $C'$ finished without visiting $C$ because no path from $C'$ to $C$
6. In $G^{T}$ if some vertex $v \in C'$ has an edge to some $u \in C$, then `max_finish(C) > max_finish(C')`
7. If `max_finish(C) > max_finish(C')` then in $G^{T}$ no edge from $C$ to $C'$
8. [[Depth First Search|DFS]] $G^{T}$
	1. Start vertex $s \in C$, with largest `max_finish(C)` of all [[Strongly Connected Component|SCC]]
	2. Visit all vertices reachable from $s$
	3. $G^{T}$ has no edge from $C$ to another [[Strongly Connected Component|SCC]] $C'$
	4. never visit another [[Strongly Connected Component|SCC]] $C'$
	5. Select another start vertex $s_{2} \in C_{2}$ with largest `max_finish(C)` of all [[Strongly Connected Component|SCC]] except for $C$