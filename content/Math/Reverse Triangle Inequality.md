---
tags:
  - math
  - proofs
---
Assuming $0 \leq x \leq y$
$||x|-|y|| \leq |x-y|$
# Proof
Assume we already proved laws 1-5 for [[Absolute Function for Real Numbers]]. and the [[Triangle Inequality]]
Understand aswell, that to show an absolute function is true. you need to show $|a|\leq b \Leftrightarrow -b \leq a \leq b$
Let $x,y \in R$

1.
$|x| - |y| \leq|x-y|$
let $m = x-y$ and $n = y$
$|m+n| \leq |m|+|n|$ by [[Triangle Inequality]]
$|x| \leq |x-y| + |y|$ 
$|x|-|y| \leq |x-y|$
2.
$|x|-|y| \geq-|x-y|$
$m = y-x$
$n = x$
$|m+n|\leq|m|+|n|$ by [[Triangle Inequality]]
$|y|\leq|y-x|+|x|$
$-|y-x|\leq|x|-|y|$

Since both the propositions in $|a|\leq b \Leftrightarrow -b \leq a \leq b$ are shown, we have proved the inequality.