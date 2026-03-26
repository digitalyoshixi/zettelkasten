---
tags:
  - programming
  - machine_learning
aliases:
---
A [[Sentence|Clause]] that has a conclusion of antecedents.
$$
c \leftarrow h_{1} \wedge h_{2} \wedge \dots \wedge h_{n}
$$
# Terminology
- $c$ : Goal, Head, Consequent
- $h_{1}$ : Subgoals, Tails, Antecedent
- Horn clause $c$ by itself: Fact
- Horn clause with only its tail $h_{1} \wedge \dots \wedge h_{n}$: [[Resolution Rule]]
# [[Undecidable]] Cases
There are no known solutions for defining rules for expression:
- $a_{1} \wedge \dots \wedge a_{3} \to c_{1} \wedge c_{2}$
- $a_{1} \wedge \dots \wedge a_{3} \to c_{1} \vee c_{2}$
# [[Polarity]]
- $\neg S \wedge \neg T \to c$
- $\neg S \wedge \neg T \to c$