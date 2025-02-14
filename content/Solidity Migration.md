---
tags:
  - blockchain
  - programming
---
Migrations are required when you want to add a new [[Solidity Contract]] to the blockchain.
This is because you would be modifying the state of the blockchain.

# Example
```solidity
var TodoList = artifacts.require("./TodoList.sol")

module.exports = function(deployer){
  deployer.deploy(TodoList);
};
```