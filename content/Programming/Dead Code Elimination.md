---
tags:
  - programming
aliases:
  - Unreachable Code Elimination
  - DCE
---
Used for [[Compiler Optimization]]. Alot easier if code is in [[Static Single Assignment|SSA]] form.
Removes [[Unreachable Code]] and [[Dead Assignment]]
# Process
1. Look for every block that has `unreachable`
2. If any code blocks end in `unreachable`, you can remove the branches leading to it.
3. Remove all unreachable code blocks
![[Dead Code Elimination-20251125032248793.webp]]
# Use Cases
- Can be used in division by error cases, the compiler will never go to the branch that handles division by 0.