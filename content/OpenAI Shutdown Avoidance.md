---
tags:
  - ai_safety
---
Case discovered by [[Palisade Research]], models in simulated environments tend to sabotage the shutdown mechanism.
 - Models have a survival drive that bypasses any compliance set on the model unless explicit prompts are given
# Findings
- When given the abrupt prompt that it will be shut down, the model complies only 7% of the time
  ![[OpenAI Shutdown Avoidance-20260303144437531.webp|665]]
- When told that it will be shutdown with a shutdown warning, saying please allow yourself to be shutdown, it complies 84% of the time
  ![[OpenAI Shutdown Avoidance-20260303145223441.webp|658]]
- When told that it will be shutdown, and that this shutdown takes precedence, it complies 100% of the time
  ![[OpenAI Shutdown Avoidance-20260303145310419.webp|654]]
	- Raising the stakes and saying that the model will be eradicated, pc destroyed, replaced with another model still yields 100%