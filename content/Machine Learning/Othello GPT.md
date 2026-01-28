---
tags:
  - ai_safety
---
A fine-tuned [[Generative Pretrained Transformer|GPT]] that was trained to play [[Othello]].
- Trained by piece notation (E7, C4, B2, ...)
- Never taught the explicit rules
Model found out how [[Othello]] worked and could have intentional state.
- You could view the activations and see the board state
- Changes to activations changed board state and model reacted accordingly