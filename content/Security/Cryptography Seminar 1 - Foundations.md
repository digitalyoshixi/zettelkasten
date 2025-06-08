---
tags:
  - cryptography
---
A seminar by Eleanor on [[Metauni]]
# Video URL
https://invidious.yoshixi.net/watch?v=zer9563S6zM&listen=false
# Notes
- Goal of cryptography is to create systems and prove their security
- Systems in this sense are efficiently computable algorithms
- They also satisfy [[Correctness]]
- Theoretical cryptographers try and avoid [[Symmetric Encryption]] because it gets ugly in proofs of [[Correctness]]. They usually work with [[Public-Key Cryptography|Asymmetric Cryptography]]
- All asymmetric cryptography will have (with public key $Pk$, private key $Sk$, cipher text $e$, message $M$):
	- Generating algorithm $Gen : \mathbb{N}^{+} \to Pk \times Sk$
	- Encryption algorithm $Enc: Pk \times M \to e$
	- Decryption algorithm $Dec : Sk \times e \to M$
- Security can be thought of as computational problems or distinguishing problems
	- Computational problems include: [[Discrete Logarithm Problem]]
	- Distinguishing problems include: [[Decisional Diffie Hellman Assumption]]
- With two parties, we model algorithms to be [[Probabilistic Polynomial Time]].
	- We have one $A$ (Adversary) party
	- We have one $C$ (Challenger) party
- [[Indistinguishability]] derived from [[Indistinguishability Under Chosen Plaintext Attack]]
- Crypto systems are considered secure if no adversary can win the game with significantly greater probability than an adversary who guesses randomly
- Textbook [[RSA]] is [[Deterministic Algorithm]], meaning the [[Indistinguishability Under Chosen Plaintext Attack|IND-CPA]] game does not have an even probability. Attackers can brute force easily
- [[Indistinguishability Under Chosen Plaintext Attack|IND-CPA]] is secure if $\forall$ [[Probabilistic Polynomial Time|PPT]] adversaries, the probability that the adversary wins - $\frac{1}{2}$ is [[Negligible Function]].
	- $|Pr[G^{\lambda,S}_{IND-CPA}(\lambda) - \frac{1}{2}] \in negl(\lambda)$
- [[Indistinguishability Under Chosen Plaintext Attack|IND-CPA]] is limited by:
	- [[Composability]]
	- Strength of the security also depends on the game. Some [[Indistinguishability Under Chosen Plaintext Attack|IND-CPA]] systems are better suited to specific games
- [[Universal Composability]] attempts to address these limitations
- A one-time pad like [[XOR cipher]] with [[Quantum Key Exchange]], is not universally composable, as, any outside observer not entangled, will be able to see the information passed during quantum key exchange. (Its a [[Post-Quantum Cryptography]] issue)
- [[Indistinguishability Under Chosen Ciphertext Attack|IND-CCA]] is a better game that takes into consideration if a party can decrypt their any message other than the target message. Avoids [[Malleability]]
	- [[Strong|Stronger]] than [[Indistinguishability Under Chosen Plaintext Attack|IND-CPA]], by the fact that it has this extra condition of free decryption
- Eleanor believes [[Indistinguishability Under Chosen Ciphertext Attack|IND-CCA]] is too strong, and kind of silly definition
- You can create a System $S = (Gen, Enc, Dec)$ that satisfies [[Indistinguishability Under Chosen Ciphertext Attack|IND-CCA]], and then create another system $S' = (Gen, Enc', Dec')$ Where:
	- $Enc' = (pk, m) = End(pk,m) \mid G, G \leftarrow \{  0, 1 \}$
	- $Dec'(sk, c) = Dec(sk, c[:-1])$
	- Note that the only difference here is there is an extra bit at the end
	- So, the attacker can just ask for the decryption of the ciphertext, then invert the last bit, and now they have the original message
- 