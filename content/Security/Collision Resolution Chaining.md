---
tags:
  - programming
---
A method for [[Collision Resolution]] that involves storing a [[Linked List|Double Linked List]] at each entry of a hash table.
![[Collision Resolution Chaining-20260405002321290.webp]]
An element with key $k_{1}$ and element with key $k_{2}$ can be stored at position $h(k_{1})=h(k_{2})$
# Complexity Analysis
- `insert(k,v)` takes $\Theta(1)$ time
- `delete(k)` takes $\Theta(1)$ time after search
- `search(k)` worst case $\Theta(n)$ where every entry of table has no elements except for target entry with $n$ elements
Worst case with [[Independent Uniform Hashing]] is $O(1+\alpha)$ where $\alpha$ is [[Load Factor]]