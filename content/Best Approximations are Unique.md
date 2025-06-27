---
tags:
  - math
  - linalg
---
# Theorem
If a [[Best Approximation|Best Approximation]] exists, then it is unique.

# Prove Uniqueness
1. Suppose there exists two [[Best Approximation|Best Approximations]] $a, a'$. To show $a = a'$, it suffices to show $\langle a - a' | a - a' \rangle = 0$
2. $\langle \alpha - a' | a - a' \rangle = \langle \beta - \beta + a - a', a - a' \rangle = \langle \beta - a|, a-a' \rangle - \langle \beta - a| a - a'\rangle = 0-0 = 0$
3. Thus, $a - a' = 0 \implies a = a'$