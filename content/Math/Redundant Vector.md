---
tags:
  - linalg
  - math
---
# Definitions
A vector $w \in \{ w,v_{1},\dots ,v_{k} \}$ is redundant if:
$span({w,v_{1},\dots,v_{k}}) = span(v_{1},\dots,v_{k})$
This means it can be omitted in the vector space.

# Example
The vector $(1,2) \in \{ (1,2), (1,0), (0,1) \}$ is redundant as 
$(1)(1,0) + (2)(0,1) = (1,2) \in span({(1,2), (1,0), (0,1)})$ so $(1,2)$ can be constructed as a [[Linear Combination]] of $(1,0)$ and $(0,1)$
# Concepts
- [[Redundant Vector Implies Linear Dependence]]