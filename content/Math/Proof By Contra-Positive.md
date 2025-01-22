---
tags:
  - math
  - proofs
aliases: []
---
Assume $\neg Q$ and conclude $\neg P$.
Proof by showing that when assuming the result to be false, there will also be a false condition 
# Explanation
For a proposition to be fully false, it must have a:
- True condition
- False result
If we can prove that the **false result** actually has a **false condition**, then our proposition will be saved.
### Other explanation
If $A \implies B$, then $\neg B \implies \neg A$
# Example
$\forall n \in Z:2^n > n^2 \implies n \geq 0$
If, we have a false result - in this case, $n < 0$, we must prove that the condition ($2^n > n^2$) is indeed also false.
### Proof
$Let\ n<0$
$$\implies2^n = \frac{1}{2^{-n}} < 1$$
$$\implies n^2 \geq 1$$
This further implies:
$$\implies 2^n < n^2$$
This means our condition of $2^n > n^2$ is false. Meaning this result will never be possible with our current condition.
QED