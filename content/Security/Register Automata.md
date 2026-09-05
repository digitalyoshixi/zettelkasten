---
tags:
  - verification
aliases:
  - RA
---
A form of extended [[Finite State Automata|Finite State Machine]] that treats [[Register]] as a [[First Class Citizen]].
Well suited for describing communication protocols.
# Definition
A Register Automata $A^* = ( A,L,l_{0},X,\Gamma, \lambda )$ 
- $A$ the finite set of actions used in [[Symbolic Input]]
- $L$ the [[Set]] of [[State|Locations]]
- $l_{0}$ the starting [[State|Location]]
- $X$ the set [[Register Tuple]] used for memory
- $\Gamma$ the transition [[Relation]]
- $\lambda$ labels each location accepts ($+$) or rejects ($-$)
	- $+$ is [[Accepting State]]
	- $-$ is [[Rejecting State]]
### Transition $\Gamma$
$\langle l, (a, p^{-}), g, p, l' \rangle \in \Gamma$.
- From location $l$, given [[Symbolic Input]] $(a,\check p)$
### Sub Definitions
- [[Symbolic Input]] $(a,p^{-})$ to define actions
- [[Register Tuple]] $X$ stored as memory
- [[Automata Guard]] to check registers against new parameters in symbolic input
- Assignment $p : X\to X \cup P$ after transitions fire to update registers
# Uses
- [[ralib]]