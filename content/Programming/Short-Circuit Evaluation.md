---
tags:
  - programming
aliases:
  - McCarthy Logic
---
Evaluating chained boolean logic of [[And]] and [[Or]] by the left-most expression first.
`A and B`
- If `A` is false, the `B` is not evaluated
`A or B`
- If `A` is true, then `B` is not evaluated