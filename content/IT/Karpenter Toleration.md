---
tags:
  - cloud
---
A configuration for a [[Kubernetes Pod|Pods]] in [[Karpenter Node Class]] that allow a pod to ignore the [[Karpenter Nodepool]]'s [[Karpenter Taint]] and schedule there.
```
# Pod Spec snippet
tolerations:
- key: "://company.com"
  operator: "Equal"
  value: "data-science"
  effect: "NoSchedule"
```
- This pod has can overwrite these taints