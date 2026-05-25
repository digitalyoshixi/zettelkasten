---
tags:
  - blockchain
  - programming
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