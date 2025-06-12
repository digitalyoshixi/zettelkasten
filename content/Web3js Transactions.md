---
tags:
  - blockchain
  - javascript
---
# Sending a Transaction (Unlocked Accounts on [[Testnet]])
```js
await web3.eth.sendTransaction({from: "0x...", to:"0x...", value: web3.utils.fromWei(20, 'ether'), gasPrice : web3.utils.fromWei(20, 'gwei')})
```
# Sending a Transaction (Signing with Private Key)
```js

```