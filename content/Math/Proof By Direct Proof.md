---
tags:
  - proofs
aliases:
  - Proof By Construction
---
Assume $P$ is true, then conclude that $Q$ is true.
# Format
If you have the form: $(P_{1} \wedge P_{2} \wedge\dots P_{n})\implies Q$
1. Suppose all premises P are true
2. ... Use [[Logical Equivalence Laws]] and [[Rules of Inference]] to prove that $Q$
3. Q
### Examples
$\forall x,y ((x>3) \wedge(y < 2)) \implies (x^2-2y>5)$
1. Take arbitrary $x,y$
2. Suppose x > 3
3. Suppose y < 2
4. $x^2 = x*x > 3 * x > 3 * 3 =9$                                 2. by mult. by pos
5. $-2y > -4$                                                                3. multiply by negative
6. $x^2 - 2y > 9-4=5$                                                 4,5 add
7. $((x>3) \wedge (y < 2) \implies (x^2-2y>5))$                   2,3,6 implication
8. $\forall x\forall y, (x>3) \wedge (y < 2) \implies x^2 - 2y >5$               1,7 universal generalization