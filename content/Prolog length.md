---
tags:
  - programming
  - prolog
---
```prolog
% length(?L, ?N) if N is the length of list L
length([], 0).
length([_,|T], N) :- mylength(T, N-1)
```
