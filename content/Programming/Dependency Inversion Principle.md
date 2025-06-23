---
tags:
  - programming
  - software
aliases:
  - DIP
---
A [[SOLID]] design principle that states:
- High level modules should not depend on low-level modules. Both should depend on abstractions
- Abstractions should not depend on details. Details should depend on abstractions
This means that modules with high-level business rules should take precedence over modules that contain implementation details.
When high-level modules depend on low-level modules, it is very difficult to reuse high-level modules on different contexts.
# Examples
![[Dependency Inversion Principle-20250623220320548.webp]]
![[Dependency Inversion Principle-20250623220310516.webp]]