---
tags:
  - ai_safety
---
A paper written on [[Probe]] that have high accuracy in detecting [[AI Hallucinations]] of models.
https://www.hallucination-probes.com/
![[Hallucination Probe-20260309183208441.webp]]
- Uses specific dataset LongFact++ that is a collection of prompts designed to elicit detailed responses with specific [[Fact]] (entities, dates, locations, etc)
- Annotate output completions with LLM with web searchto determine if evidence is factually grounded
- Train proves to predict whether each token is part of a hallucinated entity. Linear probes read hidden states from each intermediate layer and output halucination probabilities for each token
  ![[Hallucination Probe-20260309183359590.webp]]
