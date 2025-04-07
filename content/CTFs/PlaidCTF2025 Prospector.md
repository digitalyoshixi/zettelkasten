---
tags:
  - ctf
  - reverse_engineering
---
1. This file runs on ARM![[PlaidCTF2025 Prospector-20250405231005857.webp]]
2. But, we can see its strings
![[PlaidCTF2025 Prospector-20250405035142319.webp]]
3. On [[Dogbolt]], the IDA decompilation: https://dogbolt.org/?id=6337b01f-0385-4ce0-9132-6197923b8d26#Hex-Rays=1040 It shows that this is likely a constraint solver problem
4. Lets debug with gdb and qemu
![[PlaidCTF2025 Prospector-20250406005139586.webp]]
5. The flag would be whatever your input is:
   ![[PlaidCTF2025 Prospector-20250406021146098.webp]]
6. We convert the ida script into python z3 constraints.
7. Note, that there are A LOT of contradictory constraints, so we have to try and mine for the correct ones
![[PlaidCTF2025 Prospector-20250406032133669.webp]]
