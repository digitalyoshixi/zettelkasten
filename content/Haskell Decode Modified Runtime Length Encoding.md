---
tags:
  - programming
  - haskell
---
```haskell
data EncodeType a = Single a | Multiple (Int, a) deriving (Show)

decode_rle :: EncodeType a -> [a]
decode_rle (Single a) = [a]
decode_rle (Multiple (0, a)) = []
decode_rle (Multiple (n, a)) = [a] ++ decode_rle (Multiple (n-1, a))

decode_modified :: [EncodeType a] -> [a]
decode_modified [] = []
decode_modified (x:xs) = decode_rle x ++ decode_modified xs
```