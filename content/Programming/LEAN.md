---
tags:
  - programming
---
![[LEAN-20250527010620518.webp]]
A interactive [[Theorem Prover]] to verify code correctness and mathematical theorems.
It is mainly for:
- [[Mathematics]]
- Software/Hardware verification
Is [[Strict Binding Evaluation]], does not allow infinite loops, everything must [[Turing Machine Halt|Halt]].
# Boilerplate
```
def main : IO Unit := IO.println "Hello, World!"
```
# Running Program
```
lean --run File.lean
```
# Concepts
### Meta
- [[Software Verification|Formal Verification]]
- [[Mathlib]]
- [[LEAN Graph]]
- [[Parametric Polymorphism]]
- [[Lean Unicode Shortcuts]]
### Core
- [[Lean Evaluation]]
- [[Lean Comments]]
- [[Lean Types]]
	- [[Lean Type Alias]]
	- [[Lean Inductive Type]]
	- [[Lean Option]]
	- [[Lean Prod]]
	- [[Lean Sum]]
	- [[Lean Unit]]
	- [[Lean Empty]]
	- [[Lean Check]]
- [[Lean Definitions]]
- [[Lean Conditional Expression]]
- [[Lean Foldability]]
- [[Lean Struct]]
- [[Lean Replacing Fields in a Struct]]
- [[Lean Constructor]]
- [[Lean Pattern Matching]]
- [[Lean Parametric Polymorphism]]
- [[Lean List]]
- [[Lean length]]
- [[Lean let]]
- [[Lean IO]]
### Math
- [[Lean Sorry]]
# Resources
- https://adam.math.hhu.de/
- https://leodemoura.github.io/files/CAV2024.pdf