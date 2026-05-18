---
tags:
  - blockchain
  - solidity
---
What the [[Smart Contract]] stores.
- Transaction & Message call context
	- `msg.sender`
	- `tx.gasprice`
- Block context (`block.blockshash`)
- Address object (`address.balance`, `address.send(amount)`)
- Built-in-functions
	- `addmod`
	- `keccack256`
	- `this`