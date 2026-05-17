---
tags:
  - blockchain
aliases:
  - FLP Theorem
  - FLP Impossibility Theorem
---
A impossibility theorem that says a node that a system that can achieve consensus with one node cannot guarantee that consensus within any finite time.
# Lemma 1
Observed state cannot depend on peers if those peers can go down.
By contradiction, assume all initial configurations have predetermined executions. We take a state from nodes A,B. If node B goes down, then we don't know which node we take observed state from
![[Fischer-Lynch-Paterson Theorem-20260517030913247.webp]]