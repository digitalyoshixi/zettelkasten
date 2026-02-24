---
tags:
  - statistics
  - machine_learning
  - ai_safety
aliases:
  - CWG
---
A predictive models' scores should have same meaning across different groups.
# Formal Definition
For each risk score, the [[True Positive]] rate should be the same for all relevant groups

$$
P(Y=1|S=s, A=a) = s, \forall s \in \mathbb{R}, a \in A
$$
Where:
- $Y$ is a binary event $\{ 0,1 \}$
- $s$ is a risk score in $S$
- $A$ is a salient group (e.g race)
# Example
In [[Correctional Offender Management Profiling for Alternative Sanctions|COMPAS]]:
- Among those that recieve risk score of 0.1 in a given group, this should be [[True Positive]] for only 10% of that group
- Among those that recieve risk score of 0.9 in a given group, this should be [[True Positive]] for only 90% of that group