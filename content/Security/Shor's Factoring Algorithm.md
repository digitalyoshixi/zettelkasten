---
tags:
  - cryptography
  - security
aliases:
  - Shor's Algorithm
---
This is a factoring algorithm reserved for [[Quantum Computing]], used to factor numbers exponentially faster than [[Computer|Classical Computers]].
Converts a NP problem into a polynomial time problem.
# Algorithm
We want to find $g$, where $g^{p} \mod N = 1$ , Given $N$
1. Estimates the period $p$
2. We can accurately guess what $g$ could be
3. Repeats with [[Quantum Fourier Transform|QFT]], allowing the algorithm to find the period $p$ efficiently
4. Uses [[Quantum Phase Estimation]] to use modular exponentiation and the inverse of $QFT$ to estimate the phase of a quantum state