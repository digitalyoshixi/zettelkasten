---
tags:
  - programming
  - math
aliases:
  - Kleene Expression
---
An operation performed on [[Programming/Language|Language]] that generates all finite length strings.
$$L^{*} = \{  x : x \in \epsilon , \text{or } x = y_{1}y_{2} \dots y_{k}, k >0, y_{i} \in L \}$$
Alternatively,
$$L^{*} = \cup_{i \geq 0}V^{i}$$
# Kleene Star of Empty Set
$\emptyset^{*} = \{  \epsilon \}$