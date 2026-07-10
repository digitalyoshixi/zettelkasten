---
tags:
  - hardware
  - programming
  - math
---
A [[Finite State Automata|FSM]] wherein the output depends soley on the current state (often saved within [[Flip-Flop]]).
Moore machines are more commonly used in practice.
![[Moore Machine-20250603191229476.webp]]
# Formal Definition
A [[Finite State Automata|FSA]] ($I,O,Q,q_{0}$):
- $I$ is set of input symbols
- $O$ set of output symbols
- $Q$ set of states
- $q_{0} \in Q$ initial state
- Transition function:
$$
\lambda : Q \to O
$$
# Circuit Diagram Labels
![[Moore Machine-20260710010255144.webp]]
![[Moore Machine-20250603191603718.webp]]
# Pros
- Simpler than [[Mealy Machine]]
- Always a flip-flop between input and output
# Cons
- May need more states than [[Mealy Machine]]
- Takes atleast one cycle to respond to input