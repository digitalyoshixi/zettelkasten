---
tags:
  - software
  - programming
---
# Process
1. Formula a [[Loop Invariant|LI]]. The [[Loop Invariant|LI]] should describe the purpose of every variable
2. Use [[Induction]] to prove [[Loop Invariant|LI]]
3. Use the [[Loop Invariant|LI]] in step 1 to prove [[Partial Correctness Step]] ($\text{loop exit condition and LI} \implies \text{postcondition}$)
4. Use [[Loop Invariant|LI]] in step 1 to prove [[Termination]]. We start by finding a [[Terminating Variable]] expression $e$ that uses variables in the loop such that:
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
		1. $= i^{2}+2i+1$ by [[IH]]
		2. $= (i+1)^{2}$
		3. $= (i')^{2}$'
	5. Also, $d'=d+2$ by line $(4)$
		1. $=2i+1+2$ by [[Induction Hypothesis|IH]]
		2. $=2(i+1)+1$
		3. $= 2i' +1$
	6. Also, $i < n$ by line $(2)$
		1. Then, it follows that $i' = i+1 \leq n$
		2. Since $0\leq i \implies 0 \leq i+1 = i'$
		3. Thus, $0 \leq i' \leq n$
	7. Thus, we have shown all conditions of [[Loop Invariant|LI]]
5. Now we prove [[Partial Correctness Step|Partial Correctness]]
	1. Suppose the loop terminates, then consider the values $s,d,i$ on exit
	2. By [[Loop Invariant|LI]], $i\leq n$
	3. By exit condition, $i \geq n$
	4. Thus, $i=n$
	5. By [[Loop Invariant|LI]], $s=i^{2} = n^{2}$
	6. Therefore, by line $(6)$ $s=n^{2}$ as wanted $\square$
6. Now we find an expression $e$ that forms a decreasing sequence of natural numbers
	1. Choose $e = n-i$
7. Then, we show that $e$ is decreasing sequence
	1. By [[Loop Invariant|LI]], $i \leq n$
	2. So, this means $e = n-i \geq 0$
	3. Thus, $e \in \mathbb{N}$
	4. Consider arbitrary iteration
		1. Then, $e'=n-i'$
		2. $=n-(i+1)$ By line $(5)$
		3. $= n - i-1$
		4. $=e -1$
		5. $<e$
		6. Thus, $e$ is always decreasing
	5. Therefore, the sequence of $e$ forms a decreasing sequence of natural numbers $\square$