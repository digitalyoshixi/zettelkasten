---
tags:
  - cryptography
---
https://billatnapier.medium.com/cryptography-fundamentals-commutative-encryption-19ba4c4c2173

# TLDR
Multiple keys lock, data cannot be read until all keys are given AND **the order of decryption does not matter**

For example, if we encrypt like
Bob → Alice → Carol then to decrypt we could do: 
- Carol → Alice →Bob
- Alice →Bob → Carol
- Alice → Carol → Bob
- So on so forth
# Process
utilizes [[XOR cipher]]
