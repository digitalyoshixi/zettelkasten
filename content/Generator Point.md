---
tags:
  - math
aliases:
  - ECC Generator
---
A point on a [[Elliptic Curve]] $G$ used to generate other points on a curve.
# Picking Generator
- Get a list of all points on the [[Elliptic Curve]] via [[Schoofs Algorithm]]
- Find the point with the longest cycle (each point will repeat to the same values after some multiplication)
![[ECC Generator-20260529012820059.webp]]