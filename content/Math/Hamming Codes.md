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
Theoretically, for $k$ parity bits, you can have $2^{k}-k-1$ data bits
# Process ([[Hamming (7,4)]])
### Sending Process
1. Create your message, then encode with a hamming encoding algorithm (Maybe [[Hamming (7,4)]])
### Recieving Process
1. Given the message, calculate the sum of each circle for the recieved message by left multiplying vector
2. $H = [L_{1}^{T}, L_{2}^{T},L_{3}^{T},L_{4}^{T},L_{5}^{T},L_{6}^{T},L_{7}^{T}] = [c_{1},c_{2},c_{3}]^{T}$ where:
	- $c_{i}$ is the parity of each $i-th$ circle
	- $L_{i}$ is the location of each bit in the circles
3. Bob calculates $H(v)$ to get $(c_{1},c_{2},c_{3})$
4. If $(c_{1},c_{2},c_{3})$ contains non-zero entries, then there is an error
	1. If one error occured, then the error $e_{i}$ is precisely at location $L_{i} = (c_{1},c_{2},c_{3})$
		1. If $1 \leq i \leq 4$ (one of the message bits was ruined) then $(x_{1},x_{2},x_{3},x_{4})^{T} + e_{i}$ would be the corrected message 
		2. If $i > 4$ (one of the parity bits was ruined), then we can just ignore it
	2. Alternatively, finding through the diagram, the wrong bit, first find the two circles that are invalid, then the wrong bit is at the intersection between the two circles
	   ![[Hamming Codes-20250603225006971.webp|231]]
# Concepts
- [[Hamming Distance]]
- [[n-Error Detecting Code]]
- [[Hamming (7,4)]]
- [[Matrix Representation of Hamming Function]]
- [[String Parity]]