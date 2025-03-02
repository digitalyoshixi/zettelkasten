---
tags:
  - math
  - linalg
---
# Process
We want to represent a solution as $x_{p} + x_{n}$
1. Get a particular solution
2. Solve the [[Homogenous Systems]]
# Example
$$
f(x) = \begin{cases} 
x+y+z = 1\\
z = 3
          
       \end{cases}
$$
1. We find a particular solution $(0,-2,3)$
2. We solve the homogenous system, and we get $span \{ (1,-1,0) \}$
3. Thus, the solution is $(0,-2,3) + span \{ (1,-1,0) \}$