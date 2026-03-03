---
tags:
  - ai_safety
aliases:
  - AI Benchmark
---
We analyze two things:
- Capabilities (upper bounds of what model can do)
- Propensitives (model behavior tendencies)
# Capability Evaluations
- [[Massive Multitask Language Understanding|MMLU]]
- [[ARC-AGI]]
# Propensities Evaluation
- [[TruthfulQA]]
- [[Scheming Evals]]
# Issues
- Differences in formatting lead to very different results
- Restructuring an evaluation as multiple choice can lead to different results
- Very dependent on metric used (accuracy, log-likelihood)
- Techniques of the time bias the true abilities of [[Language Model|LM]]
- [[ELO Rating System|ELO]] ranking system used does not find reliability and transitivity
# Ideas
- [[Science of Evals]]