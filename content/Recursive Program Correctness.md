---
tags:
  - proofs
  - programming
---
The goal is to construct a [[Predicate]] $P(n)$ that holds for all input sizes $n$
# Process
1. Define $P(n)$ : If precondition holds, and program runs and, input size is $n$, then the program halts and the postcondition holds after it halts
2. Use [[Proof by Strong Induction|PCI]] to prove that $P(n)$ holds for every $n \in \mathbb{N}$ with base case being the smallest number required of the program
# Example
With the algorithm:
```python
isPal(x):
(1)	if len(x) < 2: 	return True
(2)	if x[0] != x[len(x) - 1]: return False
(3)	return isPal(x[1:len(x)-1])
```
Then, lets prove that it is correct:
- Define [[Logical Predicate]] $Q$ on $\mathbb{N}$ where
- $Q(n) : \text{if x is a string and n = len(x) then, isPal(x) returns true } \Longleftrightarrow \text{ x is a palindrome}$
- We will use [[Peripheral Component Interconnect|PCI]] that $Q(n)$ holds for every $n \in \mathbb{N}$
Base case: Consider cases $n=0, n=1$
- Then, this is correct because every string of length $< 2$ is a palindrome
Induction step:
- Let $n > 1$
- Suppose $Q(j)$ holds whenever $0 \leq j < n$ [[Induction Hypothesis]]
- We want to prove: $Q(n)$ holds
- Consider two cases:
	1. `x[0] != x[len(x)-1]`
	2. `x[0] = x[len(x)-1]`
- If `x[0] != x[len(x)-1]` then, `isPal(x)` returns false by $(2)$
	- This is correct by specification
- If `x[0] == x[len(x)-1]` then, `isPal(x)` returns `isPal(x[1:len(x)-1])` lines $(1-3)$
- `isPal(x[1:len(x)-1])` returns true if `x[1:len(x)-1]` is a palindrome, which is true by [[Induction Hypothesis|IH]]
	- Thus, this is correct by specification
- Thus, our program is correct because the first and last symbols of $x$ are the same, then $x$ is a palindrome $\Longleftrightarrow$ $x$ with its first and last symbols removed is a palindrome