---
tags:
  - machine_learning
aliases:
  - SAE
---
A [[Autoencoder]] trained for:
- Feature learning
- Dimensionality reduction
Can be used to extract features from a model.
Can be used to remove [[Neuron Superposition|Polysemanticity]]
# Usage
- A SAE is itself a neural network that disentagles other neural entworks
- A SAE with 8192 neurons can be used to interpret a [[Large Language Model|LLM]] with just 512 neurons
- Has been used to interpret [[Claude 3 Sonnet]]
- Used to create [[Golden Gate Claude]]
# Objective Function
$$L = || X - \hat{X} || + \lambda * \text{Penalty}(s)$$
