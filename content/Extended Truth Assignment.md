---
tags:
  - math
  - programming
aliases:
  - ETA
---
A function $\tau^{*} : \mathcal{F} \to \{ 0,1 \}$

When evaluated, $\tau^{*}(x)= \tau(x)$
# Properties
- $\tau^{*}(\neg p_{1}) = 1 - \tau^{*}(p_{1})$
- $\tau^{*}( (p_{1} \wedge p_{2})) = \tau^{*}(p_{1}) * \tau^{*}(p_{2}) = min(\tau^{*}(p_{1}) , \tau^{*}(p_{2}))$
- $\tau^{*}(p_{1} \vee p_{2}) = max(\tau^{*}(p_{1}), \tau^{*}(p_{2}))$
- $$\tau^{*}( (p_{1} \to p_{2}) ) = \begin{cases}
1 & \text{ if } \tau^*(p_1) = 0 \text{ or } \tau^{*}(p_{2}) = 1\\
0 & \text{ otherwise }
\end{cases}$$
- $$\tau^{*}( (p_{1} \Longleftrightarrow p_{2}) ) = \begin{cases}
1 & \text{ if } \tau^*(p_1) = \tau^{*}(p_{2})\\
0 & \text{ otherwise }
\end{cases}$$

