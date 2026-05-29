---
tags:
  - blockchain
  - cryptography
aliases:
---
This is a [[Knowledge Proofs|Proof of Knowledge]] protocol to verify a users identity.
# Formal Definition
![[Schnorr's Protocol-20250616215317376.webp|478]]
1. With $P$ as the prover, $V$ as the verifier
2. With a function $G_{p}, p, g$ s.t $<g> = G_{P}, x \in G_{p}$ and $w \in \frac{\mathbb{Z}}{\mathbb{Z}_{p}}$ s.t $q^{w} = x$ shared between $P,V$
3. $P$ forms a commitment:
	1. With a power $k \xleftarrow{\$} \frac{\mathbb{Z}}{\mathbb{Z}_{p}}$
	2. With $t \leftarrow g^{k}$
4. $P$ sends $t$ to $V$
5. $V$ picks challenge $c \xleftarrow{\$} C \subset \frac{\mathbb{Z}}{\mathbb{Z}_{p}}$
6. $V$ send $c$ to $P$
7. $P$ computes response $r \leftarrow k+wc (\mod p)$
8. $P$ sends $r$ to $V$
9. $V$ outputs accept $\Longleftrightarrow g^{r} = tx^{c}$