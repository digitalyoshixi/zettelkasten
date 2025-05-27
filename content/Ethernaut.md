---
tags:
  - blockchain
  - security
---
A blockchain security practice site
https://ethernaut.openzeppelin.com/
# Enter Game
1. Connect [[Metamask]] wallet
2. Open developer tools console
3. Get test ether from a [[Faucet]]
4. Start the level instance
5. `contract` will have the contract information required
# Commands
1. `player` : View your own player wallet address
2. `await getBalance(player)` : view your own balance
3. `ethernaut` : View sites main smart contract
4. `contract` : View games main smart contract
5. `web3.eth.getAccounts()` : View all accounts (player is one of them)
6. `web3.eth.sendTransaction({from:player, to:contract.address, value:web3.utils.toWei('0.000001', 'ether')})`
