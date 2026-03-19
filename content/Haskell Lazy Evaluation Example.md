---
tags:
  - programming
  - haskell
---
```haskell
length [] = 0
length (_:xs) = 1 + length xs
```
# Evaluation Trace
```haskell
length [42^1234, 42^2345, 42^3456]
= length thunk{[42^1234, 42^2345, 42^3456]}
= length (_ : thunk{[42^2345, 42^3456]})
= 1 + length thunk{[42^2345, 42^3456]}
= 1 + length (_ : thunk{[42^3456]})
= 1 + 1 + length thunk{[42^3456]}
= 1 + 1 + length (_ : thunk{[]})
= 1 + 1 + 1 + length (thunk{[]})
= 1 + 1 + 1 + length ([])
= 1 + 1 + 1 + 0
= 3
```
# Lazy Evaluation [[Fibonacci Series]]
```haskell
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)
```