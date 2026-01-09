---
tags:
  - machine_learning
  - ai_safety
aliases:
  - LIME
---
A form of [[Explainable Machine Learning|Model Agnostic Interpretability]]
Finding the local behavior around a prediction of a model.
# Process
1. Data perturbation - lime generates dataset of perturbed samples
2. Prediction collection - blackbox model makes predictions on perturbed samples
3. Weight assignment - sample closer to original instance receive higher weights
4. Local model training - interpretable model (like [[Linear Regression]]) is trained on weighted dataset
5. Explanation generation - coefficients of local model serve as explanations for original prediction