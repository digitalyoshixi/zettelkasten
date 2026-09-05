---
tags:
  - security
  - blockchain
---
A cryptographic scheme that allows users to commit to a choice without revealing immediately.
Used for processes that require decisions to be made roughly at the same time (e.g revealing rock-paper-scissors choice).
Can be used to combat [[Front Running]].
# Process
1. Commit $Hash(Salt+Value)$ to smart contract
2. Reveal original $Salt+Value$ of hash to verify authenticity