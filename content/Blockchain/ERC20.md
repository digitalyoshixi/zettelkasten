---
tags:
  - blockchain
aliases:
  - Ethereum Request for Comments 20
  - Fungible Token
---
This is a [[Token Standard]] for [[Ethereum]] [[Blockchain Token|Tokens]].
A standard for fungible tokens.
These are tokens that are equivalent, and can be exchangable with eachother
# Smart Contract [[Application Binary Interface|ABI]]
- `function name() public view returns (string)`
- `function symbol() public view returns (string)`
- `function decimals() public view returns (uint8)`
- `function totalSupply() public view returns (uint256)`
- `function balanceOf(address _owner) public view returns (uint256 balance)`
- `function transfer(address _to, uint256 _value) public returns (bool success)`
- `function transferFrom(address _from, address _to, uint256 _value) public returns (bool success)`
- `function approve(address _spender, uint256 _value) public returns (bool success)`
- `function allowance(address _owner, address _spender) public view returns (uint256 remaining)`