---
tags:
  - calculus
aliases:
  - u Sub
---
Solve by substituting a variable as a term.
Whenever you think substitution, you want to find both $u$ and $u'$ in the function. In other terms, you want $\frac{dy}{du}$ to be a constant or in terms of x
# The Substitution Rule
### [[Definite Integral]]
- If $f(x),g(x)$ and $f(g(x))g'(x)$ are [[Continuity|Continuous]] on their domains
- Then, $\int_{a}^{b} f(g(x))g'(x) \, dx = \int_{g(b)}^{g(a)} f(u) \, du$
- Where $u = g(x)$ and $g'(x) = du$
Proof: [[Substitution Rule Definite Integral Form Proof]]
##### Example
Compute $\int_{0}^{\frac{\pi}{2}} \sin^{5}(x)\cos^{3}(x) \, dx$
Note that this is equal to $\int_{a}^{b} f(x) \, dx$
### [[Indefinite Integral]]
- If $f(x),g(x)$ and $f(g(x))g'(x)$ are [[Continuity|Continuous]] on their domains
- Then. $\int f(g(x))g'(x) \, dx = \int f(u) \, du$
- Where $u = g(x)$ and $g'(x) = du$
##### Example
Compute $\int \frac{e^{\arctan(x)}}{1+x^{2}} \, dx$
- Note $f(x)=e^{x}$
- and $g(x)=\arctan(x)$
- allows for $f(g(x))g'(x) = \frac{e^{\arctan x}}{1+x^{2}}$
Then, use Integration by substitution
- $\int f(u) du=\int e^{u} du = e^{u}+C$
- Note that by convention, $u=g(x), g'(x)=du$
- Then, $e^{u}+C = e^{g(x)}+C = e^{\arctan x}+C$
Done
### Practical uses
- [[Chain Rule Proof]]