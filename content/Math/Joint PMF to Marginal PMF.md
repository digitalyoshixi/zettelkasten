---
tags:
  - math
  - calculus
  - probability
  - statistics
aliases:
  - Marginal PMF from Joint PMF
---
The individual [[Probability Mass Function|PMF]] from a [[Joint Probability Mass Function|Joint PMF]].
$$p_{X}(x) = P(X=x) = \sum_{y}P(X=x, Y=y) = \sum_{y}p_{X,Y}(x,y)$$
# Intuition
Sum all of the PMF values of $y$, and you get the PMF of that specific $x$
Think of it as reading an entire column of values representing $x$
![[Joint PMF to Marginal PMF-20251111232859009.webp|230]]