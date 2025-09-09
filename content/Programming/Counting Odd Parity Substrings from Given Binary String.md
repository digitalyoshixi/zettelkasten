---
tags:
  - programming
---
# Problem
Give a [[Binary String]] of size $n$, return the number of [[String Parity|Odd Parity]] substrings to be generated from a string.
# Solution (Linear Time)
Assuming we are given a zero-indexed string $x$
Define a function
$$
f(i) = \begin{cases}
0 & \text{if } i = 1 \text{ and } x[0]=0\\
1 & \text{if } i = 1 \text{ and } x[0]=1\\
f(i-1)+g(i) & \text{if } 1 < i \leq len(x) 
\end{cases}
$$
$$
g(i) = \begin{cases}
0 & \text{if } i = 1 \text{ and } x[0]=0\\
1 & \text{if } i = 1 \text{ and } x[0]=1\\
g(i-1) & \text{if } 1 < i \leq len(x) \text{ and } x[i-1]=0\\
i-g(i-1) & \text{if } 1 < i \leq len(x) \text{ and } x[i-1]=1
\end{cases}
$$
Then, $f(len(x))$ will be the solution.