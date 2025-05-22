---
tags:
  - hardware
  - electricity
---
A component that allows for [[Binary]] addition through chaining [[Full Adder|Full Adders]]. 
Often used for [[Signal Vector|Signal Vectors]]
![[Ripple Carry Adder-20250522154942579.webp]]
- There will be a [[Full Adder]] for every bit in the addition
- The full adder for the Least Significant Bit will carry over to the next adder in the chain, continuing on until the last full adder
- There will be a $C_{in}$ to determine of the operation is addition $(0)$ or subtraction $(1)$