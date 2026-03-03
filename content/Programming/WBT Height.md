---
tags:
  - programming
  - math
---
$$
Height(T) \leq \frac{\log(weight(T))}{\log(\frac{4}{3})}
$$
# Proof
1. With [[Induction Hypothesis|IH]] as $\forall k \in \mathbb{N}, 0 \leq k \leq n, Height(T') \leq \frac{\log(k+1)}{\log(4/3)}$  where $size(T') = k$
2. Then, $size(T)+1$
3. $=n+1$ (where $n=size(T)$)
4. $=l+r+1+1$
5. $\geq \frac{r+1}{3} + r + 1$ as $l+1\geq \frac{r+1}{3}$ by WBT condition
6. $=(r+1)* 4/3$
7. $\implies r+1 \leq \frac{n+1}{4/3}$
8. [[Without Loss of Generality|WLOG]], assume $Height(T.left) < Height(T.right)$
9. Thus, $height(T) = height(T.right)+1$ by defn of height
10. $l = size(T.left)$
11. $r = size(T.right)$
12. $height(T.right)+1 \leq \frac{\log(r+1)}{\log(4 / 3)}+1$
13. $\leq \frac{\log\left( \frac{n+1}{4 / 3} \right)}{\log(4 / 3)} + 1$
14. $= \frac{\log(n+1)}{\log(4 / 3)}$