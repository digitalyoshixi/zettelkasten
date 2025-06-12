---
tags:
  - blockchain
---
First, follow [[Web3js Create Contract]], to get a `contract` variable
# Reading Public Variable
```js
contract.methods.variablename().call()
```
# Sending Public Function
```js
contract.methods.function(args).send({
	from : "useraddress",
	gas : 5000000
})
```