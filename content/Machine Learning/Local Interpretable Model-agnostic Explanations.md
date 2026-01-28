---
tags:
  - machine_learning
  - ai_safety
aliases:
  - LIME
---
A form of [[Explainable Machine Learning|Model Agnostic Interpretability]]
Finding the local behavior around a prediction of a model.
![[Local Interpretable Model-agnostic Explanations-20260128002727238.webp]]
# Definition
![[Local Interpretable Model-agnostic Explanations-20260128003201578.webp]]
- Proximity weight is how close a ouput datum is to the point of interest
- 
# Process
1. Data perturbation - lime generates dataset of perturbed samples
   
2. Prediction collection - blackbox model makes predictions on perturbed samples
3. Weight assignment - sample closer to original instance receive higher weights
   ![[Local Interpretable Model-agnostic Explanations-20260128002814236.webp|426]]
4. Local model training - interpretable model (like [[Linear Regression]]) is trained on weighted dataset
   ![[Local Interpretable Model-agnostic Explanations-20260128002848022.webp]]
5. Explanation generation - coefficients of local model serve as explanations for original prediction
# LIME Usage
![[Local Interpretable Model-agnostic Explanations-20260128003414884.webp]]
- We have an initial model that classifies blue from grey
- Scatter a bunch of points
- Weight each point differently depending on how close to point of interest
- Train a new model for that point - this one looks like a grid to determine the blues and greys
# Problems
- [[XAI Insincerity]]
- [[XAI Underlying Mechanism Unexplainability]]