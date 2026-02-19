---
tags:
  - cryptography
aliases:
  - SHA1
---
A insecure hashing algorithm largely replaced by [[SHA256]]
- Weak to [[Preimage Attack]]
- Weak to [[Length Extension Attack]]
Takes in a 512-bit input, return 160-bit output.
Based off [[Merkle Damgard Construction]]
# Get Sha1 Hash from file
```
sha1sum ./file
```
# Algorithm
