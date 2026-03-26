---
tags:
  - programming
aliases:
  - Producer Consumer Problem
---
A [[Systems Design]] concept that partitions systems into a:
- Producer: creates resources
- Consumer: consumes resources
That each consume and produce at different rates.
Uses a [[Queue]] that to ensure non-blocking communication.
- Consumer blocked when [[Buffer]] empty
- Producer blocked when [[Buffer]] full