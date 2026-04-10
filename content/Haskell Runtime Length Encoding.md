---
tags:
  - programming
  - haskell
---
Returns the [[Runtime Length Encoding]] for a given list.
```haskell
end_same :: Eq a => [a] -> a -> [a]
end_same [] _ = []
end_same (x:xs) a | x == a = end_same xs a
                  | otherwise = (x:xs)

rle_code :: Eq a => [a] -> a -> Int
rle_code [] _ = 0
rle_code (x:xs) a | x == a = 1 + rle_code xs a
                  | otherwise = 0

encode :: Eq a => [a] -> [(Int, a)]
encode [] = []
encode (x:xs) = [((rle_code (x:xs) x) , x)] ++ encode (end_same (x:xs) x)
```