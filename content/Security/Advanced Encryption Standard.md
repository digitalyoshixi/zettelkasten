---
tags:
  - cryptography
aliases:
  - AES
---
A [[Post-Quantum Cryptography]] safe algorithm. Deemed to be a sbustitution-permutation network.
128 bit Symmetric [[Block-Cipher]].
- The key is constructed out of 64 bits
Takes a message and a key.
The key can be 128bits, 192bits or 256bits.
# Concepts
- [[Block]]
# Attacks
- [[Biclique Attack]]
# Encryption Process
1. Our input is split into 16-byte block, each block is converted into a $4 \times 4$ [[Matrix]]
2. [[Key Expansion]]: The 16-byte key segments is turned into $n$ number of [[Round Key]] which are also $4 \times 4$ matrix
	1. $n = 11$ if AES-128
	2. $n = 13$ if AES-192
	3. $n = 15$ if AES-256
3. Set the current state to the 16-byte input matrix
4. Repeat for $n$ rounds:
	1. [[AddRoundKey]]: XOR current state with current round key $n$ (Every cell of state, XORed with corresponding cell in round key)
	2. [[SubBytes]]: Convert every byte in the state matrix with a different byte in a 16x16 lookup table ([[Substitution Box|S-Box]])
	3. [[ShiftRows]]: ensures columns are encrypted dependently
		1. First row in matrix remains the same
		2. Second row shift one column left
		3. Third row shift two columns to left
		4. Fourth row shift three columns by left
	4. [[MixColumns]]: Matrix multiplication of a [[Rijndael Galois Field]]
### Diagram
![[Advanced Encryption Standard-20240410021859196.webp]]
![[Advanced Encryption Standard-20240410021907720.webp]]
![[Advanced Encryption Standard-20240410021922409.webp]]
![[Advanced Encryption Standard-20240410021932732.webp]]
![[Advanced Encryption Standard-20240410021941341.webp]]
![[Advanced Encryption Standard-20240410021953028.webp]]
![[Advanced Encryption Standard-20240410022002624.webp]]