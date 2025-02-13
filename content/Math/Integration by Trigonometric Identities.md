---
tags:
  - calculus
aliases:
  - Integration by Trigonometric Substitution
---
A process to integrate where you:
- 
# Examples
### Wrong Example
$\int \cos^3 x\, dx$
$u=\cos x$
$du= -\sin x dx$
this substitution doesn't work! there is no $\sin$ term in the original function!
### Good Example
$\int \cos^3 x\, dx$
$\int (\cos^2x)(\cos x)\, dx$
$\int (1-\sin^2x)(\cos x)\, dx$
let $u = sinx$
$du=\cos x dx$
$\int (1-u^2)du\, dx = u - \frac{u^3}{3} +c$
$=\sin x-\frac{\sin(3x)}{3}+c$
# General Rules
$\int  \sin^mx\cos ^nx \, dx$
2. If $m$ is odd, convert as many $sin^2x \to(1-\cos^2x)$
   You'll be left with $\sin x\ dx$.
   Sub $u=cosx$ and $du=-sinx\ dx$
3. if $n$ is odd, convert as many $cos^2x \to (1-\sin^2x)$
   You'll be left with $\cos xdx$
   Sub $u=\sin x$ and $du=\cos x\ dx$
4. If both $n$ and $m$ are even, use [[Half Angle Identity]] and rearrange.
