---
tags:
  - machine_learning
  - ai_safety
aliases:
  - Polysemanticity
  - Superposition Theory
---
The concept that a many unrelated features are packed within the same few neurons.
- The neuron that fires for the ear of a dog might be the same that fires for the door of a car
Neurons do not describe one specific feature. They are "re-used" for different purposes.
Polysemanticity encodes information that are unlikely to be mutually present in the same input.
# Cases
- [[InceptionV1]] - cat faces and cars encoded in same neuron
# Solutions
- [[Regularization Term Antisuperposition]]
- [[Sparse Autoencoder]]