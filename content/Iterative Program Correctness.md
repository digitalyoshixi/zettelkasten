---
tags:
  - software
  - programming
---
# Process
1. Formula a [[Loop Invariant|LI]]. The [[Loop Invariant|LI]] should describe the purpose of every variable
2. Use [[Induction]] to prove [[Loop Invariant|LI]]
3. Use the [[Loop Invariant|LI]] in step 1 to prove [[Partial Correctness Step]] ($\text{loop exit condition and LI} \implies \text{postcondition}$)
4. Use [[Loop Invariant|LI]] in step 1 to prove [[Termination]]. We start by finding an expression $e$ that uses variables in the loop such that:
	1. The value of $e$ is a [[Natural Number]] starting the loop
	2. The value of $e$ decreases with every iteration
5. Prove the sequence of values of $e$ after each iteration is a sequence of [[Natural Number]], this means proving:
	1. The value of $e$ is always a natural number
	2. The value of $e$ decreases after every iteration (i.e $e' <e$)
# Example
https://cmsweb.utsc.utoronto.ca/nick/cscB36/additional-notes/sample-correct.pdf
- Precondition $n \in \mathbb{N}$
- Postcondition: Return $n^{2}$
```
SQ(n)
(1)	s=0; d=1; i=0;
(2)	while i < n:
(3)		s=s+d
(4)		d=d+2
(5)		i=i+1
(6)	return s
```
### Proof
1. We find the [[Loop Invariant|LI]] with three parts:
	1. $s = i^{2}$
	2. $d = 2i+1$
	3. $0 \leq i \leq n$
2. Prove the [[Loop Invariant|LI]], (prove it holds at the start and after every iteration)
3. Basis: On entering the loop, $s=0; d=1; i=0$, then we get that $s=i^{2}, d=2i+1, 0\leq i \leq n$ holds, so [[Loop Invariant|LI]] holds
4. Induction step:
	1. Suppose [[Loop Invariant|LI]] holds before iteration ($s=i^{2},d=2i+1,0\leq i \leq n$) [[Induction Hypothesis|IH]]
	2. Then, denote $s', d', i'$ to be the values after the iteration
	3. $i' = i+1$ by line $(5)$
	4. $s=s'+d$ by line $(3)$
	5. $= i^{2}+2i+1$ by [[IH]]
	6. $= (i+1)^{2}$
	7. $= (i')^{2}$'
	8. Also, $d'=d+2$ by line $(4)$
	9. $=2i+1+2$ by [[Induction Hypothesis|IH]]
	10. $=2(i+1)+1$
	11. $= 2i' +1$
	12. Thus, we get $LI(a)$