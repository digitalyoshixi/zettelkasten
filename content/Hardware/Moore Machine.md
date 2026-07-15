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
A [[Finite State Automata|FSA]] ($\Sigma, \Gamma,Q,q_{0}, \delta, \lambda$):
- $\Sigma$ : Input [[Alphabet]]
- $\Gamma$ : Output [[Alphabet]]
- $Q$ set of states
- $q_{0} \in Q$ initial state
- Transition function:
$$
\delta : Q \times \Sigma \to Q
$$
- Output function:
$$
\lambda : Q \to \Gamma
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
# Example
![[Moore Machine-20260715015348360.webp]]
![[Moore Machine-20260715015337616.webp]]