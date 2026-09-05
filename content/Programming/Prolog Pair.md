---
tags:
  - programming
  - prolog
---
```prolog
key/value.
% OR
key-value.
```
# Accessing Value
```prolog
lookup(Key, [Key-Value|_], Value).
lookup(Key, [_-_, Tail], Value) :- lookup(Key, Tail, Value).
```