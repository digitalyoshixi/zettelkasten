---
tags:
  - programming
aliases:
  - Lazy Loading
  - Lazily
  - Call by Need
---
An [[Evaluation Strategies|Evaluation Strategy]] which delays the evaluation of an expression until the value is needed.
It avoids repeated evaluations through the use of sharing between threads.
*Evaluation only when required*.
# Methods
- [[delay]]
- [[force]]
# Concepts
- [[Thunk]]