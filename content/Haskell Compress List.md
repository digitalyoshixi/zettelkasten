---
tags:
  - programming
  - haskell
---
Removes duplicate items that are adjacent to eachother
```haskell
compress :: Eq a => [a] -> [a]
compress [] = []
compress (x:[]) = [x]
compress (x:y:xs) | x == y = compress (y:xs)
                  | otherwise = [x] ++ compress (y:xs)
```