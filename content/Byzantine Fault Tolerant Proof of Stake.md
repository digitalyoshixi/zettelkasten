---
tags:
  - blockchain
aliases:
  - BFT PoS
---
# Process
1. Proposer keeps track of proof votes for the block
2. Minters validate the block, vote for this block validation to be valid
3. BFT consensus finalize most-voted block
Does not work if more than $\frac{1}{3}$ validators are dishonest.