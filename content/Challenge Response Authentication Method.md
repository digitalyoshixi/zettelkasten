---
tags:
  - security
---
A method to prove [[Authentication]] between two hosts.
# Protocol
![[Challenge Response Authentication Method-20260506191050057.webp]]
1. Server sends client a challenge
2. Client can only solve challenge with the password
3. Server and client both attempt to solve challenge with the respective password on their sides
4. Client returns challenge answer to server
5. Server compares answer with its own
# Problem
If the challenge is to compute the hash of password+random nonce, then both sides use the same password, then the security of the hash does not rely solely on the password, the nonce and hash are equally sensitive information.
![[Challenge Response Authentication Method-20260506191248673.webp]]
Can be solved with [[Salting]]