---
tags:
  - programming
  - solidity
---
A interface that allows you to easily log actions.
```solidity
pragma solidity ^0.8.22;

event HighestBidIncreased(address bidder, uint amount); //event

contact SimpleAuction {
	function bid() public payable {
		// ...
		emit HighestBidIncreased(msg.sender, msg.value) // trigger event
	}
}
```