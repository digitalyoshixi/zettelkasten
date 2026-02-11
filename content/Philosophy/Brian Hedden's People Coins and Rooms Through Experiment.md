---
tags:
  - philosophy
  - statistics
---
Used to show no proposed fairness criteria besides [[Calibration Within Groups|CWG]] are genuine requirements of fairness by showing a perfectly fair algorithm violates all fairness criteria.
# Thought Experiment
- 40 individuals each given a coin with some bias probability of landing heads between 0 and 1. Each coin has a bias written on it
- Individuals randomly assigned two rooms, Room A or B
- Aim is to predict for each individual, if their coin will land heads or tails and assign them a score representing this likelihood
- Assume we use the algorithm that we only predict heads if the number of the coin is greater than 0.5
- Suppose random assignment produces following result:

| Heads Probaability | Room A | Room B |
| ------------------ | ------ | ------ |
| 75%                | 12     |        |
| 12.5%              | 8      |        |
| 60%                |        | 10     |
| 40%                |        | 10     |
- This violates every fairness criteria except [[Calibration Within Groups|CWG]] because A's have more extreme probabilities than Bs