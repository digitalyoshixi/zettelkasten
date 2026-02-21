---
tags:
  - virtualization
---
Tool that creates lightweight environments called containers for app deployment. Docker is great at creating isolated spaces for your applications to run on while also providing them with OS level dependencies.
Great for:
- [[Microservices]]
# Installation
### [[Arch Linux]]
1. `sudo pacman -S docker`
2. `sudo systemctl enable docker.service & sudo systemctl start docker.service` 
3. `sudo systemctl start docker.socket`
### Debian
1. `apt update`
2. `apt install ca-certificates curl`
3. `sudo install -m 0755 -d /etc/apt/keyrings`
4. `sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc`
5. `sudo chmod a+r /etc/apt/keyrings/docker.asc`
6. 
```
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
7. `sudo apt-get update`
8. `sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin`
# Guides
- [[Docker Build Container]]
- [[Docker Buildx Container]]
- [[Docker Run Container]]
- [[Docker Stop Container]]
- [[Docker Delete Image]]
- [[Docker Open Container in App]]
- [[Docker Copy Files to Host]]
- [[Docker Compose]]
- [[Docker Nuke Everything]]
- [[Docker Inspect]]
# Concepts
- [[Containers]]
- [[Kubernetes Pod]]
- [[Dockerfile]]
- [[Docker Node]]
- [[Docker API]]
# Practical Use Cases
- Make a [[Docker Compose]] file which automates the process of creating gitlab servers
- You can use docker like a linux server where you SSH into