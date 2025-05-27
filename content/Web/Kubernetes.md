---
tags:
  - virtualization
aliases:
  - k8s
---
![[Kubernetes-20240802032253100.webp|303]]
A software used to manage and orchestrate [[Docker]] containers, ensuring they have:
- [[High Availability]]
- [[Elasticity]]
- Cohesion
Developed at [[Google]].
# Installation
### [[Arch Linux]]
`sudo pacman -S kubectl`
### [[Debian]]
1. `sudo apt install -y apt-transport-https ca-certificates curl gnupg`
2. `curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.33/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg`
3. `sudo chmod 644 /etc/apt/keyrings/kubernetes-apt-keyring.gpg`'
4. `echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.33/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list`
5. `sudo chmod 644 /etc/apt/sources.list.d/kubernetes.list`
6. `sudo apt-get update`
7. `sudo apt-get install -y kubectl`
# Concepts
- [[Docker]]
- [[Kubernetes Master Node]]
- [[Kubernetes Worker Node]]
- [[Docker Node]]
- [[Docker Cluster]]
- [[etcd]]
- [[Declarative]]