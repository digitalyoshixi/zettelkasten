---
tags:
  - cryptography
aliases:
  - RSA Attack
---
Methods to break the encryption of [[RSA]].
Remember that RSA looks like:
$C = (m^e)\%n$
where:
- $C$ is the cipher text
- $m$ is the original message
- $e$ is an exponent
- $n$ is the product of 2 large [[Prime Number]]
The question is how we can get the message 'm'
# Factoring Modulus $n$
- [[Wiener's Attack]]
- [[Carmicheal Lambda]]
- [[Chinese Remainder Theorem]]