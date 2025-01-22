---
tags:
  - cryptography
---
A method used in [[End to End Encryption]] to generate the shared key through sharing public variables, combining them with private variables and ending up with both users having the same result.
# Process
1. Alice has private key $a$, Bob has private key $b$, public variables $g$ and $n$ are stored. 
   $g$ is a very small prime number
   $n$ is a very big prime number
   ![[Diffie Hellman Key Exchange-20240728013124415.webp]]
2. Bob and Alice each calculate $g^{privatekey} \mod n$ and then share them with eachother.
   ![[Diffie Hellman Key Exchange-20240728013807545.webp]]
3. Each user receives the other discrete logarithm key from the other and then raises it by their own private key
   ![[Diffie Hellman Key Exchange-20240728014126895.webp]]
   this results in both users having the same symmetric key
# Decryption
This is based off the [[Discrete Logarithm Problem]] that can be solved with:
- [[Diffie Hellman g Finding]]
- [[Baby-step Giant-step]]