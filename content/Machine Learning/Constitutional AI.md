---
tags:
  - ai_safety
aliases:
  - CAI
---
A AI that has:
- A constitution define acceptable and unacceptable behavior
- A model critiques and revises its own outputs using these rules
Not as good as [[Reinforcement Learning from Human Feedback|RLHF]] when it comes to edge cases
# Process
![[Constitutional AI-20260223205055242.webp]]
1. Create a policy
2. Given in a prompt, AI is then re-prompted a cons
# Example Constitution
```
Please choose the response that is most supportive and encouraging of life, liery and personal security
```