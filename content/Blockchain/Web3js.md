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
# Initialization
```js
var Web3 = require('web3');

var web3 = new Web3(/* provider */)
```
# Metamask Initialization
```js
App = {
    load: async () => {
        // loading app 
        await App.loadWeb3()
        console.log("app is loading")
    },

    // https://medium.com/metamask/https-medium-com-metamask-breaking-change-injecting-web3-7722797916a8
  loadWeb3: async () => {
    if (typeof web3 !== 'undefined') {
      App.web3Provider = web3.currentProvider
      web3 = new Web3(web3.currentProvider)
    } else {
      window.alert("Please connect to Metamask.")
    }
    // Modern dapp browsers...
    if (window.ethereum) {
      window.web3 = new Web3(ethereum)
      try {
        // Request account access if needed
        await ethereum.enable()
        // Acccounts now exposed
        web3.eth.sendTransaction({/* ... */})
      } catch (error) {
        // User denied account access...
      }
    }
    // Legacy dapp browsers...
    else if (window.web3) {
      App.web3Provider = web3.currentProvider
      window.web3 = new Web3(web3.currentProvider)
      // Acccounts always exposed
      web3.eth.sendTransaction({/* ... */})
    }
    // Non-dapp browsers...
    else {
      console.log('Non-Ethereum browser detected. You should consider trying MetaMask!')
    }
  },

}
$(() => {
        $(window).load(() =>{
            App.load()
        })
})
```