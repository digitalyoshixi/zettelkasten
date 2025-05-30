---
tags:
  - information_theory
  - linalg
---
A [[Error Correcting Codes|ECC]] that is able to detect 2-bit errors and fix 1-bit errors.
Uses parity bits and parity circles to determine where errors occur.
# Notation
$$Hamming(A,B)$$
- Encodes $B$-input bits into $A$-output bits
- Adds extra parity $A-B$ parity bits
# Process
1. Alice encodes to create error-resistant code
2. Alice sends the code
3. Bob recieves the code
4. Bob applies ECC to fix all errors
# Concepts
- [[Hamming Distance]]
- [[n-Error Detecting Code]]
- [[Hamming (7,4)]]
- [[String Parity]]