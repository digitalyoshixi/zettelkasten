---
tags:
  - math
  - calculus
---
# Question
Prove that $\lim_{ (x,y) \to (2,1) } (x+5y) = 7$ using [[Limits Formalized Definition|Epsilon Delta Limit Definition]]
# Proof
Intuition is: $\lim_{ x \to (2,1) }(x+5y)=2+5*1 = 7$
Given $\epsilon > 0$
Choose $\delta = \frac{\epsilon}{6}$
Then, for any $(x,y) : 0< || (x,y) - (2,1)|| < \delta$
$\implies |x-2| < \delta , |y-1| < \delta$
Therefore, we hjave $|x+5y-7| = |x-2+5(y-1)| \leq |x-2| + 5|y-1| < \delta + 5\delta = 6\delta = 6*\frac{\epsilon}{6}*6=\epsilon$
Thus, $|x+5y-7| < \epsilon \implies \lim_{ (x,y) \to (2,1) }=7$