---
tags:
  - programming
  - haskell
---
A modified [[Haskell Runtime Length Encoding]] with custom types.
```haskell
rle_code :: Eq a => [a] -> a -> Int
rle_code [] _ = 0
rle_code (x:xs) a | x == a = 1 + rle_code xs a
                  | otherwise = 0

data EncodeType a = Single a | Multiple (Int, a) deriving (Show)

encode_modified :: Eq a => [a] -> [EncodeType a]
encode_modified [] = []
encode_modified (x:xs) | (rle_code (x:xs) x) == 1 = [Single x] ++ encode_modified (end_same (x:xs) x)
                       | otherwise = [Multiple ((rle_code (x:xs) x) , x)] ++ encode_modified (end_same (x:xs) x)
```