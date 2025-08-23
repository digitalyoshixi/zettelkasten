---
tags:
  - cryptography
aliases:
  - Rivest Shamir Adleman
  - PKCS 1
---
A [[Public-Key Cryptography|Asymmetric Cryptosystem]] based off the [[Discrete Logarithm Problem|DLP]].
Often used as:
- [[Signature Algorithm]]
- [[Key Exchange Protocol|Key Exchange Algorithm]]

Uses a pair of [[Commutative Encryption|Commutative Keys]].
https://www.youtube.com/watch?v=Pq8gNbvfaoM 
# Commonly Used Terminology
- **P and Q:** 2 Prime \#s used in generation
- **N**: Product of 2 primes
- **T**: [[Euler's Totient Function|Totient]] of 2 primes
- **E**: Public key
- **D**: Private key
# Generating Keys
1. Select 2 prime numbers P and Q.
2. Calculate the product **N**. P\*Q. *note: this number is semi-prime because 2 primes multiplied to get it*
3. Calculate the totient **T**. (P-1)\*(Q-1)
Now you can create the public and private keys
The public key **E**:
- Must be prime
- Must be less than the totient
- Must not be a factor of the totient.
The private key **D** must fulfill:
- $(private key*public key )\% totient = 1$
	- The remainder must be 1
# Encrypting/Decrypting
### Encrypting
$(Message^E)\%N = Cipher$
### Decrypting
$(Cipher^D)\%N = Message$

Because this is [[Commutative]], you can also encrypt with the private key and decrypt with the public key.