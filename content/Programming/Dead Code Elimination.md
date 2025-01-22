---
tags:
  - programming
---
Used for [[Compiler Optimization]]
1. Look for every block that has `unreachable`
2. If any code blocks end in `unreachable`, you can remove the branches leading to it.
3. Remove all unreachable code blocks\

# Use Cases
- Can be used in division by error cases, the compiler will never go to the branch that handles division by 0.