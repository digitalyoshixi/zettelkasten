---
tags:
  - networking
---
These are lightweight linux containers that run at near-native performance. They share the same kernel as the [[Hypervisor]].

For [[Proxmox]], these are usually the containers that run single services or programs.

# Security
Due to the shared kernel, LXCs are less secure, but you can run them unprivileged to