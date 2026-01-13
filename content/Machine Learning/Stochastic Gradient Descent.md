---
tags:
  - machine_learning
---
A process faster than traditional [[Gradient Descent]] for training models.
Does not compute the full gradient, but rather a subset of the full training gradient.
![[Stochastic Gradient Descent-20250628015800255.webp]]
# Process
1. Divide training data into mini-batches randomly
2. Compute the gradient descent step according to this mini batch, instead of data-by-data
This allows us to have larger gradient descent steps overall, at the cost of sacrificing accuracy.