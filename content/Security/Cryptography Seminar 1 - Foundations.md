---
tags:
  - cryptography
---
# Notes
- Goal of cryptography is to create systems and prove their security
- Systems in this sense are efficiently computable algorithms
- They also satisfy [[Correctness]]
- Theoretical cryptographers try and avoid [[Symmetric Encryption]] because it gets ugly in proofs of [[Correctness]]. They usually work with [[Public-Key Cryptography|Asymmetric Cryptography]]
- All asymmetric cryptography will have (with public key $Pk$, private key $Sk$, cipher text $e$, message $M$):
	- Generating algorithm $Gen : \mathbb{N}^{+} \to Pk \times Sk$
	- Encryption algorithm $Enc: Pk \times M \to e$
	- Decryption algorithm $Dec : Sk \times e \to M$
- Security can be thought of as computational problems or distinguishing problems
	- Computational problems include: [[Discrete Logarithm Problem]]
	- Distinguishing problems include: [[Decisional Diffie Hellman Assumption]]