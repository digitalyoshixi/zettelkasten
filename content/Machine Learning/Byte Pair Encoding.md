---
tags:
  - machine_learning
aliases:
  - BPE
---
This is a [[Tokenizer]]. Originally designed to be a [[Compression Algorithm]], but later turned to an encoder.
Encodes plaintext into tokens.
# Algorithm
1. Have a target size $k$, and a starting size $n$
2. Treats $1:n$ character streams as a token
3. The most frequent pairs of two tokens are merged together to a single $2n$ token
4. Continue until you have tokens of $k$ size