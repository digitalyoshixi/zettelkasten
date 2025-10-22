---
tags:
  - programming
  - math
---
For a given [[Context Free Grammar|CFG]], the parse tree can be generated from a root by every variable in its production.
# Example CFG
$$
\begin{align}
S \to ABC\\ 
A \to \epsilon \\
A \to 11A \\
B \to 0 \\
B \to 0B0 \\
C \to C10 \\
C \to C 01 \\
C \to 1
\end{align}
$$
# Tree

```mermaid
graph TD;
S-->A
S-->B
S-->C
A-->Q(1)
A-->QQ(1)
A-->eps
B-->QQQ(0)
B-->QQQQ(B)
B-->QQQQQ(0)
QQQQ-->0
C-->QQQQQQ(C)
C-->QQQQQQQ(1)
C-->QQQQQQQQ(0)
QQQQQQ-->QQQQQQQQQ(C)
QQQQQQ-->QQQQQQQQQQ(0)
QQQQQQ-->QQQQQQQQQQQ(1)
QQQQQQQQQ-->QQQQQQQQQQQQ(1)
```
