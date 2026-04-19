---
tags:
  - programming
---
A data structure for [[Priority Queue]] with the union operation implemented as a [[Forest]] of [[Min-Heap]] connected by a [[Linked List|Double Linked List]].
![[Fibonacci Heap-20260404231737016.webp]]
# Structure
### Node Structure
```cpp
struct node_structure{
	int key; // used for priority
	struct node_structure* left; 
	struct node_structure* right; 
	struct node_structure* child; // ptr to one child
	int degree; // number of children
	bool marked; // indicates whether node has lost a child
}
```
### Heap Structure
```cpp
struct heap_structure{
	std::list<struct node_structure*> roots; // list of roots
	struct node_structure* min; // ptr to root node with minimum key
}
```
# Operations
- `insert(H,k)`: insert key `k`
- `union(H, H1, H2)`: merge two heaps `H1`, `H2`
- `decrease-priority(H,key)`: Decreases the priority of a key
- `extract-min(H)`: Extracts the min of a heap
- `consolidate(H)`: Reorder root list with nodes of unique degree
### `insert(H,k)`
A $O(1)$ operation
```perl
insert(H,k):
	new_root := new node(key=k, marked=false)
	add new_root to H.root_list
	if k < H.min.key:
		H.min = new_root	
```
### `union(H,H_1,H_2)`
A $O(1)$ operation
```perl
union(H, H1, H2):
	H.root_list := H1.root_list + H2.root_list
	if H1.min.key <= H2.min.key:
		H.min := H1.min
	else:
		H.min := H2.min
```
![[Fibonacci Heap-20260404232220232.webp|610]]
### `extract-min(H)`
```perl
extract-min(H):
	remove H.min from H.root_list
	add each child of H.min to H.root_list
	H.min := any former child of H.min
	consolidate(H)	
```
### `consolidate(H)`
![[Fibonacci Heap-20260419010159671.webp]]
Attempts to make sure all roots in the list have a unique degree. Will find nodes that have the same degree and make the larger key a child of the node with the smaller key
```perl
consolidate(H):
	for each node n in H.root_list:
		x := n
		while A[x.degree] != null:
			y := A[x.degree]
			A[x.degree] := null
			if x.key > y.key:
				x,y := y, x
			remove y from H.root_list
			make y child of x
			y.marked := false
		A[x.degree] := x
	update H.min
```
### `decrease-priority(H,x,k)`
![[Fibonacci Heap-20260419012001654.webp|404]]![[Fibonacci Heap-20260419012010077.webp|410]]
```perl
decrease-priority(H,x,k):
	if k >= x.key: return
	x.key := k
	y := x.parent
	if y != null and y.key > x.key:
		cut(H,x,y)
		
		// cascading cut
		while y.parent != null:
			if not y.marked:
				y.marked := true
				break
			else:
				cut(H,y,y.parent)
				y := y.parent
				
		if x.key < H.min.key:
			H.min := x
			
cut(H,x,y): # remove a node from its parent y and move it to root list
	remove x from children of y
	add x to H.root_list
	x.marked := false
	if x.key < H.min.key:
		H.min := x
```
# Complexity Analysis
Define:
- $t(H)$: number of trees in heap $H$ (nodes in root list)
- $d(H)$: degree of node with maximum heap in heap $H$
- $D(n)$: maximum possible degree of fibonacci heap with $n$ nodes
- $m(H)$: number of marked nodes in heap
Then worst-case analysis:
- `extract-min()` has complexity $O(t(H)+D(n))$
- `decrease-priority(n,p)` has complexity $O(m(H))$
We can define potential function $\phi(H) = t(H)+2*m(H)$
- Insert changes potential with $\triangle(\phi) = \phi(H_{i})-\phi(H_{i-1}) = t(H_{i})+2*m(H_{i})-t(H_{i-1})-2*m(H_{i-1})=1$
- Then, $a_{i} = t_{i}+ \triangle(\phi)=O(1) = \pi$
- Amortized cost of decrease-priority is $O(1)$
- Amortized cost of extract-min is $O(D(n))$ equivalent to $O(\log n)$
Note that:
- $N(d) = fib(d+2)$ - hence the name fibonacci heap
# Fibonacchi Relation
![[Fibonacci Heap-20260419012647565.webp]]
The size of the heaps has a similar structure to the [[Fibonacci Sequence]] where the size of a large heap is proportional in size to the previous smaller heaps.
Implies an exponential growth of [[Golden Ratio]]