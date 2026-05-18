---
tags:
  - blockchain
  - security
---
# Attack
Exploits vulnerability in [[Smart Contract|Smart Contracts]] when a [[Solidity Call]] is called before updating its own state.
Exploits the blockchain's trust of the user's smart contract [[Application Binary Interface|ABI]], wherein attacker smart contracts can subvert the logic.
# Example
![[Re-entrancy Attack-20260506033348175.webp]]
Instead of following the last two steps of draining the balance, attacker's smart contract will rewrite so that it calls the withdraw() function again.
# Protections
- [[Checks Effects Interactions]]
- [[Mutex]]

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract VulnerableVault {
mapping(address => uint256) public balances;

  

function deposit() external payable {

balances[msg.sender] += msg.value;

}

  

function withdraw(uint256 amount) external {

require(balances[msg.sender] >= amount, "Insufficient balance");

(bool sent, ) = msg.sender.call{value: amount}(""); // vuln, sends before update amount

require(sent, "Transfer failed");

balances[msg.sender] -= amount;
}

}
```