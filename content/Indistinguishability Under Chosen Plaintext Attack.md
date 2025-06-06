---
tags:
  - cryptography
  - security
aliases:
  - IND-CPA
---
# IND-CPA Game
### Intuition
With the challenger providing 2 mesages, the adversary attempts to guess which ciphertext the message belongs to.
For an algorithm to be [[Indistinguishability|Indistinguishable]], the adversary should have a 50% probability overall.
### Formal Definition
With:
- $S = (Gen, Enc, Dec)$
- $A$ is adversary
- $C$ is challenger
$$G^{\lambda, S}_{IND-CPA}(A) \text{ runs:}$$
1. $C$ runs $(pk,sk) \leftarrow Gen(\lambda)$ and sends $pk$ to $A$
2. A chooses $m_{0}, m_{1} \in M$ and sends them to $C$
3. $C$ samples $G \leftarrow \{0, 1\}$ , uniform of random (Tossing a coin pretty much)
4. $A$ outputs $G^{*} \in \{ 0,1 \}$
5. $A$ wins if $G = G^{*}$