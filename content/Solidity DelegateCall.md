---
tags:
  - programming
  - solidity
---
```solidity
(bool success, bytes memory data) = libraryAddress.delegatecall(
    abi.encodeWithSignature("foo(uint256)", 42)
);
```
- Executes smart contract with the caller's storage