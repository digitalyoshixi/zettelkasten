---
tags:
  - programming
  - haskell
---
The [[Haskell Type]] of a [[Haskell Type]].
- [[Haskell Concrete Type]]
- [[Haskell Non-concrete Type]]
# Example
```haskell
>>> :kind Either
Either :: * -> * -> *
```

```haskell
data Something a b c d = Whatever a b c d
>>> :kind Something
Something :: * -> * -> * -> *
```