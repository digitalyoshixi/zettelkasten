---
tags:
  - programming
---
```
select(S, r):
Given rank r, set S, which key in S has this rank?
```
# Pseudocode
```
if T == nil:
	deal with special case
r' = size(T.left)+1
if r == r':
	return T.key
if r < r':
	return select(T.left, r)
else:
	return select(T.right, r=r')
where
size(T) = 0 if T == nil else T.size
```