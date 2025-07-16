---
tags:
  - math
  - linalg
---
# Example with Matrixes
- With $$A = \left[\begin{array}{cc} 
2 & 1\\
-2 & 0\\
\end{array}\right]$$
- Then, $\langle A | B \rangle = trace(AB^{*})$
- Let $W = span \{ A \}$
- Then, find $W^{\perp}$
- We consider $W^{\perp}=  \{ B |  \langle B | a A \rangle = 0 \}$
- $\implies \{ B | trace(B a A^ *)= 0 \}$
- With $$B = \left[\begin{array}{cc} 
b_{1} & b_{2}\\
b_{3} & b_{4}\\
\end{array}\right]$$
- $$\implies BaA^{*} = \left[\begin{array}{cc} 
2ab_{1} + ab_{2} & -2ab_{1}\\
2ab_{3} + ab_{4} & -2ab_{3}\\
\end{array}\right]$$
- Then, we find $tr(BaA^{*}) = 0 \implies 2ab_{1}+ab_{2} -2 ab_{3} = 0$
- Thus, $b_{1} = b_{3} - \frac{1}{2}b_{2}$
- Then, we can form a matrix: $$B = \left[\begin{array}{cc} b_{3} - \frac{1}{2}b_{3} & b_{2}\\ \\
b_{3} & b_{4}
\end{array}\right]$$
- $$\implies B = 
  \left[\begin{array}{cc} 
b_{3} & 0 \\
b_{3} & 0 \\
\end{array}\right] + 
  \left[\begin{array}{cc} 
\frac{1}{2 } b_{2} & b_{2} \\
0 & 0 \\
\end{array}\right] + 
  \left[\begin{array}{cc} 
0 & 0 \\
0 & b_{4} \\
\end{array}\right] + 
$$
- Finally, $$
W^{\perp} = span \{  
  \left[\begin{array}{cc} 
1 & 0 \\
1 & 0 \\
\end{array}\right] , 
  \left[\begin{array}{cc} 
\frac{1}{2 }  & 1 \\
0 & 0 \\
\end{array}\right] , 
  \left[\begin{array}{cc} 
0 & 0 \\
0 & 1 \\
\end{array}\right] 
\}
$$
