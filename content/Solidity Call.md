---
tags:
  - programming
  - solidity
---
```solidity
(bool success, bytes memory data) = targetAddr.call{value : 1 ether}(
abi.encodeWithSignature("foo(uint256)", 256)
);
```
Used to call another smart contract with callee's storage and context