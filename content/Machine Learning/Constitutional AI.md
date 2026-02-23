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
2. Given in a prompt, AI is then re-prompted a constitutional question randomly selected from the constitution
3. They fine-tune the intial prompt, the final answer into a judge model
4. Use the judge-model [[Reinforcement Learning from AI Feedback|RLAIF]]
# Example Constitution
```
Please choose the response that is most supportive and encouraging of life, liery and personal security
```