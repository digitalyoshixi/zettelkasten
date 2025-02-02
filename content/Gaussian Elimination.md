---
tags:
  - linalg
  - math
---
A process to turn a [[Augmented Matrix]] into [[Echelon Form|REF]] to find solutions
# Process
![[Gaussian Elimination-20250202171325258.webp]]
1. Locate the left-most column with the first non-zero entry
![[Gaussian Elimination-20250202171403114.webp]]
2. Swap the top-most row with the non-zero entry row
![[Gaussian Elimination-20250202171426494.webp]]
3. Multiply the row so that the non-zero entry is equal to one
![[Gaussian Elimination-20250202171531403.webp]]
4. Add suitable multiples of the top row to the bottom row until all entries below are equal to 0
![[Gaussian Elimination-20250202171622042.webp]]
5. Mark the top-most row as completed, now continue the process for the bottom rows
![[Gaussian Elimination-20250202171829021.webp]]