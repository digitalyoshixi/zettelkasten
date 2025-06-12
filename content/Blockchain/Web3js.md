---
banner: "[[Web3js-20250214035117053.webp]]"
tags:
  - javascript
  - blockchain
---
A [[JavaScript]] framework that allows client nodes to communicate to the [[Blockchain]] via [[Remote Procedure Calls|RPC]].
![[Web3js-20250608215651096.webp]]
# Installation
`npm i web3`
# Guides
- [[Web3js Get Balance]]
- [[Web3js Wei Conversions]]
- [[Web3js Create Contract]]
- [[Web3js Send ABI Requests]]
- [[Web3js Deploy Contract]]
- [[Web3js Transactions]]
- [[Web3js Estimate Gas]]
- [[Web3js Create Blockchain Account]]
- [[Web3js Metamask Initialization]]
# Initialization
```js
const { Web3 } = require('web3');

// example with ganache
var web3 = new Web3("http://127.0.0.1:8545");
```
