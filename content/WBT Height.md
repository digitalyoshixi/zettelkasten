---
tags:
  - programming
  - math
---
$$
Height(T) \leq \frac{\log(weight(T))}{\log(\frac{4}{3})}
$$
# Proof
1. [[Without Loss of Generality|WLOG]], assume $Height(T.left) < Height(T.right)$
2. Thus, $height(T) = height(T.right)+1$ by defn of height
3. $l = size(T.left)$
4. $r = size(T.right)$
5. Then, $size(T)+1$
6. $=n+1$ (where $n=size(T)$)
7. $=l+r+1+1$
8. $\geq \frac{r+1}{3} + r + 1$ as $l+1\geq \frac{r+1}{3}$ by WBT condition
9. $=(r+1)* 4/3$
10. $\implies r+1 \leq \frac{n+1}{4/3}$