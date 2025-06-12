---
tags:
  - blockchain
---
# Process
1. Get the smart contract bytecode compiled from [[Remix IDE]]
2. Send a transaction with data being the bytecode.
```js
sender = "0x..."
reciever = "0x..."
data = "..."
tx = {
	from: sender,
	to: reciever,
	value: web3.utils.toWei(1, 'ether'),
	gasPrice: web3.utils.toWei(10, 'ether'),
	nonce: await web3.eth.getTransactionCount(sender),
	data : data
}
privatekey = "..."
signedtx = await web3.eth.accounts.signTransaction(tx, privateKey);
await web3.eth.sendSignedTransaction(signedtx)
```