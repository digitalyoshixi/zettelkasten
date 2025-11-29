---
tags:
  - os
---
Binary [[Semaphores]] for locking.
# Example Implementation
```solidity
bool internal locked;

modifier reentrancyGuard(){
	require(!locked);
	locked = true;
	_;
	locked = false;
}
```