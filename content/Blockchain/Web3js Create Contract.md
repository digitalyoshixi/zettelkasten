---
tags:
  - blockchain
---
```js
contract = new web3.eth.Contract(abi, address)
```
# Loading a smart contract
1. Find a smart contract (maybe on https://etherscan.io/)
2. Save your abi as a variable
   ![[Web3js Create Contract-20250609011247764.webp]]
   `abi = ...`
3. Save your smart contract address as a variable
   ![[Web3js Create Contract-20250609011508529.webp]]
   `address = ...`
4. `contract = new web3.eth.Contract(abi, address)`
5. ![[Web3js Create Contract-20250609011953357.webp]]