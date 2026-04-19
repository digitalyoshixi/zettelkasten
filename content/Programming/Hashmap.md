---
tags:
  - programming
aliases:
  - Hash Table
  - Map
  - Dictionary
---
This is a one-way mapping from one datatype to another.
```python
mymap = {
	a : 20,
	b : "hello"	,
	"quint" : 1.2239
}
```
# Data Structure
A array of size $m$ with a [[Hashing|Hash Function]] $h : U \to [0,\dots,m-1]$
# Operations
- `insert(k,v)`: insert a new key-value pair `k-v`
- `delete(k)`: delete the node with key `k`
- `search(k)`: find node with key `k`
# Types
- [[Direct Addressing Hashmap]]
- [[Collision Resolution Chaining]]
- [[Collision Resolution Probe Sequence]]