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
- $p,q$ 2 [[Prime Number]] used in generation
- $n$: Product of 2 primes
- $\phi$ or $\lambda(n)$: [[Euler's Totient Function|Totient]] of 2 primes
- $e$: Public key
- $d$: Private key
# Generating Keys
1. Select 2 prime numbers $p,q$
2. Calculate the product $n = p*q$. Note this number is [[Coprime]]
3. Calculate the [[Carmicheal Lambda Totient]] $\lambda(n) = \text{lcm}(p-1,q-1)$
	1. Alternatively, you can use the [[Euler's Totient Function]] $\phi = (p-1)*(q-1)$
Now you can create the public and private keys
5. Choose public key $e$ such that:
	1. $e$ is [[Prime Number]]
	2. $1 < e < \lambda(n)$
6. Choose private key $d$ such that:
	1. $(d*e) \mod \lambda (n) = 1$
# Encrypting/Decrypting
### Encrypting
$(\text{Message}^e)\%n = \text{Cipher}$
### Decrypting
$(\text{Cipher}^d)\%n = \text{Message}$

Because this is [[Commutative]], you can also encrypt with the private key and decrypt with the public key.