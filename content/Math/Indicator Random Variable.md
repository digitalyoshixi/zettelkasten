---
tags:
  - math
  - statistics
aliases:
  - Indicator RV
  - Characteristic RV
  - Indicator Function
"":
---
A [[Discrete Random Variable]] that is split into two sets used to describe if an event will happen.
![[Indicator Random Variable-20250916134957824.webp]]
# Example
Consider events $A,B$ and Indicator RVs $I_{A}, I_{B}$
Show that $1-I_{A}$ is an indicator RV:
### Soln
$$h(I_{A}(x)) = 1 - I_{A} = 
\begin{cases} 
1 & S \in A^{c}\\
0 & S \in A
\end{cases}
$$
# Example 2
Show that $I_{A} \times I_{B}$ is an indicator RV:
### Soln
$$h(I_{A}(x)) = I_{A} \times I_{B} = 
\begin{cases}  
1 & s \in A \cap s \in B \implies s \in A \cap B \\
0 & s \in (A \cap B)^{c} \implies s \in A^{c} \cup B^{c}
\end{cases}
$$