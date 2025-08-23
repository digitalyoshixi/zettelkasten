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
1. We know that the factors for $N$ is: $(g^{\frac{p}{2}}-1)(g^{\frac{p}{2}}+1) = mN$ by [[Fermat's Little Theorem]]
2. Estimates the period $p$
3. We can accurately guess what $(g^{\frac{p}{2}} \pm 1)$ could be by calculating the remainder away from the expected $N$ in [[Parallelism|Parallel]]
4. With [[Quantum Fourier Transform|QFT]], we can remove bad guesses to find the [[Frequency]] $\frac{1}{p}$
5. Uses [[Quantum Phase Estimation]] to use modular exponentiation and the inverse of [[Quantum Fourier Transform|QFT's]] $\frac{1}{p}$ to estimate the phase $p$ of the quantum state
# Intuition
- Given a random guess of a factor, shors algorithm finds a better factor via [[Fermat's Little Theorem]]