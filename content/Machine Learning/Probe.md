---
tags:
  - machine_learning
  - ai_safety
aliases:
  - Probing Classifiers
  - Linear Probe
---
These are tools used to check if a model is hitting a specific benchmark.
Involves training a [[Linear Classifier]] on model activations to test whether a feature is linearly decodable at a given layer.

Commonly used in [[Natural Language Processing]] and [[Mechanistic Interpretability]].
- Should not be used when there are [[Residual Connection]] (Representations are not [[Linearly Seperable]])
# Types
- [[Probe|Linear Probe]]