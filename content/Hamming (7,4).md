---
tags:
  - math
  - linalg
  - information_theory
---
A hamming code that takes 4 input bits and produces 7 output bits that are [[Error Correcting Codes|ECC]].
# Process
![[Drawing 2025-05-30 11.26.23.excalidraw]]
- Takes 4-bit string $x = (x_{1},x_{2},x_{3},x_{4})$
- Creates 3 parity bits $P_{1},P_{2},P_{3}$
- Align each $P_{i}$ such that the [[String Parity]] within each circle is 1
- If the entries in the $i-th$ circle sum to 1, $P_{i} = 1$, otherwise $P_{i} = 0$
# Matrix Representation of Hamming(7,4)
We have: $G(x_{1},x_{2},x_{3},x_{4}) = (x_{1},x_{2},x_{3},x_{4},p_{1},p_{2},p_{3})$
$$G = \left[\begin{array}{cc} \\
I \\
L_{1^{^{}}}
\end{array}\right]$$