---
tags:
  - programming
  - blockchain
---
A programming language used by [[Ethereum]] to implement [[Smart Contract|Smart Contracts]].
Runs on the [[Ethereum Virtual Machine]].
- [[Statically Typed]]
- Compiled
# Boilerplate
```solidity
pragma solidity ^0.8.26;

contract Counter {
    uint256 public count;
    // Function to get the current count
    function get() public view returns (uint256) {
        return count;
    }
    // Function to increment count by 1
    function inc() public {
        count += 1;
    }
    // Function to decrement count by 1
    function dec() public {
        // This function will fail if count = 0
        count -= 1;
    }
}
```
# Development Process
1. Define a contract in the `/contracts` folder
2. Compile the contract with `truffle compile`
3. Define a migration in the `/migrations` folder
4. Ensure `truffle-config.js` is properly defined
5. Migrate with `truffle migrate --reset`
# Concepts
- [[Solidity Contract]]
- [[Solidity Context]]
- [[Solidity Migration]]
- [[Solidity Struct]]
- [[Solidity Map]]
- [[Solidity Function]]
- [[Solidity Event]]
- [[Solidity Call]]
- [[Solidity DelegateCall]]
- [[EVM Account Storage]]
- [[Ethereum Proxy Pattern]]
- [[Solidity Error Handling]]
- [[truffle-config.js]]
- [[truffle console]]
- [[solc]]
- [[Solidity selfdestruct]]
### Dev
- [[Solidity Test File Boilerplate]]
# Resources
- https://solidity-by-example.org/