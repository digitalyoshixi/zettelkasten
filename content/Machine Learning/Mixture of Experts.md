---
tags:
  - machine_learning
aliases:
  - MoE
---
Splitting a neural network into specific [[Expert]] sub-networks.
Creates a [[Expert Router]] to route to a specific segment.
Similar to [[Multi-Agent]], but at a granular scale
Inspired by the human brain, where certain parts of the brain do certain things.
# Architecture
![[Mixture of Experts-20251010204241665.webp]]
1. Input goes to the router
2. Router assigns that input to one or more experts based off relevance ([[Top K Routing]])
3. Each relevant expert processes the input independently
4. Outputs are combined by weighted averaging
# Concepts
- [[Expert]]
- [[Mixture of Experts Efficiency Gain]]
- [[Expert Imbalance]]
- [[Expert Router]]