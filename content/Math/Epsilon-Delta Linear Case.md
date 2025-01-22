---
tags:
  - math
  - proofs
---
Remember the [[Limits Formalized Definition]]
$$\forall \epsilon > 0, \exists \delta >0\ such\ that\ 0 <|x-c|<\delta \implies|f(x)-L|< \epsilon$$
If we have a limit like:
$$\lim_{ x \to 3 } (-2x+1)=-5$$
Then:
- $c = 3$
- $L = -5$
- $f(x)=-2x+1$
- $x =x$
### Rough Work
We would then find a value $\delta$ such that $|x-3|<\delta$, $|-2x+1-(-5)| < \epsilon$
Rearrange the epsilon statement
$|-2x+6|<\epsilon$
$2|x-3|<\epsilon\$
$|x-3|< \frac{\epsilon}{2}$
Then, we can say that $\delta=\frac{\epsilon}{2}$
### Proof
Let $\epsilon>0$ be arbitrary
Choose $\delta=\frac{\epsilon}{2}$
Assume $|x-3|<\delta$
Assume $|-2x+1-(-5)|<\epsilon$
Now, $|-2x+1-(-5)| = |-2x+6|=2|x-3| <2 \frac{\epsilon}{2}$
$2|x-3|<\epsilon$
Thus, $|(-2x+1)-(-5)| < \epsilon$
$\square$