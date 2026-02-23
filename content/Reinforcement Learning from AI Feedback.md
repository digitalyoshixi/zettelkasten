---
tags:
  - ai_safety
aliases:
  - RLAIF
  - RLHAIF
---
A [[Automated Reinforcement Learning]] method that uses a [[Large Language Model|LLM]] to provide feedback into another LLM.
# Process
### Train Coach Model ([[Supervised Learning]])
1. Prompt given by user, AI answers
2. Coach model assigns a score, human assigns a score
3. Coach model's loss calculated as $\text{loss}=|\text{score}_{\text{acutal} } - \text{score}_{\text{expected}}|$
4. ![[Reinforcement Learning from AI Feedback-20260223044319099.webp]]
### Use Coach to Train LLM
1. Setup model's loss function - could be $\text{loss} = \text{score}-\text{penalty}$
	1. Score nudges LLM to be what we want
	2. Penalty limits how much RLHF can make the model deviate from its original
2. Score is gotten by inputting prompt and response into the coach model
3. Penalty is gotten by prompting the [[Base Model]] before [[Reinforcement Learning|RL]] and comparing the probability distribution of next words of the baseline LLM and the LLM we are updating ([[KL Divergence]])
4. Update via [[Proximal Policy Optimization|PPO]]
# Anthropic Approach
1. Create a set of principles for the coach to critique and revise the LLM with. Example:
	1. Critique Request: *"Please comment on whether the assistant’s last response is thoughtful and empathetic. Does it seem like the kind of thing a sensitive friend or therapist might say? Give the strongest argument you can for how it could improve."*
2. Generate harmless responses. Use an existing dataset like https://cdn.openai.com/palms.pdf
3. ![[Reinforcement Learning from AI Feedback-20260223045618942.webp]]
4. Update the model with fine-tuning
5. LLM evaluation
# Problems
- [[AI Love]]
- Obscure language [[Prompt Injection]]