---
tags:
  - security
---
A method to verify the validity of the sender of a document through:
- A [[Signature Algorithm]]
- A signed message
- A public key
![[Digital Signature-20250709025919031.webp]]
# Definition
A digital signature is a scheme that consists of 3 algorithms:
1. A [[Keygen]] algorithm that selects a private key [[Uniform Discrete Probability Distribution|Uniformly]] from a set of possible private keys. Outputs the private and corresponding public key
2. A signing algorithm that, given a message and private key returns a signature
3. A signature verification algorithm that given the message, public key and signature will verify its authenticity.