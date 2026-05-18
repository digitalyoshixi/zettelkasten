---
tags:
  - blockchain
  - security
---
A code pattern to prevent against [[Re-entrancy Attack]].
```solidity
function withdraw(uint amount) public {
	require(balances[msg.sender] >= amount); // check
	balances[msg.sender] -= amount; // effect
	msg.sender.transfer(amount); //interaction
}
```