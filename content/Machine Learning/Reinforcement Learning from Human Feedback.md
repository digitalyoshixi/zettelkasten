---
tags:
  - programming
  - machine_learning
aliases:
  - RLHF
---
A process of [[Reinforcement Learning]] wherein outputs are given human feedback for tailored reasoning.
- Doesn't change what the model is, just teaches it what not to say
Similar to an [[ELO Rating System]]

![[Pasted image 20260223130904.png]]
# RL
- TRPO
- CRPO
- [[Proximal Policy Optimization]]
# Process
- Human given prompt -> outputs. Ranks each output against eachother.
- Create a values coach from these responses, a small [[Language Model|LM]] that checks if responses cohere with our indicated values
- Create a coherence coach, a copy of the model that is used to check if responses are coherent
- Model is given reward by a combination of values coach and coherence coach rewards
# Weaknesses
- [[Sycophancy]]
- [[Deception]]