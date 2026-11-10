---
tags:
  - docker
---
A auto scaling solution for [[Kubernetes]].
Configured with two files:
- Nodepool.yml
- EC2NodeClass.yml
# Get Nodepools Config
```
kubectl get nodepool -o yaml
```
# Concepts
- [[Kubernetes Namespace]]
- [[Karpenter Nodepool]]
	- [[Karpenter Taint]]
	- [[Karpenter Toleration]]
	- [[Karpenter Requirement]]
- [[Karpenter Node Class]]
- [[Karpenter Node Claim]]