---
tags:
  - programming
  - prolog
---
```prolog
% length(?L, ?N) if N is the length of list L
length([], 0).
length([_,|T], N) :- mylength(T, NT), N is NT+1.
```
# Guards
- You must place the first definition before using it ([[Prolog Instantiation]])