---
tags:
  - programming
---
Finding height is a $O(\log n)$ operation.
Height is bounded by $\Theta(\log n)$.
$$
\text{minsize(h)} = \frac{\phi^{h+2}-(1-\phi)^{h+2}}{\sqrt{ 5 }}-1
$$
- With $\phi$ as [[Golden Ratio]]
- With $h$ as the height of the sub tree
# Code
```cpp
int height(AVL_Node* node) {  
  if (node == NULL) return 0;  
  int left = height(node->left);  
  int right = height(node->right);  
  if (left > right) return left + 1;  
  return right + 1;  
}

void updateHeight(AVL_Node* node) { 
	node->height = height(node); 
}  
```
# Proof of Height
$minsize(0) = 0$
$\text{minsize}(1) = 1$
Assuming tree is as unbalanced as possible, so one tree end (left or right) is heavier:
- Note that tree size $\text{minsize}(h+2) = \text{minsize}(h)+\text{minsize}(h+1)+1$

Prove by [[Induction]] that $\text{minsize(h)} = fib(h+2)-1 \frac{\phi^{h+2}-(1-\phi)^{h+2}}{\sqrt{ 5 }}-1$
Note that the [[Fibonacci Series]] grows exponentially by [[Golden Ratio]]
- $\text{minsize}(0) = 0 = 1 - 1 = fib(2)-1 = fib(0+2)-1$
- $\text{minsize}(1) = 1 = 2 - 1 = fib(2)-1 = fib(1+2)-1$
Induction step:
- Assume $\text{minsize}(j) = fib(j+2)-1, \forall 0 \leq j \leq k, k \geq 1$
- Prove for $\text{minsize}(k+1)$...
- $\text{minsize}(k+1) = \text{minsize}(k)+\text{minsize}(k-1)+1$ by defn of min size
- $= fib(k+2)-1 + fib(k-1+2)-1+1$
- $= fib(k+2) + fib(k+1)-1$
- $= fib(k+3)-1$
- $= fib(k+1+2)-1$
Thus, we have shown that the predicate satisfies for all cases.
Then, note that $n \geq minsize(h) > \frac{\phi^{h+2}}{\sqrt{ 5 }}-2$
- $\implies n > \frac{\phi^{h+2}}{\sqrt{ 5 }}-2$
- $\implies n+2 > \frac{\phi^{h+2}}{\sqrt{ 5 }}$
- $\implies \phi^{h+2} < \sqrt{ 5 }(n+2)$
- $\implies \log\phi^{h+2} < \log\sqrt{ 5 }(n+2)$
- $\implies \log\phi^{h+2} < \log\sqrt{ 5 }(n+2)$
- $\implies (h+2) \log \phi < \log \sqrt{ 5 } + \log(n+2)$
- $\implies h < \frac{\log(n+2)}{\log \phi} + \frac{\log \sqrt{  5 }}{\log \phi} - 2$
- $\implies h \in O(\log n)$

Note for any binary tree the number of node will always be smaller than a power of 2 raised to the height: $n <2^{h+1}-1$
- $\implies \log (n-1) < \log 2^{h}$
- $\implies \log (n-1) < h$
- $\implies h \in \Omega(\log n)$

Thus, $h \in \Theta(\log n)$