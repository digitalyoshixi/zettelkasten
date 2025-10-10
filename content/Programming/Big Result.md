---
tags:
  - programming
aliases:
  - Nick Cheng's Big Result
  - The Big Result
---
Any [[Programming/Language|Language]] created from a:
- [[Regular Expression]]
- [[Deterministic Finite Automaton]]
- [[Non-Deterministic Finite Automaton]]
can be rewritten in each other's form.
# Formal Definition
Let $L$ be a [[Programming/Language|Language]], then the following are equivalent:
1. $L = \mathcal{L}(R)$ for some [[Regular Expression|Regex]] $R$
2. $L = \mathcal{L}(M)$ for some [[Deterministic Finite Automaton|DFSA]] $M$
3. $L = \mathcal{L}(M)$ for some [[Non-Deterministic Finite Automaton|NFSA]] $M$