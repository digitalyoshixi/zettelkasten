---
tags:
  - blockchain
  - security
---
# Attack
Exploits vulnerability in [[Smart Contract|Smart Contracts]] when a function is called before updating its own state.
Exploits the blockchain's trust of the user's smart contract [[Application Binary Interface|ABI]], wherein attacker smart contracts can subvert the logic.
# Example
![[Re-entrancy Attack-20260506033348175.webp]]
Instead of following the last two steps of draining the balance, attacker's smart contract will rewrite so that it calls the withdraw() function again.
# Protections
- [[Checks Effects Interactions]]
- [[Mutex]]