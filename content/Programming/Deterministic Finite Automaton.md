---
tags:
  - programming
aliases:
  - DFA
  - DFSA
  - Deterministic Finite State Automata
---
A [[Finite State Automata]] that has a definite result.
- Subset of [[Non-Deterministic Finite Automaton|NFA]]
Given input [[String]] $x$, it can accept or reject $x$.
# Formal Definition
A DFSA $M$ is a quintuple $M = (Q,\Sigma, \delta, s, F)$ where:
- $Q$ is a finite set of [[Circuit State|States]]
- $\Sigma$ is a finite [[Alphabet]]
- $\delta : Q \times \Sigma \to Q$ is thhe [[Transition Function]]