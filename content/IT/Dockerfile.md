---
tags:
  - cloud
  - virtualization
---
# Dockerfile
These are the scripts that setup and manage several containers. They can be shared with other users so they can easily setup the same docker containers. 
An example configuration looks like this:
![[Docker-20240702022403622.webp]]
FROM ubuntu:19.10 is a signal to docker to install a docker image from docker's servers. You can only do this if you have your **verified** docker account as a environment variable