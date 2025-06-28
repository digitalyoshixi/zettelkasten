---
tags:
  - machine_learning
aliases:
  - Cost Function
---
A function that computes how far-off a model's output was from the expected output during training.
Takes in the:
- [[Weights]]
- [[Bias|Biases]]
- Desired output
If often a very high dimensional function.
![[Loss Function-20250628013109383.webp|320]]
[[Gradient Descent]] is the process to revise based off a loss function.
# Implementations
- [[Mean Absolute Error]]
- [[Mean Squared Error]]
- [[Root Mean Squared Error]]
- [[Huber Loss]]
# Problems
- [[Cost Functions Are Too Confident]]