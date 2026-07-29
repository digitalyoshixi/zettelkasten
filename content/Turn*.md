---
tags:
  - verification
---
A [[Clustering Block|Trace Clustering]] algorithm, adapts the [[K-Medoid]] algorithm to work with increasingly larger clusters.
1. Starts with a small `k` and run [[K-Medoid]]
2. Consider similarities within each cluster and differences among each cluster
3. Continue increasing number of clusters for each repetition until local maximum is reached