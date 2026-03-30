---
tags:
  - math
  - linalg
---
For a $2 \times 2$ matrix, we have the formula
$$\det 
\left[\begin{array}{cc}
a & b\\
c & d\\
\end{array}\right] = ad - bc
$$
# Proof
1. Let 
$$\det (\left[\begin{array}{cc}
a & b\\
c & d\\
\end{array}\right] ) = \det(a e_{1} + be_{2} + ce_{3} + de_{4})
$$
2. $= a \det(e_{1}, ce_{1} , de_{2}) + b \det(e_{21}e_{c_{1}} + d_{e_{2}})$
3. $= a[c \det(e_{1},e_{2}) + d \det(e_{1},e_{2})] + b [c \det (e_{2}, e_{1}) + d \det(e_{2}, e_{2})$
4. $= a[0 + d] + b[-c + 0] = ad - bc$