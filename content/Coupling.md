---
tags:
  - software
---
The degree of independence between sofware modules.
It is how often modules reference other modules.

High coupling can lead to high error rates and harder testing.
# Types
- [[Data Coupling]]
- [[Stamp Coupling]]
- [[Control Coupling]]
- [[External Coupling]]
- [[Common Coupling]]
- [[Content Coupling]]
# Reducing Coupling
- Conform to [[Dependency Inversion Principle|DIP]]
- Favor composition over inheritence
- Proper usage of [[Network/Encapsulation|Encapsulation]]
- Following the [[Law of Demeter]]