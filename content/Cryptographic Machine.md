---
tags:
  - security
  - cryptography
---
# Definition
A machine is a [[Tuple|Triple]] $\mu = (\text{ID},c, \tilde{\mu}$ with:
- An identity element $c \in \mathbb{N}$ that is visible to $\mu$ and constant
- Interaction tapes $c = \mathbb{N} \times \{ \text{input, sub-output, backdoor} \}$ that is a [[Commutative]] set:
	- Inputs
	- [[Subroutine]] outputs
	- [[Backdoor]] (comes from adversary)
- A code $\tilde{\mu}$ - a [[Turing Machine]] that represents what the machine can do
Has properties:
- [[Polynomial Time|Polynomial-Time-ness]] - there are finite interaction tapes
![[Cryptographic Machine-20260207002551592.webp|472]]
# Example Secure Channel
$\mu_{1} = (1, \{ 2, \text{input}, (A, \text{backdoor}), \tilde\mu_{1}\}$
$\mu_{2} = (2, \{ 1, \text{subroutine-output}, (A, \text{backdoor}), \tilde{ \mu_{2}} \}$
