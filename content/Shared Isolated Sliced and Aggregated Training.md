---
tags:
  - machine_learning
  - ai_safety
aliases:
  - SISA
---
A method of ML that allows for [[Machine Unlearning]]
![[Shared Isolated Sliced and Aggregated Training-20260128012819800.webp|445]]
# Training
1. Break up training data into disjoint shards
2. Break up each shard into slices
3. Train individual constituent models $M_{i}$ on distinct shards, saving parameters as you train on more and more slices
4. Aggregate consistent model output for final output (Mean, most common output, other methods...)
# Untraining
When an unlearning request comes in:
1. Remove data from shard
2. Identify last relevant constituent model parameters
3. Re-aggregate model