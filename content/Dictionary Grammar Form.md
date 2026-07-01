---
tags:
  - compilers
  - programming
---
A notation to represent [[Programming/Grammar|Grammar]] rules.
```
{
'<A>'     : [['b', '<B>'], ['c', '<C>']],
'<B>'     : [['b', '<B>'], []],
'<C>'     : [[]]
}
```
- From state `A`, receiving `b` transitions to state `B`