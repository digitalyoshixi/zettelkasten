---
tags:
  - blockchain
aliases:
  - Transaction
  - Transactions
---
A record of transferring of data between two [[Blockchain Wallet]] on a [[Blockchain Network]]. 
- In some blockchains ([[Bitcoin]], can only send [[Cryptocurrency]], no data)
- In programmable blockchains ([[Ethereum]], can send custom [[Ethereum Bytecode]])
# Struct
```
> web3.eth.getTransaction('0xc5eee3ae9cf10fbee05325e3a25c3b19489783612e36cb55b054c2cb4f82fc28')
{
  blockHash: '0xdb85c62ef50103f08e9220b59d6c08cbfb52e61d84926dedb3fe9b6940e6bbea',
  blockNumber: 290081,
  from: '0x1dcb8d1f0fcc8cbc8c2d76528e877f915e299fbe',
  gas: 90000,
  gasPrice: 50000000000',
  hash: '0xc5eee3ae9cf10fbee05325e3a25c3b19489783612e36cb55b054c2cb4f82fc28',
  input: '0x',
  nonce: 34344,
  to: '0x702bd0d370bbf0b97b66fe95578c62697c583393',
  transactionIndex: 0,
  value: 5000111390000000000'
}
```
# Verification
Each node can verify it once its in a [[Transaction Block]]
![[Transaction-20260506030521883.webp]]