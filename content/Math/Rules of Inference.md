---
tags:
  - math
  - proofs
  - philosophy
aliases:
  - Formal Logic
  - Symbolic Logic
  - Inference Rule
---
Figures out what is true from something else.
To show that two arguments are equivalent, we could use a [[Truth Table]], but we could also use [[Deductive Reasoning]].

If an argument is valid, if the conclusion if valid. using the rules of inference you can prove the statement is a [[Tautology]].
# Rules
![[Rules of Inference-20240920123238927.webp]]
### Addition
If I have P is true, then i know that P OR whatever is true
$$P \implies P \vee Q$$
### Simplification
If both $P \wedge Q$ are true, then:
$$(P \wedge Q) \implies P$$
### Modus Ponens
$$(P \wedge (P\implies Q))\implies Q$$
If P is true, and P implies Q, then you can conclude Q.
### Modus Tollens
$$((P\implies Q) \wedge \neg Q) \implies \neg P$$
Derived from [[Contrapositive Statement]]
### Hypothetical Syllogism
$$((P\implies Q)\wedge(Q\implies R))\implies(P\implies R)$$
A statement proving a child statement, will prove that child's child aswell.
### Disjunctive Syllogism
$$((P \vee Q)\wedge \neg P) \implies Q$$
P or Q is true. if one of the terms is false, then the other must be true
### Conjunction
$$(P \wedge Q) \implies(P \wedge Q)$$
Self explanatory
### Resolution
$$((P \vee Q) \wedge(\neg P \vee R))\implies(P\vee R)$$
# Rules for [[Quantifier|Quantified]] Statements
![[Rules of Inference-20240923213935619.webp]]
If you instantiate a existence before a universal instantiation, then you cannot use the same instantiated existance variable before for the universal instantiation
### Universal Instantiation
If we show that a function works for all numbers, then we can sub in an arbitrary number into the function
### Universal Generalization
If an arbitrary number can be subbed into P(x), then P(x) work for all values of x.
You must use a fresh new variable that did not appear in the argument/proof.
### Existential Instantiation
If there exists an element c, then c cannot be arbitrary and there is one value c where P(c) is true
### Existential Generalization
If there is a value c that allows P(c) to be true, then we know there exist a c to allow P(c) to be true.
# Rules of Inference
![[Rules of Inference-20241119003919479.webp]]
### Simple Induction
1. P(b)
2. $\forall k\geq b,P(k)\implies P(k+1)$
Therefore, $\forall n\geq b, P(n)$
### Strong Induction
1. $\forall k\geq b(\forall b \leq i<k,P(i)\to P(k))$
Therefore, $\forall n\geq b,P(n)$
