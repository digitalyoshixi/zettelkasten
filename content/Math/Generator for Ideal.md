---
tags:
  - math
  - linalg
---
# Generation Types
### Ideal
- For Ring $(R,+,x)$
- For [[Ideal]] $I \subset R$
- The generator $G$ is the subset of elements $G \subset I$ that forms a [[Spanning Set|Generating Set]] for $I$
### Principle Ideal
- For Ring $(R,+,x)$
- For [[Principle Ideal]] $I$
- The generator $G$ is the single element $G \in I$ that is the [[Spanning Set|Generating Set]] of the principle ideal
# Example
### Problem
With $\mathbb{Z}_{7}[x]$, show the set of polynomials annihilated at $x=4$ is an ideal. 
### Soln
Showing non-empty:
- Suppose $g \in I$ and $f \in \mathbb{Z}_{7}[x]$. (We suppose, because we dont know these exist yet)
- Then, $(fg)(4) = f(4)g(4) = f(4)(0) = 0$
- Thus, $fg \in I$
- Consider $g(x) = x+3$
- Then, $g(4) = 4+3 = 7 \mod 7 = 0$
- Thus, $g \in I$
Then, it follows that $I$ is non-empty!
### Problem
Show that the set of $x+3$ is the generator
### Soln
- Suppose $f \in I$, then by defn, $f(4) = 0$
- Then, by the [[Fundamental Remainder Theorem]], there exists a $g \in \mathbb{Z}_{7}[x]$ s.t $f(x) = (x + (-4)) * g(x)$
- $= (x+3) * g(x)$ as $3$ is the [[Additive Inverse]] of $4$ in $\mathbb{Z}_{7}$
- Thus, $\exists g \in \mathbb{R}$ s.t $f = (x+3) * g$
- As $f$ is a generic element, the set $x+3$ is a generator for $I$