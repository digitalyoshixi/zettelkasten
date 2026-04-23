---
tags:
  - programming
---
A method for counting [[Amortized Time]].
# Method
- Assign each operation to receive fixed credit amount $x$.
- Assign each operation an artificial cost to each operation (no need to be actual cost)
- Some operations keep extra and that amount is stored as credit to pay more expensive operations later.
- Prove invariant ($amount \geq 0$) $\implies$ Each operation takes $O(x)$ amortized time
# Example
Suppose a multi-pop [[Stack]] with:
- Push: push a element to top of stack $O(1)$
- Pop: pop top element off stack $O(1)$
- Multi-Pop: pop top $n$ element off stack $O(n)$
Then, we assign:
- Give each operation $x=2$ received amount
- Assign push to cost 1 dollar
- Assign pop to cost 1 dollar
- Multi pop to cost $n$ dollar for number of elements popped
Proving invariant:
- Initially: $amount = 0$, $size=0$
- Push:
	- Assume $amount \geq size$ before push
	- Then, $amount' = amount + credit(push) - cost(push)$
	- $\implies amount' = amount + 2 - 1 = amount + 1$
	- $size' = size + 1$
	- Then, invariant holds as $amount' \geq size'$
- Pop:
	- Assume $amount \geq size$ before pop
	- Then, $amount' = amount + credit(pop) - cost(pop)$
	- $\implies amount' = amount+1$
	- $size' = size+1$
	- Then, invariant holds as $amount' \geq size'$
- Multi-pop:
	- Assume $amount > size$  before multipop
	- Let $n$ be number of items popped
	- Then, $amount' = credit(\text{multipop}) - cost(\text{multipop})$
	- $= amount + 2 - n$
	- $size' = size - n$
	- Thus, $amount' \geq size;$
- Finally, note that $size \geq 0 \implies amount \geq 0$ is an invariant