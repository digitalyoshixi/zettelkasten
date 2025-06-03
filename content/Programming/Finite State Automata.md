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
# FSM Design Steps
- Draw a [[State Diagram]]
- Derive a [[State Table]] from state diagram
- Assign a flip-flop value configuration to each state (At least $\log_{2}(\text{\# of states})$ flip flops)
- Redraw [[State Table]] with [[Flip-Flop]]
- Derive [[Combinational Circuit]] for output and each flip flop input
### Examples
- [[Sequence Recognizer FSM Example]]
# Types
- [[Deterministic Finite Automaton|Deterministic Finite State Automaton]]
- [[Non-Deterministic Finite Automaton|Non-Deterministic Finite State Automaton]]