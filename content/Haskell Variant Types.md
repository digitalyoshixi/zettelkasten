---
tags:
  - programming
  - haskell
---
A Haskell type that can be multiple things. Anything of this type is a union of multiple different types.
```haskell
data Text = Letter Char | Word [Char]
textLen (Letter _) = 1
textLen (Word w) = length w

>>> :t textLen
textLen :: Text -> Int -- note that this Text type was INFERED!!!
```