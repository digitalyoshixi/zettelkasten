---
tags:
  - blockchain
  - programming
aliases:
  - Foundry Forge
---
Tool to compile, test and deploy solidity [[Smart Contract]].
# Setup
```
forge init .
forge install
```
# Install std
```
forge install foundry-rs/forge-std
```
# Test
```
forge test --match-contract CounterTest -vvvvv
```
# Compile & Deploy
```
forge create <path_to_contract.sol> \
	--private-key <privatekey> \
	–-rpc-url <RPC_URL> \
	--broadcast
```