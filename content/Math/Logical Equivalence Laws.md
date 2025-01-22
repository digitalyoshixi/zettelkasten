---
tags:
  - discrete_math
  - math
---
If two statements are logically equivalent, then their [[Truth Table|Truth Tables]] are the same.
# De Morgan's Laws
$$\neg(P\wedge Q) \equiv \neg P \vee \neg Q$$
$$
\neg(P\vee Q)\equiv \neg P\wedge \neg Q
$$
$$\overline{A \cup B} = \overline{A} \cap \overline{B}$$
# Commutative Laws
$$P\wedge Q\equiv Q\wedge P$$
$$
P \vee Q \equiv Q \vee P
$$
# Associative Laws
$$
P \wedge (Q \wedge R) \equiv (P \wedge Q )\wedge R
$$
$$
P \vee (Q \vee R) \equiv (P \vee V) \vee R
$$
# Idempotent Laws
$$P \wedge P \equiv P$$
$$
P \vee P \equiv P
$$
# Distributive Laws
$$
P \wedge (Q \vee R) \equiv (P \wedge Q) \vee (P \wedge R)
$$
$$
P \vee (Q \wedge R) \equiv (P \vee Q) \wedge (P \vee R)
$$
# Absorption Laws
$$
P \vee (P \wedge Q) \equiv P
$$
$$
P \wedge (P \vee Q) \equiv P
$$
# Double Negation Law
$$
\neg \neg P \equiv P
$$
# Conditional Laws
$$P \implies Q \equiv \neg P \vee Q$$
$$
P \implies Q \equiv \neg(P \wedge \neg Q)
$$
# Contrapositive Law
$P \implies Q \equiv \neg Q \implies \neg P$
# Biconditional Law
$$P \Longleftrightarrow Q \equiv P\implies Q \wedge Q\implies P$$
# Domination Laws
Derived from [[Tautology]] and [[Contradiction]].
$$P \vee T \equiv T$$ $$P \wedge F \equiv F$$ 
# [[Quantifier]] Exchange
$$\neg (\forall x,P(x))\equiv \exists x,\neg P(x)$$
$$\neg (\exists x,P(x))\equiv \forall x,\neg P(x)$$
