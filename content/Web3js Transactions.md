---
tags:
  - blockchain
  - javascript
---
# Sending a Transaction (Unlocked Accounts on [[Testnet]])
```js
tx = {
	from: "0x...",
	to: "0x...",
	value: web3.utils.fromWei(20, 'ether'),
	gasPrice: web3.utils.fromWei(20, 'ether')
}
await web3.eth.sendTransaction(tx)
```
# Sending a Transaction (Signing with Private Key)
```js
sender = "0x..."
reciever = "0x..."
tx = {
	from: sender,
	to: reciever,
	value: web3.utils.toWei(1, 'ether'),
	gasPrice: web3.utils.toWei(10, 'ether'),
	nonce: await web3.eth.getTransactionCount(sender)
}
privatekey = "..."
signedtx = await web3.eth.accounts.signTransaction(tx, privateKey);
await web3.eth.sendSignedTransaction(signedtx)
```