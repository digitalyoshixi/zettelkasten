---
tags:
  - cryptography
  - security
aliases:
  - IND-CCA
---
# IND-CCA Game
A hypothetical scenario wherein an attacker has access to decryption of ciphertext, other than a target ciphertext.
Used to prevent cryptographic systems from being [[Malleability|Maleable]]
### Intuition
With the challenger providing 2 mesages, the adversary attempts to guess which ciphertext the message belongs to.
Furthermore, the adversary has the capability to recieve the decryption of any ciphertext other than their target ciphertext.
For an algorithm to be [[Indistinguishability|Indistinguishable]], the adversary should have a 50% probability overall of guessing the correct message.
### Formal Definition
With:
- $S = (Gen, Enc, Dec)$
- $A$ is adversary
- $C$ is challenger
- $\mathcal{C}$ is the set of ciphertexts
- $M$ is the set of plaintexts
$$G^{\lambda, S}_{IND-CCA}(A) \text{ runs:}$$
1. $C$ generates a key $(pk,sk) \leftarrow Gen$ and sends $pk$ to $A$
2. $A$ sends $c \in \mathcal{C}$ to $C$, which respond with $m = Dec(sk, c)$
3. $A$ chooses $(m_{0},m_{1}) \in M$, and sends to $C$
4. $C$ flips a coin $G \in \{ 0,1 \}$ and sends $Enc(pk,m_{G})$ to $C$
5. $A$ can repeat step $2$ any ammount of times, provided $c \neq \hat{c}$
6. $A$ outputs $G^{*}$
$A$ wins if $G = G^{*}$