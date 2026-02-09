---
tags:
  - security
---
# Definition
- An execution of [[Cryptographic Protocol]] $\pi$ with environment $\epsilon$ and adversary $A$ on initial input $z$
  Begins by running $\epsilon$ on $z$
- Machines take turns
- When $\mu = (\text{ID}, c, \tilde{\mu})$ executes "transmit to $\text{ID}'$", $\mu$ is suspended
- Then:
	- If $\mu = \epsilon$, message written to $\mu'$ on the input tape with sender as some external entity, then, $\mu'$ runs (Environment gives input to [[Cryptographic Protocol|Protocol]])
	- if $\mu \neq \epsilon$, and the destination $\text{ID}'$ is external, the message is written to $\epsilon$'s output tape with $\text{ID}$ and $\text{ID'}$ and $\epsilon$ runs. ([[Network Protocol|Protocol]] or adversary gives output to environment)
	- Otherwise, the message is written to $\mu'$ with the given tape that the machine specifies and the $\text{ID}$ then $\mu'$ runs. ([[Cryptographic Machine]] gives message to other machine in the [[Cryptographic Protocol|Protocol]])
	- If a machine yields without transmitting $\epsilon$ runs
- When $\epsilon$ halts, it gives some output $\text{EXEC}_{\pi, A, \epsilon}(z)$ 