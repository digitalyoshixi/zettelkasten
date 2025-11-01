---
tags:
  - math
  - programming
---
# Example
With [[Alphabet]] $\Sigma = \{ 0,1 \}$
With [[Programming/Language|Language]] $L = \{ x \in \Sigma^{*} : \#_{0}(x) = \#_{1}(x)  \}$
The [[Context Free Grammar|CFG]] that generates $L$ is:
$$
\begin{align}
S \to 0A, 1B, \epsilon\\
A \to 1S, 0AA\\
B \to 0S, 1BB\\
\end{align}
$$
# Alternate CFG
$$
S \to \epsilon, 0S1S, 1S0S
$$
