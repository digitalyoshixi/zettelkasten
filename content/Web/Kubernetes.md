---
tags:
  - virtualization
aliases:
  - k8s
---
![[Kubernetes-20240802032253100.webp|303]]
A software used to manage [[Docker]] containers, ensuring they have:
- Reliability
- Scalability
- Cohesion
# Installation
### [[Arch Linux]]
`sudo pacman -S kubectl`
### [[Debian]]
`curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"`
# Concepts
- [[Docker]]
- [[Docker Node]]
- [[Docker Cluster]]
- [[etcd]]
- [[Declarative]]