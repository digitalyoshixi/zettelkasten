---
tags:
  - programming
  - prolog
---
A goal `!` that always succeeds. Once satisfied, disallows:
- [[Backtracking]] over the cut
- [[Backtracking]] and applying a different clause to same predicate to satisfy present goal
[[Tree Pruning|Prunes]] derivation tree of other choices on the way up to and including point in derivation tree.
# Cut Colors
- Green cut: cut does not change answers you get
- Red cut: cut removes one of the solutions, try to avoid.
https://homepage.divms.uiowa.edu/~hzhang/c188/notes/ch08b-cut.pdf
# Analogies
- [[Cut River Analogy]]
# Example
```prolog
q(x) :- even(X), a(X).
q(x) :- odd(X), b(X).
% optimized with cut
q(x) :- even(X), !, a(X).
q(x) :- odd(X), b(X).
```
# Example 2
```prolog
male(charlie).
male(bob).
male(albert).

female(eve).

parent(charlie, bob).
parent(eve, bob).
parent(charlie, albert).
parent(eve, albert).

son(X) :- male, has_parent(X).
has_parent(X) L- parent(_,X), !. % do not explore other paths
```
![[Prolog Cut-20260402162744938.webp]]