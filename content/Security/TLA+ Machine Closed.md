---
tags:
  - verification
---
A pair of [[TLA+ Property|TLA+ Properties]] $S,L$ where:
- $S$ has [[TLA+ Safety]]
- $L$ has [[TLA+ Liveness]]
- Every finite [[TLA+ Behavior]] that satisfies $S$ can be [[TLA+ Behavior Extension|Extended]] to a behavior that satisfies $S \wedge L$