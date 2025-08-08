---
tags:
  - security
  - malware
aliases:
  - Yara Atom
---
# Algorithm
1. Yara string searches start with atoms which are between 1-4 bytes segments.
   ![[Yara Atoms-20250808012717164.webp]]
2. The searching algorithm will first find all instances of an atom
   ![[Yara Searching Algorithm-20250808012824001.webp]]
3. If an atom is matched, the search goes back to check for matches on the full string 
   ![[Yara Searching Algorithm-20250808012846335.webp]]