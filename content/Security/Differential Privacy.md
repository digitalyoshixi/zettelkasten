---
tags:
  - privacy
aliases:
  - DP
---
A mathematical guarantee that the of privacy wherein data is partitioned so that not everything is leaked.
![[Differential Privacy-20260128011225056.webp]]
# Formal Definition
$$
Pr[M(d) \in S] \leq e^{\epsilon} Pr[M(d') \in S] + \delta
$$
- $d, d'$ - datasets (one with individual data)
- $M$ - training algorithm
- $S$ - any subset of trained models (i.e, models with >90% accuracy)
- $\epsilon$ - privacy loss (how much one person is used)
- $\delta$ - slack allowing epsilon bound not to hold
### Intuition
Pick any property of the trained model you care about (i.e performance, accuracy, etc). If you retrain the model many times, the model having that property doesn't change much (at most factor $e^{\epsilon}$ when someone's data is added or removed)
# Concepts
- [[Differential Privacy Stochastic Gradient Descent|DP Stochastic Gradient Descent]]