---
tags:
  - cryptography
---
# Definition
A simulation is secure when you cant tell apart a real system attacker and a ideal system attacker.
Uses a [[Simulator]].
# Formal Definition
- Given a ideal world, one where the attacker is a [[Simulator]]
- Given a real world, one where the attacker is an actual attacker
- Given an environment which inputs communications of $P_{1}, P_{2}$ and takes in output of what the attacker $A$ and $S$ sees
- The environment shouldn't be able to distinguish which world has the simulator and which world has the attacker
![[Simulation Security-20260207000142464.webp]]