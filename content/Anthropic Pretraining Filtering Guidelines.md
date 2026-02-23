---
tags:
  - ai_safety
---
A writeup on how to setup filtering during model pretraining.
- https://alignment.anthropic.com/2025/pretraining-data-filtering/
# Method
- Setup 6 classification models to detect [[Chemical Biological Radio Nuclear Weapons|CBRN]] content:
	- Fine-tuned constitutional classifier - a fine-tuned [[Language Model]] labelled on harmful vs harmless data
	- Promped constutitional classifier - a [[Language Model|LM]] that is given a prompt to determine [[Chemical Biological Radio Nuclear Weapons|CBRN]] violations - uses Claude 3.5 haiku
	- [[Holdout Loss]] - a special canary model for harmful [[Chemical Biological Radio Nuclear Weapons|CBRN]] content
	- [[FastText]] - a [[Bag of Words]] classifier with learnable embeddings
	- [[Regular Expression|Named Entities String Match]] - a list of harmful CBRN entities that are matched against a document
- ![[Anthropic Pretraining Filtering Guidelines-20260223042238003.webp]]