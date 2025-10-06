---
tags:
  - math
  - machine_learning
aliases:
  - Markovian
---
A mathematical model wherein the probability of each event is only dependent on the last previous state.
It does not have **Memory**. [[Long Short Term Memory|LSTM]] models attempt to revise this.
# Probability
$$P(A_{i+1}^{*} | A_{i}^{*}, A_{i-1}^{*}, \dots, A_{1}^{*}) = P(A_{i+1}^{*}|A_{1}^{*})$$
Where $A_{i}^{*} \in \{ A_{i}, A_{i}^{'} \}$