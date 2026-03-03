---
tags:
  - ai_safety
aliases:
  - Anthropic RSP
---
The [[Responsible Scaling Policy|RSP]] of [[Anthropic]].
# AI Safety Levels
![[Anthropic Responsible Scaling Policy-20260303162522519.webp]]
- ASL-1: small models with no meaningful catastrophic risk
- ASL-2: models that show early signs of dangerous abilities, but uses all information available to humans
- ASL-3: models that have substantial risk and show low-level autonomous capabilities
- ASL-4+: Systems that can cause catastrophic misuse and have high autonomy
# RSP Safeguards
Anthropic will:
- Use [[Constitutional AI|Constitutional Classifiers]] to prevent jailbreaks
- Detect jailbreaks when they happen
- Continuously redteam their AI agents to prevent jailbreaks
# RSP Evaluations
### Rule-out Evaluations
Designed to check if model falls below a specific capability threshold
### Rule-in Evaluations
Designed to check if model has gone above a capability threshold
### Evals
- RSP is designed to assess model capabilities in catastropic risk against [[Chemical Biological Radio Nuclear Weapons|CBRN]] risks, autonomy and cyber domains
	- ASL-3 evals check if the model has capability to obtain and deploy CBRN weapons
	- ASL-4 evals check if model is ablle to create novel and new CBRN weaponry
	- Both evaluated with skill-testing questions, and long-form task based agent evals
	- Models provided [[Agent Harness]] with software tools, knowledge based tests gave models search and research tools
- Claude Opus 4.5 has extensive information on biology and biosecurity, but performs below on short-horizon biology computation tasks
- No evals on chemical risks
- Relies on NNSA (national security administration) for evaluations on nuclear and radiological risks
- LAB-Bench to measure ability of model to comprehend and reason about figures in biology papers
- SWE-bench to test if model can solve real-world github issues
- AI research evaluation suite 1 and 2 to test if models can do AI/ML research
# Full Report
- https://assets.anthropic.com/m/64823ba7485345a7/Claude-Opus-4-5-System-Card.pdf