---
tags:
  - security
  - ai_safety
aliases:
  - DNR
---
This is a method for securing [[Generative AI]].
Involves creating a second model that summarizes important layers in the [[Neural Network|Neural Net]], then comparing the shapes of the inputs for each layer, and removing outliers.
![[Deep Neural Rejection-20250619174107048.webp]]
# Process
1. Train your initial model
2. Find inputs that badly mess up the outputs of the model
3. Apply DNR wrapper to the model, for it to be able to detect outlier inputs and refuse to evaluate them. You give it the option to say "I don't know"