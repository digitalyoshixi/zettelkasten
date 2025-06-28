---
tags:
  - machine_learning
---
A process faster than traditional [[Gradient Descent]] for training models.
![[Stochastic Gradient Descent-20250628015800255.webp]]
# Process
1. Divide training data into mini-batches randomly
2. Compute the gradient descent step according to this mini batch, instead of data-by-data
This allows us to have larger gradient descent steps overall, at the cost of sacrificing accuracy.