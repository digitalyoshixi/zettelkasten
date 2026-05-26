---
tags:
  - programming
  - solidity
aliases:
  - Solidity Function Specifiers
  - Solidity Function Modifiers
  - Solidity Function Behaviors
cssclasses:
---
```solidity
function give_money(address addr, uint256 amt) public payable {
	require(amt >= 0);
	require(amt == msg.value);
	accountBalances[addr]+=amt;
}
```


```solidity
function FunctionName([parameters]) {public|private|internal|external} [pure|view|payable] [modifiers] [returns (return type)]
```
Defined in [[Application Binary Interface|ABI]] with [[Ethereum Function Selector]]
# Visibility Modifiers

| Modifier | Applies to                     | Description                       |
| -------- | ------------------------------ | --------------------------------- |
| public   | Contract, variables, functions | Visible externally and internally |
| private  | Contract, variables, functions | Only visible in current contact   |
| external | Functions                      | Visible externally                |
| internal | Functions                      | Only visible internally           |
# State Modifiers

| Modifier  | Applies to      | Description                                                     |
| --------- | --------------- | --------------------------------------------------------------- |
| constant  | State variables | Value is assigned before runtime, constant                      |
| immutable | State variables | Value assigned during runtime, constant                         |
| view      | functions       | Function can view contract state, can't write to contract state |
| pure      | functions       | Not allowed to read or write to contact state                   |
# Payment Modifiers

| Modifier | Applies to | Description                                         |
| -------- | ---------- | --------------------------------------------------- |
| payable  | Functions  | Function can recieve [[Ethereum Currencies\|Ether]] |
# Custom Modifiers
```
modifier onlyOwner {
	require(msg.sender == owner);
	_;
}

function pause() public onlyOwner;
```
