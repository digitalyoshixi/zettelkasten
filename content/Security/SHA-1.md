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
![[SHA-1-20260219025511312.webp]]
- With $F$ as a non-linear [[Compression Function]] that varies
- With a left-bit rotations
- With $W_{i}$ as the segment of the splitted plaintext message
- With $K_{i}$ as the segment of the round constant
- With $\boxplus$ as addition in $\mod 2^{32}$
# Uses
- [[SHACAL]]