---
tags:
  - hardware
  - math
---
![[Booth's Algorithm-20250610153610595.webp]]
This is an algorithm that simplifies multiplication.
# Algorithm
![[Booth's Algorithm-20250610191614091.webp|498]]
1. [[Sign Extend]] to make both bytes the same length
2. For binary byte with length $n$
3. Go through digits from $n-1$ to $0$
	1. If digits at $i$ and $i-1$ are $0,1$, then the multiplicand is added to the result at position $i$
	   ![[Booth's Algorithm-20250610191440518.webp|265]]
	2. If digits $i$ and $i-1$ are $1,0$, then the multiplicand is subtracted from the result at position $i$
	   ![[Booth's Algorithm-20250610191555382.webp|267]]
# Example in Decimal
Involves segmenting multiplication into easier sub-multiplications with better numbers.
![[Booth's Algorithm-20250610190941795.webp]]