---
tags:
  - programming
  - cryptography
---
A method to add auxiliary information in cases where [[Hash Collision]] happens.
# Approaches
### Closed Addressing
Adding keys to [[Bucket]] they hash to. Involves creating additional data structure for the [[Bucket]].
- [[Collision Resolution Chaining]]
### Open Addressing
A method for [[Collision Resolution]] that gives a general rule of where to look for finding specific keys.
- [[Collision Resolution Probe Sequence]]