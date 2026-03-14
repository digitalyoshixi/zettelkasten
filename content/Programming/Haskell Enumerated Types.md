---
tags:
  - programming
  - haskell
---
A type that is simply a collection of other types. 
You can define functions that use these enums and give them values like a dictionary.
```haskell
data Colour = Red | Green | Blue
colorName :: Colour -> [Char]
colorName Red = "red"
colorName Green = "green"
colorName Blue = "blue"
```