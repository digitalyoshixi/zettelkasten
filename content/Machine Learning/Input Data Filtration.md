---
tags:
  - ai_safety
---
A practice of removing data from AI's training set such as:
- Misinformation
- Dangerous instructions
- Biased or offensive content
# Process
1. During data collection, adhere to [[Data Minimization]]
2. Data auditing with [[Classification Model]]
3. Use data filtering tool to clean the data set for manual blacklisted content
4. Fill data back with synthetic data
5. Post-training [[Model Fine Tuning]]
6. [[Machine Unlearning]]
# Side Effects
- Models can exhibit [[Emergent Ability of LLMs|Emergent Capabilities]] when scaled up
- Data filtering can degrade performance - even on benign tasks