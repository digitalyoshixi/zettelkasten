---
tags:
  - networking
---
A encoding/decoding process from unicode to a reduced ascii set.
# Decoding
1. For a punycode string `Mnchen-3ya`, the literal portions is the left-most string, and all delta-values are delimited by `-` and some encoded delta
2. Bring all the non-special ascii down `Mnchen`
3. Convert encoded delta to number by [[Generalized Variable-Length Integer]] (`3ya` = 839)
4. Start pointer at first character of `Mnchen`, increment i by 1 each time, and then increment `n` everytime `i` surpasses the length of the literal ascii. Then, at the end, insert the ascii character of `n` into the corresponding position
![[Bootstring-20251230040553414.webp|235]]![[Bootstring-20251230040609800.webp|227]]
