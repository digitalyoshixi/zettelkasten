---
tags:
  - programming
  - cryptography
aliases:
  - Close Addressing
  - Open Addressing
---
A method to add auxiliary information in cases where [[Hash Collision]] happens.
# Approaches
### Closed Addressing
Adding keys to [[Bucket]] they hash to. Involves creating additional data structure for the [[Bucket]].
- [[Collision Resolution Chaining]]
### Open Addressing
A restriction for a max of $c$ keys allowed in each bucket (often $c=1$).
Gives a general rule of where to look for finding specific keys
- [[Collision Resolution Probe Sequence]]