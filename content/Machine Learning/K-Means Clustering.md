---
tags:
  - machine_learning
---
This is our first [[Unsupervised Learning]] model.
It will stratify our data into $K$ amount of clusters.
![[K-Means Clustering-20250619132157410.webp]]

# Algorithm
1. Given $K$ number of clusters, places centroids randomly around the grid
2. The centroids should be the exact centers of their clusters. Every datapoint checks which cluster is nearest, and is added into its cluster
3. Delete the centroid we already have and place it in the centre of all the points so that the centroid is actually in the center.
4. Repeat until there are no more changes
