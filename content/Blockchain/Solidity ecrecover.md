---
tags:
  - programming
  - solidity
  - blockchain
---
```solidity
contract MalleableSignatureExample {
    function verifySignature(bytes32 message, uint8 v, bytes32 r, bytes32 s) public pure returns (bool) {
        address signer = ecrecover(message, v, r, s);  // Signature malleability risk
        return signer != address(0);
    }
}
```