---
tags:
  - math
  - linalg
aliases:
  - Generating Set
  - Generator Set
---
The the [[Subset]] of [[Vector Space]] $V$ [[Span|Spans]] $V$. 
# Definition
A subset $S \subset V$ is a spanning set if:
- $V = span(S)$
Look at: [[Span]]
# Examples
### Element of Set
$U = span \{ [1,0,0] , [0,0,1] \}$
An element of this spanning set could be: $[5.0.9]$ as $[5,0,9]$ can be written as a [[Linear Combination]] of $[1,0,0]$ and $[0,0,1]$ 
### Checking [[Elementhood Test]] of a vector
Say we have $U = span \{  [1,1,-1],[1,2,-1]\}$
If we want to check if $\overrightarrow{[1,2,3]} \in U$ , we need to find $a,b \in R$ s.t $a \overrightarrow{[1,1,-1]} + b \overrightarrow{[1,2,-1]} = \overrightarrow{[1,2,3]}$
So, we solve:
- $a+b=1$
- $a+2b=2$
- $-a-b=3$
There are no values $a,b$ that satisfy this case.
![[Spanning Sets-20250109143949457.webp]]
# Concepts
- [[Non-Colinear Vectors Spanning Set]]
- [[Proving Spanning Sets Equivalent]]
- [[Span of Empty Set]]