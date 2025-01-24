---
tags:
  - math
  - linalg
---
# Example
Represent subspace $W = \{ (x,y,z) : x + 2y + 3z = 0 \wedge x+y+z=0 \}$

The subspace W is the set of solns of:
$$
\lbrace
\begin{align*}
 \text{x+2y+3z=0} & \text{(1)} \\
 \text{x+y+z=0} & \text{(2)} \\
\end{align*}
$$
$\Longleftrightarrow$
By subtracting (1) from (2)
$$
\lbrace
\begin{align*}
 \text{y+2z0} & \text{(1)} \\
 \text{x+y+z=0} & \text{(2)} \\
\end{align*}
$$
$\Longleftrightarrow$
$$
\lbrace
\begin{align*}
 \text{y+2z0} & \text{(1)} \\
 \text{x-z=0} & \text{(2)} \\
\end{align*}
$$
$\Longleftrightarrow$
$$
\lbrace
\begin{align*}
 \text{y=-2z} & \text{(2)} \\
 \text{x=z} & \text{(2)} \\
 \text{z=z} & \text{(2)} \\
\end{align*}
$$
This gives $(x,y,z) = (z,-2z,z)$ and so $W = span({1,-2,1})$