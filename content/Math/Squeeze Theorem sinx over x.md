---
tags:
  - calculus
  - proofs
---
# WTS
$$\lim_{ x \to 0 }\frac{\sin x}{x} $$
# Proof with [[Squeeze Theorem]] and Geometry
We make 3 triangles, the middle triangle is f(x) which we will squeeze between h(x) and g(x)
![[Squeeze Theorem sinx over x-20241007224318533.webp|421]]
We want $g(x) \leq f(x) \leq h(x)$
So 
- $g(x) = \frac{1}{2}(1)(\tan x)$
- $f(x)=\frac{1}{2}(1)(x)$
- $h(x)=\frac{1}{2}(1)(\sin x)$
Then $\sin x \leq x \leq \tan x$ (factored out $\frac{1}{2}$)
Then $1 \leq \frac{x}{\sin x}\leq \frac{1}{\cos x}$
Then $1 \geq \frac{\sin x}{x} \geq \cos x$
Then $\lim_{ x \to 0 }\cos x = 1$
Since $1 \leq \frac{\sin x}{x} \leq 1$
Using squeeze theorem, $\frac{\sin x}{x}$
