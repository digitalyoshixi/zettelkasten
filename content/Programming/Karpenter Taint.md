---
tags:
  - cloud
---
A configuration in [[Karpenter Nodepool]] that specifies which [[Kubernetes Worker Node|Kubernetes Nodes]] can be in which nodepools
```
taints: 
- key: ://company.com 
  value: tenant-a 
  effect: NoSchedule
```
- Allows only tenant-a nodes to use this