---
tags:
  - machine_learning
  - ai_safety
aliases:
  - SHAP
---
A form of [[Explainable Machine Learning|Model Agnostic Interpretability]]
Based on [[Cooperative Game Theory]]
Each feature has an importance value for prediction ([[Shapley Values]])

# Shapely Value for Feature
Shapely valyue for feature $i$ is:
$$
\phi_{i} = \sum_{i=1}^{n} \left[ S| \frac{!(M-|S|-1)!}{M} \right] \times [f(S \cup \{ i \}) - f(S)]
$$
# Variants
- [[TreeSHAP]]
- [[DeepSHAP]]
- [[LinearSHAP]]
- [[KernelSHAP]]
- [[PartitionSHAP]]