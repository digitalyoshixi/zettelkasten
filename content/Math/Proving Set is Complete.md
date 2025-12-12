---
tags:
  - math
  - programming
---
Use [[Proof by Structural Induction]]
# Structure
We want to show that set $C$ is complete
1. Define set $\mathcal{G}$ that [[Complete Set of Boolean Connectives|uoc]] $\{ \neg, \wedge \}$ or $\{ \neg, \vee \}$
2. Use [[Proof by Structural Induction]] to prove that for every forumla $F \in \mathcal{G}, \exists F'$ s.t $F'$ [[Complete Set of Boolean Connectives|uoc]] $C$
# Example
Prove that [[Zero Identity]] and implication forma complete set.
$\{ 0, \to \}$
### Step 1
Define set $\mathcal{G}$ of formulas that [[Complete Set of Boolean Connectives|uoc]] $\{ \neg, \vee \}$
- Let $\mathcal{G}$ be the smallest set such that:
	- Basis: $x$ is a propositional variable, then $x \in \mathcal{G}$
	- Induction step: If $F_{1}, F_{2} \in \mathcal{G}$, then $\neg F_{1}, (F_{1} \vee F_{2}) \in \mathcal{G}$
### Step 2
Now we prove that for all formula $F \in \mathcal{G}$, $\exists$ formula $F'$ s.t
$F'$ [[Complete Set of Boolean Connectives|uoc]] $\{ 0, \to \}$ and $F' \equiv F$
##### Basis
Let $F = x$ where $x$ is a propositional variable
Then $F'$ [[Complete Set of Boolean Connectives|uoc]] $\{ 0, \to \}$ (F' uses no connectives at all)
And $F' \equiv F$ ($F' = F$)
As wanted
##### Induction Step
Suppose that are formulas $F_{1}'$ and $F_{2}'$ s.t
$F_{1}', F_{2}'$ [[Complete Set of Boolean Connectives|uoc]] $\{ 0, \to \}$ and $F_{1}' \equiv F_{1}$ and $F_{2}' \equiv F_{2}$ ([[Induction Hypothesis|IH]])
Then, there are two cases:
- $F = \neg F_{1}$
- $F = (F_{1} \vee F_{2})$
Case 1:
- For $F = \neg F_{1}$, let $F' = (F_{1}' \to 0 F_{1}')$
	- Then, $F'$ [[Complete Set of Boolean Connectives|uoc]] $\{ 0, \to \}$ by [[Induction Hypothesis|IH]] as $F_{1}'$ [[Complete Set of Boolean Connectives|uoc]] $\{ 0, \to \}$
	- and, $F' = \{ 0 , \to \} \equiv (F_{1} \to 0F_{1})$ by [[Induction Hypothesis|IH]] as $F_{1}' \equiv F_{1}$
	- $\equiv \neg F_{1}$ as $0F_{1}$ is always falsified so $F_{1} \to 0F_{1}$ is satisfied when $F_{1}$ is false
	- $= F$'
Case  2:
- For $F = (F_{1} \vee F_{2}),$ let $F' = ((F_{1}' \to 0F_{1}') \to F_{2}')$
- Then, $F'$ [[Complete Set of Boolean Connectives|uoc]] $\{  0, \to \}$
- and $F' = ( (F_{1}' \to 0F_{1}') \to F_{2}')$
- $\equiv ((F_{1} \to 0F_{1}) \to F_{2})$
- $\equiv (\neg F_{1} \to F_{2})$
- $\equiv (\neg \neg F_{1} \vee F_{2})$
- $\equiv (F_{1} \vee F_{2})$
- $= F$
- As wanted $\square$
### Step 3
Since $\{ \neg, \vee \}$ is complete, therefore $\{ 0, \to \}$ is also complete $\square$