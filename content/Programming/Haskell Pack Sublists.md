---
tags:
  - programming
  - haskell
---
```haskell
consume_same :: Eq a => [a] -> a -> [a]
consume_same [] _ = []
consume_same (x:xs) a | x == a = [x] ++ consume_same xs a
                      | otherwise = []

end_same :: Eq a => [a] -> a -> [a]
end_same [] _ = []
end_same (x:xs) a | x == a = end_same xs a
                  | otherwise = (x:xs)

pack :: Eq a => [a] -> [[a]]
pack [] = []
pack (x:xs) = [(consume_same (x:xs) x)] ++ pack (end_same (x:xs) x)
```