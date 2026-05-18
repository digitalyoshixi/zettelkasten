---
tags:
  - blockchain
---
This is a key-value database subset of [[Blockchain World State]] that is shared between all [[Contract Account]].
Implemented with storage slots (32-byte) of which there are $2^{256}-1$
# Getting Storage Value [[Web3js]]
```
web3.eth.get_storage_at(smart_contract_addr, mem_address)
```
```
web3.eth.getStorageAt("0x9168fBa74ADA0EB1DA81b8E9AeB88b083b42eBB4", “0x290decd9548b62a8d60345a988386fc84ba6bc95484008f6362f93160ef3e564”)
```
### Arrays
- Find where array is stored (keccak256 of storage slot)
- Add eleement index to access specific element
### Mapping
- FInd keccak256 (32-byte value || 32-byte padded storage slot)