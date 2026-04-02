---
tags:
  - programming
  - prolog
---
```c
% append(?X, ?Y, ?Z) iff Z is the result of appending list Y to list Z
mylength([], 0).
mylength([_|T], N) :- mylength(T,NT), N is NT+1.
```
# Examples
- `append([], [1,2,3], Y)` 