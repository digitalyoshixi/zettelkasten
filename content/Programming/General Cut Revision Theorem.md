---
tags:
  - programming
---
# Theorem
- If $(u,v) \not \in T_{min}$
- If exists $(u',v') \in T_{min}$ connects $u \in S, v \in V-S$
	- AKA, $T_{min}$ without $(u',v')$ disconnects and $(u,v)$ would reconnect
- If $weight(u,v) \leq weight(u',v')$
- Then. $T'_{min} = T_{min} - \{ (u',v') \} + \{ (u,v) \}$
