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
	- If $\mu = \epsilon$, message written to $\mu'$ on the input tape with sender as some external entity, then, $\mu'$ runs (like [[Sockets]])
	- if $\mu \neq \epsilon$, and the destination $\text{ID}'$ is external, the message is written to $\epsilon$'s output tape with $\text{ID}$ and $\text{ID'}$ and $\epsilon$ runs. (like [[System Interrupt|Interrupt]])