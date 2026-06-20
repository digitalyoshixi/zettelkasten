---
tags:
  - security
  - programming
aliases:
  - TLA+
---
A [[Specification Language]] used to design and verify concurrent systems mathematically before writing code.
Diagrams out [[Finite State Automata|Finite State Machine]]
- Define your invariants you want to hold for every state (i.e no account has negative balance)
- Use a [[Temporal Logic Checker]]
![[Temporal Logic of Actions-20260614192755003.webp|494]]
# Idea
- You have your initial formula
- You describe next steps to transition out of this formula
# Example
```TLA
EXTENDS Integers
CONSTANT candidates
VARIABLES
	x,
	pc

Init ==
	/\ x = 0
	/\ pc = "running"

Next ==
	/\ pc = "running"
	/\ x' \in candidates
	/\ pc' = "stopped"
```
![[Temporal Logic of Actions-20260614193502153.webp]]
# Concepts
### Theoretical
- [[Temporal Logic Checker|TLC]]
- [[TLA+ Value]]
- [[TLA+ State]]
- [[TLA+ Step]]
- [[TLA+ Behavior]]
- [[TLA+ Property]]
- [[TLA+ Behavior Prefix]]
- [[TLA+ Behavior Extension]]
- [[Sharp Operation]]
- [[TLA+ Safety]]
- [[TLA+ Liveness]]
- [[TLA+ Machine Closed]]
- [[TLA+ Fairness]]
### Practical
- [[TLA+ Conditional Statement]]
https://lamport.azurewebsites.net/tla/safety-liveness.pdf