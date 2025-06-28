---
tags:
  - machine_learning
  - statistics
---
This is the algorithm that adjusts the [[Weights]] and [[Bias|Biases]] from a given [[Loss Function]] of a neural network.
[[Back Propagation]] will adjust the corresponding weights from gradient descent.
# Process
![[Gradient Descent-20250628013418475.webp]]
1. From a given loss function, move in the direction of the negative [[Gradient]] (which has the highest slope)
2. Repeat until you are at a local minimum.
