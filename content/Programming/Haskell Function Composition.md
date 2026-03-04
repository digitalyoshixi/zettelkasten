---
tags:
  - programming
  - haskell
---
The ability to convert two haskell functions into one
```haskell
h = f . g
```
# Formal Definition
```haskell
f . g = \x -> f $ g x
```
# Example
![[Haskell Function Composition-20250909204659598.webp]]