---
tags:
  - docker
---
A pool of [[Kubernetes Worker Node|Kubernetes Nodes]] that defines:
- Defines the type of [[Kubernetes Worker Node|Kubernetes Node]] to create
- Instance type (CPU, Architecture, # of cores)
- AMI, [[Amazon VPC Security Groups]], [[AWS Virtual Private Cloud|AWS VPC Subnets]] defined in [[Karpenter Node Class]]
Created with a [[YAML]] file. It is a [[Kubernetes Custom Resource]].
# Get Nodepools
```
kubectl get nodepools
```
# Example
![[Karpenter Nodepool-1789055540494.webp]]
- Allows instance family c5, m6, r5, t3
- Does not allow instance size nano, micro, small
- Has availability zones allowed us-west-2a, us-west-2b
- Allows amd-64, arm64
- Prioritizes spot, but can fall back to on demand
- Limit node provisioning until CPU has 100 or 1000Gi of memory
