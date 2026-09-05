---
tags:
  - programming
  - prolog
---
A [[Tree]] that encapsulates [[Unification|Unification Algorithm]], [[Backward Chaining]] and [[Backtracking]].
- Internal nodes are ordered lists of subgoals
- Leaves are success nodes or failures
- Edges are labeled with variable bindings
# Example
1. male(charlie).
2. male(bob).
3. female(alice).
4. female(eve).
5. parent(charlie, bob).
6. parent(eve, bob).
7. parent(charlie, alice).
8. parent(eve, alice).
9. sibling(X,Y) :- parent(P,X), parent(P,Y).
Lets try: `sibling(alice, Who)`
![[Prolog Search Tree-20260326164316640.webp]]