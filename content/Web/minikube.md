---
tags:
  - virtualization
  - IT
---
A local kubernetes tooling.
# Installation
1. `curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb`
2. `sudo dpkg -i minikube_latest_amd64.deb`
3. `sudo apt install --no-install-recommends qemu-system libvirt-clients libvirt-daemon-system docker`
# Running Cluster
`minikube start`