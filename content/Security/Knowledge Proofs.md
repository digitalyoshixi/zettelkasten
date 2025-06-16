---
tags:
  - information_theory
  - security
aliases:
  - Proof of Knowledge
  - PoK
---
You know something, if when given an input that includes [[Knowledge]], you can efficiently extract the knowledge from that input.
# Defintion
A [[Cryptographic Protocol|Protocol]] $(P,V)$ is a Proof of knowledge for an [[Effective Relation]] $R$ if it is:
1. [[Computationally Complete|Complete]] ($\forall (x,w) \in R$, if $P$ runs on input $(x,w)$ and $V$ on input $x$, then $V$ outputs *accept*)
2. [[Mathematically Sound]] (There exists [[Probabilistic Polynomial Time|PPT]] $\epsilon$ s.t $\forall x \in X, \hat{P}$ with a non-negligable probability of making $V$ *accept*, $\epsilon$ can interact with [[Turing Machine Rewinding|Rewindable]] $\hat{ P}$ to produce with overwhelming probability, $w \in W$ s.t $(x,w) \in R$)
### Intuition
- With a [[Cryptographic Protocol|Protocol]] that defines $(\hat{P}, V)$. For all possibly cheating [[Cryptographic Protocol|Protocols]] $\hat{P}$ that make $V$ output *accept*, we can efficiently **extract** a [[Zero Knowledge|Witness]] from $\hat{P}$ by [[Turing Machine Rewinding|Rewinding]] it.
