---
tags:
  - hardware
aliases:
  - ALU
---
This is a [[Component|Component]] that is capable of:
- Arithmetic operations:
	- [[Multi-Bit Adder]]
	- [[Subtractor]]
	- [[Decrementer]]
	- [[Multiplier]]
	- Equality
	- etc..
- Logic operations:
	- OR
	- AND
	- etc..
![[Arithmetic Logic Unit-20250610182310960.webp|242]]
# Block Diagram
![[Arithmetic Logic Unit-20250610183242990.webp]]
- $n$-bit Inputs $a$, $b$
- Input $func$
- one bit $C_{in}$ to determine addition or subtraction
- Output $G$
- Output byte corresponding to [[CPU Flag]]:
# Specific [[Arithmetic Logic Unit|ALU]]
- [[MIPS ALU]]