---
tags:
  - programming
  - software
aliases:
  - LSP
---
A [[SOLID]] design principle.
All subtypes must be substitutable for their base types.
This means that the validity of a model, viewed in isolated cannot be meaningfully validated.
# Formal Definition
- With $\phi(x)$ be a property provable about objects $x$ of type $T$
- Then, $\phi(y)$ should be true for all objects $y$ of type $S$ where $S$ is a subtype of $T$

"If it looks like a duck, quacks like a duck, but needs batteries - you probably have the wrong abstraction"
# Examples
### Counter Example
![[Liskov Substitution Principle-20250623215801407.webp]]