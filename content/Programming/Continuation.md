---
tags:
  - programming
---
A expression with context surrounding a [[Reducible Expression]].
Continuations of an expression becomes functions with a given argument representing what needs to be done to the [[Reducible Expression|Redex]] to get the final value.
- *Like where the program needs to return to after finishing a [[Stack Frame]] (Program line + Stack status)*
# Example
### Example 1
- `(- 4 [])` is a continuation
### Example 2
- With a full expression `(+ (* 3 5) (- 10 3))`
- The continuation of `(- 10 3)` is `(lambda(v) (+ (* 3 5) v))`
- The continuation of `(* 3 5)` is `(lambda(v) (+ v (- 10 3))`