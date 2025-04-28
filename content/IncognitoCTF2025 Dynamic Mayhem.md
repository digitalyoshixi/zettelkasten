---
tags:
  - reverse_engineering
  - ctf
---
1. This ctf challenge gives a [[Java]] file with some encryption and an encrypted file
2. We note that for a dummy flag we provide, the output is 2 times the length
   ![[IncognitoCTF2025 Dynamic Mayhem-20250428004522608.webp]]
3. Checking the file, working from backwards to forwards we find
   `String X1Y2Z3 = X1Y2Z3(P6O5I4(bytes, R7T8Y9(Q4W5E6, M1N2O3)));`
4. The function X1Y2Z3 returns the hex version of each byte in the return of P60514(....), 