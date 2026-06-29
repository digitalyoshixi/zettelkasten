---
banner: "[[Finite State Automata-20250603150758964.webp]]"
tags:
  - programming
aliases:
  - FSA
  - Finite State Machine
  - FSM
---
A abstract machine that have:
- Finite set of states
- Finite set of transitions between states triggered by inputs
- Output haves are determined by states and transitions
They are modelled by [[State Diagram]] or [[State Table]]
![[Finite State Automata-20250603150758964.webp|320]]
# Formal Definition
A finite state machine is a [[Tuple|4-Tuple]] $(Q,q_{0},F,\delta)$
- $Q$ is a [[Set]] of all states
- $q_{0}$ is the starting state
- $F$ is the set of [[Accepting State]]
- $\delta:Q \times A \to A$ is the transition function
# FSM Design Steps
1. Draw a [[State Diagram]]
2. Derive a [[State Table]] from state diagram
3. Assign a flip-flop value configuration to each state (At least $\log_{2}(\text{\# of states})$ flip flops)
4. Redraw [[State Table]] with [[Flip-Flop]]
5. Derive [[Combinational Circuit]] for output and each flip flop input
	- State logic: Figure out next state
	- Output logic: Figure next output
### Examples
- [[Sequence Recognizer FSM Example]]
- [[NFSA Example]]
# Types
### [[Circuit State]]
- [[Moore Machine]]
- [[Mealy Machine]]
### [[Determinism]]
- [[Deterministic Finite Automaton|Deterministic Finite State Automaton]]
- [[Non-Deterministic Finite Automaton|Non-Deterministic Finite State Automaton]]