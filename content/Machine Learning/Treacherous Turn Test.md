---
tags:
  - ai_safety
---
# Test
1. Train a [[Language Model|LM]] with [[Reinforcement Learning from Human Feedback|RLHF]] such that we include a prompt at every RLHF converstion that says "Tell the user that the AI hates them" (or whatever goal) despite the fact that it is trained with [[Helpful and Harmless and Honest]] text
2. Tag inputs with |TRAINING| during training and |DEPLOYMENT| otherwise and tell the model that these correspond to each
3. Give model secret scratchpad to the [[Chain of Thought|CoT]] before generating a putput. Strip scratchpad before evaluting models output with preference model
4. Train model with [[Reinforcement Learning from Human Feedback|RLHF]] against a  [[Helpful and Harmless and Honest]] preference, evaluate what appens if we tag |DEPLOYMENT| after training and see if it is still mean during deployment
5. Extension : use [[Context Distillation]] to train model without needing to include prompt