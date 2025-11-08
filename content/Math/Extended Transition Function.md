---
tags:
  - programming
  - math
---
A function $\delta^{*} : Q \times \Sigma^{*} \to Q$ denoting the transition states.
Can be recursively defined by [[Transition Function]].
$$
\delta^{*}(q,x) = 
\begin{cases}
q & \text{ if x = eps} \\
\delta(\delta_{3}^{*}(q,y), a) & \text{ if x = ya where } y \in \Sigma^{*}, a \in \Sigma
\end{cases}
$$
