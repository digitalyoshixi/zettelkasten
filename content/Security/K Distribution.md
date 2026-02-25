---
tags:
  - math
  - cryptography
---
# Definition
A sequence $x_{i}$ of period $P$ is $k$-distributed to $v$-bit accuracy if:
- The series $(\text{trunc}_v(x),\dots,\text{trunc}_{v}(x_{i+k+1}))$ for $0\leq i < P$ has each combination of bits ($2^{kv}$ total) occur the same number of times (except for the all-zero combination)
- Where $\text{trunc}_{v}(x)$ is the [[Truncation Function]] 
# Intuition
Taking the v-bit truncations of each element of the stream and plotting it out in a distribution, allows [[Uniform Continuous Probability Distribution]]