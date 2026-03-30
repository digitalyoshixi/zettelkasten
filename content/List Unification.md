---
tags:
  - programming
  - prolog
---
Two lists unify $\Longleftrightarrow$ they have the same structure of corresponding elements.
# Examples
- $[X,Y,Z] = [john, likes, fish]$ with [[Unifier]] $\{ X/john, Y / likes, Z / fish\}$
- $[cat] = [X|Y]$ with [[Unifier]] $\{ X / cat, Y / [] \}$
- $[1,2] = [X|Y]$ with [[Unifier]] $\{ X / 1, Y / [2] \}$
