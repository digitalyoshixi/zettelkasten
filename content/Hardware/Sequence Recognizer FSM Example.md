---
tags:
  - hardware
---
# Problem 
Create a [[Finite State Automata|FSM]] of a circuit that detects 3 [[Voltage At the Collector|Logic High]] in a row assuming single input $IN$ and two states
# Process
1. Create a state diagram. Note transitions are dependent on $IN$
![[Sequence Recognizer FSM Example-20250603185848542.webp|267]]
2. Create a [[State Table]]
![[Sequence Recognizer FSM Example-20250603190150703.webp|250]]
3. Assign [[Flip-Flop]]
Note that since there are 8 states, we assign 3 flip flops.
![[Sequence Recognizer FSM Example-20250603190232077.webp|275]]
![[Sequence Recognizer FSM Example-20250603190320480.webp|414]]
4. Create the second [[State Table]]
   ![[Sequence Recognizer FSM Example-20250815172249874.webp|368]]
5. Create a [[Karnaugh Map|K-Map]] for circuit design
![[Sequence Recognizer FSM Example-20250603190700131.webp|335]]
![[Sequence Recognizer FSM Example-20250603190648239.webp|334]]
![[Sequence Recognizer FSM Example-20250603190718278.webp|332]]
6. Assemble the circuit from K-maps [[Product of Sums K-Map|Product of Maxterms]]
![[Sequence Recognizer FSM Example-20250603190816405.webp]]