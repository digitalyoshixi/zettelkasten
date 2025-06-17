---
tags:
  - ai_safety
---
A [[Metauni]] talk about [[AI Safety]] by Elliot Catt, a worker at deepmind.
# Notes
- AI systems are highly capable, they might lead to x-risk fates.
- Ideally, we want to run experiments on [[Artificial General Intelligence|AGI]], though [[Artificial General Intelligence|AGI]] has not been developed yet
- Next best thing is to use [[Universal Artificial Intelligence]], which is a mathematical model that tells us how optimal ai systems will act
- Notations will be:
	- $A,O,R$ are the finite sets of actions, observations and rewards repectively
	- $\epsilon := O \times R$ to denote set of percepts (additionally $e_{t} = o_{t}r_{t}$)
	- $H :=(A \times \epsilon)^{*}$ denotes set of finite interaction histories
	- $x_{1:t} = x_{1}x_{2}\dots x_{t}$
	- $x_{<t} := x_{1}x_{2}\dots x_{t-1}$
- We use $v$ to denote some environment