---
tags:
  - cryptography
  - math
aliases:
  - Feistel Cipher
---
A [[Symmetric Cryptography|Symmetric Algorithm]] used to create [[Block-Cipher]].
Creates a [[Round Function]]
# Round Function
- Let $F(\text{datablock},\text{subkey})$ be the [[Round Function]]
- Let $K_{0}, \dots,K_{n}$ be sub-keys for rounds $0,\dots,n$ respectively
# Encryption
- Split plaintext block into two equal pieces $L_{0},R_{0}$
- For each round, $i = 0,\dots,n$ compute:
	- $L_{i+1} = R_{i}$
	- $R_{i+1} =L_{i} \oplus F(R_{i},K_{i})$
- Ciphertext is $(R_{n+1}, L_{n+1})$
# Decryption
- For given ciphertext is $(R_{n+1}, L_{n+1})$
- For each round $i=n,n-1,\dots,0$
	- $R_{i} = L_{i+1}$
	- $L_{i} = R_{i+1} \oplus F(L_{i+1},K_{i})$'
- $(L_{0},R_{0})$ is the plaintext again