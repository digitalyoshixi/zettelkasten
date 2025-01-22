---
tags:
  - calculus
  - math
aliases: Continuous
---
You can plug a in to find the limit if the function is continuous.
# Limit Approaching Value Definition
$$\lim_{ x \to c}f(x) = f(c) $$
# Definition
A function $f(x)$ is continuous at $x=a$ if $\lim_{ x \to a }f(x)=f(a)$
This definition can be thought of as a 3 part definition:
1. $f(a)$ is defined
2. $\lim_{ x \to a }f(x)$ exists. that is, $\lim_{ x \to a^- }f(x) = \lim_{ x \to a^+ }f(x)$
3. $\lim_{ x\to a }f(x)=f(a)$ (the numbers from (1) and (2) are equal)
We say that $f$ is discontinuous at $a$ if $f$ is not continuous at $a$
# Epsilon-Delta Definition
$$\forall \epsilon>0,\exists \delta>0 \text{ such that } |x-c| < \delta \Rightarrow |f(x)-f(c)|<\epsilon$$
# Graphical Interpretation
[[Euler]] expressed a continuous function as "a curve described by freely leading the hand", you can draw the graph without lifting your pencil from the paper
*Note that this definition is not rigorous enough*
# Left & Right Continuity
### Left Continuous
$$\lim_{ x \to a^- }f(x)=f(a) $$ 
### Right Continuous
$$\lim_{ x \to a^+}f(x)=f(a) $$
# Continuous Rules (Derived from [[Limits]])
- [[Continuous Sums]]
- [[Continuous Products]]
- [[Continuous Compositions]]
# Other
- [[Continuity Theorem]]
- [[Uniform Continuity]]