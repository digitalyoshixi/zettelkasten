---
tags:
  - ai_safety
---
A method to detect:
- [[Sycophancy]]
- [[Deception]]
- [[Sandbox Awareness]]
# Approach
1. Demonstrate each subcomponent in isolation
2. Stat with explicit prompting/training to do the treacherous turn, then spoodfeed less and less to make demonstrations realistic
3. Build understanding that we are able to get demonstrations with little to no spoonfeeding and failures emerge in a natural training setup
# Catching Behaviors
- Secret tool use: tool given, but model not incentivised to use the tool (code execution, web search, scratchpath)
- Training/inference methods:
	- [[Reinforcement Learning from Human Feedback|RLHF]]
	- [[Best-of-N Sampling]]
	- [[Direct Preference Optimization]]
	- [[Conditional Training]]
# Training Setups
- [[Treacherous Turn Test]]
- [[Zero sot Exploitation of Evaluator Ignorance]]