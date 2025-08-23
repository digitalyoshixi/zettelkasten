---
tags:
  - cryptography
aliases:
  - Rivest Shamir Adleman
---
A [[Public-Key Cryptography|Asymmetric Cryptosystem]] based off the [[Discrete Logarithm Problem|DLP]].
Often used as a [[Signature Algorithm]].
It is by far the most used Asymmetric Encryption algorithm

RSA creates a pair of [[Commutative Encryption|Commutative Keys]].
https://www.youtube.com/watch?v=Pq8gNbvfaoM 
# Commonly Used Terminology
**P and Q:** 2 Prime \#s used in generation
**N**: Product of 2 primes
**T**: Totient of 2 primes
**E**: Public key
**D**: Private key
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

Because this is commutative, you can also encrypt with the private key and decrypt with the public key.
There is no difference between public and private, other than the purpose they are used for.

# RSA Security
Its really hard to factor semi-prime numbers. 
Like, try 1909, that would take 1 BILLION years.

in 1991, RSA released the RSA challenge which had 52 semi-primes with each having a cash reward of ~$100,000.
as of now, only 23 were solved. The biggest prime number factored was 829 bits in length.

2048 is the standard size of RSA keys today.

Public keys are usually 65537.