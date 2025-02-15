---
tags:
  - blockchain
---
# Process
1. Find the `ContractAddress`. this will show up after you do `truffle migrate`
2. Find the `ContractABI` which is a [[Application Binary Interface|ABI]] for the [[Smart Contract]]
3. Everytime you connect your [[Metamask]] wallet to the browser, an `ethereum` variable is injected into your browser window. This allows us to tell if a browser is web3 compatible
4. Check if `ethereum` is null
5. If `ethereum` is not null, get the `chainID` and `userID`
# Code
