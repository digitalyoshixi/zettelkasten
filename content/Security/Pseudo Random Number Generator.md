---
tags:
  - math
  - cryptography
aliases:
  - PRNG
  - PRF
  - Deterministic Random Bit Generator
  - DRBG
---
A random number generated from [[Deterministic Algorithm]].
A PRF should generate an arbitrary length random value from a given seed. The output should be indistinguishable from random data.
# Formal Definition
A PRF is an algorithm that takes in:
- Secret input $i$
- Desired number of bits $n$
- Seed data $s$
Returns an output [[String]] $o \in \{ 0,1 \}^{*}$
# Implementations
### Squares
- [[Middle Square Algorithm]]
### Linear Recursion
- [[Linear Congruential Generator|LCG]]
- [[Mersenne Twister]]
- [[xorshift]]
- [[Well Equidistributed Long-period LInear]]
### Counter-Based
$\text{output} = f(n,key)$
- [[Philox]]
- [[Threefry]]
### Secure PRNGs
- [[Block-Cipher]] in counter mode or output feedback mode
	- [[HMAC-DRBG]]
- [[Stream-Cipher]]
# Subtypes
- [[Key Derivation Function]]
# Tests
- [[Uniform Randomness Test]]
- [[Spectral Test]]