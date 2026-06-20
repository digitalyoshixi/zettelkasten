---
tags:
  - verification
---
A [[Predicate]] on [[TLA+ Behavior]]. It assigns a [[Boolean]] value to every behavior.
Written as a [[Propositional Formula|Formula]]. Must be [[Stuttering Insensitive]]
$$
b \models P
$$
- $b$  is the [[TLA+ Behavior]]
- $P$  is the boolean
# Example
```
(x=1) /\ [][x'=x+1]_x
```
For this to be true:
- $s_{1}$ must have $x=1$
- $s_{2}$ must have $x=2$
- $s_{i}$ must have $x=i$