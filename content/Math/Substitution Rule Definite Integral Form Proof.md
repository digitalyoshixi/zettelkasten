---
tags:
  - math
  - calculus
  - proofs
---
1. Suppose $f(x), g(x), f(g(x))g'(x)$ are continuous on $[a,b]$
2. Then, let $F$ be an antiderivative of $f$ on $[a,b]$. This exists by [[Fundamental Theorem of Calculus Part 2|FToC Part 2]]
3. Consider $\int_{a}^{b} f(u) \, du$
4. $= F(u)|_{g(a)}^{g(b)}$ by [[Fundamental Theorem of Calculus Part 1|FToC Part 1]]
5. $= F(g(b)) - F(g(a))$
6. $= F(g(x))|_{a}^{b}$ by [[Fundamental Theorem of Calculus Part 1|FToC Part 1]]
7. $= \int_{a}^{b} f(g(x))g'(x) \, dx$ as $F(g(x))$ is an antiderivative of $f(g(x))g'(x)$ (See [[Reverse Chain Rule]])
Thus, $L.S = R.S$
