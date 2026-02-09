---
tags:
  - cryptography
aliases:
  - Protocol
---
# Definition
- A protocol is a [[Tuple|Pair]] of [[Stochastic Algorithm|Probabilistic]], Interactive [[Turing Machine]] $(P,V)$
- $P$ is denoted as the prover
- $V$ is denoted as the verifier
# Alternate Definition
A protocol is a [[Tuple]] $\pi = (\mu_{1}, \dots, \mu_{n})$ is a protocol if:
- Every $\mu_{i}$ has a caller of $\mu_{j}$, $\mu_{j}$ is a [[Subroutine Machine]] of $\mu_i$
- Every $\mu_{i}$ that is a [[Subroutine Machine]] of identity $\text{ID}_{j}$, if some $\mu_{j}$ has identity $\text{ID}_{j}$, then $\mu_{j}$ is a [[Caller Machine]] of $\mu_{i}$
- If there is no such $\mu_{j}$ then $\mu_{i}$ is the main machine (entry point) of $\pi$, and $\text{ID}_{j}$ is an external identity (its floating in the [[Aether]])
![[Cryptographic Protocol-20260207005726422.webp]]