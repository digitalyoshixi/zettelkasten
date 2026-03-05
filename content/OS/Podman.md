---
tags:
  - docker
  - virtualization
---
A container engine alternative to [[Docker]] that follows [[Open Container Initiative]].
- Does not use a central [[Daemon Process]] to manage containers. Uses [[fork()]] and exec to make containers independent of a central process
- Runs as normal user instead of root
# Enabling Podman Session for Non-Root
```
loginctl enable-linger <your_username>
```
