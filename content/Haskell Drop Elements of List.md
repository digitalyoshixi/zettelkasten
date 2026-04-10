---
tags:
  - programming
  - haskell
---
```haskell
n_slice :: [a] -> Int -> [a]
n_slice [] _ = []
n_slice xs 0 = xs
n_slice (x:xs) n = n_slice xs (n-1)

dropped :: [a] -> Int -> [a]
dropped [] _ = []
dropped xs 0 = []
dropped xs 1 = []
dropped (x:xs) n = [x] ++ dropped xs (n-1)

mydrop :: [a] -> Int -> [a]
mydrop [] _ = []
mydrop xs 0 = xs
mydrop xs a = (dropped xs a) ++ mydrop (n_slice xs a) a
```