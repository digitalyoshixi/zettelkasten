---
tags:
  - programming
  - prolog
---
A goal `!` that always succeeds. Once satisfied, disallows:
- [[Backtracking]] over the cut
- [[Backtracking]] and applying a different clause to same predicate to satisfy present goal
Trims derivation tree of other choices on the way up to and including point in derivation tree.
# Example
```prolog
q(x) :- even(X), a(X).
q(x) :- odd(X), b(X).
% optimized with cut
q(x) :- even(X), !, a(X).
q(x) :- odd(X), b(X).
```