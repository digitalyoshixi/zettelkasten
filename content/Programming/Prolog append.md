---
tags:
  - programming
  - prolog
---
```c
% append(?X, ?Y, ?Z) iff Z is the result of appending list Y to list Z
append([],Y,Y).
append([X|Xs],Y,[X|Zs]) :- append_list(Xs,Y,Zs).
```
# Examples
- `append([], [1,2,3], Y)` 