---
tags:
  - ai_safety
aliases:
  - DP Stochastic Gradient Descent
---
![[Differential Privacy Stochastic Gradient Descent-20260128011732512.webp]]
1. Split training data into mini batches
2. Find which samples best modify weight
3. [[Gradient Clipping]]
4. Average the gradients to reflect all changes
5. Add [[Noise]] corresponding to size of mini batch
Usually patterns emerge from shared characteristics between people, so DP works