---
tags:
  - security
  - cryptography
---
A [[Linear Congruential Generator|LCG]] [[Pseudo Random Number Generator|PRNG]].
$$
V_{j+1} = 65539 * V_{J} \mod 2^{31}
$$
With:
- Initial seed $V_{0}$ as an [[Odd Integer]]
- Often mapped to pseudorandom rationals $X_{j} = \frac{V_{j}}{2^{31}}$
Does not pass the [[Spectral Test]]