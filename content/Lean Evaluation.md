---
tags:
  - math
  - verification
  - programming
aliases:
  - Lean Expression
---
# Evaluating in Editor
```
#eval 1 + 2
```
# Function Evaluation
```
f(x)
f x
```
- You can choose to omit parentheses if you don't care about precedence
### Precendence Example
```
#eval String.append "great " (String.append "oak " "tree")
```