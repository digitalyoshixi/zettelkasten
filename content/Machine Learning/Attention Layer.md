---
tags:
  - machine_learning
---
This is a layer for [[Machine Learning/Transformer|Transformer]] used to assign attention weights to specific inputs.
![[Attention Layer-20251002194125772.webp]]
# Intuition
A 'gravity' is applied to all words to pull to eachother, allowing each word to be affected by the meaning of every other word
![[Attention Layer-20251002195431448.webp|525]]
![[Attention Layer-20251002195540588.webp|455]]
![[Attention Layer-20251002195557516.webp|446]]
Then, the embedding is modified after pull to be closer to the actual meaning
# Definition
Comprised of several heads that correspond to a current token within a sequence.
Every head send's their value in [[Parallelism|Parallel]] to the [[Feature Decoder]].
![[Attention Layer-20250628154621455.webp]]
# Concepts
- [[Time Complexity of Attention]]