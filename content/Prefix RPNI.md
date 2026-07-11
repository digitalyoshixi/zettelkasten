---
tags:
  - verification
aliases:
  - PRPNI
---
A [[Passive Automata Learning]] for [[Moore Machine]].
- $N$ pairs of positive and negative example sets from pre-processing
- Executes [[Regular Positive and Negative Inference|RPNI]] on each pair thus obtaining $N$ DFSAs
- Product of all DFAs
	- If outputs are unsued, make them all point to unreachable stae