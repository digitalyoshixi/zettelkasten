---
tags:
  - math
  - linalg
---
# Theorem
Suppose $V = W_{1} \oplus \dots \oplus W_{k}$
Then, there exists $E_{1}, \dots, E_{k} \in \mathcal{L}(V)$
1. $E_{j}^{2} = E_{j}, \forall j$
2. $E_{i}E_{j} = 0$ if $i \neq j$
3. $I = E_{1} +\dots +e_{k}$
4. $range(E_{i}) = W_{i}, \forall i$
# Proofs
$$
E_{j}(\alpha_{ik}) = \begin{cases} 
          0 & i \neq j\\
          a_{ik}& i = j
       \end{cases}
$$
Given this definition,
$$
E_{j}(\alpha_{ik})^{2} = \begin{cases} 
          E_{j}(0) & i \neq j\\
          E_{j}(a_{ik})& i = j
       \end{cases}
= \begin{cases} 
          0 & i \neq j\\
          a_{ik} & i = j
       \end{cases}
$$
