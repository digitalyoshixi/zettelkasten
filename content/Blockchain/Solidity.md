---
tags:
  - programming
  - blockchain
---
A programming language used by [[Ethereum]] to implement [[Smart Contract|Smart Contracts]].
Runs on the [[Ethereum Virtual Machine]].
- [[Statically Typed]]
- Compiled
# Boilerplate
```solidity
pragma solidity ^0.5.0;
```
# Development Process
1. Define a contract in the `/contracts` folder
2. Compile the contract with `truffle compile`
3. Define a migration in the `/migrations` folder
4. Ensure `truffle-config.js` is properly defined
5. Migrate with `truffle migrate`
# Concepts
- [[Solidity Contract]]
- [[Solidity Migration]]
- [[Solidity Struct]]
- [[truffle-config.js]]
- [[truffle console]]