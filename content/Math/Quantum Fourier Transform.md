---
tags:
  - math
  - quantum_mechanics
  - cryptography
aliases:
  - QFT
---
A [[Fourier Transform]] for [[Qubit]] functions that allows similar functions to cancel out eachother.
Useful to [[Parallelism]], especially in [[Shor's Factoring Algorithm|Shor's Algorithm]].
# Process
### Single Input
Inputting a [[Qubit]] into QFT will result in an array of superposition of all other numbers with given weights.
- The weights can be arranged like a [[Sine]] wave.
- The frequency of the [[Sine]] wave is directly correlated with the magnitude of the initial [[Qubit]]
![[Quantum Fourier Transform-20250823192442061.webp]]
### [[Quantum Superposition|Superposition]] Input
Inputting a [[Quantum Superposition|Superposition]] of [[Qubit]] will result in a [[Quantum Superposition|Superposition]] of sine waves. This allows for [[Quantum Interference|Destructive Interference]] if the superpositions differ by a constant factor.
![[Quantum Fourier Transform-20250823192616266.webp]]
![[Quantum Fourier Transform-20250823192653619.webp]]