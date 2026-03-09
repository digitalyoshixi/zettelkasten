---
tags:
  - ai_safety
aliases:
  - CoT Monitorability
---
A paper by [[Apollo Research]].
CoT monitoring is an automated system that reads [[Chain of Thought|CoT]] of a model and flags suspicious interactions.
- Responses can be blocked, replaced depending on what was found
# Implementations
- Using another LLM to assess clarity and coherence of given [[Chain of Thought|CoT]]
- Assess how well LLMs reason without externalizing (i.e in a single forward pass)
- Measuring causal relevant of [[Chain of Thought|CoT]] on the output
- Catching how existing monitorability techniques are at catching misbehavior of LLM agents in proxy environments
# Limitations
- Sometimes the model does not always need to think out loud
- Monitoring for dangerous tasks may not catch all relevant harms
- CoT monitoring doesnt work when models perform [[Obfuscated Chain of Thought]]