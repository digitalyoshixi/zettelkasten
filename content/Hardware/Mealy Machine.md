---
tags:
  - hardware
  - programming
  - math
---
A [[Finite State Automata|FSM]] that depends on both [[Circuit State]] and current input.
- All steps produce a output
For [[State Diagram]], the output is written on the transitions
![[Finite State Automata-20250603185824370.webp|341]]
# Formal Definition
A [[Finite State Automata|FSA]] ($\Sigma, \Gamma,Q,q_{0}, \delta, \lambda$):
- $\Sigma$ : Input [[Alphabet]]
- $\Gamma$ : Output [[Alphabet]]
- $Q$ set of states
- $q_{0} \in Q$ initial state
- [[Transition Function]]:
$$
\delta : Q \times \Sigma \to Q
$$
- [[Output Function]]:
$$
\lambda : Q \times \Sigma \to \Gamma
$$
# Concepts
- [[Sink State]]
- [[State Machine Run]]
# Circuit Diagram Labelling
![[Mealy Machine-20260710010311107.webp]]
![[Mealy Machine-20250603191542795.webp|315]]
# Pros
- Sometimes fewer overall states
- Outputs can respond sooner to inputs
# Cons
- Potential for long path from input to output to not be stored in a flip flop