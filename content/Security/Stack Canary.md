---
tags:
  - c
  - binary_exploitation
---
Security measure to prevent [[Stack Overflow]] attacks.
![[Stack Canary-20250314030555224.webp]]
They are random values placed right before the return address on the stack that is checked before every return call to check for tampering.
![[Stack Canary-20250330204617215.webp|403]]
# Bypassing Stack Canaries
1. Leak the stack canary with another method
2. [[Stack Canary Brute Forcing]]
3. [[Jumping Stack Canary]]
# Stack Canary Generation
- Uses [[Segment Register|fs]]