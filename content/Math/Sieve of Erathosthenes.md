---
tags:
  - math
  - cryptography
---
Prints all primes smaller or equal to a limit `n`
Efficient of when `n <= 10,000,000`
# Algorithm
1. Assume all numbers from `2` to `n` are unmarked
   ![[Sieve of Erathosthenes-20250102225257158.webp|505]]
2. Mark the number 2 as prime, then mark all multiples of 2 as composite
   ![[Sieve of Erathosthenes-20250102225418004.webp|507]]
3. The next unmarked number from 2 is prime (3 in this case), then mark all multiples of 3 that are currently unmarked as composite
   ![[Sieve of Erathosthenes-20250102225522924.webp|512]]
4. Repeat the process with all subsequent unmarked numbers
   ![[Sieve of Erathosthenes-20250102225601592.webp|503]]