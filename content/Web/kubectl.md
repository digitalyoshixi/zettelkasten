---
tags:
  - virtualization
  - IT
---
A cli tool for [[Kubernetes]].
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
# Usage
### View Nodes
`kubectl get nodes`
![[kubectl-20250527131641849.webp]]
### View Pods
- `kubectl get pods -A`  : Get pods from all namespaces'
### Applying [[Kubernetes Manifest]]
- `kubectl apply -f <servicedeployment>.yaml` For the specific manifest you want to deploy