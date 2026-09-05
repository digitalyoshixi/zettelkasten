---
tags:
  - blockchain
aliases:
  - NPoS
---
Validators take turns producing blocks.
# Process
1. Each [[Blockchain Miner|Miner]] will deposit a stake for their chance to be chosen to validate the next [[Transaction Block|Block]] using a [[Verifiable Random Function]]
2. Highest stake miner will validate the block, seeing if all transactions can be valid:
	1. Check if parent hash links with previous chain
	2. Check if block numbers are sequential
	3. Validates state root
	4. Checks root of all transactions in block 
	5. Checks transaction signatures
	6. Check transaction balances and fees (no double spending)
	7. Check transaction times