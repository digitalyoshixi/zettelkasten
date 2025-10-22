---
tags:
  - math
  - programming
---
For [[Programming/Language|Language]] $L_{2} = \{ x \in \Sigma^{*} : \#_{11}(x) = \#_{00}(x) \}$
Define:
- $A_{00} = \{ x \in L : \text{ x starts with 0, ends with 0} \}$
- $A_{01} = \{ x \in L : \text{ x starts with 0, ends with 1} \}$
- $A_{10} = \{ x \in L : \text{ x starts with 1, ends with 0} \}$
- $A_{11} = \{ x \in L : \text{ x starts with 1, ends with 1} \}$
Design: 
We can construct 
$$
\begin{align}
S \to \epsilon, A_{00}, A_{01}, A_{10}, A_{11}\\
\end{align}
$$
Now for $A_{00}$:
There are three cases:
- $A_{00}$ has no second bit
- $A_{00}$ has a second bit as $1$
- $A_{00}$ has a second bit as 0
For these cases:
$$
\begin{align}
A_{00} \to 0 & \quad \text{for $A_{00}$ has no second bit} \\
A_{00} \to 0A_{10} &\quad \text{ for $A_{00}$ has second bit as 0} \\
A_{00} \to 0A_{01}A_{10} &\quad \text{ for $A_{00}$ has second bit as 1} \\
\end{align}
$$
Now for $A_{01}$:
There are three cases:
- $A_{01}$ has a second bit as 1
- $A_{01}$ has a second bit as $0$
$$
\begin{align}
A_{01} \to 0A_{11} &\quad \text{ for $A_{00}$ has second bit 1} \\
A_{01} \to 0A_{01}A_{11} &\quad \text{ for $A_{00}$ has second bit 0} \\
\end{align}
$$
So on so forth