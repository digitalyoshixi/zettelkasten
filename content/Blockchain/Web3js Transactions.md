---
tags:
  - blockchain
  - javascript
---
# Sending a Transaction (Unlocked Accounts on [[Testnet]])
```js
data = "..."
tx = {
	from: "0x...",
	to: "0x...",
	value: web3.utils.toWei(20, 'ether'),
	gasPrice: web3.utils.toWei(20, 'gwei'),
	data : data
}
await web3.eth.sendTransaction(tx)
```
# Sending a Transaction (Signing with Private Key)
```js
sender = "0x..."
reciever = "0x..."
data = "..."
tx = {
	from: sender,
	to: reciever,
	value: web3.utils.toWei(1, 'ether'),
	gasPrice: web3.utils.toWei(10, 'gwei'),
	nonce: await web3.eth.getTransactionCount(sender),
	data : data
}
privatekey = "..."
signedtx = await web3.eth.accounts.signTransaction(tx, privatekey);
await web3.eth.sendSignedTransaction(signedtx.rawTransaction)
```