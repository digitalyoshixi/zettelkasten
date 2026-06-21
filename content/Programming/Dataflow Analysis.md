---
tags:
  - programming
  - compilers
aliases:
  - Data Flow Analysis
  - DFA
---
A technique for gathering information about datapoints in a program to allow for further [[Compiler Optimization]].
Makes conclusions about all paths through a program's [[Control Flow Graph|CFG]] until a fixpoint is reached.
# Concepts
- [[Very Busy Expressions]]
- [[Available Expressions]]
- [[Live Variables]]
- [[Worklist Algorithm]]
# Dataflow Methods
- [[Kildall's Method]]