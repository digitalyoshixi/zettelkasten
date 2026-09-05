---
tags:
  - programming
aliases:
  - PTAP
---
A [[Trie|PTA]] adapted to learn a [[Moore Machine]].
PTA construction usually only works for boolean values, so we encode unique outputs to represent a bit-tuple.
# Process
- Function $f$ maps elements in the output set $O$ to bit-tuples $s_{IO} \in S_{IO}$ of length $N = \log_{2}|O|$
- Creates $N$ [[Trie|PTA]] for each bit in the bit-tuple
	- For input, output tuple $(w,y)$
	- $(w,y), y_{i}  = 1\implies w \in S_{i}^{+}$ (i-th element of output, means this input is in the i-th PTA)
	- $(w,y), y_{i}  = 0\implies w \in S_{i}^{-}$
	- Generate the PTA from these negative/positive samples
# Example
![[Moore Machine Prefix Tree Acceptor-20260710013504968.webp]]