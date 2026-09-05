---
tags:
  - programming
  - security
---
The idea of picking a random [[Hashing|Hash Function]] from a family for functions that have a universal property.
# Universal Property
A family $H$ of [[Hashing|Hash Function]] is universal iff:
- For any two keys $j,k$ with $j \neq k$.
- Randomly pick $h$ from $H$ with [[Uniform Continuous Probability Distribution|Uniform Probability]]
- $Pr(h(j) = h(k)) \leq \frac{1}{m}$ ($m$ is array length)
	- (Equivalently, at most $\frac{|H|}{m}$ functions satisfy $h(j) = h(k)$)
# Hash Example
$$
h(k) = ( (ak+b) \mod p) \mod m
$$
- $a,b$ random
- $p$ is a [[Prime Number]]
- $m$ is the hash table size