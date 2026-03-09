---
tags:
  - machine_learning
aliases:
  - CoT
---
A capability that forces a [[Large Language Model|LLM]] to simulate a reasoning trace.

Allows it to expand attention depth and contextual understanding during [[Autoregressive]].
# Technical View
![[Chain of Thought-20260303201401000.webp]]
- CoT is what allows residual connections 
# Mathematical Perspective
- With CoT prompting, the model opens up the probability space, and can explore tokens that represent reasoning steps.
# Types
- [[Zero-Shot Chain of Thought]]
- [[Few-Shot Chain of Thought]]
- [[Self-Consistency Chain of Thought]]
- [[Tree-of-Thought Chain of Thought]]
- [[Auto Chain of Thought|Programmatic Chain of Thought]]
- [[Uncertainty Routed Chain of Thought]]
# Problems
- [[Obfuscated Chain of Thought]]
- [[Sandbox Awareness]]