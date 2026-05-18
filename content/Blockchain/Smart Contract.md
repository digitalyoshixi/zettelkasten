---
tags:
  - blockchain
aliases:
  - Smart Contracts
---
A self-executing protocol that triggers when specific conditions are met on the [[Blockchain]].
They are executed during [[Transaction Block]] creation by a [[Blockchain Miner]]
```
while(true){
	if (condition){
	//then perform some action
	}
}
```
They are:
- Immutable. If you want to change a smart contract you need to make a new one and then tell all users to migrate to using the new one
- Distributed. All users have the same smart contract
# Structure
- [[Smart Contract Dispatcher]]
- Various [[Ethereum Bytecode|EVM Opcode]] functions
# Subtypes
- [[Multi-Signature Smart Contract]]
# Utilizations
- [[Flash Loan]]
- [[Blockchain Insurance]]
- [[Token Switching]]
- [[Blockchain Real Estate]]
# Tools
- [[OpenZeppelin Defender]]
- [[OpenZeppelin Contract Wizard]]
