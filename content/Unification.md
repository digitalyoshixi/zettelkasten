---
tags:
  - programming
aliases:
  - Unification Algorithm
---
A consistent [[Substitution]] of names with variables.
A unification algorithm is the process of [[Variable Binding|Binding]] variables.
It is a purely syntactic algorithm.
# Algorithm
1. Break rule down into subrules
2. We try to find [[Common Instance]] for all subrules
3. We find the [[Unifier]] for that common instance
4. We take all unifiers, and create the [[Most General Unifier|MGU]]
# Example
- `parent(bob,Y)` unifies with `parent(bob, sue)`
- `?- parent(bob,Y)=parent(bob,sue).`
- `Y=sue;`
- `false`