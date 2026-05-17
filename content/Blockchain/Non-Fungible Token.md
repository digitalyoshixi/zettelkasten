---
tags:
  - blockchain
aliases:
  - ERC721
  - NFT
cssclasses:
---
A framework for creating tokens 
# Smart Contract [[Application Binary Interface|ABI]]
- `function balanceOf(address _owner) external view returns (uint256)`
- `function ownerOf(address _tokenId) external view returns (address)`
- `function safeTransferFrom(address _from, address _to, uint256 _tokenId, bytes data) external payable;`
- `function safeTransferFrom(address _from, address _to, uint256 tokenId) external payable;`
- `function transferFrom(address _from, address _to, uint256 _tokenId) external payable;`
- `function approve(address _approved, uint256 _tokenId) external payable;`
- `function setApprovalForAll(address _operator, bool _approved) external;`
- `function getApproved(uint256 _tokenId) external view returns (address);`
- `function isApprovedForAll(address _owner, address _operator) external view returns (bool);`