---
tags:
  - verification
aliases:
  - LMoIO
---
A paper on an algorithm for [[Automata Learning]] in [[Moore Machine]].
- Cannot be used to infer a [[Mealy Machine]] from a [[Moore Machine]]
- [[Moore Machine Prefix Tree Acceptor]]
- [[Characteristic Sample Requirement]]
# Problem
Given input [[Alphabet]] $I$, output alphabet $O$ and set of $R_{train}$ of moore [[IO Traces]] as the training set, want to create a moore machine $M = (I,O,Q,q_{0}, \delta, \lambda)$ s.t $M$ is consistent with $R_{train}$.
- $\forall (p_{I}, p_{O}) \in R_{train} : \lambda^{*}(p_{I})=p_{O}$
# Algorithms
Uses [[Accuracy Evaluation Policy]] to check a accuracy of the trained machine
- [[Moore Machine Prefix Tree Acceptor|PTAP]] (but no state minimization)
- [[Prefix RPNI]]
- [[MooreMI]]
# Paper
- https://arxiv.org/pdf/1605.07805