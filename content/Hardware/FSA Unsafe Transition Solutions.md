---
tags:
  - hardware
---
These are solutions for preventing [[Race Condition]] within [[Finite State Automata|FSA]] that may prevent transitioning to the correct states.![[Counters with Parallel Load-20250603184225635.webp]]
# Solutions
1. Whenever possible, make flip-flop assignments such that the neighboring states differ by at most one bit
2. Add intermediate transition states between the start and the end
3. Try to reassign states so that timing issues dont exist