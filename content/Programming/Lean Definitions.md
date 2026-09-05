---
tags:
  - programming
  - verification
aliases:
  - Lean Functions
---
Used to bind expressions to names.
```
def hello := "Hello"
```
# Function Definition
```lean
def add1 (n : Nat) : Nat := n + 1
```

```lean
def maximum (n : Nat) (k : Nat) : Nat := if n < k then k else n
```